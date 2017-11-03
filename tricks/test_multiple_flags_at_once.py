x, y, z = 0, 1, 0

# one.
if x == 1 or y == 1 or z == 1:
    print('passed')

# two.

if 1 in (x, y, z):
    print('passed')

# just test for truthiness.
#   three.
if x or y or z:
    print('passed')

#   four.
# Return True if bool(x) is True for any x in the iterable.
# if the iterable is empty. Return False. 
if any((x, y, z)):
    print('passed')

#  five.
# Return True if bool(x) is True for all x in the iterable.
# if the iterable is empty. Return True.
if all((x, y, z)):
    print('passed')