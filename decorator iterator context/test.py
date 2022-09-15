
def dec_arg(arg):

    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(arg=arg, *args, **kwargs)
            return res
        return wrapper
    return decorator

@dec_arg(50)
def sqr(num, n, **kwargs):

    return (num**2 + kwargs['arg'])


print(sqr(1, 45))

def dec_arg(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, arg, **kwargs)
            return res
        return wrapper
    return decorator

@dec_arg(20)
def sqr(num, n):

    return (num**2) + n


print(sqr(1))