xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

# one.
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
result = sorted(xs.items(), key=lambda x: x[1])

# two.
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
import operator
result = sorted(xs.items(), key=operator.itemgetter(1))
# help document.
"""
class itemgetter(builtins.object)
 itemgetter(item, ...) --> itemgetter object
 Return a callable object that fetches the given item(s) from its operand.
 After f = itemgetter(2), the call f(r) returns r[2].
 After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
"""