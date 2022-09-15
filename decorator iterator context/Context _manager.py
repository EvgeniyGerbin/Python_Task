class MyContext:
    def __init__(self, file_name, method):
        self.method = method
        self.file_name = file_name

    def __enter__(self):
        self.file_obj = open(self.file_name, self.method)
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


with MyContext('Context.txt', 'w') as file:
    file.write('Hello World!')

