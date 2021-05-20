import time
import multiprocessing


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s).. ')
    time.sleep(seconds)
    print('Done Sleeping..')
    return seconds

if __name__ == '__main__':
    start = time.perf_counter()
    processes = []

    for i in range(10):
        p = multiprocessing.Process(target=do_something, args=[i])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
