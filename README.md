# AHS File Analysis
A lightweight file analysis and extraction tool for HPE's Active Health System (`.AHS`) files.

## Disclaimer
This tool was made for educational purposes.

## Prerequisites
* Python
* [Poetry](https://python-poetry.org/docs) (or the [pip](https://pypi.org/project/pip/) package management tool.)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/tarranprior/ahs-analysis.git
```

2. Change the directory:
```bash
cd ahs-analysis
```

3. Install the dependencies:
```bash
# Install using Poetry:
poetry install

# Install using pip:
pip install -r requirements.txt
```

## Usage
```bash
ahs-analysis.py [-h] [--extract] source
```
