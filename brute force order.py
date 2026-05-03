list = [13, 9, 14, 6, 2, 20]

k = 0


for i in range(len(list)):
    
    for j in range(len(list)):
       
        if list[i] > list[j]:
            
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            k=k+1

print(list)
print(k)