# Writing guidelines

A living record of the conventions we're settling on as notes get rewritten,
and of the content-type taxonomy as we discover it. Per `CLAUDE.md`, the
taxonomy is being built up from concrete examples rather than designed
up front — this file is where that accumulates. Update it whenever a new
convention is agreed, or a new content type shows up that doesn't fit the
existing list.

## Content type taxonomy (so far)

Based on `docs/Unit 5/5_1_1_density.md`.

| Content type | Markdown convention | Purpose |
| --- | --- | --- |
| Definition | `!!! abstract "Definition: <Term>"` | Formal statement of a term/quantity: word equation, symbol equation, units, and any notable properties (e.g. scalar/vector). |
| Warning / common pitfall | `!!! warning "Warning:"` | Flags a common mistake or confusable notation (e.g. ρ vs p). |
| Required formula(e) | `!!! note "Required formulae: <topic>"` | Spec-required formula(e) not already covered inside a Definition block — sometimes given as a diagram/image rather than typeset. |
| Memory aid / technique | nested `??? note "..."` inside a Definition (collapsible) | A study technique or mnemonic (e.g. formula triangle) — useful but not itself examinable content. |
| Worked example (calculation) | `!!! Example "Worked Example (calculation)"` + nested `??? success "Answer:"` | A calculation-style question with a step-by-step, initially-hidden answer. |
| Examiner tips | `!!! tip "Examiner Tips and Tricks"` | Exam technique advice — not core content, but useful guidance (unit conversion, how to structure a practical write-up, etc). |
| Core practical | `## Core practical N: <name>` heading, with sub-headings (Equipment / Variables / Method / Results / Analysis of results / Evaluating the experiments → Systematic errors / Random errors / Safety considerations); split into `=== "<case>"` tabs when the practical varies by scenario | Structured, multi-part write-up matching the Edexcel "core practical" requirement. |
| Side note / aside | plain prose under a sub-heading, no admonition | Supplementary, non-examinable context: common misconceptions, extra depth, historical anecdotes. |
| Reference data | plain markdown table, no admonition | Supplementary factual data (e.g. typical densities) — not a formula to apply, not narrative prose either. |
| Illustrative diagram | plain image, no admonition | Supports the surrounding prose directly (e.g. particle-arrangement diagram) — distinct from a *Required formula* diagram, which is spec content to memorise and apply. |
| Cross-syllabus application / link | plain prose with an inline markdown link | Points to where a concept is used or reappears elsewhere in the syllabus (e.g. density → convection currents). |

Not yet seen in this note but worth watching for as we do more pages:
worked examples that aren't calculations (e.g. "explain" / "describe"
questions), and the "Classical practical" idea mentioned in `CLAUDE.md`
(practicals beyond the specified core-practical list).

## General writing principles

- **Prefer prose over bullet lists.** Reserve bullets for genuinely
  parallel/discrete items (a sequence of steps, several independent
  variables, a handful of independent tips). A single point wrapped in a
  bullet should just be a sentence.
- **Admonition titles use a `Label: specifics` pattern** where it helps
  scanning — e.g. `Definition: Density`, `Required formulae: volumes of
  simple shapes` — so the content *type* is visible at a glance, separate
  from the specific topic.
- **Core practicals keep every tab present across every sub-section**, even
  when a tab ends up empty for a given scenario (e.g. "Regular solid" has
  no extra Safety considerations beyond the others) — rather than dropping
  the tab. Keeps navigation predictable across practicals.

## Open questions / future ideas (parking lot)

Ideas to revisit later — not implemented now.

- **Silently tagging individual content blocks.** The eventual goal (see
  `CLAUDE.md`, convergence with the revision platform / question DB) is
  sub-page tagging — a specific Definition or worked example carrying
  spec-point/content-type metadata, not just the page it lives on.
  Admonitions like Definition/Required formulae/Worked Example already
  self-identify via their title; the gap is the untitled prose (asides,
  reference data, cross-links). Two candidate mechanisms for later:

  1. **HTML comments** as inline markers, e.g.
     `<!-- tag: type=aside -->` placed just before a block. Fully invisible
     on the rendered page (HTML comments are stripped by Python-Markdown),
     cheap to add, greppable — but only readable from the markdown source,
     not from the built site.
  2. **`attr_list`** (already enabled in `mkdocs.yml`), e.g.
     `{: #density-def .content-definition }` attached to a block. Produces
     real ids/classes in the rendered HTML, so a script could crawl the
     *built* site rather than the source, and it opens the door to
     future CSS/JS tooling (e.g. "show only Worked Examples"). More
     visible in the markdown source, and has syntax constraints on which
     elements can carry it.

  Likely direction when we get there: comments for cheap/invisible
  tagging now, `attr_list` if/when tags need to survive into the built
  site for tooling. Not adopting either yet — revisit once the taxonomy
  above has settled and there's a concrete tagging task to do.

## Change log

- 2026-08-11: initial version, drafted from `docs/Unit 5/5_1_1_density.md`.
