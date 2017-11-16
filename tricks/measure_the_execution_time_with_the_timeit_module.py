import timeit

# 0.03606944642825069
# 
times = timeit.timeit('-'.join([str(n) for n in range(100)]), number=10000)
print(times)

# 0.07355483159694455
times = timeit.timeit('-'.join([str(n) for n in range(100)]), number=10000)
print(times)
# 0.06709907465773282
times = timeit.timeit('-'.join([str(n) for n in range(100)]), number=10000)
print(times)