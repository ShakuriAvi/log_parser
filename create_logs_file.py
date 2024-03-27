import random
import datetime
import os

# Define arrays of page IDs and actions
page_ids = ["home", "product_page", "checkout", "profile", "search"]
actions = ["view", "click", "submit"]

# Generate random user ID between 1 and 20
def random_user_id():
    return random.randint(1, 20)


# Generate random timestamp within the last 2 weeks
def random_timestamp():
    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(days=14)
    random_time = start_time + (end_time - start_time) * random.random()
    return random_time.strftime('%Y-%m-%d %H:%M:%S')
# Generate random HTTP status code
def random_status_code():
    return random.choice([200, 404, 500])

# Generate random bytes transferred
def random_bytes_transferred():
    return random.randint(1000, 10000)

# Generate random duration between 1 and 180 seconds
def random_duration():
    return random.randint(1, 180)
# Generate random log entry
def generate_log_entry():
    timestamp = random_timestamp()
    user_id = random_user_id()
    page_id = random.choice(page_ids)
    action = random.choice(actions)
    duration = random_duration()
    status_code = random_status_code()
    bytes_transferred = random_bytes_transferred()
    return f"{timestamp},{user_id},{page_id},{action},{duration},{status_code},{bytes_transferred}"

def create_logs_files():
    # Define the number of log files to generate
    num_files = 50
    # Define the number of log entries per file
    num_entries_per_file = 10000

    # Create a directory to store the log files
    if not os.path.exists("log_files"):
        os.makedirs("log_files")

    # Generate log files
    for i in range(num_files):
        filename = f"logs/log_file_{i+1}.txt"
        with open(filename, "w") as file:
            file.write("Timestamp,User_ID,Page_ID,Action,Duration(seconds),Status_Code,Bytes_Transferred\n")
            for _ in range(num_entries_per_file):
                log_entry = generate_log_entry()
                file.write(log_entry + "\n")

if __name__ == "__main__":
    create_logs_files()
