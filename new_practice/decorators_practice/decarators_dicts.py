_functions = {}


def register(f):
    global _functions
    _functions[f.__name__] = f
    return f


@register
def foo():
    return 'bar'
