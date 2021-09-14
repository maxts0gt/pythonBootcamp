def is_authenticated_decorator(function):
    def wrapper(*args):
        print(f'You called: {function.__name__}{args}')
        result = function(args[0], args[1], args[2])
        print(f'It returned: {result}')
    return wrapper


@is_authenticated_decorator
def a_function(x, y, z):
    return x + y + z


a_function(1, 2, 3)
