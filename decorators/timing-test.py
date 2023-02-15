from time import perf_counter

def timing_test(count):
    '''This function runs the same function count times and returns the average run time'''
    def speed_test(func):
        run_times = []
        def wrapper(*args, **kwargs):
            for _ in range(count):
                start_time = perf_counter()
                func()
                end_time = perf_counter()
                run_times.append(end_time-start_time)
            return sum(run_times)/len(run_times)
        return wrapper
    return speed_test


@timing_test(1000)
def do_sth():
    start = 0
    for i in range(1000):
        start += i

print(do_sth())
