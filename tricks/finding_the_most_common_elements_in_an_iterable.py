# collections.Counter lets you find the most common
# elements in an iterable:
import collections
c = collections.Counter('helloworld')
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'd': 1, 'w': 1, 'r': 1})
print(c)
# [('l', 3), ('o', 2), ('h', 1)]
print(c.most_common(3))