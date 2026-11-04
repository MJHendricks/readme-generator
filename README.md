# readme-generator

## Overview
`readme-generator` is a Python project that processes and summarizes files from a project repository to generate a README.md. The script uses a combination of Python and OpenAI's GPT model to extract relevant information and create a comprehensive README for the repository.

## Features
- **File Summarization**: Extracts and summarizes configuration files and code files to provide a brief overview of their contents and purpose.
- **README Generation**: Uses an AI model to generate a README file based on the summarized information.
- **Directory Scanning**: Automatically scans a specified repository for configuration and code files, excluding certain directories and files.
- **Cache Mechanism**: Caches summarized files to avoid redundant processing and improve performance.

## Usage
To use `readme-generator`, you need to have Python installed on your machine. Then, you can run the following command in your terminal:

```bash
python main.py --path /path/to/your/repository
```

This command will scan the specified repository, summarize the files, and generate a README.md in the current directory. You can also run the script with the `-h` or `--help` option to see available command-line arguments and options.

## Installation

See project files for setup details.

## Project Structure

```
README.md
config.py
main.py
readme.py
scan.py
summary.py
```
