from time import perf_counter

def timing_test(count):
    '''This function runs the same function count times and returns the average run time'''
    def speed_test(func):
        run_times = []
        def wrapper(*args, **kwargs):
            for _ in range(count):
                start_time = perf_counter()
                func(*args, **kwargs)
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

@timing_test(1000)
def do_sth2(val):
    cnt = 0
    for _ in range(val):
        cnt += 1


print(do_sth())
print(do_sth2(100))
