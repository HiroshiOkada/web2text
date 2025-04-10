# web2text

Render JavaScript-heavy websites as text using Playwright and w3m.

## Description

`web2text` is a command-line tool that uses Playwright to render JavaScript-heavy websites and w3m to convert the rendered HTML into readable text. Its main purpose is to help create questions for AI language models like ChatGPT by extracting clean, formatted text from websites. It's also useful for users who want to browse modern web content in a text-only format.

## Requirements

- Python 3.6+
- w3m (text-based web browser)
- Playwright and its browser dependencies

## Installation

```bash
git clone https://github.com/HiroshiOkada/web2text.git
cd web2text
pip install -e .
playwright install
```

## Usage

```bash
web2text https://example.com
```

If Playwright fails to render the page (due to timeout or other issues), it will automatically fall back to using w3m directly.

## How It Works

1. Uses Playwright to fully render a webpage, including JavaScript content
2. Captures the rendered HTML
3. Feeds the HTML to w3m for text rendering
4. If Playwright fails, falls back to direct w3m rendering

## License

MIT License
