a =[1, 2, 3]
b = a
# True.
print(a is b)
# True.
print(a == b)

c = list(a)
# False.
print(a is c)
# False.
print(a == c)

# 如果两个变量指向同一个对象则is返回True.
# "is" expressions evaluate to True if two #   variables point to the same object
# 如果两个变量拥有相同的值则==返回True。
# "==" evaluates to True if the objects #   referred to by the variables are equal