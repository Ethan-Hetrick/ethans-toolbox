# SAM Utilities

This page documents the small helper scripts in the repo for inspecting SAM files and working through alignment metadata.

## Included scripts

### `scripts/sam/flags.py`

Summarizes SAM flag counts and prints them as a table.

```bash
python scripts/sam/flags.py -a alignments.sam
```

### `scripts/sam/header.py`

Parses SAM header lines and prints a table with tag descriptions.

```bash
python scripts/sam/header.py -a alignments.sam
```

## Related note

The repo also includes a separate page with a `samtools markdup` example for custom read-name layouts.
