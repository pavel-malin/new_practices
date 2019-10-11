# If a KeyError error is detected
def get_fruits(basket, fruit):
    try:
        return basket[fruit]
    except KeyError:
        return None


# Checks for a key
def get_fruits_k(basket, fruit):
    if fruit in basket:
        return basket[fruit]


# Avoid having to look for errors and check for a key from the very
# beginning with get()
def get_fruits_e(basket, fruit):
    return basket.get(fruit)


# The dict.get() method can return a default value instead of None
def get_fruits_n(basket, fruit):
    # Return the fruit, Banana if the fruit cannot be found.
    return basket.get(fruit, Banana())
