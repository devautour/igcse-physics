# IGCSE Physics Notes (Edexcel 4PH1)

## Purpose

A set of course notes for Edexcel IGCSE Physics (4PH1), built with MkDocs
Material. This project is one of several that will eventually converge:
a revision platform (separate project) and an exam question database
(separate project) are meant to align with this project's course structure.

**The course "backbone"/"blueprint"** has **not been defined yet** as of
2026-08-10. `docs/` structure and `mkdocs.yml` nav are the current working
draft, organizational only — the section numbering (`2_2_3_...`) is **not**
meant as an implicit reference to specification points.

The intended granularity for spec-point/tag data is **sub-page content
blocks**, not whole pages or sections — e.g. tagging a specific Definition
or worked example, not the page it lives on. The planned approach is to
introduce structured callouts for content types (Definitions, Classical
explanations, "Classical practicals" extending the spec's core-practical
notion, etc.) as a first step, with the full taxonomy expected to be
discovered/refined iteratively rather than fixed up front. `blueprint
drafts/` is where this is being experimented with (see its entry below). The
user plans
to brainstorm this design in a future session once there are concrete
examples to work from — don't try to design the taxonomy preemptively.

## Environment

- Conda env: **`igcse-physics`** (Python 3.12), created 2026-08-10. Spec in
  [`environment.yml`](environment.yml).
- Contains: `mkdocs`, `mkdocs-material`, `pymdown-extensions`, `ipykernel`
  (matches the trio used in `.github/workflows/ci.yml`, plus ipykernel for
  running the notebooks in `notebooks/`).
- A Jupyter kernel named **"Python (igcse-physics)"** is registered for use
  in VS Code notebooks — select it instead of the `base` kernel the existing
  notebooks currently default to.
- No other conda env or venv existed in this project before this setup.

To use it:

```bash
conda activate igcse-physics
mkdocs serve      # live preview at http://127.0.0.1:8000
mkdocs build       # writes to site/ (not currently gitignored — build
                    # to a temp/scratch dir, or add site/ to .gitignore
                    # before building into the repo)
```

Or without activating: `conda run -n igcse-physics mkdocs serve`.

If the env is ever missing/broken, recreate with:

```bash
conda env create -f environment.yml
```

Shell note: on this machine, Git Bash sources `~/.bash_profile`, which emits
a harmless `cygpath` usage error + "No such file or directory" on every
`Bash` tool call. Ignore it — it doesn't affect command execution.

## Project structure

- `docs/` — the actual course notes (MkDocs source). Organized as `Unit 1`
  through `Unit 8`, each with an `index.md` and numbered sub-pages matching
  the nav in `mkdocs.yml`.
- `docs/assets/images/` — diagrams/images referenced from the notes (289
  files as of 2026-08-10).
- `mkdocs.yml` — site config + nav tree. This is the current (draft) course
  structure.
- `notebooks/` — helper Python scripts the user edits/runs via VS Code
  (`scripts.ipynb`, `renumbering_subtasks.ipynb`). Stdlib-only currently
  (`pathlib`, `os`, `re`, `shutil`).
- `reference/` — authoritative curriculum source material (spec PDF,
  syllabus excerpt, extracted spec points, learning log, savemyexam
  downloads). See [`reference/README.md`](reference/README.md) for a full
  index — it's kept up to date and is the right place to look first.
- `backup/` — gitignored manual backups of earlier drafts, incl.
  `sme-igcse-physics.md` (606KB), an old monolithic notes file that predates
  the current per-unit split in `docs/`. Historical reference only.
- `blueprint drafts/` — experiments with formats/structure for the future
  blueprint (e.g. `Unit-5.md`), not just generic in-progress content. Named
  this way (renamed from `drafts/`) so the folder's purpose is unambiguous.
- `scratch/` — one-off Python scripts (currently: manual pptx-XML parsers
  via `zipfile`/`xml.etree`, used to extract the learning log into
  `reference/`).
- `orphaned_images_backup/` — gitignored, 2402 page/image files, looks like
  a full raw image extraction (e.g. from a source PDF/pptx) that
  `docs/assets/images/` was later curated down from. Not yet confirmed with
  user beyond the name.

## Known issues (as of 2026-08-10, not yet fixed)

`mkdocs build` succeeds but warns about nav/filename mismatches — a few
`docs/` files have typos vs. what `mkdocs.yml` nav references, so they're
silently excluded from the built site:

- `Unit 1/1_1_2_investigationg-motion.md` (file) vs.
  `Unit 1/1_1_2_investigating-motion.md` (nav)
- `Unit 2/2_1_3_uses-and-dangers-of-static-electricity.md` (file) vs.
  `Unit 2/2_1_3_uses-and-danger-of-static-electricity.md` (nav)
- `Unit 2/2_2_3_electrical_components.md` (file, underscore) vs.
  `Unit 2/2_2_3_electrical-components.md` (nav, hyphen)

`docs/index.md` also isn't referenced in the nav at all (may be intentional
as a homepage — unconfirmed).

## Tooling notes

- VS Code Python extension is configured to default to conda for env/package
  management (`.vscode/settings.json`).
- CI (`.github/workflows/ci.yml`) deploys to GitHub Pages on push to `main`,
  using a fresh pip install of the mkdocs trio — not the conda env above,
  but pinned to the same versions (`mkdocs==1.6.1`, `mkdocs-material==9.7.7`,
  `pymdown-extensions==11.0.1`). Bump both places together when upgrading.
