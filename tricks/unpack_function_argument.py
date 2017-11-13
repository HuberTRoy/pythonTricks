
# Fcuntion argument unpacking.
def myFunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)

dict_vec = {'x': 1, 'y': 0, 'z': 1}

# 1, 0, 1
print(myFunc(*tuple_vec))

# 1, 0, 1
print(myFunc(**dict_vec))