score = input("Enter Score: ")
scr = float(score)

if 0.0 <= scr <= 1.0:
    try:
        if scr >= 0.9:
            print('A')
        elif scr >= 0.8:
            print('B')
        elif scr >= 0.7:
            print('C')
        elif scr >= 0.6:
            print('D')
        elif scr < 0.6:
            print('F')
    except:
        print("Oops! Something goes wrong!")
        quit()
else:
    print("Oops! Something goes wrong!")
