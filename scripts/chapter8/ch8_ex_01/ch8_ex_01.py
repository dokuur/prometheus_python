fname = input("Enter file name: ")
fh = open(fname).read().split()
lst = list()
for line in fh:
    if line not in lst:
        lst.append(line)
    else:
        continue
    lst.sort()
print(lst)
