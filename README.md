# readme

## Overview

`readme` is a Python project that automates the generation of a README.md file based on a given repository. The tool processes the repository, extracts relevant files, summarizes the content of each file, and generates a comprehensive README.md file that includes sections such as Overview, Features, Installation, Usage, and Project Structure. The generated README.md file is stored in the repository directory for easy reference.

## Features

- **Automated README Generation**: `readme` scans a repository, extracts important files, and generates a detailed README.md file.
- **AI-based Summary**: Each file's content is summarized using an AI model, providing a concise overview of the file's main functions, classes, and purpose.
- **User-Friendly Interface**: The tool is designed to be simple and easy to use, requiring minimal configuration.

## Installation

To install `readme`, follow these steps:

1. **Clone the Repository**: Clone the `readme` repository from GitHub.
2. **Install Dependencies**: Install the required Python dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the AI Model**: If you want to use an AI model for file summarization, configure it by setting up the Ollama model and ensuring it's accessible.

## Usage

To use `readme`, navigate to the repository directory and run the following command:

```bash
python main.py /path/to/repository
```

This command will process the specified repository and generate a README.md file in the repository directory. The README.md file will contain a summary of each file in the repository.

## Project Structure

The project directory contains the following files and directories:

- `main.py`: The main entry point of the project.
- `readme.py`: The script to generate the README.md file.
- `scan.py`: The function to scan the repository and categorize files.
- `summary.py`: The function to summarize file content.

Each file is designed to handle its specific role in the project's automation process.