from Bio import SeqIO

from utils import (
    calculate_base_counts,
    calculate_gc_at,
    quality_check,
    save_report,
)

print("=" * 50)
print("🧬 GenomeQC Toolkit")
print("=" * 50)

print()

fasta_file = input("Enter FASTA file path: ")

report_path = "output/quality_report.txt"

for record in SeqIO.parse(fasta_file, "fasta"):

    sequence = str(record.seq)

    length = len(sequence)

    counts = calculate_base_counts(sequence)

    gc_content, at_content = calculate_gc_at(length, counts)

    print(f"Sequence ID      : {record.id}")
    print(f"Description      : {record.description}")
    print(f"Sequence Length  : {length} bp")
    print(f"GC Content       : {gc_content:.2f}%")
    print(f"AT Content       : {at_content:.2f}%")

    print("\nBase Composition")
    print("----------------")

    for base, value in counts.items():
        print(f"{base} : {value}")

    print("\nQuality Assessment")
    print("------------------")

    checks = quality_check(gc_content, counts["N"])

    for item in checks:
        print(item)

    save_report(
        report_path,
        record,
        length,
        gc_content,
        at_content,
        counts,
        checks,
    )

print(f"\nReport saved successfully to: {report_path}")
print("=" * 50)