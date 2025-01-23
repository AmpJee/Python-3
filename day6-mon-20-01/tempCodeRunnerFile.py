
qres = Queue()

N = 100
threads_count = 8

num_cores = multiprocessing.cpu_count()
print(f"Number of cores: {num_cores}")

getcontext().prec = 100

start_time = time.time()

thread_list = []
for i in range(threads_count):
    t = threading.Thread(target=e_serie_part, args=(i * N // threads_count, (i + 1) * N // threads_count, qres))
    thread_list.append(t)
    t.start()

for t in thread_list:
    t.join()

end_time = time.time()

print(f"Threads finished. Elapsed time: {end_time - start_time}. {qres.qsize()} elements in queue.")

e_approx = 0

while not qres.empty():
    e_approx += qres.get()

print(f"e approximation: {e_approx}")