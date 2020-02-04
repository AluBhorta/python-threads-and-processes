from bench import bench
import concurrent.futures as futures


def _write_to_file(file_path, data, mode='w'):
    with open(file_path, mode) as file:
        file.write(data)
        print(f'{file_path} was written to file...')


@bench
def do_write(data_len=1000000):
    f_path = f"data/data-{str(data_len)}"
    data = "hi " * data_len

    _write_to_file(f_path, data, "w")


@bench
def do_read(data_len, i):
    f_path = f"data/data-{str(data_len)}"

    with open(f_path, "r") as f:
        data = f.read()
        print(f"data was read by {i}. len of data: {len(data)}...")


def exec_with_threads(func, *a, **kw):
    with futures.ThreadPoolExecutor() as executor:
        executor.submit(func, *a, **kw)


def exec_with_processes(func, *a, **kw):
    with futures.ProcessPoolExecutor() as executor:
        executor.submit(func, *a, **kw)


if __name__ == "__main__":

    dl = int(1e8)

    # for _ in range(10):
    #     exec_with_threads(do_read, dl)
        # exec_with_processes(do_read, dl)

    with futures.ThreadPoolExecutor() as executor:
        [executor.submit(do_read, dl, i) for i in range(20)]

    
    # do_write(dl)
    # do_read(dl)
