from sys import getsizeof

values = (x*2 for x in range(10000))
print("gen:" getsizeof(values))

print(len(values))

