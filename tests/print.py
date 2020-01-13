import functools
from collections import Iterable


def log(func):
    @functools.wraps(func)
    def wrap():
        pass

    return wrap


print('hello')
