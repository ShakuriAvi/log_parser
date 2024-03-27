from files_manager import FilesManager
from log_handler import LogHandler

import multiprocessing

DIRECTORY_NAME = 'logs'


class LogsManager:
    def __init__(self):
        """
        Initializes the LogsManager object.
        Creates an instance of FilesManager to manage log files.
        """
        self.files_manager = FilesManager()

    def process_log(self, log):
        """
        Processes an individual log using LogHandler.

        Parameters:
        - log: Log entry to be processed.

        Returns:
        - Result of log processing.
        """
        log_handler = LogHandler(log)
        return log_handler.run()

    def run(self):
        """
        Runs the LogsManager to process logs from multiple files in parallel.
        Prints the total number of processed logs.
        """
        with multiprocessing.Pool(processes=4) as pool:
            log_results = pool.map(self.process_log, self.files_manager.stream_files())
        filter_logs = sum(1 for result in log_results if result is True)
        print("Total logs processed:", filter_logs)
