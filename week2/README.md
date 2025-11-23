# Week 2: Regular Expressions and Text Processing

This folder contains assignments for Week 2 of the Natural Language Processing course, focusing on regular expressions and pattern matching in Python.

## Structure

### Part 1: Basic Regex
- `task1.py` - Basic regex pattern matching exercises
- `test_regex.py` - Test cases for regex patterns

### Part 2: Text Extraction
- `task4.py` - Extract URLs, emails, and hashtags from text
- `input.txt` - Sample input text with various patterns
- `test_task4.py` - Comprehensive test suite with 84+ test cases
- `result/` - Output directory containing:
  - `urls.txt` - Extracted URLs (https, http, ftp)
  - `emails.txt` - Extracted emails (.com, .org, .edu, .net)
  - `hashtags.txt` - Extracted hashtags

## Usage

### Task 4: Text Extraction
```bash
cd part2
python task4.py
```

Extracts:
- **URLs**: `scheme://hostname/path?query` (https, http, ftp only)
- **Emails**: `username@domain.tld` (.com, .org, .edu, .net only)
- **Hashtags**: `#word` (letters, digits, underscores only)

### Running Tests
```bash
cd part2
python test_task4.py
```

## Requirements
- Python 3.x
- Standard library only (no external dependencies)
