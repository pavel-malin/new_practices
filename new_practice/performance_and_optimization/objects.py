class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Foobar(object):
    def __init__(self, x):
        self.x = x


class Foobars(object):
    __slots__ = ('x',)

    def __init__(self, x):
        self.x = x


@profile
def main():
    f = [Foobar(42) for i in range(100000)]  # Foobar -->> Foobars memory


if __name__ == '__main__':
    main()
