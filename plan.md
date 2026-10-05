# Target

create a python script to list all of the file path of the user-provided directory recursively.

Regarding the args, you can use the module `argparse` to handle the command-line arguments.

# Input

- d (directory): the directory path provided by the user
- t (target): the target folder name
- o (output): the output file path where the list of file paths will be saved, default="./output/output.txt"

# code structure

def parse_args() -> argparse.Namespace:
    ...

def main() -> int:
    ...

# Output

absolute file paths of all files in the user-provided directory recursively.

```text
/path/to/abc/target_filePath
/path/to/b/target_filePath
...
```
