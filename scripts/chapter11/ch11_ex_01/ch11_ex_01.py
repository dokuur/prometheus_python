# Імпортуємо модуль RE (Regular Expresion) для роботи з текстом та файлами
import re

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'regex_sum_42.txt'

ofn = open(fname).read()

# Читаємо файл порядково, знаходимо цифри, та додаємо результат пошуку до списку
for number in ofn:
    numbers = re.findall('[0-9]+',ofn)

# Використовуємо самий простий, "класичний", метод обчислення суми всих чисел в
# списку
snumb = 0
for numb in numbers:
    snumb = snumb + int(numb)
print('Sum calculated with classic method: ', snumb)

# Для обчислення кінцевої суми використовуємо метод sum. В результаті ми беремо
# змінну numb2 та перетворюємо її тип з str в int, бо неможно додавати str
# та int
print(f'Sum with method sum: {sum(int(numb2) for numb2 in numbers)}')
