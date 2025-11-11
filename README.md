# Static Site Generator

A Python-based static site generator that converts Markdown to HTML using a custom node-based architecture.

## Features

- Converts Markdown syntax to HTML nodes
- Supports headings, paragraphs, lists, blockquotes, and code blocks
- Handles inline markdown (bold, italic, links, images, code)
- Recursively processes content folders to generate multiple pages
- Copies static assets (CSS, images, etc.) to the output directory
- Starts a local development server for preview
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
PYTHONPATH=. uv run python src/main.py
```

Or use the provided script (which also starts a local server on port 8888):
```bash
./main.sh
```

The script will:
1. Copy all files from the `static/` folder to `public/`
2. Recursively process all `index.md` files in the `content/` folder
3. Generate HTML pages using `template.html`
4. Start a local HTTP server at `http://localhost:8888` (if using `main.sh`)

### Content Structure

Place your Markdown files in the `content/` folder:
- `content/index.md` → `public/index.html`
- `content/contact/index.md` → `public/contact/index.html`
- `content/about/index.md` → `public/about/index.html`
- etc.

Each `index.md` file should start with a heading (`# Title`) which will be used as the page title.

## Project Structure

```
.
├── content/         # Markdown source files (organized in folders)
│   └── index.md     # Main page content
├── static/          # Static assets (CSS, images, etc.)
├── public/          # Generated HTML output (created by the script)
├── template.html    # HTML template with {{ Title }} and {{ Content }} placeholders
├── src/
│   ├── nodes/       # Core node classes (HTMLNode, LeafNode, ParentNode, TextNode)
│   ├── utils/       # Markdown parsing and conversion utilities
│   └── main.py      # Main entry point
└── main.sh          # Build script (generates site and starts server)
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
