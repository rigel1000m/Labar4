import random

from exer.List import LinkedList

listik = LinkedList()
sum = 0
for i in range(53):
    listik.append(random.randint(1,10))
print('Размер = ',listik.getSize())
for i in listik.iterate():
    sum = i+sum
print('Сумма = ', sum)