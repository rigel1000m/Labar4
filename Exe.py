import random

from exer.List import LinkedList

listik =LinkedList()
negativeList = LinkedList()
positiveList = LinkedList()
#Добавление элементов в список listik
for i in range(10):
    listik.append(random.randint(-10,10))
#Проход по списку listik
for val in listik.iterate():
    #Проверка на положительное число
    if(val> 0):
    #Добавление в положительный список
        positiveList.append(val)
    #Проверка на отрицательное число
    elif(val<0):
    #Добавление в отрицательный список
        negativeList.append(val)
    #Если значение будет 0, то пропускаем его
    else:
        continue
print('Отрицательные числа:')
for i in negativeList.iterate():
    print(i)
print('Положительные числа:')
for i in positiveList.iterate():
    print(i)