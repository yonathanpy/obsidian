![banner](https://publicdomainpictures.net/pictures/250000/t2/cyber-security-1515836154wzI.jpg)

# OBSIDIAN

Advanced file and system forensic analyzer for security researchers.

---

## Overview

OBSIDIAN scans directories and files to detect anomalies using entropy and hash calculations.  
It provides structured logging and deterministic output for forensic workflows.

---

## Architecture

```text
core/
  analyzer.py  -> entropy & hash logic
  logger.py    -> logging system

modules/
  entropy_scan.py  -> directory scanning

main.py          -> entry point
