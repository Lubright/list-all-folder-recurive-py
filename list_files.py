import argparse
import os
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Recursively list the absolute paths of all files in a directory."
    )
    parser.add_argument(
        "-d",
        "--directory",
        required=True,
        help="the directory path provided by the user",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="./output/output.txt",
        help="the output file path where the list of file paths will be saved "
        "(default: %(default)s)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    root = os.path.abspath(args.directory)
    if not os.path.isdir(root):
        print(f"Error: '{args.directory}' is not a valid directory.", file=sys.stderr)
        return 1

    file_paths = []
    for dirpath, _dirnames, filenames in os.walk(root):
        for filename in filenames:
            file_paths.append(os.path.join(dirpath, filename))
    file_paths.sort()

    output_path = os.path.abspath(args.output)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(file_paths))
        if file_paths:
            f.write("\n")

    print(f"Found {len(file_paths)} files. Saved to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
