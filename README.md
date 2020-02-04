# Python Threads & Processes

Note:

- Use Multiprocessing for: CPU bound tasks - compute intensive
- Use Multithreading for: I/O bound tasks - network, file operations

- loops/lists should be iterated within the *context manager* (`with _ as _: `) iteratively running beside `executor.submit` or within `executor.map`. No point in iterating over loops/lists outside the *context manager*.


## Resources

- Python Docs for [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- Python [Threading Tutorial](https://www.youtube.com/watch?v=IEEhzQoKtQU) by
  Corey Schafer
- Python [Multiprocessing Tutorial](https://www.youtube.com/watch?v=fKl2JW_qrso) by
  Corey Schafer

## Deps

- python 3.6
- virtualenv
