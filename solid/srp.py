class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as f:
            contents = f.read()
        return contents


class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        # process data and return result
        pass


class ResultWriter:
    def __init__(self, result, output_file_path):
        self.result = result
        self.output_file_path = output_file_path

    def write_result(self):
        with open(self.output_file_path, 'w') as f:
            f.write(self.result)
