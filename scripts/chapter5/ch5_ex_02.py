numbers = []
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)

print('Maximum is',largest)
print('Minimum is',smallest)
