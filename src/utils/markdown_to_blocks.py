def markdown_to_blocks(markdown: str) -> list[str]:
    result = markdown.split("\n\n")

    result = map(lambda line: line.strip(), result)
    result = filter(lambda line: line != "", result)

    return list(result)
