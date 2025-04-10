#!/usr/bin/env python3

import sys
import subprocess
from playwright.sync_api import sync_playwright

def render_web_to_text(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url, timeout=10000)  # Set timeout to 10 seconds
            html_content = page.content()
            browser.close()

        # Use w3m to render the HTML content to text
        process = subprocess.Popen(['w3m', '-dump', '-T', 'text/html'], 
                                    stdin=subprocess.PIPE, 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=html_content.encode('utf-8'))

        if process.returncode != 0:
            sys.exit(1)

        return stdout.decode('utf-8')
    except Exception as e:
        fallback_process = subprocess.Popen(['w3m', '-dump', url], 
                                            stdout=subprocess.PIPE, 
                                            stderr=subprocess.PIPE)
        fallback_stdout, fallback_stderr = fallback_process.communicate()

        if fallback_process.returncode != 0:
            sys.exit(1)

        return fallback_stdout.decode('utf-8')

def main():
    if len(sys.argv) != 2:
        print("Usage: web2text <URL>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    text_output = render_web_to_text(url)
    print(text_output)

if __name__ == "__main__":
    main()
