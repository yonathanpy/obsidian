
# OBSIDIAN

Advanced file and system forensic analyzer for security researchers.

---

## Overview

OBSIDIAN scans directories and files to detect anomalies using entropy and hash calculations.  
It provides structured logging and deterministic output for forensic workflows.

---

## Architecture

core/
  analyzer.py  -> entropy & hash logic
  logger.py    -> logging system

modules/
  entropy_scan.py  -> directory scanning

main.py          -> entry point


---

## Features

- Recursive directory scanning  
- Entropy analysis to detect suspicious files  
- SHA-256 hashing for integrity check  
- Detailed logging system  
- Lightweight and modular  

---

## Usage

```bash
python main.py

Input the target directory, e.g.:

/home/user/documents

Output

Logs to console + obsidian.log file with entries like:

[2026-03-19 12:01:01] [INFO] File: /home/user/documents/test.pdf | Hash: <hash> | Entropy: 7.82
