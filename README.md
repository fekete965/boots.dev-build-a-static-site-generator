# Static Site Generator

A Python-based static site generator that converts Markdown to HTML using a custom node-based architecture. Perfect for generating simple, fast websites from Markdown files with support for GitHub Pages deployment.

## Features

- 🚀 **Simple & Fast**: Convert Markdown to HTML with a single command
- 📝 **Full Markdown Support**: Headings, paragraphs, lists, blockquotes, code blocks, and inline formatting
- 🔗 **Rich Inline Elements**: Bold, italic, links, images, and inline code
- 📁 **Recursive Content Processing**: Automatically processes nested folder structures
- 🎨 **Static Asset Management**: Copies CSS, images, and other assets automatically
- 🌐 **GitHub Pages Ready**: Built-in support for GitHub Pages deployment with base path handling
- 🧪 **Well Tested**: Comprehensive test coverage
- 🎯 **Clean Architecture**: Custom node-based HTML representation

## Requirements

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (Python package manager)

## Quick Start

1. **Clone and install**:
   ```bash
   git clone <repository-url>
   cd boots.dev-build-a-static-site-generator
   uv sync
   ```

2. **Create your content**:
   - Add Markdown files in the `content/` folder
   - Each page should be named `index.md` in its folder
   - Start each file with a heading (`# Title`) for the page title

3. **Build and preview**:
   ```bash
   ./main.sh
   ```
   Visit `http://localhost:8888` to see your site!

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

### Build for Production (GitHub Pages)

Build the site with a base path for GitHub Pages:
```bash
./build.sh
```

Or manually:
```bash
PYTHONPATH=. uv run python src/main.py "https://github.com/fekete965/boots.dev-build-a-static-site-generator/"
```

The base path argument is used to fix relative URLs (`href="/"` and `src="/"`) for GitHub Pages deployment.

### Local Development

For local development with a preview server:
```bash
./main.sh
```

This will:
1. Copy all files from the `static/` folder to `docs/`
2. Recursively process all `index.md` files in the `content/` folder
3. Generate HTML pages using `template.html`
4. Start a local HTTP server at `http://localhost:8888`

**Note:** For local development, you can run without a base path:
```bash
PYTHONPATH=. uv run python src/main.py
```

### Content Structure

Place your Markdown files in the `content/` folder:
- `content/index.md` → `docs/index.html`
- `content/contact/index.md` → `docs/contact/index.html`
- `content/about/index.md` → `docs/about/index.html`
- `content/blog/post-name/index.md` → `docs/blog/post-name/index.html`

Each `index.md` file should start with a heading (`# Title`) which will be used as the page title.

### Supported Markdown Features

The generator supports the following Markdown syntax:

#### Block Elements
- **Headings**: `# H1`, `## H2`, `### H3`, etc. (up to H6)
- **Paragraphs**: Regular text separated by blank lines
- **Unordered Lists**: `-`, `*`, or `+` prefixes
- **Ordered Lists**: `1.`, `2.`, `3.`, etc.
- **Blockquotes**: Lines starting with `>`
- **Code Blocks**: Triple backticks (```)

#### Inline Elements
- **Bold**: `**text**` or `*text*`
- **Italic**: `_text_`
- **Inline Code**: `` `code` ``
- **Links**: `[text](url)`
- **Images**: `![alt text](image-url)`

#### Example

```markdown
# My Page Title

This is a **bold** paragraph with _italic_ text and `inline code`.

## A List

- Item one
- Item two
- Item three

> This is a blockquote

Here's some code:

```
def hello():
    print("Hello, World!")
```

[Visit my site](https://example.com)
```

### Template File

The `template.html` file is used as a wrapper for all generated pages. It should contain:
- `{{ Title }}` - Placeholder for the page title (from the first heading)
- `{{ Content }}` - Placeholder for the generated HTML content

Example template:
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>{{ Title }}</title>
    <link href="/index.css" rel="stylesheet" />
  </head>
  <body>
    <article>{{ Content }}</article>
  </body>
</html>
```

### GitHub Pages Deployment

The `build.sh` script generates the site with the correct base path for GitHub Pages. The output is generated in the `docs/` folder, which can be used as the GitHub Pages source directory. The script automatically fixes all relative URLs (`href="/"` and `src="/"`) to use the repository's base path.

**Setup Steps:**
1. Run `./build.sh` to generate the site
2. Commit and push the `docs/` folder
3. In GitHub repository settings, set Pages source to `/docs` folder
4. Your site will be available at `https://<username>.github.io/<repository-name>/`

## Project Structure

```
.
├── content/         # Markdown source files (organized in folders)
│   ├── index.md     # Main page content
│   └── blog/        # Example: blog posts
│       └── post-name/
│           └── index.md
├── static/          # Static assets (CSS, images, etc.)
│   ├── images/      # Image files
│   └── index.css    # Stylesheet
├── docs/            # Generated HTML output (created by the script, used for GitHub Pages)
├── template.html    # HTML template with {{ Title }} and {{ Content }} placeholders
├── src/
│   ├── nodes/       # Core node classes (HTMLNode, LeafNode, ParentNode, TextNode)
│   ├── utils/       # Markdown parsing and conversion utilities
│   └── main.py      # Main entry point
├── build.sh         # Production build script (for GitHub Pages)
└── main.sh          # Development script (generates site and starts server)
```

### Key Components

- **Nodes**: Tree-based representation of HTML structure
  - `HtmlNode`: Base class for all HTML elements
  - `LeafNode`: Represents self-closing or text-only elements
  - `ParentNode`: Represents elements with children
  - `TextNode`: Intermediate representation for markdown parsing
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

## Troubleshooting

### ModuleNotFoundError: No module named 'src'

Make sure you're running the script with `PYTHONPATH=.`:
```bash
PYTHONPATH=. uv run python src/main.py
```

### Static folder not found

Ensure the `static/` folder exists in the project root. The script will create the output folder automatically, but the source `static/` folder must exist.

### Pages not generating

- Check that your Markdown files are named `index.md` (not `Index.md` or `INDEX.md`)
- Ensure each `index.md` file starts with a heading (`# Title`)
- Verify the `content/` folder structure matches your expected output structure

### GitHub Pages URLs not working

Make sure you're using `build.sh` (not `main.sh`) for production builds, as it includes the base path argument needed for GitHub Pages.

## License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
