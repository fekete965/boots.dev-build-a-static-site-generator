def extract_title(markdown_str: str) -> str:
    potential_lines = list(
        filter(
            lambda line: line.startswith("# "), markdown_str.split("\n"),
        )
    )

    if len(potential_lines) == 0:
        raise Exception("No title found in markdown")

    return potential_lines[0][2:].strip()
