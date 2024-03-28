import json
import csv

class FileReadingStrategy:
    """
    Abstract base class for file reading strategies.
    Subclasses must implement the read_file method.
    """
    def read_file(self, file_path: str):
        """
        Abstract method to read a file.
        """
        raise NotImplementedError("Subclasses must implement read_file method")

class TextFileReadingStrategy(FileReadingStrategy):
    """
    Strategy for reading text files.
    """
    def read_file(self, file_path: str):
        """
        Reads a text file and returns its contents as a list of dictionaries.
        """
        logs = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            headers = lines[0].strip().split(',')
            for line in lines[1:]:
                values = line.strip().split(',')
                log = {headers[i]: values[i] for i in range(len(headers))}
                logs.append(log)
        return logs

class JSONFileReadingStrategy(FileReadingStrategy):
    """
    Strategy for reading JSON files.
    """
    def read_file(self, file_path: str):
        """
        Reads a JSON file and returns its contents as a list of dictionaries.
        """
        with open(file_path, 'r') as file:
            return json.load(file)

class CSVFileReadingStrategy(FileReadingStrategy):
    """
    Strategy for reading CSV files.
    """
    def read_file(self, file_path: str):
        """
        Reads a CSV file and returns its contents as a list of dictionaries.
        """
        logs = []
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                logs.append(row)
        return logs

# Dictionary mapping file extensions to corresponding reading strategy classes
FILE_ENTITY = {
    "txt": TextFileReadingStrategy,
    "csv": CSVFileReadingStrategy,
    "json": JSONFileReadingStrategy
}

class FileReader:
    """
    Class responsible for reading files based on their type.
    """
    def __init__(self, file_type: str):
        """
        Initializes the FileReader object with the specified file type.
        """
        self.reading_strategy = self.__init_file_entity(file_type)()

    def __init_file_entity(self, file_type: str):
        """
        Initializes the appropriate reading strategy based on the file type.
        """
        return FILE_ENTITY[file_type]

    def read(self, file_path: str):
        """
        Reads a file using the corresponding reading strategy.
        """
        return self.reading_strategy.read_file(file_path)
