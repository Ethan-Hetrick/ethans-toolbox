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

## Make into a kraken database

```bash
# Extract Taxonomy IDs from assembly report output by NCBI datasets
jq -r '[.accession, .organism.taxId] | @tsv' assembly_data_report.jsonl > taxIDs.txt

# Add kraken header
while read -r fasta; do name=$(echo "$fasta" | cut -f12 -d'/'); taxID=$(rg $name taxIDs.txt | cut -f2); sed "s#>#>|kraken:taxid|${taxID}|#g" $fasta > ${name}.krakhead.fasta; done < genome-paths.txt

# Add to kraken database
fasta in ./*krakhead*; do kraken2-build --add-to-library $fasta --db krakendb; done

# Add taxonomy database and build
kraken2-build --download-taxonomy --db krakendb
kraken2-build --build --db krakendb
```
