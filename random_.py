import random

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 8, 9]))
print(random.choices([1, 2, 3, 8, 9], k=2))
print(random.choices("Nilofar13691362", k=5))

# data = "".join([1, 2, 12])
# print(data)
print("".join(random.choices("Nilofar13691362", k=5)))
# print("".join(random.choices([1, 2, 3, 8, 9], k=2)))
print(type("".join(random.choices("Nilofar13691362", k=5))))
