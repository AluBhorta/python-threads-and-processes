# Python Threads & Processes

Project for demonstration of usage of threads and processes using the fantastic concurrent.futures module (which provides a high-level interface for asynchronous task execution) as compared to the standard multiprocessing and threading modules.

You should:

- Use Multiprocessing for: CPU bound tasks - compute intensive
- Use Multithreading for: I/O bound tasks - network, file operations

- loops/lists should be iterated within the executor *context manager* (`with _ as _: `) iteratively running `executor.submit` or within `executor.map`. No point in iterating over loops/lists outside the *context manager*.


## Further Resources

- Python Docs for [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- Python [Threading Tutorial](https://www.youtube.com/watch?v=IEEhzQoKtQU) by
  Corey Schafer
- Python [Multiprocessing Tutorial](https://www.youtube.com/watch?v=fKl2JW_qrso) by
  Corey Schafer

## Deps

- python 3.6
- virtualenv
