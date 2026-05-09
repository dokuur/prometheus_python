whours = int(40)

def computepay():
    hours = float(input("Enter Hours: "))
    hrate = float(input("Enter Hours Rate: "))
    return hours, hrate

hours, hrate = computepay()

if hours > whours:
    try:
        upay = whours * hrate + ((hours - whours) * (hrate * 1.5))
    except:
        upay = -1
if hours <= whours:
    upay = hours * hrate
print(upay)
