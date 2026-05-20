name = input("Enter file:")
# name = 'mbox-short.txt'

fr = open(name)
frn = list()
ml = list()

for line in fr:
    if not line.startswith("From "):
        continue
    sline = line.rstrip()
    frn = sline.split(' ')
    ml.append(frn[1])

    mail = dict()
    for emails in ml:
        mail[emails] = mail.get(emails, 0) +1

bigcount = None
bigword = None
for word,count in mail.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
