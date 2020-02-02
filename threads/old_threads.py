import time
import threading


def wait_for(sec):
    print(f"Waiting for {sec} sec(s)...")
    time.sleep(sec)
    print(f"Done waiting for {sec} sec(s)...")


def run_one_by_one():
    '''running threads sequentially'''
    th1 = threading.Thread(target=wait_for, args=[1])
    th2 = threading.Thread(target=wait_for, args=[1])

    th1.start()
    th2.start()

    th1.join()
    th2.join()


def run_in_loop():
    secs = [5, 4, 3, 2, 1]
    threads = [threading.Thread(target=wait_for, args=[sec]) for sec in secs]

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    t1 = time.perf_counter()

    # run_one_by_one()
    run_in_loop()

    t2 = time.perf_counter()

    print(f"Time taken {round(t2-t1, 4)} sec(s)...")
