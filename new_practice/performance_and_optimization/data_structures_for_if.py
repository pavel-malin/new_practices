fields = ['foo', 'bar']


def has_invalid_fields(fields):
    for field in fields:
        if field not in ['foo', 'bar']:
            return True
    return False


# Removing the iteration
def has_invalid_fields_n(fields):
    return bool(set(fields) - set(['foo', 'bar']))
