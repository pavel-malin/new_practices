# Multiprocessing for simultaneous actions
import multiprocessing
import random


def compute(n):
    return sum([random.randint(1, 100) for i in range(1000000)])


pool = multiprocessing.Pool(processes=4)
print("Results: %s" % pool.map(compute, range(4)))
