def quicksort(_list, start, end): # лгоритм быстрой сортировки
    if end - start > 1:
        p = partition(_list, start, end)
        quicksort(_list, start, p)
        quicksort(_list, p + 1, end)


def partition(_list, start, end):
    pivot = _list[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and _list[i] <= pivot):
            i = i + 1
        while (i <= j and _list[j] >= pivot):
            j = j - 1

        if i <= j:
            _list[i], _list[j] = _list[j], _list[i]
        else:
            _list[start], _list[j] = _list[j], _list[start]
            return j


def ship_distance(_list): # вывод
    return f'Корабль: {_list[0]} последний раз был на связи по координатам: {_list[-1]}; и двигался в направлении: {_list[3]}.'


qq=[]
distance = []
with open('C:/Users/Kids01/Desktop/Нуруллин Тимур Булатович  1537/Вариант 9/space.csv', encoding='utf8') as f: # чтение файла и выполнение алгоритма
    name = f.readline()
    a = f.readlines()
for i in range(len(a)):
    a[i] = a[i][:-1]
    a[i] = a[i].split(',')
    a[i].append(a[i][2])
    a[i][2] = a[i][2].split()
    distance.append((int(a[i][2][0])**2 + int(a[i][2][1])**2)**0.5)
    a[i][2] = (int(a[i][2][0])**2 + int(a[i][2][1])**2)**0.5


quicksort(distance,0,len(distance))
for i in range(len(distance)): # применение быстрой сортировки к списку
    x=0
    while distance[i] not in a[x]:
        x+=1
    qq.append(a[x])

qq=qq[8:]
print(ship_distance(qq))
