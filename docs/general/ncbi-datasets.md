# NCBI Datasets Tutorial

Below is an example of how to use the NCBI datasets tool to pull a reference dataset

```bash
# Download enterobacteriacea reference genomes
datasets download genome taxon "Enterobacteriaceae" \
    --dehydrated \
    --filename enterobacteriaceae.zip \
    --assembly-version 'latest' \
    --api-key "${NCBI_API_KEY}" \
    --mag "exclude" --exclude-atypical \
    --assembly-source "RefSeq" \
    --assembly-level "complete"

# Unzip
unzip enterobacteriaceae.zip

# Rehydrate
datasets rehydrate --api-key "${NCBI_API_KEY}" --directory ./ --max-workers 24

# Download genome summary
datasets summary genome taxon "Enterobacteriaceae" \
    --assembly-version 'latest' \
    --api-key "${NCBI_API_KEY}" \
    --mag "exclude" --exclude-atypical \
    --assembly-source "RefSeq" \
    --assembly-level "complete" > enterobacteriaceae_summary.json

# Generate summary using dataformat
dataformat tsv genome --package ./enterobacteriaceae.zip > enterobacteriaceae_summary.tsv

# Create sample list
find $(realpath ncbi_dataset/) -name "*.fna" -type f > genome_list.txt
```
