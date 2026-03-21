![banner](https://publicdomainpictures.net/pictures/250000/t2/cyber-security-1515836154wzI.jpg)

██████╗ ██████╗ ███████╗██╗██████╗ ██╗ █████╗ ███╗   ██╗
██╔═══██╗██╔══██╗██╔════╝██║██╔══██╗██║██╔══██╗████╗  ██║
██║   ██║██████╔╝███████╗██║██████╔╝██║███████║██╔██╗ ██║
██║   ██║██╔══██╗╚════██║██║██╔══██╗██║██╔══██║██║╚██╗██║
╚██████╔╝██████╔╝███████║██║██║  ██║██║██║  ██║██║ ╚████║
 ╚═════╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

# OBSIDIAN

Deterministic file analysis engine focused on entropy profiling, integrity verification, and anomaly detection.

---

## Profile

OBSIDIAN is built for environments where visibility matters more than automation.  
It performs low-level inspection of files using mathematical and cryptographic methods without abstraction layers.

This is not a scanner.  
This is an analysis engine.

---

## Core Capabilities

- Shannon entropy calculation across binary data  
- SHA-256 hashing for integrity verification  
- Recursive filesystem traversal  
- Structured logging with persistent output  
- Deterministic results without external dependencies  

---

## Architecture

core/
  analyzer.py   -> entropy + hashing engine  
  logger.py     -> structured logging system  

modules/
  entropy_scan.py  -> directory traversal and execution  

main.py           -> execution entry point  

---

## Execution Model

1. Traverse target directory  
2. Read file as raw bytes  
3. Compute entropy distribution  
4. Generate SHA-256 digest  
5. Log structured output  

---

## Usage

python main.py

Enter target directory when prompted:

/path/to/target

---

## Output Behavior

Each file produces a structured record:

[INFO] File: /data/archive.bin  
Hash: 9f86d081884c7d659a2fe...  
Entropy: 7.91  

---

## Interpretation

0.0 – 4.0    -> Low complexity (text / structured data)  
4.0 – 7.0    -> Mixed content  
7.0 – 8.0    -> High entropy (compressed / encrypted / packed)  

---

## Design Principles

- No hidden processing  
- No external services  
- No machine learning  
- Direct binary inspection only  

---

## Use Cases

- Identify packed or encrypted files  
- Verify file integrity across environments  
- Detect anomalous binaries in datasets  
- Pre-analysis before reverse engineering  

---

## Limitations

- No file type inference  
- No signature database  
- No automatic classification  

This is intentional.

---

## Roadmap

- JSON output mode  
- Parallel file processing  
- Signature matching module  
- CLI argument support  

---

## Environment

Designed for controlled lab environments and workflows.

---
