import time

def start_timer():
    return time.perf_counter()

def stop_timer(start_time):
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time