import time
import concurrent.futures as futures
from bench import bench


def _run_for(n=int(1e7)):
    c = 0
    for i in range(n):
        c += 1
    return c


@bench
def run_sequencially(n=10):
    for _ in range(n):
        print(_run_for())


@bench
def run_with_threads(n=10):
    with futures.ThreadPoolExecutor() as executor:
        fs = [executor.submit(_run_for) for _ in range(n)]

        for f in fs:
            print(f.result())


@bench
def run_with_processes(n=10):
    with futures.ProcessPoolExecutor() as executor:
        fs = [executor.submit(_run_for) for _ in range(n)]

        # for f in futures.as_completed(fs):
        for f in fs:
            print(f.result())


if __name__ == "__main__":

    n = 20

    # run_sequencially(n)
    # run_with_threads(n)
    run_with_processes(n)
