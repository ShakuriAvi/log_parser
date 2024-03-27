from logs_manager import LogsManager

import time

def start():
    start_time = time.time()
    logs_manager = LogsManager()
    logs_manager.run()
    print("--- %s seconds ---" % (time.time() - start_time))



if __name__ == '__main__':
    start()