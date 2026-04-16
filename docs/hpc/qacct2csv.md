# qacct2csv

`qacct2csv` is a small Python helper that transposes `qacct` output into CSV format.

Script path:

```text
HPC/qacct2csv.py
```

## Usage

```bash
# Generate a qacct log and convert it to CSV
qacct -j <job_name> -d <days> -o <owner> > qacct.log
python HPC/qacct2csv.py --input qacct.log --output qacct.log.csv

# Or read from stdin and write to stdout
qacct | python HPC/qacct2csv.py > qacct.log.csv
```

## Help Menu

```bash
usage: qacct2csv.py [-h] [--input INPUT] [--output OUTPUT]

Transpose qacct logs into a CSV format.

options:
  -h, --help       show this help message and exit
  --input INPUT    Input file path
  --output OUTPUT  Output file path (optional)
```

## Conda Environment

```bash
conda env create -n qacct2csv_env -f HPC/qacct2csv.yml
```
