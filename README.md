# Static Site Generator

A Python-based static site generator that converts Markdown to HTML using a custom node-based architecture.

## Features

- Converts Markdown syntax to HTML nodes
- Supports headings, paragraphs, lists, blockquotes, and code blocks
- Handles inline markdown (bold, italic, links, images, code)
- Comprehensive test coverage
- Code formatting with Black

## **Requirements**

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd boots.dev-build-a-static-site-generator
```

2. Install dependencies:
```bash
uv sync
```

## Usage

Run the main script:
```bash
PYTHONPATH=src uv run python src/main.py
```

Or use the provided script:
```bash
./main.sh
```

## Project Structure

```
src/
├── nodes/           # Core node classes (HTMLNode, LeafNode, ParentNode, TextNode)
├── utils/           # Markdown parsing and conversion utilities
└── main.py          # Main entry point
```

### Key Components

- **Nodes**: Tree-based representation of HTML structure
- **Markdown Parsing**: Converts markdown text to node trees
- **HTML Generation**: Converts node trees to HTML strings

## Development

### Running Tests

Run all tests:
```bash
./test.sh
```

Or directly:
```bash
PYTHONPATH=src uv run python -m unittest discover -s src -p "test_*.py"
```

### Code Formatting

This project uses [Black](https://black.readthedocs.io/) for consistent code formatting.

Format all Python files:
```bash
./format.sh
```

Check formatting without making changes:
```bash
./format.sh --check
```

Or use Black directly:
```bash
uv run black src/                    # Format files
uv run black --check src/            # Check formatting
```

### Code Style

- Line length: 100 characters
- Target Python version: 3.10+
- Formatter: Black 25.9.0+

## License

[Add your license here]
