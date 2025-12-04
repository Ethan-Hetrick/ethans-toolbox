### Marking different sorts of duplicate reads using samtools markdup

This is an example using a minimap2 alignment. The read header string matching is the difficult part. This example is for a read header that looks like `@INSTR1:001:000000000-TESTX:1:1101:10000:2000 1:N:0:1`.

```bash
samtools markdup \
  -r \ # remove dup reads instead of marking
  -d 100 \ # max optical duplicate pixel distance
  --read-coords ([@!-9;-?A-~]+:[0-9]+:[!-9;-?A-~]+:[0-9]+:[0-9]+):([0-9]+):([0-9]+) \ # custom read-coordinate regex
  --coords-order txy \ # coordinate ordering: template, x, y
  --reference reference.fasta \ # reference FASTA used to fix flags/coords
  -@ 6 \ # threads
  -T sample_prefix \ # prefix for temp files
  -f sample_prefix_markdup.txt \ # duplication metrics output file
  sample_sorted.bam \  # input sorted BAM
  sample_dedup.bam # output cleaned BAM
```

> Note: Pixel distance here is for MiSeq/HiSeq, it depends on the sequencer
