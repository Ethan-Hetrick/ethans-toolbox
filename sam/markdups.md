### Marking different sorts of duplicate reads using samtools markdup

This is an example using a minimap2 alignment. The read header string matching is the difficult part. This example is for a read header that looks like `@M04906:104:000000000-M3NG7:1:1101:15637:1926 1:N:0:12`

```bash
samtools markdup \
  -r \ # remove dup reads instead of marking
  -d 100 \ # max optical duplicate pixel distance
  --read-coords ([@!-9;-?A-~]+:[0-9]+:[!-9;-?A-~]+:[0-9]+:[0-9]+):([0-9]+):([0-9]+) \ # custom read-coordinate regex
  --coords-order txy \ # coordinate ordering: template, x, y
  --reference M129.fasta \ # reference FASTA used to fix flags/coords
  -@ 6 \ # threads
  -T 1-3101721458_S5_L001 \ # prefix for temp files
  -f 1-3101721458_S5_L001_markdup.txt \ # duplication metrics output file
  1-3101721458_S5_L001_sorted.bam \  # input sorted BAM
  1-3101721458_S5_L001.bam # output cleaned BAM
```
