numbers = [1,1,2,3,4,5,6,7,8,9]
first = set(numbers)
second = {1, 4}
#second.add(5)
#second.remove(5)
#len(second)
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

print(first[0])