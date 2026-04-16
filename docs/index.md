# Ethan's Toolbox

This site collects the notes, job aids, and small utilities in this repo into a structure that is easier to browse than a loose folder of Markdown files.

## Sections

- `One-liners`: reusable shell helpers and quick command snippets
- `HPC`: cluster-focused tools and terminal workflow notes
- `Nextflow`: development checklists and contribution notes
- `Containers`: Singularity-based setup guides
- `General`: broader reference material that does not need its own section

## Local Preview

```bash
python3 -m pip install -r requirements-docs.txt
mkdocs serve
mkdocs build --strict
```

## Repo Notes

The documentation pages now live under `docs/`. The helper scripts live under `scripts/`:

- `scripts/hpc/qacct2csv.py`
- `scripts/sam/flags.py`
- `scripts/sam/header.py`
