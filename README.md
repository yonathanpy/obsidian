<p align="center">
  <img src="./assets/obsidian_binary_analysis.svg" width="400" alt="OBSIDIAN Binary Analysis Banner" />
</p>


![status](https://img.shields.io/badge/status-stable-black)
![python](https://img.shields.io/badge/python-3.x-blue)
![license](https://img.shields.io/badge/license-MIT-grey)

Deterministic binary inspection engine for entropy profiling and integrity verification.

---

## Overview

OBSIDIAN is a low-level file analysis tool built for precise, repeatable inspection of binary data.

It operates directly on raw bytes and produces deterministic outputs using strict mathematical methods.  
No heuristics, no probabilistic models, no external services.

---

## Features

- Shannon entropy computation (byte-level)
- SHA-256 hashing for integrity validation
- Recursive directory traversal
- Structured logging output
- Deterministic execution model
- Zero external dependencies

---

## Architecture

```
core/
 ├── analyzer.py       # entropy + hashing primitives
 └── logger.py         # structured logging

modules/
 └── entropy_scan.py   # traversal + execution logic

main.py                # entry point
```

---

## Execution Pipeline

1. Traverse target directory  
2. Read files as raw byte streams  
3. Compute entropy values  
4. Generate SHA-256 digest  
5. Emit structured log output  

Execution is linear and state-independent.

---

## Usage

```bash
python main.py
```

Input:

```
/path/to/target
```

---

## Output

```
[INFO] File: /data/archive.bin
Hash: 9f86d081884c7d659a2feaa0c55ad015...
Entropy: 7.91
```

---

## Entropy Scale

| Range       | Meaning                                |
|------------|----------------------------------------|
| 0.0 – 4.0  | Low entropy (text / structured data)   |
| 4.0 – 7.0  | Mixed content                          |
| 7.0 – 8.0  | High entropy (compressed/encrypted)    |

---

## CLI (planned)

```bash
python main.py --path /target --json --threads 4
```

---

## Design Constraints

- No abstraction layers  
- No hidden processing  
- No signature databases  
- No machine learning components  
- No automatic classification  

All outputs are directly derived from input data.

---

## Use Cases

- Detection of packed or encrypted binaries  
- File integrity verification across environments  
- Entropy-based anomaly detection  
- Pre-analysis for reverse engineering  
- Dataset inspection in forensic workflows  

---

## Limitations

- No file type detection  
- No signature matching  
- No behavioral analysis  
- No automatic labeling  

---

## Roadmap

- JSON output mode  
- Parallel processing  
- CLI argument support  
- Signature matching module  

---

## Environment

Designed for controlled environments including:

- Security research labs  
- Reverse engineering workflows  
- Forensic analysis pipelines  

---

