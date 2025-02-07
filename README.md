# Python Web Crawler
A simple recursive web crawler written in Python to discover and list all links within a target domain.


## Features
- Recursively crawls URLs starting from a specified target

- Converts relative links to absolute URLs

- Avoids duplicate links during crawling

- Handles URL fragments (e.g., #section)

- Simple error handling for connection issues

- Command-line interface with URL argument

## Installation
1. Ensure Python 3.x is installed

2 .Install required packages:

```bash
pip install requests
```
## Usage
```bash
python crawler.py -u <target_url>
```
Replace <target_url> with the website you want to crawl (e.g., example.com).

Note: Always ensure you have permission to crawl the target website.

## How It Works
1. Request Handling:

- Sends HTTP GET requests to URLs

- Handles connection errors gracefully

2. Link Extraction:

- Uses regex to find all href attributes in HTML content

- Converts relative URLs to absolute URLs using urljoin

3. Crawling Logic:

- Recursively processes new URLs within the same domain

- Skips already visited links to prevent loops

- Removes URL fragments (everything after #)

## Example Usage
```bash
python crawler.py -u https://example.com
```
Sample output:
```bash
https://example.com/page1
https://example.com/page2
https://example.com/subdir/page3
...
```

## Limitations
- Basic crawler without JavaScript rendering

- Does not handle forms or authenticated content

- No rate limiting or politeness delay

- Does not respect robots.txt

- Limited to same-domain links by default

- Simple regex-based parsing (not full HTML parser)



## Disclaimer
⚠️ This tool is intended for educational and ethical use only.
Unauthorized monitoring of keystrokes on devices you do not own or have explicit permission to access is illegal.
The developers assume no liability for misuse of this software.
