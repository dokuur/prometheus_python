fname = input("Enter file name: ")
fr = open(fname)
frn = list()
count = 0

for line in fr:
    if not line.startswith("From "):
        continue
    count += 1
    sline = line.rstrip()
    frn = sline.split(' ')
    print(frn[1])

print("There were", count, "lines in the file with From as the first word")
