list = [13, 9, 14, 6, 2, 20]

small = list[0]

for i in range(len(list)):
    
    if small > list[i]:
       
        small = list[i]

print(small)