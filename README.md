# ethans-toolbox

Practical job aids, utilities, and notes for bioinformatics, HPC, containers, Git, and Nextflow work.

The MkDocs source for the documentation site lives in `docs/`, with site configuration in `mkdocs.yml`.

To preview the site locally:

```bash
python3 -m pip install -r requirements-docs.txt
mkdocs serve
mkdocs build --strict
```

Utility scripts remain in the repo root under directories such as `HPC/` and `sam/`.
