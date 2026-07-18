# 🧬 GenomeQC Toolkit

A lightweight Python utility for performing preliminary quality assessment of DNA sequences in FASTA format before downstream bioinformatics analyses such as BLAST, alignment, and annotation.

## Features

- Read FASTA files using Biopython
- Calculate sequence length
- Calculate GC and AT content
- Count nucleotide composition (A, T, G, C, N)
- Perform basic sequence quality assessment
- Generate a quality report (`quality_report.txt`)

## Technologies Used

- Python 3
- Biopython
- Git
- GitHub

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Enter:

```text
sample_data/brca1.fasta
```

The report is automatically saved to:

```text
output/quality_report.txt
```

## Future Improvements

- Support multiple FASTA sequences
- CSV export
- Interactive command-line options
- GC content visualization
