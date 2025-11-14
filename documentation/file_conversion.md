# pandoc

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
