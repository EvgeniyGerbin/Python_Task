import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_func = time.perf_counter()
        value = func(*args, **kwargs)
        end_func = time.perf_counter()
        run_func = end_func - start_func
        print(f"Function {func.__name__!r} completed for {run_func:.6f} sec!")
        return value
    return wrapper


@timer
def sqr(n):
    print(n ** 2)

sqr(5)
