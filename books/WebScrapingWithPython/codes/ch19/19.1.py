# 19.1.py
# Multithread

import threading
import time


def print_time(thread_name, delay, iterations):
    start = int(time.time())
    for i in range(0, iterations):
        time.sleep(delay)
        print(f"{int(time.time())-start} - {thread_name}")


threads = [
    threading.Thread(target=print_time, args=("A", 3, 33)),
    threading.Thread(target=print_time, args=("B", 5, 20)),
    threading.Thread(target=print_time, args=("C", 1, 100)),
]

# Start all threads
[t.start() for t in threads]
# Wait all threads to complete
[t.join() for t in threads]
