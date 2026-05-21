#Напишіть програму, яка прочитає файл mbox-short.txt і визначить розподіл по
#годинах доби для кожного з повідомлень. Ви можете витягнути годину з рядка
# 'From ', знайшовши час і розділивши рядок вдруге двокрапкою.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
#Після того, як ви накопичили кількість повідомлень для кожної години, виведіть
# їх, відсортовані за годинами, як показано нижче (у бажаному результаті).

fname = input("Enter file name: ")
# Якщо довжина імені файлу менше 1, то ім'я файлу буде mbox-short.txt
if len(fname) < 1:
    fname = 'mbox-short.txt'


lst = list()
dt = list()
dth = list()
hours = list()
# Відкриваємо файл
handle = open(fname)
dh = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    lst = line.rstrip().split(' ')
    dt.append(lst[6])
    for i in dt:
        dth = i.rstrip().split(':')
    # Додаємо години до списку
    hours.append(dth[0])

# Рахуємо кількість потраплянь годин у списку
for hour in hours:
    dh[hour] = dh.get(hour, 0) + 1

# Виводимо години та кількість їх потраплянь в порядку зростання
count = None
dhours = None
for (k, v) in sorted(dh.items()):
    if count is None or v > count:
        dhours = k
        count = v
    print(k, v)
