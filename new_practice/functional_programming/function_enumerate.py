# Without enumerate

i = 0
while i < len(mylist):
    print("Item %d: %s" % (i, mylist[i]))
    i += 1


# With enumerate


for i, item in enumerate(mylist):
    print("Item %d: %s" % (i, item))
