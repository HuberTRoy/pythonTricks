from collections import namedtuple

# use string.
Car = namedtuple('Car', 'name color')

# use other iterable class.
Car = namedtuple('Car', ['name', 'color'])

my_car = Car('rabbit', 'light gray')

# light gray.
print(my_car.color)

# Car(name='rabbit' , color='light gray')
print(my_car)

# Namedtuples are immutable.
# AttributeError: can't set attribute.
my_car.color = 'blue'