class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    # extra param to handle an exception if it occurs
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

# Already availabe to run with context manager
with open('sample.txt', 'w') as f:
    f.write("The quick brown fox jumped over a lazy dog.")

# User defined context manager
with Open_File('sample.txt', 'w') as f:
    f.write('Testing.. from class')

print(f.closed)