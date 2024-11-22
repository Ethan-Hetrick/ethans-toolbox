# qacct2csv usage

This is a python script which transposes `qacct` logs to csv format.

```bash
# Generate a qacct log and transpose it
qacct -j <job_name> -d <days> -o <owner> > <qacct.log>
transpose_qacct.py --input <qacct.log> --output <qacct.log.csv>

# Read and print to stdout
qacct | transpose_qacct.py
```

```bash
# Help menu
usage: transpose_qacct.py [-h] [--input INPUT] [--output OUTPUT]

Transpose qacct logs into a CSV format.

options:
  -h, --help       show this help message and exit
  --input INPUT    Input file path
  --output OUTPUT  Output file path (optional)
```