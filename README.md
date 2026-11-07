# README Generator

## Overview

This is a Python-based tool designed to analyze and summarize code files from a local folder using the Ollama language model. This tool helps generate a comprehensive README.md file that includes summaries of the code and metadata of the repository.

## Features

- **Code Analysis**: The tool scans the repository for code files and prioritizes them based on their size and relevance.
- **Summarization**: It uses the Ollama language model to generate summaries of each code file.
- **Caching**: Results are cached to speed up future runs.
- **Error Handling**: Ensure Ollama is running.
- **File Processing**: It processes and summarizes files from a project repository to generate a README file.

## Installation and Usage

You need to have Python and the Ollama language model installed.

1. **You can download and install Ollama** from the [official website](https://ollama.ai/).

2. **Install Required Packages**: Install the necessary packages by running the following command in your terminal:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download a model**: 
   ```bash
   ollama pull qwen2.5-coder:3b
   ```

4. **Configure the Project**: Open config.py and set MODEL to the name of a model you have installed (run `ollama list` to see them).

5. **Run the Main Script**: Execute the main script `main.py` with the path to your target directory as an argument.
   ```bash
   python main.py /path/to/your/project
   ```

6. **Check the Output**: The `README-gernerated.md` file will be generated in your chosen directory. Review the generated file for mistakes and make any necessary adjustments.

**Important Notes**:
- Ensure that the Ollama model is running and accessible on the network.

## Project Accuracy
This project was tested on 1 of my own projects for accuracy, the results have been tabulated below. Future changes that result in an increase in accuracy will be noted:

| Repo | Invented | Wrong usage | Missed | Notes |
|---|---|---|---|---|
| readme-generator | 1 | 2 | 2 | Added a feature that does not exist. Misunderstood the config.py file. Forgot to include that running the project requires the path as an argument. Did not note that the file generated is called "README-generated.md". Instructions in incorrect order.|

## Known Limitations
- Config files in subfolders may produce incorrect install commands.

## Planned Improvements

**Under consideration**:
- Accepting github url's as args.
- Subfolder-aware install commands
- Support more config file types
