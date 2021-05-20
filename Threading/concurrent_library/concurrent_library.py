import time
import concurrent.futures


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s).. ')
    time.sleep(seconds)
    return f'Done Sleeping.. {seconds} second(s)'


start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [i for i in range(1, 10)]
    results = [executor.submit(do_something, sec) for sec in reversed(secs)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
