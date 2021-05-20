import time
import threading


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s).. ')
    time.sleep(seconds)
    print('Done Sleeping..')
    return seconds


start = time.perf_counter()
threads = []

for i in range(10):
    t = threading.Thread(target=do_something, args=[i])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
