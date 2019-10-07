# Finding the first item in a list that satisfies a given condition,
# without using lambda()
import operator
from functools import partial
from first import first


def greater_than_zero(number):
    return number > 0


print(first([-1, 0, 1, 2], key=greater_than_zero))


# Instead of changing the behavior of a function, it changes the arguments
# it receives.

def greater_than(number, min=0):
    return number > min


print(first([-1, 0, 1, 2], key=partial(greater_than, min=42)))

# The version can be made shorter
print(first([-1, 0, 1, 2], key=partial(operator.le, 0)))
