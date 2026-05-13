print("Variant 1:")
fruit = "watermalone"
index = len(fruit) - 1
while index >= 0:
    letter = fruit[index]
    print(index,letter)
    index = index - 1

print("\nVariant 2:")
fruit2 = "watermalone"
fruit2 = fruit2[::-1]
index2 = 0
while index2 < len(fruit2):
    letter = fruit2[index2]
    print(index2,letter)
    index2 = index2 + 1