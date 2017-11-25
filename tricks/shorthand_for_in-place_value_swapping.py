a = 23
b = 42
# The "classic" way to do it with a temporary variable:
tmp = a
a = b
b = tmp

# Python also lets us use this short-hand:
a,b = b,a
