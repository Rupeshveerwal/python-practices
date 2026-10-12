import argparse
import csv


NULL_VALUES = {"", "na", "n/a", "null", "none"}


def clean_csv(input_path, output_path):
    """Clean a CSV by trimming cells, blanking null markers, and removing duplicates."""
    with open(input_path, "r", newline="", encoding="utf-8-sig") as input_file:
        reader = csv.reader(input_file)
        header = next(reader, None)
        if header is None:
            raise ValueError("The input CSV is empty.")

        cleaned_header = [clean_value(value) for value in header]
        cleaned_rows = []
        seen_rows = set()
        removed_rows = 0

        for row in reader:
            cleaned_row = [clean_value(value) for value in row]
            row_key = tuple(cleaned_row)
            if row_key in seen_rows:
                removed_rows += 1
                continue
            seen_rows.add(row_key)
            cleaned_rows.append(cleaned_row)

    with open(output_path, "w", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(cleaned_header)
        writer.writerows(cleaned_rows)

    return len(cleaned_rows), removed_rows


def clean_value(value):
    value = value.strip()
    return "" if value.casefold() in NULL_VALUES else value


def main():
    parser = argparse.ArgumentParser(description="Clean a CSV file.")
    parser.add_argument("input", help="CSV file to clean")
    parser.add_argument("output", help="Where to save the cleaned CSV")
    args = parser.parse_args()

    kept_rows, removed_rows = clean_csv(args.input, args.output)
    print(f"Saved {kept_rows} rows to {args.output}; removed {removed_rows} duplicate rows.")


if __name__ == "__main__":
    main()