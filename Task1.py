#Task1
a = 6
b = 5
print (a, b)
c = input('Введите первое число: ')
d = input('Введите второе число: ')
s = input('Введите текст строки: ')
print(c, d, s, sep = '\n')

#Task2
sec = int(input('Введите количество секунд: '))
h = str(sec // 3600)
m = (sec // 60) % 60
s = sec % 60
if m < 10:
    m = '0' + str(m)
else:
    m = str(m)
if s < 10:
    s = '0' + str(s)
else:
    s = str(s)
print(h, m, s, sep = ':')

#Task3
n = int(input('Введите число: '))
str_n = str(n)
sums = n
sum_str = str(n)
for i in range(1, 3):
    sum_str = sum_str + str_n
    sums = sums + int(sum_str)
print(sums)

#Task4
a = int(input('Введите целое положительное число: '))
m = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print(m)

#Task5
revenue = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержек: '))
profit = revenue - costs
if profit > 0:
    print('фирма работает в прибыль')
    profitability = profit / revenue
    print('рентабельность выручки составляет: ', profitability)
    staff = int(input('Введите кол-во сотрудников: '))
    ppp = profit / staff
    print('прибыль в расчете на одного сотрудника составляет: ', ppp)
else:
    print('фирма работает в убыток')

#Task6
a = int(input('Введите а: '))
b = int(input('Введите b: '))
i = 0
while (a < b):
    a = 1.1 * a
    i += 1
print('Номер дня, на который общий результат спортсмена составит не менее', b, 'километров -', i)
