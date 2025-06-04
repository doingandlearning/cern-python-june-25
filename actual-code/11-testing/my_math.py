def add(a, b):
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("Must be numbers")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("Must be numbers")

    return a + b


