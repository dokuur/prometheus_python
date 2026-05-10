num = 0.0
count = 0

while True:
    snum = input("Enter a number: ")
    if snum == "done":
        break
    try:
        fnum = float(snum)
    except:
        print("Invalid data")
        continue
    num = num + fnum
    count = count + 1

print(num, count, num/count)
