from modules import entropy_scan

target = input("Enter directory to scan: ")
results = entropy_scan.run(target)
print("\nScan completed. Files analyzed:", len(results))
