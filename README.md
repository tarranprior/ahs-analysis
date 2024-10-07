# AHS File Analysis
A lightweight file analysis and extraction tool for HPE's Active Health System (`.AHS`) files.

## Introduction

## Disclaimer
This tool was made for educational purposes.

## Prerequisites
* Python and [Poetry](https://python-poetry.org/docs) (or the [pip](https://pypi.org/project/pip/) package management tool)
* An Active Health System (AHS) file.

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

The contents of a typical `.AHS` file includes the following files after extraction.
```powershell
-rwxrwx--- 1 root   833176  0001989-2024-08-20.bb
-rwxrwx--- 1 root   422278  0001991-2024-08-20.bb
-rwxrwx--- 1 root   715956  0001992-2024-08-20.bb
-rwxrwx--- 1 root   663146  0001993-2024-08-20.bb
-rwxrwx--- 1 root   672137  0001994-2024-08-20.bb
-rwxrwx--- 1 root   726934  0001995-2024-08-20.bb
-rwxrwx--- 1 root   652703  0001996-2024-08-20.bb
-rwxrwx--- 1 root   723348  0001997-2024-08-20.bb
-rwxrwx--- 1 root   699662  0001998-2024-08-20.bb
-rwxrwx--- 1 root   697564  0001999-2024-08-20.bb
-rwxrwx--- 1 root   732963  0002000-2024-08-20.bb
-rwxrwx--- 1 root   654561  0002001-2024-08-20.bb
-rwxrwx--- 1 root   739563  0002002-2024-08-20.bb
-rwxrwx--- 1 root   708510  0002003-2024-08-20.bb
-rwxrwx--- 1 root   674891  0002004-2024-08-20.bb
-rwxrwx--- 1 root  1337254  0002005-2024-08-20.bb
-rwxrwx--- 1 root   289881  0002009-2024-09-05.bb
-rwxrwx--- 1 root   785387  0002010-2024-09-05.bb
-rwxrwx--- 1 root   699545  0002011-2024-09-05.bb
-rwxrwx--- 1 root   900471  0002013-2024-10-02.bb
-rwxrwx--- 1 root   901465  0002015-2024-10-02.bb
-rwxrwx--- 1 root   661088  0002016-2024-10-02.bb
-rwxrwx--- 1 root    28808  bcert.pkg.xml
-rwxrwx--- 1 root     3224  clist.pkg
-rwxrwx--- 1 root     8436  counters.pkg
-rwxrwx--- 1 root      823  CUST_INFO.DAT
-rwxrwx--- 1 root    15360  file.pkg.txt
```
