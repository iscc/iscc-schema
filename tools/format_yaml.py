# -*- coding: utf-8 -*-
import pathlib
import yaml

HERE = pathlib.Path(__file__).parent.absolute()


def reformat():
    # Note: The glob pattern "**/*.yaml" finds all YAML files under the parent directory.
    for f in HERE.parent.glob("**/*.yaml"):
        # Load the YAML data using safe_load.
        with f.open("rt", encoding="utf-8") as infile:
            data = yaml.safe_load(infile)

        # Dump the YAML data as a string.
        # (We deliberately do not pass an encoding so that safe_dump returns a str.)
        dumped = yaml.safe_dump(
            data,
            indent=2,
            width=88,
            sort_keys=False,
            default_flow_style=False,
            allow_unicode=True,
        )

        # Post-process the dumped string to insert an empty line before each top–level element.
        # We define a top–level element as any line that does not start with whitespace.
        lines = dumped.splitlines()
        new_lines = []
        first_line = True
        for line in lines:
            if not first_line and line and not line[0].isspace():
                # Insert a blank line before any non-indented (top–level) line.
                new_lines.append("")
            new_lines.append(line)
            first_line = False

        processed = "\n".join(new_lines) + "\n"

        # Write the processed string back to the file.
        with f.open("wt", encoding="utf-8", newline="\n") as outf:
            outf.write(processed)


if __name__ == "__main__":
    reformat()
