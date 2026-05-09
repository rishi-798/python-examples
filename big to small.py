list = [13, 9, 14, 6, 2, 20]

big = list[0]
for i in range(len(list)):
    if big < list[i]:
        big = list[i]

print(big)