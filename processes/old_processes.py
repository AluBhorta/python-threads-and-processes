import time
import multiprocessing


def wait_for(sec):
    '''target func'''
    print(f"Waiting for {sec} sec(s)...")
    time.sleep(sec)
    print(f"Done waiting for {sec} sec(s)...")


def run_one_by_one():
    '''running threads sequentially'''
    p1 = multiprocessing.Process(target=wait_for, args=[1])
    p2 = multiprocessing.Process(target=wait_for, args=[1])

    p1.start()
    p2.start()

    p1.join()
    p2.join()


def run_in_loop():
    secs = [5, 4, 3, 2, 1]
    processes = [multiprocessing.Process(target=wait_for, args=[sec]) for sec in secs]

    for p in processes:
        p.start()

    for p in processes:
        p.join()


t1 = time.perf_counter()

# run_one_by_one()
run_in_loop()

t2 = time.perf_counter()

print(f"Time taken {round(t2-t1, 4)} sec(s)...")
