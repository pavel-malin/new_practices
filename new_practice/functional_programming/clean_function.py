# Not pure function


def remove_last_item(mylist):
    """Removes the last item from a list."""
    mylist.pop(-1)  # List Modigcation


# Net of the same function
def butlast(mylist):
    return mylist[:-1]  # Returns a copy mylist
