import time
import concurrent.futures


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s).. ')
    time.sleep(seconds)
    return f'Done Sleeping.. {seconds} second(s)'


start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [i for i in range(1, 10)]
    results = executor.map(do_something, secs)

    # if there is any exception in do_something method
    # it will be raised when its value is retreived from the results 
    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
