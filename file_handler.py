from entity.file import FileReader


class FileHandler:
    logs_file = None

    def __init__(self, file_name: str):
        """
        Initializes the FileHandler object with the given file name.

        Parameters:
        - file_name: Name of the log file to be handled.
        """
        self.file_name = file_name
        self.file_reader = FileReader(self.__get_file_type(file_name))

    def __get_file_type(self, file_name: str):
        """
        Determines the file type based on the file extension.

        Parameters:
        - file_name: Name of the log file.

        Returns:
        - File type (e.g., 'csv', 'json', 'txt').
        """
        return file_name.split(".")[1]

    def read(self):
        """
        Reads the log file using the appropriate file reader based on the file type.

        Returns:
        - List of logs extracted from the file.
        """
        return self.file_reader.read(self.file_name)
