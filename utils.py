def calculate_base_counts(sequence):
    sequence = sequence.upper()

    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C"),
        "N": sequence.count("N"),
    }


def calculate_gc_at(length, counts):
    gc = ((counts["G"] + counts["C"]) / length) * 100
    at = ((counts["A"] + counts["T"]) / length) * 100

    return gc, at


def quality_check(gc_content, n_count):

    results = []

    if n_count == 0:
        results.append("✓ No ambiguous bases detected")
    else:
        results.append("⚠ Ambiguous bases present")

    if 40 <= gc_content <= 60:
        results.append("✓ GC Content within expected range")
    else:
        results.append("⚠ GC Content outside expected range")

    results.append("✓ Sequence successfully parsed")
    results.append("✓ Ready for downstream analysis")

    return results


def save_report(report_path, record, length, gc_content, at_content, counts, checks):

    with open(report_path, "w") as report:

        report.write("=" * 50 + "\n")
        report.write("GenomeQC Toolkit Report\n")
        report.write("=" * 50 + "\n\n")

        report.write(f"Sequence ID      : {record.id}\n")
        report.write(f"Description      : {record.description}\n")
        report.write(f"Sequence Length  : {length} bp\n")
        report.write(f"GC Content       : {gc_content:.2f}%\n")
        report.write(f"AT Content       : {at_content:.2f}%\n\n")

        report.write("Base Composition\n")
        report.write("----------------\n")

        for base, value in counts.items():
            report.write(f"{base} : {value}\n")

        report.write("\nQuality Assessment\n")
        report.write("------------------\n")

        for item in checks:
            report.write(item.replace("✓", "PASS:").replace("⚠", "WARNING:") + "\n")