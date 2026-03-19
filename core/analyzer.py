import math
import hashlib
import os
from core.logger import logger

def entropy(data):
    freq = [0]*256
    for b in data:
        freq[b] += 1
    e = 0
    for f in freq:
        if f == 0: continue
        p = f / len(data)
        e -= p * math.log2(p)
    return e

def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

def analyze_file(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        e = entropy(data)
        h = hash_file(path)
        logger.log("INFO", f"File: {path} | Hash: {h} | Entropy: {round(e,2)}")
        return {"file": path, "hash": h, "entropy": e}
    except Exception as ex:
        logger.log("ERROR", f"Cannot analyze {path}: {ex}")
        return None

def scan_dir(directory):
    results = []
    for root, _, files in os.walk(directory):
        for f in files:
            res = analyze_file(os.path.join(root, f))
            if res: results.append(res)
    return results
