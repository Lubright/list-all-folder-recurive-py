import argparse
import os
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Recursively list the absolute paths of all folders named "
        "<target> under the input directory."
    )
    parser.add_argument(
        "-d",
        "--directory",
        required=True,
        help="the input directory to search in",
    )
    parser.add_argument(
        "-t",
        "--target",
        required=True,
        help="the target folder name to look for",
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
    for dirpath, dirnames, _filenames in os.walk(root):
        for dirname in dirnames:
            if dirname == args.target:
                file_paths.append(os.path.join(dirpath, dirname))
        # Do not descend into matched folders (e.g. nested node_modules).
        dirnames[:] = [d for d in dirnames if d != args.target]
    file_paths.sort()

    output_path = os.path.abspath(args.output)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(file_paths))
        if file_paths:
            f.write("\n")

    print(f"Found {len(file_paths)} '{args.target}' folders. Saved to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
