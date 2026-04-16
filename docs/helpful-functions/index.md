# Helpful Functions

Small shell helpers and command snippets that are handy enough to keep around.

## Copy a file into the clipboard

This helper copies either a file's contents or piped stdin into the X clipboard using `xsel`.

```bash
clip() { [ $# -gt 0 ] && xsel --clipboard --input < "$1" || xsel --clipboard --input; }
```

Example:

```bash
clip notes.txt
```

```bash
echo "hello" | clip
```

## Run a tool on all matching files

This is a safer version of the original one-liner because it handles paths with spaces.

```bash
find ~/Project -name "*fastq*" -type f -print0 | xargs -0 fastqc -t 4 -o fastqc_out
```

## Open an HTML file from the CLI

Use `xdg-open` to open a local HTML file in your default browser.

```bash
xdg-open file.html
```

## Break command-line flags onto separate lines

This `sed` one-liner is handy when you want to reformat a long command so each option starts on its own indented line.

```bash
sed '/^\t/! s/ \(-\{1,2\}[a-zA-Z0-9-]*\)/ \\\n\t\1/g'
```
