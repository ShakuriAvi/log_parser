import os
from file_handler import FileHandler


import multiprocessing

DIRECTORY_NAME = 'logs'


class FilesManager:
    files_names_lst = None

    def __init__(self):
        """
        Initializes the FilesManager object.
        Sets the directory path and retrieves the list of file names in the directory.
        """
        self.directory_path = DIRECTORY_NAME
        self.__get_files_name()

    def __get_files_name(self):
        """
        Retrieves the list of file names in the directory and stores it in files_names_lst.
        """
        self.files_names_lst = os.listdir(self.directory_path)
        print("Files in the directory:", self.files_names_lst)

    def stream_files(self):
        """
        Streams logs from multiple files in parallel using multiprocessing.

        Yields:
        - Each log extracted from the files in the directory.
        """
        with multiprocessing.Pool(processes=4) as pool:
            files_results = pool.map(self.file_process, self.files_names_lst)
        logs_file = [item for sublist in files_results for item in sublist]
        for log in logs_file:
            yield log

    def file_process(self, file_name: str):
        """
        Processes an individual file to extract logs.

        Parameters:
        - file_name: Name of the file to be processed.

        Returns:
        - List of logs extracted from the file.
        """
        file_execute = FileHandler(f"{self.directory_path}/{file_name}")
        return file_execute.read()
