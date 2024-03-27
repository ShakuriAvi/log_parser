from datetime import datetime, timedelta

DAYS_AGO = 7


class LogHandler:
    def __init__(self, log):
        """
        Initializes the LogHandler object with the given log entry.

        Parameters:
        - log: Log entry to be processed.
        """
        self.log = log

    def run(self):
        """
        Runs the log processing logic.
        If the log is not valid, prints it and returns True.
        Otherwise, returns False.

        Returns:
        - True if the log is not valid, False otherwise.
        """
        if self.not_valid():
            self.__info(self.log)
            return True
        return False

    def not_valid(self):
        """
        Checks if the log is not valid based on criteria.

        Returns:
        - True if the log is not valid, False otherwise.
        """
        timestamp = self.log.get("Timestamp")
        user_id = self.log.get("User_ID")
        status_code = self.log.get("Status_Code")

        return self.is_few_days_ago(timestamp) and self.check_user(user_id) and self.status_code_error(status_code)

    def check_user(self, user_id):
        """
        Checks if the user ID meets a certain condition.

        Parameters:
        - user_id: User ID to be checked.

        Returns:
        - True if the user ID meets the condition, False otherwise.
        """
        return int(user_id) % 2 == 0

    def status_code_error(self, status_code):
        """
        Checks if the status code indicates an error.

        Parameters:
        - status_code: Status code to be checked.

        Returns:
        - True if the status code indicates an error, False otherwise.
        """
        return int(status_code) >= 400

    def is_few_days_ago(self, date_string):
        """
        Checks if the date is within the specified number of days ago.

        Parameters:
        - date_string: Date string to be checked.

        Returns:
        - True if the date is within the specified number of days ago, False otherwise.
        """
        converted_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        current_date = datetime.now()
        one_week_ago = current_date - timedelta(days=DAYS_AGO)
        return converted_date < one_week_ago

    def __info(self, item):
        """
        Prints the given item (log entry).

        Parameters:
        - item: Item to be printed.
        """
        print(item)
