import zipfile
import xml.etree.ElementTree as ET
import os
import re

pptx_path = 'reference/IGCSE Physics Learning Log.pptx'
out_md = 'reference/retrieval_tasks.md'

unit_names = {
    range(1, 10): 'Unit 1: Forces and Motion',
    range(10, 17): 'Unit 2: Electricity',
    range(17, 21): 'Unit 3: Waves',
    range(21, 22): 'Unit 4: Energy Resources and Energy Transfers',
    range(22, 26): 'Unit 5: Solids, Liquids and Gases',
    range(26, 31): 'Unit 6: Magnetism and Electromagnetism',
    range(31, 36): 'Unit 7: Radioactivity and Particles',
    range(36, 41): 'Unit 8: Astrophysics and Cosmology'
}

def get_unit(task_num):
    for r, u in unit_names.items():
        if task_num in r:
            return u
    return 'General Physics'

def parse_slide(z, slide_name):
    slide_num = re.search(r'\d+', slide_name).group()
    rels_name = f'ppt/slides/_rels/slide{slide_num}.xml.rels'
    rel_map = {}
    if rels_name in z.namelist():
        rels_tree = ET.fromstring(z.read(rels_name))
        for rel in rels_tree.iter():
            r_id = rel.attrib.get('Id')
            target = rel.attrib.get('Target')
            if r_id and target and 'media/' in target:
                rel_map[r_id] = os.path.basename(target)

    ns = {
        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }
    
    slide_tree = ET.fromstring(z.read(slide_name))
    spTree = slide_tree.find('.//p:spTree', ns)
    
    shapes = []
    task_num = None
    section_title = None
    
    for child in spTree:
        tag = child.tag.split('}')[-1]
        
        xfrm = child.find('.//a:xfrm', ns)
        if xfrm is None:
            spPr = child.find('.//p:spPr', ns)
            if spPr is not None:
                xfrm = spPr.find('a:xfrm', ns)
        
        x, y, cx, cy = 0, 0, 0, 0
        if xfrm is not None:
            off = xfrm.find('a:off', ns)
            ext = xfrm.find('a:ext', ns)
            if off is not None:
                x, y = int(off.attrib.get('x', 0)), int(off.attrib.get('y', 0))
            if ext is not None:
                cx, cy = int(ext.attrib.get('cx', 0)), int(ext.attrib.get('cy', 0))
        
        texts = []
        for p in child.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}p'):
            t_str = ''.join([node.text for node in p.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t') if node.text])
            if t_str.strip():
                texts.append(t_str.strip())
        
        full_text = ' '.join(texts).strip()
        
        t_match = re.search(r'Task\s*(\d+)', full_text, re.I)
        if t_match and task_num is None:
            task_num = int(t_match.group(1))
            continue
            
        if full_text in ['Forces and motion', 'Electricity', 'Waves', 'Energy resources and energy transfers', 'Solids, liquids and gases', 'Magnetism and electromagnetism', 'Radioactivity and particles', 'Astrophysics', 'Magnetism  and electromagnetism']:
            section_title = full_text
            continue
            
        if re.match(r'^\d+$', full_text) or full_text.startswith('Complete by'):
            continue
            
        table_rows = []
        if tag == 'graphicFrame':
            tbl = child.find('.//a:tbl', ns)
            if tbl is not None:
                for tr in tbl.findall('a:tr', ns):
                    row_cells = []
                    for tc in tr.findall('a:tc', ns):
                        cell_text = ''.join([node.text for node in tc.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t') if node.text]).strip()
                        row_cells.append(cell_text)
                    table_rows.append(row_cells)
        
        img_file = None
        if tag == 'pic':
            blip = child.find('.//a:blip', ns)
            if blip is not None:
                embed_id = blip.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                img_file = rel_map.get(embed_id)
        
        shapes.append({
            'tag': tag,
            'pos': (x, y, cx, cy),
            'texts': texts,
            'table_rows': table_rows,
            'img_file': img_file
        })

    if task_num is None:
        return None, None, []

    valid_shapes = [s for s in shapes if s['texts'] or s['table_rows'] or s['img_file']]
    valid_shapes.sort(key=lambda s: (s['pos'][1], s['pos'][0]))
    
    # Cluster into subtask boxes (shapes whose y/x center boundaries overlap or are within distance threshold)
    boxes = []
    for s in valid_shapes:
        placed = False
        sy = s['pos'][1]
        sx = s['pos'][0]
        for b in boxes:
            by = b['pos'][1]
            bx = b['pos'][0]
            if abs(sy - by) < 2200000 and abs(sx - bx) < 3500000:
                if s['texts']:
                    for txt in s['texts']:
                        if txt not in b['texts']:
                            b['texts'].append(txt)
                if s['table_rows']:
                    b['table_rows'] = s['table_rows']
                if s['img_file'] and s['img_file'] not in b['images']:
                    b['images'].append(s['img_file'])
                placed = True
                break
        if not placed:
            boxes.append({
                'pos': s['pos'],
                'texts': list(s['texts']),
                'table_rows': list(s['table_rows']),
                'images': [s['img_file']] if s['img_file'] else []
            })
            
    return task_num, section_title, boxes

def format_table(table_rows):
    if not table_rows:
        return ""
    
    md_table = []
    headers = table_rows[0]
    md_table.append('| ' + ' | '.join(headers) + ' |')
    md_table.append('| ' + ' | '.join([':---'] * len(headers)) + ' |')
    
    for row in table_rows[1:]:
        md_table.append('| ' + ' | '.join(row) + ' |')
        
    return '\n'.join(md_table) + '\n\n'

def generate_markdown():
    with zipfile.ZipFile(pptx_path, 'r') as z:
        slide_names = sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)],
                             key=lambda x: int(re.search(r'\d+', x).group()))
        
        md = ['# Edexcel IGCSE Physics (4PH1) - Retrieval Practice Tasks\n\n']
        md.append('Extracted from Science Faculty Learning Log (40 Tasks covering Units 1–8), structured by visual subtask boxes.\n\n---\n\n')
        
        current_unit = None
        
        for slide_name in slide_names:
            task_num, section_title, boxes = parse_slide(z, slide_name)
            if task_num is None or not boxes:
                continue
                
            unit = get_unit(task_num)
            if unit != current_unit:
                current_unit = unit
                md.append(f'## {current_unit}\n\n')
                
            md.append(f'### Task {task_num}\n')
            md.append('**Target**: `Complete by __________________` \n\n')
            
            for idx, b in enumerate(boxes, 1):
                md.append(f'#### Subtask {task_num}.{idx}\n')
                
                # Filter redundant table texts from prompts if table exists
                table_cell_set = set()
                if b['table_rows']:
                    for r in b['table_rows']:
                        for cell in r:
                            if cell:
                                table_cell_set.add(cell)
                                
                prompts = [t for t in b['texts'] if t not in table_cell_set]
                
                for p in prompts:
                    md.append(f'* {p}\n')
                if prompts:
                    md.append('\n')
                    
                if b['table_rows']:
                    md.append(format_table(b['table_rows']))
                    
                for img in b['images']:
                    md.append(f'![Diagram for Subtask {task_num}.{idx}](learning_log_images/{img})\n\n')
                    
                md.append('\n')
                
            md.append('---\n\n')
            
    with open(out_md, 'w', encoding='utf-8') as f:
        f.writelines(md)
        
    print(f"Successfully generated {out_md}")

if __name__ == '__main__':
    generate_markdown()
