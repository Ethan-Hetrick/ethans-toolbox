# pandoc

Converts documents, like marktown to microsoft word

## Install

```bash
wget https://github.com/jgm/pandoc/releases/download/3.8.2.1/pandoc-3.8.2.1-linux-amd64.tar.gz
tar -xvzf pandoc-3.8.2.1-linux-amd64.tar.gz
```

> Also available via conda

## Convert markdown to word

```bash
pandoc -f markdown -t docx file.md -o file.docx +RTS -s
```

# in2csv

Can convert various formats to csv

```bash
# Install it
pip install in2csv

# convert Excel to csv
in2csv <file.xlsx> -f xlsx > <file.csv>
```

Other helpful options:
- `--names`: Display sheet names from the input Excel file.
- `--write-sheets <SHEET>`: Name of sheets to write; "-" for all.
- `-l`: Will print line numbers, good for piping to `grep`
- `--skip-lines <int>`: Number of lines to skip
- `-H`: Disable header
- `-d <delimiter>`: Specify input delimiter
