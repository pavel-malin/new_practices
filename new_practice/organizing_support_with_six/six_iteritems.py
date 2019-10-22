import six


mydicts = {'one': 1, 'two': 2}


# To replace python 2 specific code.
for k, v in mydicts.iteritems():
    print(k, v)


# Replaced mydict.iteritems() code with python 2 and 3 compatible
# code as follows.
for k, v in six.iteritems(mydicts):
    print(k, v)
