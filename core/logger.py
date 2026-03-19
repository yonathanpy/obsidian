import datetime

class Logger:
    def __init__(self, file="obsidian.log"):
        self.file = file

    def log(self, level, message):
        entry = f"[{datetime.datetime.now()}] [{level}] {message}"
        print(entry)
        with open(self.file, "a") as f:
            f.write(entry + "\n")

logger = Logger()
