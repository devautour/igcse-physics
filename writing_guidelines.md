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
| Worked example (calculation) | `!!! example "Worked Example (calculation)"` + nested `??? success "Answer:"` | A calculation-style question with a step-by-step, initially-hidden answer. Steps follow the sequence **identify the known quantities (reading from a graph/data where relevant) → state the relevant formula/principle → substitute the known values (converting units where necessary) → rearrange → evaluate → give the answer to an appropriate precision, with unit** — matching how Edexcel mark schemes actually award marks. Substitution happens *before* rearranging: plug the raw numbers into the formula as stated, then rearrange the numeric equation to isolate the unknown, rather than rearranging symbolically first and substituting at the end. Steps are optional/mergeable depending on context — skip "rearrange" entirely when the stated formula is already solved for the quantity asked for; merge "substitute" and "evaluate" into one step for a single-line calculation; state the formula before identifying quantities when the quantities to read (e.g. which areas to measure under a graph) only make sense once the method is known. See the change log entry below (2026-08-18) for the worked-examples-alignment pass that established this. |
| Worked example (explanation) | `!!! example "Worked Example (explanation): <name>"` + nested `??? success "Model answer:"` | An "explain how/why..." style question with a qualitative (non-numeric) model answer, initially hidden — the descriptive counterpart to the calculation type (e.g. explain how an airbag reduces injury, or why a drawing pin behaves as it does). |
| Worked example (multiple choice) | `!!! example "Worked Example (multiple choice)"` + nested `??? success "Answer: <letter>"` | A question with lettered options (A/B/C/D...), where the hidden answer explains why the correct option is right *and* why each distractor is wrong — not just a calculation or a single explanation. |
| Worked example (method) | `!!! example "Worked Example (method)"` + nested `??? success "Answer:"`, steps as bold `**Step N: ...**` labels like a calculation | A step-by-step worked example that applies a physical *technique/rule* rather than doing arithmetic or writing prose — e.g. using Fleming's left-hand rule to find a force's direction, or the direction of rotation of a d.c. motor. Distinct from *calculation* (no numbers/substitution) and from *explanation* (has discrete, orderable steps, not a flowing model-answer paragraph). |
| Examiner tips | `!!! tip "Examiner Tips and Tricks"` | Exam technique advice — not core content, but useful guidance (unit conversion, how to structure a practical write-up, etc). |
| Beyond-spec extension | `??? info "Beyond the spec: <topic>"` (collapsible) — add `(A-Level preview)` after "Beyond the spec" *only* when the content genuinely belongs to a more advanced course, not just to a different spec/board | Content explicitly flagged as going beyond the **4PH1** spec specifically — optional depth for a curious reader, not something to be tested on. **Verify against `reference/spec_points.md` before adding one of these**, not from general physics knowledge of what's "usually" covered — content can be beyond 4PH1 without being beyond GCSE generally (e.g. specific latent heat is on other exam boards' GCSE specs, so it's inaccurate to call it "A-Level"; the momentum/impulse aside genuinely is A-Level content, so that qualifier stays there). Distinct from a *Memory aid* (a technique, not extra content) and from a plain *Side note* (this one is collapsible and explicitly labelled out-of-spec, so a reader can safely skip it). |
| Core practical | `## Core practical N: <name>` heading, with sub-headings (Equipment / Variables / Method / Results / Analysis of results / Evaluating the experiments → Systematic errors / Random errors / Safety considerations); split into `=== "<case>"` tabs when the practical varies by scenario | Structured, multi-part write-up matching the Edexcel "core practical" requirement. |
| Classic practical | `## Classic practical: <name>` heading, lighter-weight than a Core practical (so far just a short intro + a plain **Method** list — no Equipment/Variables/Results apparatus) | The "Classical practical" idea from `CLAUDE.md`: a hands-on activity that isn't one of the specified Core Practicals but is commonly used to tie concepts together (e.g. measuring the pressure a person exerts on the floor). First instance is provisional — revisit its structure once we have more than one example. |
| Practical/mathematical skill | `!!! note "Practical skill: <topic>"` | A reusable technique needed to obtain or process data (e.g. estimating an irregular area by counting squares on graph paper) — itself examinable, unlike a *Memory aid*, but not tied to one specific practical the way a Core/Classic practical's Method is. |
| Memory aid / technique | nested `??? note "..."` inside a Definition (collapsible) | A study technique or mnemonic (e.g. formula triangle) — useful but not itself examinable content. |
| Side note / aside | plain prose under a sub-heading, no admonition | Supplementary, non-examinable context: common misconceptions, extra depth, historical anecdotes. |
| Reference data | plain markdown table, no admonition | Supplementary factual data (e.g. typical densities) — not a formula to apply, not narrative prose either. |
| Illustrative diagram | plain image, no admonition | Supports the surrounding prose directly (e.g. particle-arrangement diagram) — not itself examinable, distinct from both *Required formula* diagrams and *Classic* diagrams below. |
| Classic diagram | `!!! info "Classic diagram: <topic>"` | A diagram that isn't a formula, but that students are expected to recognise/reproduce because it shows up directly in exam questions (e.g. the arrows-from-all-directions diagram for pressure on a submerged object) — distinct from an *Illustrative diagram*, which only supports the prose and isn't itself exam content. **Criteria still fuzzy** — see parking lot. |
| Cross-syllabus application / link | plain prose with an inline markdown link, usually under its own `### Applications in the IGCSE syllabus` sub-heading | Points to where a concept is used or reappears elsewhere in the syllabus (e.g. density → convection currents, pressure → ideal gas laws). |
| Principle | `!!! abstract "Principle: <name>"` | A general physical law/rule being asserted, rather than a term/quantity being named — e.g. conservation of energy, conservation of charge. Same admonition type as Definition (`abstract`) since both are formal statements the reader should take as given, but titled `Principle:` instead of `Definition:` to distinguish "here is a law" from "here is what this word means". First seen independently in Unit 2 (`!!! abstract "Principle of Conservation of Charge:"`, light-touch-fixed rather than retitled) and introduced directly in this form in `4_2_energy-stores-and-transfers.md`'s conservation of energy section. |

Rejected: **"Worked example (application)"** — a first attempt at labelling
short illustrative scenarios (drawing pin, tractor tyres, heeled shoes...)
that had no question/answer structure, just a flat explanation. Turned out
these were really unstated "explain why..." questions, so they were
rewritten as **Worked example (explanation)** instead (with the question
made explicit and the explanation moved into a hidden model answer) rather
than kept as a separate type. If a genuinely different "just an
illustration, not a question" case shows up later, reconsider — but treat
that as the higher bar to clear now, not the default.

## General writing principles

- **When a page is already well-written, switch to a light touch rather
  than a full rewrite.** Discovered in Unit 2's electrostatics files
  (`2_1_1`–`2_1_3`), which turned out not to be raw Save My Exams-style
  bullet dumps but already-flowing prose using patterns not seen
  elsewhere on the site (`Model explanation:`/`Standard Explanation:`,
  `Principle of X:`). For pages like this: fix only unambiguous bugs
  (stray trailing colons, admonition-type typos, casing slips, TODO
  formatting) and leave prose/structure alone — do **not** silently
  resolve taxonomy questions the page's own conventions raise (see the
  Model/Standard-Explanation and bare-Note-admonition items in the
  parking lot below); flag those for the user instead. Read the whole
  batch of files before committing to full-rewrite-everywhere, since
  quality varies file to file within the same unit.

- **Prefer prose over bullet lists.** Reserve bullets for genuinely
  parallel/discrete items (a sequence of steps, several independent
  variables, a handful of independent tips). A single point wrapped in a
  bullet should just be a sentence.
- **Admonition titles use a `Label: specifics` pattern** where it helps
  scanning — e.g. `Definition: Density`, `Required formulae: volumes of
  simple shapes` — so the content *type* is visible at a glance, separate
  from the specific topic.
- **Fix visible typos in page text (H1/headings/prose); never rename the
  underlying file or its `mkdocs.yml` nav entry as part of a content
  rewrite.** `7_3_uses-and-hasards-of-radioactivity.md`'s H1 said "hasards"
  — fixed the heading text to "hazards" (what a reader sees), left the
  filename and nav path alone. Renaming those is a coordinated,
  higher-blast-radius change (breaks bookmarks/links, needs `mkdocs.yml`
  updated in lockstep) that belongs with the other filename/nav mismatches
  `CLAUDE.md` already tracks as a known issue, not something to fix
  incidentally while rewriting prose.
- **Core practicals keep every tab present across every sub-section**, even
  when a tab ends up empty for a given scenario (e.g. "Regular solid" has
  no extra Safety considerations beyond the others) — rather than dropping
  the tab. Keeps navigation predictable across practicals.
- **Core/Classic practical heading depth is fixed**: `##` for the
  practical itself, `###` for its sub-sections (Equipment / Variables /
  Method / Results / Analysis of results / Evaluating the experiment(s)),
  `####` for Systematic errors / Random errors / Safety considerations
  nested under Evaluating. `5_2_2_heat-and-temperature.md`'s Core practical
  11 was found one level too deep throughout (`###`/`####`/`#####`) and
  promoted to match. Also drop a standalone "Aims of the experiment"
  sub-heading when it's a single sentence — fold it into the lead
  paragraph right under the practical's own heading instead (as Core
  practical 9 already did), rather than giving one sentence its own
  heading.
- **A clean `mkdocs build` only proves the page parses — verify the
  markdown source is even valid before assuming a rewrite is cosmetic.**
  This pass surfaced real pre-existing bugs unrelated to bullets/tone: an
  admonition title missing its closing quote
  (`??? info "More details (A Level preview)`, no closing `"`, in
  `5_3_1_kinetic-theory-of-gases.md`), stray colons after a closing quote
  (`!!! abstract "Definition: Absolute zero":`), a `??? "Answer:"` missing
  its `success` type, and a sentence duplicated with typos right after the
  original. None of these necessarily throw a build error — read the
  actual diff/rendered output, don't assume the source was well-formed
  going in.
- **Admonition type keywords are lower-case** (`!!! example`, not
  `!!! Example`) — matches `note`/`warning`/`tip`/`abstract` and avoids an
  arbitrary-looking inconsistency between blocks.
- **Symbol conventions are decided once and then enforced everywhere they
  recur, not just on the page that introduces them.** Confirmed so far:
  pressure is $p$ (lower-case), not $P$ — this is the advised notation
  even though it does the opposite of helping distinguish it from $\rho$
  (density); that's exactly why a warning belongs wherever the two symbols
  meet in the same formula (e.g. $p = h \rho g$ in
  [Pressure](docs/Unit%205/5_1_2_pressure.md)), not just a general warning
  on the page that first introduces $\rho$. When a note reuses a symbol/
  formula introduced elsewhere, check the source page for the convention
  rather than re-deriving it from scratch. The same clash-and-warn pattern
  applies to $p$ itself: pressure ($p = F/A$) and momentum ($p = mv$) share
  the same symbol for genuinely different quantities, which matters
  wherever a topic can be explained through either one (e.g. airbags/knee
  pads, in [Pressure](docs/Unit%205/5_1_2_pressure.md)) — flag it with a
  Warning at the point the two stories actually meet, same as ρ vs p.
  When the spec itself gives a symbol unambiguously, match it exactly:
  `6_4_transformers.md` mixed lower-case $n_p$/$n_s$ (in its own stated
  equation) with upper-case $N_p$/$N_s$ (in its own worked example) for
  the same quantity — `reference/spec_points.md` (6.19P) uses $N_p$/$N_s$,
  so that's the one to standardise on, not whichever one happens to be
  more common in the page being edited.
- **Check for duplicated content blocks, not just bullet overuse.** The
  source material repeats itself at the paragraph level, not just within
  a sentence: `6_2_motor-effect.md` had two near-word-for-word treatments
  of the straight-wire magnetic field (one as a general intro section, one
  nested under "Magnetic Field Patterns") — consolidate into one, keeping
  the union of any unique images. Smaller duplications turned up too (a
  repeated bullet in `6_3_induction.md`'s definition section, two
  redundant paragraphs both explaining why low current reduces
  transmission loss in `6_4_transformers.md`). When a page covers the same
  fact twice, merge it into the single best-placed treatment rather than
  polishing both copies independently.
- **Unfinished content is marked with an HTML comment, not visible
  placeholder text.** Convention:

  ```
  <!-- TODO: short description of what's missing
  * optional checklist of specific things to add
  * one per line
  -->
  ```

  Open (`<!-- TODO...`) and close (`-->`) make the scope of "not done yet"
  explicit and unambiguous, unlike the old bare `[TODO]` marker (which had
  no closing delimiter and blended into the following bullet list). It also
  means the placeholder text itself never shows up as reader-facing content
  once it's live on the site (comments aren't rendered, though they do
  still land in the page's raw HTML — so don't put anything sensitive in
  one). A TODO is a request for something to actually get done, not a
  permanent fixture: once it's addressed, delete the whole comment rather
  than leaving it in place. `grep -r "<!-- TODO" docs/` finds every
  outstanding one. A TODO (however written — `TODO`, possibly `to do`) is
  standing permission to act on it directly when spotted, without waiting
  to be asked again — see also TODO assignees in the parking lot below.
- **When a diagram is needed and no source asset covers it, draw one —
  don't just describe what's missing or leave a placeholder.** First
  instance: the pressure formula triangle. Save it as its own file in
  `docs/assets/images/` (SVG is fine there alongside the extracted
  `.jpg`/`.png` files — see `pressure_force_area_formula_triangle.svg`)
  and reference it with an ordinary `![...](../assets/images/...)`, same
  as every other diagram — **not** inline in the markdown. First attempt
  got this wrong (embedded the raw `<svg>` directly inside the `??? note`
  block); reverted after the source-readability cost was pointed out —
  large inline markup buries the surrounding prose structure, which is
  exactly what every other diagram convention on this site avoids. Verify
  a hand-built diagram by rendering it via `mkdocs serve` and
  screenshotting it, not just by a clean `mkdocs build` — that only
  catches parse errors, not layout (text overflowing a shape, etc). This
  is a genuine alternative to the two existing diagram sources (an
  extracted raster image, or a `mermaid` graph like the ones still used
  elsewhere, e.g. in `5_3_1`/`5_3_2`) — reach for it when neither of those
  fits and the diagram is simple enough to draw directly (mnemonic
  triangles, basic labelled shapes), not for anything that needs real
  illustrative detail.

## Notes on the source material

A lot of the current `docs/` content was parsed from Save My Exams revision
notes. That source leans heavily on bullet points (including single-point
"bullets" that are really just sentences) and inconsistent admonition
titling/structure page to page — expect this on most unrewritten pages, not
just the two done so far. Treat bullet-heavy phrasing and inconsistent
admonition titles as a default symptom of the source material rather than a
one-off, and fix it opportunistically as each page is touched, rather than
trying to sweep the whole `docs/` tree at once.

One pattern considered and **not** adopted: using blockquotes (`>`) to
echo/highlight a key sentence or formula. First seen in the "Shoes"
application example in `5_1_2_pressure.md`, rewritten as prose — it then
turned up *again*, independently, in `5_2_2_heat-and-temperature.md`
(highlighting "Electrical energy = voltage × current × time" and a
gradient/SHC sentence), also rewritten as bold prose. Two independent
occurrences means this isn't a one-off fluke — it's a recurring habit of
the source material. Keep rewriting it as prose (plain sentence, **bold**
where a term/equation needs emphasis) rather than adopting blockquote as a
convention. A related but distinct misuse showed up in Unit 6: a
blockquote holding an actual **Definition** (`6_1_magnets-and-magnetic-fields.md`'s
"A magnetic field is defined as: > The region around a magnet...",
`6_3_induction.md`'s definition of electromagnetic induction) — these
aren't a highlighted-sentence problem, they're a mislabelled *content
type* problem: the blockquote was standing in for a `!!! abstract
"Definition: ..."` admonition that should have been there from the start.
When a blockquote turns up, don't default to "make it prose" — check
whether it's actually a Definition, a Required formula, or something else
with its own established convention first. By Unit 7 the real tell turned
out not to be the blockquote at all — it's the phrase **"X is defined
as:"** (or "X is defined by:") immediately followed by a bolded sentence,
which shows up constantly, with or without a blockquote around the bold
part (isotope, activity, background radiation, half-life, contamination,
irradiation, nuclear fission, nuclear fusion, chain reaction — nine more
instances across `7_1`–`7_4`, none of them blockquoted). Treat "is defined
as:" followed by bold as the actual signal to look for, not the blockquote
syntax specifically — grep for it (`grep -rn "defined as:" docs/`) on any
page before considering it done.

Two more recurring bug categories, on top of duplication and
rendering-breaking syntax (see below): **tables split into two adjacent
`<table>` blocks that should be one** — a header-only table immediately
followed by a data-only table with no header (`7_1`'s "Summary of
properties of nuclear radiation"), or a 3-row table followed by a
separate 1-row table continuing the same series (`7_2`'s half-life
proportion table) — merge these into a single table rather than leaving
them split. And **image references to files that don't exist at all**,
not just missing the `../assets/images/` path prefix — `7_1`'s alpha/beta/gamma
comparison table pointed at `page_423_image_5_v2.jpg` and
`page_423_image_4_v2.jpg` (the latter reused for *both* the beta and
gamma rows), neither of which exists in `docs/assets/images/`. Since the
table's content was also fully redundant with the prose directly above
it, and inventing a replacement image wasn't warranted, it was dropped
entirely — but always run `ls docs/assets/images/ | grep <name>` to check
a referenced image actually exists before deciding whether to fix the
path or remove the reference.

Also seen: headings with **zero content** before the next same-level
heading. Two different root causes turned up in `7_4_fission-and-fusion.md`,
and they need different fixes — check which one applies before touching
anything: "Nuclear reactors" had no content of its own because the
content that should have been there was one heading down, under a
wrongly-nested "Control rods & moderators" sibling (a *misplacement*, fixed
by restructuring); "Conditions for nuclear fusion" was empty because that
exact content already existed later in the same page, under
"Disadvantages of fusion reactors" (a genuine *duplicate/orphan*, fixed by
deleting the empty heading). Neither of these is the `<!-- TODO -->`
case from `6_3_induction.md`, where the heading was empty because the
content was never written at all — don't assume that's always what an
empty heading means.

Other recurring bug categories worth actively scanning for, beyond bullet
overuse: content pulled entirely outside its admonition by missing/wrong
indentation (`6_4_transformers.md`'s second transformer worked example had
zero indentation, so the whole question+answer rendered as ordinary page
text, not inside the example box); admonitions missing their type keyword
or title quotes entirely (`!!! Worked Example` with no `"..."`, in
`6_2_motor-effect.md`); a typo'd admonition marker (`!+!` instead of `!!!`
in `6_3_induction.md`, which would have rendered as literal text); and two
bullets glued onto one line with no line break between them
(`6_2_motor-effect.md`'s D.C. motor section). None of these are style
issues — they're rendering bugs that predate any rewrite, and a clean
`mkdocs build` won't necessarily catch them (see the principle above on
verifying source validity).

Three more bug categories, found across Units 2–4: **tab content assigned
to the wrong tab**, not just tabs left empty — `3_4_sound-waves.md`'s Core
practical had *all* equipment (both the clap-method items and the
oscilloscope-method items) listed under the `=== "clap"` tab, leaving
`=== "Using Oscilloscope"` completely empty; fixed by actually splitting
the equipment between the two tabs based on which method uses which item,
not just by reading the tab labels. **A page's H1 not matching its actual
content** — `3_1_describing-waves.md`'s H1 read "Waves & The
Electromagnetic Spectrum", but the page only covers wave basics (the EM
spectrum is `3_2`'s separate topic); corrected the heading text only, per
the filename/nav-untouched principle above. And **factual errors in the
source material itself**, not just broken syntax or awkward phrasing —
`4_4_energy-resources.md`'s Solar cells section stated energy is
transferred "from the nuclear store of the Sun to the **thermal** store of
the solar cell", which is physically wrong (solar cells convert light
directly to electrical energy via the photovoltaic effect, with no thermal
intermediate — that's what the separate Solar Heating Panels section
correctly describes); it also called the light-absorbing part of a solar
cell "the metal", when it's a semiconductor. Both fixed by checking against
actual physics rather than assuming the source prose is trustworthy just
because it parses cleanly — this is a different kind of check from the
syntax/rendering bugs above and needs subject-matter judgement, not just
careful reading.

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
     `<!-- tag: type=aside -->` placed just before a block. Not rendered as
     visible content (correction from an earlier draft of this note: the
     comment itself still lands in the built page's raw HTML, just not
     shown to a reader — confirmed by inspecting a build), cheap to add,
     greppable from the markdown source. The [TODO marker
     convention](#general-writing-principles) above is the first concrete
     use of this — worth revisiting whether the same mechanism extends
     naturally to content-type/spec-point tags.
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
- **What actually makes a diagram "classic".** Introduced for the
  pressure-on-a-submerged-object diagram in `5_1_2_pressure.md`, but on
  reflection the criterion for "this specific diagram shows up in exam
  questions" isn't pinned down — confirmed *not* to apply to the nearby
  depth/density/pressure diagram (illustrates the formula's variables,
  nothing more), but the general rule that separates the two cases is
  still unclear even to the person making the call. Second data point: the
  changes-of-state cycle diagram in `5_2_3_temperature-and-changes-of-state.md`
  (solid/liquid/gas with all six named transitions) was also marked
  Classic — both instances so far are diagrams where the exam question
  *is* "label/reproduce this diagram", as opposed to a diagram that just
  supports understanding a formula. That's a plausible dividing line, but
  still only two examples; not urgent, revisit once more have come up.
- **TODO assignees.** Possibly extend the `<!-- TODO -->` convention with
  who's meant to act on it, e.g. `<!-- TODO @Claude: ... -->` vs
  `<!-- TODO @me: ... -->` (or other collaborators, e.g. `@Gemini`) once
  more than one kind of "who does this" shows up in practice. Not adopted
  yet — for now every TODO is treated as actionable by Claude on sight.
- **"Model explanation:" / "Standard Explanation:" admonitions.** Found in
  Unit 2's electrostatics files (`!!! abstract "Model explanation: ..."` in
  `2_1_1`, `!!! abstract "Standard Explanation: ..."` in `2_1_2`/`2_1_3` —
  inconsistently cased between files, and not one of the labels in the
  taxonomy table above). Left as-is under the light-touch policy rather
  than unified or retitled unilaterally. Open question for the user: is
  this a distinct content type (a memorised standard-answer pattern for a
  recurring exam question format, e.g. "explain why a charged rod attracts
  an uncharged object") from `Worked example (explanation)`, or should it
  just be folded into that existing type and the casing made consistent?
- **Bare `!!! note "Note:"` admonitions.** Also from the Unit 2
  electrostatics files — a short aside wrapped in a titled `note`
  admonition, distinct from the existing untitled-prose *Side note* row in
  the taxonomy (which uses no admonition at all). Left as-is under the
  light-touch policy. Open question: promote this to its own taxonomy row
  (a "boxed aside", visually separated but not collapsible/labelled like
  Beyond-spec-extension), or treat it as a Side note that should lose its
  admonition wrapper next time the page gets a full rewrite?

## Change log

- 2026-08-18: reviewed all "Worked example (calculation)" blocks site-wide (54 instances across 26 files, Units 1–8) against the step sequence identified from mark-scheme analysis in the separate `question-clips`/`mark-scheme-parsing` projects: identify known quantities → state formula/principle → substitute (converting units where necessary) → rearrange → evaluate → state the answer to an appropriate precision, with unit. Added this sequence to the taxonomy row above. The one recurring, high-value structural bug found: many examples rearranged the equation symbolically *before* substituting numbers in (e.g. `1_1_4_equations-of-motion.md`'s braking-distance example, `5_1_2_pressure.md`'s hydraulic-lift and depth-in-fluid examples, `5_3_2_ideal-gas-laws.md`'s pressure-law and Boyle's-law examples, `6_4_transformers.md`'s turns-ratio example, `8_3_cosmology.md`'s Doppler-shift example, plus others in Units 1–4) — reordered these so raw numbers are substituted into the formula first, then the numeric equation is rearranged, matching how mark schemes actually award substitution/rearrangement/evaluation marks separately. Left examples unchanged where the stated formula was already solved for the quantity being asked for (no rearranging needed), and left Unit 7's calculation examples alone entirely — they turned out to be counting/graph-reading exercises (protons/neutrons/electrons, activity × time, half-life from a graph) rather than algebraic rearrangements, so the substitute-before-rearrange fix didn't apply. Also added explicit "give the answer to an appropriate precision, with unit" closing steps to several examples that previously stopped at a bare evaluated number.
- 2026-08-11: initial version, drafted from `docs/Unit 5/5_1_1_density.md`.
- 2026-08-11: rewrote `docs/Unit 5/5_1_2_pressure.md` for consistency with
  the above. Added the "Worked example (application)" content type,
  the lower-case-admonition-keyword and symbol-consistency principles, and
  the note on Save My Exams source material above.
- 2026-08-12: replaced the bare `[TODO]` marker with an HTML-comment
  open/close convention (see General writing principles), applied to the
  one outstanding TODO in `5_1_2_pressure.md`. Corrected the parking-lot
  note above, which had wrongly said HTML comments are stripped entirely.
- 2026-08-12: acted on the user-edited TODO in `5_1_2_pressure.md` (now
  removed). Added "Worked example (explanation)" and "Classic diagram" to
  the taxonomy, extended the symbol-clash principle to cover $p$ (pressure)
  vs $p$ (momentum), and added the TODO-assignee idea (`@Claude`/`@me`) to
  the parking lot.
- 2026-08-12: retired "Worked example (application)" — merged into
  "Worked example (explanation)" by rewriting all five instances in
  `5_1_2_pressure.md` as explicit question + hidden model answer. Acted on
  a second TODO (also now removed): added a plain calculation worked
  example, introduced "Practical/mathematical skill" and the first
  "Classic practical" (pressure exerted by a person on the floor) to the
  taxonomy. Confirmed the depth/density diagram in `5_1_2_pressure.md` is
  *not* a Classic diagram, and logged that the general criterion for
  "classic" is still unclear as a parking-lot item.
- 2026-08-12: acted on a third TODO in `5_1_2_pressure.md` asking for a
  diagram (the user had deleted the page's existing `mermaid` formula
  triangle first). Built one from scratch — new principle logged above.
  Also deduplicated a "Memory aid / technique" taxonomy row accidentally
  left in twice.
- 2026-08-12: corrected the new diagram above — first attempt embedded the
  SVG inline in the markdown, which the user pointed out hurts source
  readability and breaks from how every other diagram on the site is
  done. Moved it to `docs/assets/images/pressure_force_area_formula_triangle.svg`
  and referenced it normally; updated the principle to say so explicitly.
- 2026-08-12: rewrote the rest of Unit 5 (`5_2_1`–`5_3_2`) for consistency
  with the above. Added "Worked example (multiple choice)" and
  "Beyond-spec extension" to the taxonomy; added a second Classic-diagram
  data point (changes-of-state cycle); fixed the Core/Classic practical
  heading-depth inconsistency and folded "Aims" into lead prose across all
  three practicals; fixed several pre-existing source-file syntax bugs
  (unclosed admonition quotes, missing `success` type, stray colons, a
  duplicated/garbled sentence); drew four more SVG diagrams (three
  solid/liquid/gas particle diagrams replacing broken `image_url_placeholder`
  refs, one pressure–temperature extrapolation-to-absolute-zero graph);
  the blockquote-as-highlight pattern recurred independently, confirming
  it's a recurring source habit, not a one-off.
- 2026-08-12: added a "Beyond the spec: specific latent heat" aside to
  `5_2_3_temperature-and-changes-of-state.md`, confirmed absent from 4PH1
  by checking `reference/spec_points.md` (Section 5, 5.1–5.22) directly
  rather than assuming from general GCSE knowledge. Split the
  "(A-Level preview)" qualifier out of the Beyond-spec-extension row as
  optional/conditional — it only applies when content genuinely belongs to
  a *more advanced course*, not merely to a different exam board's GCSE
  spec, which specific latent heat is an example of (unlike the momentum
  aside, which is genuinely A-Level). Also saved a persistent memory
  pointing at `reference/spec_points.md` as the authoritative spec-scope
  check for future sessions.
- 2026-08-12: rewrote all of Unit 6 (`6_1`–`6_4`) for consistency with the
  above. Added "Worked example (method)" to the taxonomy (Fleming's-rule
  and motor-rotation examples: step-by-step but non-numeric). Added three
  more Beyond-spec-extension instances (induction chargers/heaters/
  microphones in `6_3_induction.md`, verified absent from spec 6.15–6.20P).
  Found and fixed a new class of issue beyond bullets/tone: real
  duplicated content (a near-verbatim repeated section in
  `6_2_motor-effect.md`, smaller repeats in `6_3`/`6_4`) and several
  rendering-breaking syntax bugs (zero-indented content escaping its
  admonition, a missing admonition type/quotes, a typo'd `!+!` marker, two
  bullets glued onto one line, garbled mermaid node labels). Fixed an
  $N_p$/$n_p$ case-inconsistency in `6_4_transformers.md` by matching
  `reference/spec_points.md`'s notation. Broadened the blockquote-misuse
  note: it's not just a highlight-pattern habit, it also shows up hiding
  an actual Definition that should have been its own admonition. Logged
  both new bug categories (duplication, rendering-breaking syntax) as
  general principles, not one-off fixes.
- 2026-08-12: rewrote all of Unit 7 (`7_1`–`7_4`) for consistency with the
  above — the largest pass so far. Confirmed "is defined as:" + bold as
  the real signal for a missing Definition admonition (nine more
  instances, most not even blockquoted); found and fixed split-table and
  non-existent-image-reference as two new bug categories; found two
  differently-caused empty headings in `7_4` (misplaced content vs. a
  genuine orphaned duplicate) and fixed each appropriately rather than
  treating both the same; fixed a stray extra quote and an all-caps
  `ANSWER:` (cosmetic variants of the missing-`success`-type bug already
  logged). Acted on two TODOs in `7_3_uses-and-hasards-of-radioactivity.md`
  (radioactivity as a power source; a worked example showing why half-life
  matters for source selection), plus filled a gap where the page's own
  intro promised "determining the age of ancient artefacts" as a use of
  radioactivity but never delivered it (added radiocarbon dating). Fixed
  the H1 typo "hasards" → "hazards" in that page's visible heading only,
  explicitly *not* touching the filename or `mkdocs.yml` nav entry — new
  principle logged above to keep that boundary clear going forward. Left
  one page-content decision unmade: whether to draw an actual line-plot
  SVG for `7_2_radioactivity-and-half-life.md`'s two duplicate "results"/
  "graph" tables (merged them into one data table instead, describing the
  trend in prose, rather than fabricating a chart under time pressure).
- 2026-08-12: rewrote all of Unit 8 (`8_1`–`8_3`) for consistency with the
  above — smaller than Unit 7 but with its own bugs: a broken
  `!!! "tip" Examiner Tips and Tricks` (type/quotes in the wrong order,
  `8_2_stellar-evolution.md`), two byte-for-byte duplicate tables in the
  same worked example (merged), and — the one flagged in every build log
  this entire session — `8_3_cosmology.md`'s
  `../assets/images/image_url_placeholder`, which never resolved to a real
  file. Checked whether its content was redundant with the Doppler
  diagram already present earlier on the same page (it was) and dropped
  it, rather than inventing a replacement; confirmed via `mkdocs build`
  that this was the actual source of that recurring warning, not a
  separate problem — first time this session a build has come back with
  *zero* warnings of any kind. Also dropped a second dead visual in the
  same file: a "wave pattern" table entirely of `[wave]`/`[bracket]`
  placeholders with no real content, nested inside a tip whose actual
  value was the prose analogy below it. Six more "is defined as:"
  instances converted to Definition admonitions (Universe, galaxy,
  weight, orbital period, luminosity, apparent/absolute magnitude — the
  last with a source typo, "defined a" missing its final "s" — plus
  Doppler shift and redshift, both added as new Definitions even though
  the source never used the "is defined as:" phrasing for them, since
  each is the literal subject of its own page section and was otherwise
  only ever defined diffusely across several bullets). Fixed one
  content gap: the low-mass star life-cycle diagram and arrow-chain both
  name a "planetary nebula" stage between red giant and white dwarf, but
  the prose only ever explained the other two stages — added the missing
  explanation. Retitled a heading that had been phrased as a literal exam
  question ("What are two pieces of evidence that support the Big Bang
  theory?") to plain prose, and fixed one external savemyexams link that
  should have been an internal anchor to a section already present later
  on the very same page.
- 2026-08-12: rewrote all of Units 2–4 for consistency with the above —
  the first pass with genuinely mixed source quality within one batch.
  Discovered Unit 2's electrostatics files (`2_1_1`–`2_1_3`) were already
  well-written, unlike everything else touched so far this session;
  introduced a new **light-touch policy** for pages like this (see General
  writing principles above) rather than rewriting good prose for its own
  sake, and logged the two taxonomy tensions it surfaced
  (Model/Standard-Explanation admonitions, bare `!!! note "Note:"` asides)
  in the parking lot rather than resolving them unilaterally, per
  `CLAUDE.md`'s note that taxonomy design is the user's call. Added
  "Principle" to the taxonomy (conservation of energy/charge) and found
  three new bug categories: tab content assigned to the wrong tab
  (`3_4_sound-waves.md`'s Core practical had all equipment under one tab,
  leaving the other empty), a page H1 that didn't match its actual content
  (`3_1_describing-waves.md` was titled as if it covered the EM spectrum,
  which is `3_2`'s separate topic), and factual errors in the source
  itself rather than broken syntax (`4_4_energy-resources.md`'s solar
  cells section wrongly routed energy through a thermal store, and called
  the light-absorbing material "metal" instead of semiconductor). Also
  fixed the recurring split-table and non-existent-image-reference bugs
  again (`2_2_1`'s formula triangle, `4_2`'s Energy stores/transfer-pathway
  tables, `4_3`'s convection Equipment table), converted a dozen-plus more
  "is defined as:"-style blockquotes to Definition admonitions, and left
  three substantial content gaps as `<!-- TODO -->`s rather than writing
  them under time pressure: `2_2_3_electrical-components.md`'s circuit-
  symbol legend (references two non-existent image files for ~30 distinct
  symbols), and `2_2_4_analysing-simple-circuits.md`'s potential-dividers
  and analysing-changes-in-a-circuit sections (both were bare `## heading`
  + the word "TODO" with no content at all).
- 2026-08-13: acted on the two `2_2_4_analysing-simple-circuits.md` TODOs
  logged above. **Potential dividers**: added a Definition, the potential
  divider equation as a Required formulae block (no nested formula
  triangle — matches the existing precedent that ratio-style equations
  like `6_4_transformers.md`'s transformer equation don't get one), a
  calculation worked example, and a "Sensing circuits" sub-section
  explaining the thermistor/LDR/variable-resistor variant (checked
  `reference/spec_points.md` first: 4PH1 never names "potential divider"
  as such, but 2.19's "calculate the currents, voltages and resistances of
  two resistive components connected in a series circuit" is exactly this
  circuit, so it's core content, not a Beyond-spec aside). Drew a new
  circuit diagram from scratch (`potential_divider_circuit.svg`) since no
  source asset covered it — a step up in complexity from the earlier
  formula-triangle SVGs (resistor zigzags, a battery symbol, a dashed
  $V_{out}$ tap) but still a simple labelled schematic rather than
  something needing real illustrative detail, so judged to still fit that
  convention; verified by rendering via `mkdocs serve` and screenshotting,
  not just a clean build. **Analysing changes in a circuit**: covered the
  series case (current changes everywhere, since it's the same at every
  point in the loop; the changed component's own voltage moves opposite to
  the unchanged components', via the same potential-divider reasoning) and
  the parallel case (branch voltages are unaffected since they're pinned
  to the supply; only the affected branch's current and the total supply
  current change) as prose, each backed by its own worked example — a
  Worked example (method) for the series case (LDR + fixed resistor, light
  increasing) and a Worked example (explanation) for the parallel case
  (thermistor + lamp branches, temperature increasing) — deliberately
  different types so the two worked examples don't duplicate each other's
  structure. `mkdocs build` is clean (zero warnings) after this pass.
- 2026-08-13: rewrote all of Unit 1 (`1_1_1`–`1_6`), the unit the course
  actually opens with. Two files (`1_2_explaining-motion.md` and
  `1_3_applications.md`) arrived already mid-restructure — the user had
  manually cut the stopping-distance/terminal-velocity content out of
  `1_2` and moved it into a new `1_3_applications.md`, matching a split
  `index.md` already described but the file hadn't caught up to (it still
  said "*not yet written*" for 1.3) — continued that structure rather than
  treating it as unrelated in-progress work, and updated `index.md`'s
  descriptions for both pages to match. Filled several real content gaps
  discovered via `reference/spec_points.md`, not just prose/bug fixes:
  Newton's first law was never actually stated anywhere on the site (only
  referenced in passing) — added it as a Principle, with the second and
  third laws (covered elsewhere on the same page / in `1_4`) cross-linked
  rather than repeated; `1_5_stretching-effect-of-forces.md` covered the
  Core practical and elastic behaviour but skipped spec point 1.23
  entirely (Hooke's law / the linear region of a force-extension graph) —
  added a Hooke's law section between the two; and confirmed via
  `spec_points.md` that acceleration-time graphs are *not* in 4PH1 at all
  (only distance-time and velocity-time are, 1.3–1.9), so
  `1_1_3_motion-graphs.md`'s acceleration-time-graph TODO became a
  Beyond-spec aside instead of a full section — a case of the spec check
  ruling *out* content rather than justifying it, which hadn't come up
  before. Small compact TODOs (measuring time/speed/acceleration in
  `1_1_2_investigating-motion.md`, nuclear forces and lift in `1_2`) were
  written inline as usual; nuclear forces turned out to not be a named
  4PH1 force type at all (`1.12` just gives gravitational/electrostatic as
  *examples* of an open list), so it was written as a same-length sibling
  to the other forces-at-a-distance subsections rather than flagged as
  beyond-spec. Found a new diagram gap distinct from the
  broken/non-existent-image-reference pattern: `1_1_3_motion-graphs.md`
  had **no image asset at all** for four basic distance-time/velocity-time
  illustrations (constant-vs-changing slope, increasing-vs-decreasing
  velocity, the three-phase accel/constant/decel graph) — they'd been
  represented as fake data tables standing in for a chart, and one
  (changing-speed curves) had a caption with no image tag above it at all.
  Drew all four as simple axis-and-line SVGs rather than flagging as a
  follow-up, since (like the formula triangles and the potential-divider
  circuit before them) they're simple enough to draw directly — judgement
  call on where that complexity line sits keeps coming up, worth watching
  for a case that finally lands the other side of it. Found the tab
  system's worst breakage yet in `1_5_stretching-effect-of-forces.md`:
  `=== "rubber band"` and `=== "wire"` were nested *inside* the `"spring"`
  tab (wrong indentation), silently swallowing rubber band's entire
  results table — reconstructed the tab structure properly, and since no
  distinct rubber band data existed in the source at all, gave it the same
  table shape as spring's (matches the Analysis section's own description
  of the two as using identical methodology) rather than inventing
  different numbers. Also fixed a reused-image bug distinct from the
  same-image-for-different-table-rows pattern seen before: `1_4`'s
  Newton's-third-law tip referenced `page_86_chart_1_v2.jpg` twice with
  two different alt-text descriptions (Earth/book pair, then foot/ground
  pair) — merged into one reference with combined alt text, on the theory
  that it's one diagram showing both pairs together, not two separate lost
  images. Renaming `1_4`'s "Momentum & Safety Features" heading to
  sentence-case ("Momentum and safety features") broke an existing
  cross-file anchor link from `5_1_2_pressure.md` — first time a heading
  edit *in this unit* actually broke something elsewhere rather than just
  being a risk in theory; fixed the link rather than reverting the
  heading, and it's a concrete reminder of why the filename/nav-untouched
  principle above exists (anchors are exactly this fragile, just for
  in-page links instead of nav paths). Both `2_2_3`/`2_2_4` follow-up
  tasks spawned during the Units 2–4 pass (circuit-symbol legend SVGs,
  potential-divider content) completed in the background during this
  pass — their own change-log entries are above, out of chronological
  order, since they landed mid-session. `mkdocs build` is clean (zero
  warnings) across the whole site after this pass.
