import threading
import multiprocessing
from queue import Queue
import time
from decimal import Decimal
from decimal import getcontext
import math

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def e_serie_part(k_start, k_end, que=None):
    getcontext().prec = 100
    partial_sum = 0

    for k in range(k_start, k_end):
            partial_sum += Decimal(1)/factorial(k)

    if que is not None:
        que.put(partial_sum)
    else:
        return partial_sum



# print(f"e approximation: {e_serie_part(0, 100000)}")

def main():
    qres = Queue()

    N = 100000
    threads_count = 8

    num_cores = multiprocessing.cpu_count()
    print(f"Number of cores: {num_cores}")


    getcontext().prec = 100

    start_time = time.time()

    step = N // num_cores
    ranges = [(i * step, (i + 1) * step) for i in range(num_cores)]
    ranges[-1] = (ranges[-1][0], N)

    with multiprocessing.Pool(num_cores) as pool:
        results = pool.starmap(e_serie_part, ranges)
        for r in results:
            qres.put(r)

    '''
    thread_list = []
    for i in range(threads_count):
        t = threading.Thread(target=e_serie_part, args=(i * N // threads_count, (i + 1) * N // threads_count, qres))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()
    '''
    end_time = time.time()

    print(f"Threads finished. Elapsed time: {end_time - start_time}. {qres.qsize()} elements in queue.")

    e_approx = 0

    while not qres.empty():
        e_approx += qres.get()

    print(f"e approximation: {e_approx}")


if __name__ == "__main__":
    main()