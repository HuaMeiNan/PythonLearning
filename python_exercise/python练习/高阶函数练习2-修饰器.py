''' 写出一个@log的decorator，使它及支持
@log
def f():
    pass
又支持
@log('exectue')
def f():
    pass '''

import functools

def log(text):
    if isinstance(text, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s (): ' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        def wrapper(*args, **kw):
            print('call %s' % (text.__name__))
            return text(*args, **kw)
        return wrapper


@log
def now():
    print("pefrect")

now()

@log('name')
def biu():
    print("xuan")

biu()



