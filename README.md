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

You need to have Python and the Ollama language model installed. Follow these steps:

1. **Install Python and Ollama**: Ensure you have Python installed on your system. You can download and install Ollama from the [official website](https://ollama.ai/).

2. **Install Required Packages**: Install the necessary packages by running the following command in your terminal:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Main Script**: Execute the main script `main.py` to generate the README.md file.
   ```bash
   python main.py
   ```

4. **Configure the Project**: Modify the `config.py` file to set the desired configuration for the Ollama model.

5. **Check the Output**: The README.md file will be generated in the same directory as the script. Review the generated README.md file for the summaries and metadata of the repository.

**Important Notes**:
- Ensure that the Ollama model is running and accessible on the network.
- Adjust the cache settings in `config.py` to control how long cached results are stored.
- Check the network and model errors in the output to ensure smooth operation.

## Installation

```
pip install -r requirements.txt
```

## Developer Notes

Project Accuracy:

| Repo | Invented | Wrong usage | Missed | Notes |
|---|---|---|---|---|
| readme-generator | 1 | 1 | 1 | Added a feature that does not exist. Misunderstood the config.py file. Did not mention that you need to install a model from Ollama and edit the config.py file |

Some improvements I am considering:
 - Project scanning github repos via URL instead of only local files.