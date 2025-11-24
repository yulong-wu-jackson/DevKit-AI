#!/bin/bash
# Download research paper from URL (supports arxiv and direct PDFs)

set -e

URL=$1
OUTPUT_DIR=$2
FILENAME=$3

if [ -z "$URL" ] || [ -z "$OUTPUT_DIR" ]; then
    echo "Usage: $0 <paper-url> <output-dir> [filename]"
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Determine filename
if [ -z "$FILENAME" ]; then
    FILENAME="paper.pdf"
fi

OUTPUT_PATH="$OUTPUT_DIR/$FILENAME"

# Download the paper
echo "Downloading paper from: $URL"
curl -L "$URL" -o "$OUTPUT_PATH"

# Verify it's a PDF
if file "$OUTPUT_PATH" | grep -q PDF; then
    echo "✓ Successfully downloaded PDF to: $OUTPUT_PATH"
    echo "  File size: $(du -h "$OUTPUT_PATH" | cut -f1)"
else
    echo "✗ Error: Downloaded file is not a PDF"
    exit 1
fi
