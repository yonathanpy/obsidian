from core.analyzer import scan_dir

def run(target_dir):
    print(f"Scanning directory: {target_dir}")
    return scan_dir(target_dir)
