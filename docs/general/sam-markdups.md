# Marking Duplicate Reads with `samtools markdup`

This example is for a minimap2 alignment with a read header that looks like:

```text
@INSTR1:001:000000000-TESTX:1:1101:10000:2000 1:N:0:1
```

The important part is customizing the read-coordinate parsing so `samtools markdup` can identify optical duplicates correctly.

```bash
samtools markdup \
  -r \
  -d 100 \
  --read-coords '([@!-9;-?A-~]+:[0-9]+:[!-9;-?A-~]+:[0-9]+:[0-9]+):([0-9]+):([0-9]+)' \
  --coords-order txy \
  --reference reference.fasta \
  -@ 6 \
  -T sample_prefix \
  -f sample_prefix_markdup.txt \
  sample_sorted.bam \
  sample_dedup.bam
```

Option notes:

- `-r`: remove duplicates instead of only marking them
- `-d 100`: set the maximum optical duplicate pixel distance
- `--read-coords`: provide a regex that matches your instrument read name layout
- `--coords-order txy`: tell `markdup` how to interpret the parsed coordinate groups
- `--reference`: use the reference FASTA to help fix flags and coordinates
- `-T`: set the temporary-file prefix
- `-f`: write duplication metrics to a file

> Pixel distance here is shown for MiSeq or HiSeq-style data. Adjust it for the sequencer you are actually using.
