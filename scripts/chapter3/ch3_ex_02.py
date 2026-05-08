whours = int(40)

try:
    hours = float(input("Enter Hours: "))
    hrate = float(input("Enter Hours Rate: "))
    if hours > whours:
        upay = whours * hrate + ((hours - whours) * (hrate * 1.5))
    elif hours <= whours:
        upay = hours * hrate
    print(upay)
except ValueError:
    print('Error, please enter numeric input')
