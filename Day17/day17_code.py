#Challenge -  Build a context manager for safe file handling

# Custom context manager for file handling
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print(f"Closed file: {self.filename}")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True  

# Test cases
with FileManager("myfile.txt", "w") as f:
    f.write("This is a test using a custom context manager.")

with FileManager("myfile.txt", "r") as f:
    content = f.read()
    print("File content:", content)

