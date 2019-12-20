import time
import concurrent.futures as futures


def wait_for(sec):
    print(f"Waiting for {sec} sec(s)...")
    time.sleep(sec)
    return f"Done waiting for {sec} sec(s)..."


def one_by_one():
    with futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(wait_for, 1)
        f2 = executor.submit(wait_for, 1)

        print(f1.result())
        print(f2.result())


def in_loop(secs):
    with futures.ProcessPoolExecutor() as executor:
        fs = [executor.submit(wait_for, sec) for sec in secs]

        for r in fs:
            print(r)
        for r in fs:
            print(r.result())
        for r in fs:
            print(r)


def in_loop_as_completed(secs):
    with futures.ProcessPoolExecutor() as executor:
        fs = [executor.submit(wait_for, sec) for sec in secs]

        for f in futures.as_completed(fs):
            print(f.result())


def by_map(secs):
    with futures.ProcessPoolExecutor() as executor:
        results = executor.map(wait_for, secs)

        for r in results:
            print(r)


t1 = time.perf_counter()

secs = [5, 4, 3, 2, 1]
# one_by_one()
# in_loop(secs)
# in_loop_as_completed(secs)
by_map(secs)

t2 = time.perf_counter()

print(f"Time taken {round(t2-t1, 4)} sec(s)...")
