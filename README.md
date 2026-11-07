# README Generator

## Overview

The "readme-generator" project is a Python-based tool designed to analyze and summarize code files from a given repository using the Ollama language model. This tool helps generate a comprehensive README.md file that includes summaries of the code and metadata of the repository.

## Features

- **Code Analysis**: The tool scans the repository for code files and prioritizes them based on their size and relevance.
- **Summarization**: It uses the Ollama language model to generate summaries of each code file.
- **Caching**: Results are cached to speed up future runs.
- **Error Handling**: Ensure Ollama is running.
- **File Processing**: It processes and summarizes files from a project repository to generate a README file.

## Usage

You need to have Python and the Ollama language model installed.

1. **You can download and install Ollama** from the [official website](https://ollama.ai/).

2. **Install Required Packages**: Install the necessary packages by running the following command in your terminal:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Download a model**: `ollama pull qwen2.5-coder:3b` 

4. **Configure the Project**: Open config.py and set MODEL to the name of a model you have installed (run `ollama list` to see them).

5. **Run the Main Script**: Execute the main script `main.py` with the path to your target directory as an argument.
   ```bash
   python main.py /path/to/your/project
   ```

6. **Check the Output**: The README-gernerated.md file will be generated in your chosen directory. Review the generated filef or mistakes and make any necessary adjustments.

**Important Notes**:
- Ensure that the Ollama model is running and accessible on the network.

## Installation

```
pip install -r requirements.txt
```

## Developer Notes

**Project Accuracy**:


| Repo | Invented | Wrong usage | Missed | Notes |
|---|---|---|---|---|
| readme-generator | 1 | 2 | 2 | Added a feature that does not exist. Misunderstood the config.py file. Forgot to include that running the project requires the path as an argument. Did not note that the file generated is called "README-generated.md". Instructions in incorrect order.|

Some improvements I am considering:
 - Project scanning github repos via URL instead of only local files.