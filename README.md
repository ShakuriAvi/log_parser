# log_parser
# System Design: 
![image](https://github.com/ShakuriAvi/log_parser/assets/65177459/e1bcebb5-4500-4759-8c7a-3c4e8981f992)


# Project Overview
# Description
This project aims to efficiently filter a large amount of log data stored in multiple files based on criteria such as data_date, user_id, and status code. The system is composed of four key components designed to handle file input, manage logs, and filter them effectively.

# Components
1) File Handler

* Responsible for handling individual log files.
* Utilizes the Strategy design pattern to support reading CSV, JSON, and text files.
* Returns a list of logs to the File Manager upon completion.
2) File Manager

* Manages the directory of log files.
* Reads file names and dispatches them to the File Handler.
* Utilizes parallel processing to optimize file handling.
3) Log Handler

* Receives logs from the Logs Manager and checks them against specified conditions.
* Prints logs that meet the conditions and returns a count of filtered logs.
4) Logs Manager

* Coordinates the processing of logs.
* Distributes logs to the Log Handler for filtering.
* Utilizes parallel processing to enhance performance.

# Performance Comparison
Without Parallelization
Runtime: 11.494 seconds
With Parallelization
Runtime: 6.809 seconds
# Performance Improvement
The implementation of parallel processing significantly reduces the runtime of the system, improving efficiency when handling a large volume of logs. By parallelizing file handling and log filtering operations, the overall throughput of the system is enhanced, resulting in faster processing times.
