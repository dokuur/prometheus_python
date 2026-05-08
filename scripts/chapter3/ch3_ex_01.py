whours = int(40)

hours = float(input("Enter Hours: "))
hrate = float(input("Enter Hours Rate: "))

if hours > whours:
    try:
        upay = whours * hrate + ((hours - whours) * (hrate * 1.5))
    except:
        upay = -1
if hours <= whours:
    upay = hours * hrate
print(upay)
