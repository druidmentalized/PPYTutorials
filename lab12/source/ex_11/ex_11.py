class FileReader:
    @classmethod
    def read_file(cls, filename: str) -> str:
        try:
            with open(filename) as f:
                return f.read()
        except FileNotFoundError:
            return "File not found"

# Normal read
print(f"Data read: {FileReader.read_file("/Users/dmitriy/PycharmProjects/PPYTasks/lab12/source/ex_11/test_file.txt")}")

# Exception read
print(f"Data read: {FileReader.read_file("some/unexistent/location.txt")}")