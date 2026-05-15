# Run a tool on all of a file type in parallel

`find ~/Project -name "*fastq*" -type f | xargs fastqc -t 4 -o fastqc_out`

# Generate QR code

python -m pip install 'qrcode[pil]' && python -c 'import qrcode; qrcode.make("<URL>").save("<name>.png")'
