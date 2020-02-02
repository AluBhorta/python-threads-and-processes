import time
import concurrent.futures as futures


def _run_for(n=int(1e7)):
    c = 0
    for i in range(n):
        c += 1
    return c


def run_with_threads(n=10):
    with futures.ThreadPoolExecutor() as executor:
        fs = [executor.submit(_run_for) for _ in range(n)]

        for f in fs:
            print(f.result())


def run_with_processes(n=10):
    with futures.ProcessPoolExecutor() as executor:
        fs = [executor.submit(_run_for) for _ in range(n)]

        # for f in futures.as_completed(fs):
        for f in fs:
            print(f.result())


if __name__ == "__main__":

    t1 = time.perf_counter()

    # res = [_run_for() for _ in range(times)]
    # run_with_threads(20)
    run_with_processes(20)

    t2 = time.perf_counter()

    print(f'Finished in {t2-t1} seconds')
