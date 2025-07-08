# Challenge - find the faults in your code (or some opensource code), improve it by applying clean code principles and make it readable (create a PR if doing it for any opensource project). 

# Clean Code Version: Custom File Context Manager

class FileManager:
    """Context manager for safe file handling."""

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"📂 Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"✅ Closed file: {self.filename}")
        if exc_type:
            print(f"⚠️ Exception occurred: {exc_val}")
        return True  # Prevents exception propagation

def write_to_file(filename: str, content: str):
    """Writes content to a file using FileManager."""
    with FileManager(filename, "w") as file:
        file.write(content)

def read_from_file(filename: str) -> str:
    """Reads content from a file using FileManager."""
    with FileManager(filename, "r") as file:
        return file.read()

# --- Usage ---
file_name = "myfile.txt"
text = "This is a test using a custom context manager."

write_to_file(file_name, text)
content = read_from_file(file_name)

print("📝 File content:", content)


