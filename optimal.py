list = [13, 9, 14, 6, 2, 20]

i = 0

j = len(list) - 1

k = 0 

while i < j:

    k = k + 1

    if list[i] > list[j]:
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
        i = i + 1
    else:
        j = j - 1

   

print(list)
print(k)