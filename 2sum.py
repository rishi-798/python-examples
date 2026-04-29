
datavalue = input("Enter list of numbers (space-separated): ")
total = int(input("Enter the total: "))


nums = list(map(int, datavalue.split()))


seen = set()

for num in nums:
    needed = total - num 
    if needed in seen:
        print("Yes, pair found:", num, "and", needed)
        break
    seen.add(num)
else:
    print("No pair found")