import zipfile
import xml.etree.ElementTree as ET
import os

pptx_path = 'reference/IGCSE Physics Learning Log.pptx'

with zipfile.ZipFile(pptx_path, 'r') as z:
    slide_tree = ET.fromstring(z.read('ppt/slides/slide3.xml'))
    
    # Rels to get image filename
    rels_tree = ET.fromstring(z.read('ppt/slides/_rels/slide3.xml.rels'))
    rel_map = {}
    for rel in rels_tree.iter():
        r_id = rel.attrib.get('Id')
        target = rel.attrib.get('Target')
        if r_id and target:
            rel_map[r_id] = os.path.basename(target)

    ns = {
        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }
    spTree = slide_tree.find('.//p:spTree', ns)
    shapes = []
    for child in spTree:
        tag = child.tag.split('}')[-1]
        
        # Look for xfrm
        xfrm = child.find('.//a:xfrm', ns)
        if xfrm is None:
            # Maybe inside p:spPr
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
        
        img_file = None
        if tag == 'pic':
            blip = child.find('.//a:blip', ns)
            if blip is not None:
                embed_id = blip.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                img_file = rel_map.get(embed_id)
        
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
        
        shapes.append({
            'tag': tag,
            'pos': (x, y, cx, cy),
            'texts': texts,
            'img_file': img_file,
            'table_rows': table_rows
        })

    print(f"Total shapes on Slide 3: {len(shapes)}")
    for i, s in enumerate(shapes):
        tag = s['tag']
        x, y, w, h = s['pos']
        print(f"--- Element {i+1} [{tag}] (x={x}, y={y}, w={w}, h={h}) ---")
        if s['img_file']:
            print(f"   IMAGE: {s['img_file']}")
        if s['table_rows']:
            print(f"   TABLE ({len(s['table_rows'])} rows): {s['table_rows']}")
        if s['texts']:
            print(f"   TEXT ({len(s['texts'])} lines): {s['texts']}")
