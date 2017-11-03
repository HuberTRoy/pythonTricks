x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

# merging two dicts.

# one.
z = {**x, **y}
# {'c': 4, 'a': 1, 'b': 3}

# two.
z = dict(x, **y)
# {'c': 4, 'a': 1, 'b': 3}
