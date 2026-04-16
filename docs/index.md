# Ethan's Toolbox

This site collects the notes, job aids, and small utilities in this repo into a structure that is easier to browse than a loose folder of Markdown files.

## Sections

- `General`: small reference pages and command-line notes
- `Helpful Functions`: reusable shell helpers and quick snippets
- `Git`: workflow reminders and formatting troubleshooting
- `Nextflow`: development checklists and contribution notes
- `Containers`: Singularity-based setup guides
- `HPC`: cluster-specific helpers like `qacct2csv`
- `SAM`: quick references for SAM-related scripts and examples

## Local Preview

```bash
python3 -m pip install -r requirements-docs.txt
mkdocs serve
mkdocs build --strict
```

## Repo Notes

The documentation pages now live under `docs/`. The Python helper scripts still live in their original source directories:

- `HPC/qacct2csv.py`
- `sam/flags.py`
- `sam/header.py`
