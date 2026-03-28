items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]
prices = []
for items in items:
    prices.append(items[1])

x = map(lambda item: items[1], items)

print(x)