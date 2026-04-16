# File Conversion

Quick notes for converting common document and spreadsheet formats.

## Pandoc

Use Pandoc when you want to convert documents such as Markdown into Microsoft Word.

### Install

```bash
wget https://github.com/jgm/pandoc/releases/download/3.8.2.1/pandoc-3.8.2.1-linux-amd64.tar.gz
tar -xvzf pandoc-3.8.2.1-linux-amd64.tar.gz
```

> Pandoc is also available through Conda on many systems.

### Convert Markdown to Word

```bash
pandoc -f markdown -t docx file.md -o file.docx +RTS -s
```

## in2csv

Use `in2csv` when you want to convert spreadsheets and other tabular formats into CSV.

```bash
pip install in2csv

in2csv file.xlsx -f xlsx > file.csv
```

Helpful options:

- `--names`: display sheet names from the input Excel file
- `--write-sheets <SHEET>`: write a specific sheet, or `-` for all sheets
- `-l`: print line numbers, useful when piping to `grep`
- `--skip-lines <int>`: skip leading lines
- `-H`: disable header handling
- `-d <delimiter>`: specify the input delimiter
