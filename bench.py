import time
import concurrent.futures as futures


def bench(func):
    def inner(*args, **kwargs):
        t1 = time.perf_counter()
        func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f'Finished in {t2-t1} seconds')

    return inner


'''not really needed, i think'''
# def use_threads(func):
#     def inner(*args, **kwargs):
#         with futures.ThreadPoolExecutor() as executor:
#             f = executor.submit(func, *args, **kwargs)
#             return f.result()

#     return inner


'''pickling issue with ProcessPool'''
# def use_processes(func):
#     def inner(*args, **kwargs):
#         with futures.ProcessPoolExecutor() as executor:
#             f = executor.submit(func, *args, **kwargs)
#             return f.result()

#     return inner
