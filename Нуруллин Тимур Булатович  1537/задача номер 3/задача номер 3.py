def message_send(_list):
    return f'Корабль {_list[0]} последний раз был на связи по координатам: {_list[2][0]} {_list[2][1]}, что составляет: {round(_list[-1],3)} космических единиц.'


best = []
with open('C:/Users/Kids01/Desktop/Нуруллин Тимур Булатович  1537/Вариант 9/space.csv', encoding='utf8') as f:
    name = f.readline()
    a = f.readlines()
for i in range(len(a)):
    a[i] = a[i][:-1]
    a[i] = a[i].split(',')
    a[i].append(a[i][2])
    a[i][2] = a[i][2].split()
    best.append(a[i][0])
    a[i].append((int(a[i][2][0])**2 + int(a[i][2][1])**2)**0.5)
message = input()
while message != 'stop':
    if message == ['0','0'] or message not in best:
        print('error.. er.. ror..')
        message = input()
    else:
        ind = best.index(message)
        print(message_send(a[ind]))
        message = input()

