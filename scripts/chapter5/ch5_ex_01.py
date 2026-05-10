num = 0
count = 0

def average():
    average = num / count
    print(int(num), count, average)

while True:
    snum = input("Enter a number: ")
    try:
        if snum == "done":
            break
        elif num >= 0:
            fnum = float(snum)
            num = num + fnum
            count = count + 1
    except:
        print("Invalid data")
        continue

average()
