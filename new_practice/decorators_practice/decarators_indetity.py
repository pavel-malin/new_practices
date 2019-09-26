def identity(f):
    return f


@identity
def foo():
    return 'bar'


'''
Equally:

def foo():
    return 'bar'
foo = identity(foo)
'''
