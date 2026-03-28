#numbers = [3,52,54,53,92,1]
#numbers.sort()
#print(numbers)
#print(sorted(numbers,reverse=True))

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]
def sort_item(item):
    return item[1]
items.sort(key=sort_item)
print(items)