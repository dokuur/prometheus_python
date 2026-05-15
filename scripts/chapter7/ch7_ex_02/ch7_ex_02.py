fname = input("Enter file name: ")
fh = open(fname)
count = 0
s = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    fnd = line.find(':')
    sf = float(line[fnd+1::].strip())
    s = s + sf

print(f'Average spam confidence:', s/count)
