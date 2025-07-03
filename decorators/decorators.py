import functools
import time
from time import sleep

"""
template
"""
def template(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

"""
template with args
"""

def template_with_args(_func=None, *, key1=1, key2=2):
    def decorator_name(func):
        ...  # Create and return a wrapper function.

    if _func is None:
        return decorator_name
    else:
        return decorator_name(_func)

"""
log function which implemented by as decorator
print data about function call
"""
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        print(f'Calling {func_name} with args={args} kwargs={kwargs}')
        return func(*args, **kwargs)
    return wrapper

"""
timing the time it took to execute the function
"""

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f'{func.__name__} took {elapsed_time:0.4f} seconds')
        return func(*args, **kwargs)
    return wrapper


def delay(_func=None, *, rate=1):
    def slow_down(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(rate)
            func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper

    if _func is None:
        return slow_down
    else:
        return slow_down(_func)
