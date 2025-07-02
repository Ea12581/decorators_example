import functools


"""
log function which implemented by as decorator
print data about function call
"""
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        print(f'Calling {func_name} with args=({args}) kwargs=({kwargs})')
        return func(*args, **kwargs)
    return wrapper