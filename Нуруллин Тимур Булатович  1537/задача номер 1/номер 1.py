def error(_list):# функция находит ошибку
    if _list[2] == '0 0':
        return [_list[0], len(_list[1]), _list[-1].split()]


def make_report(_list):#функция составляет отчёт по примеру
    return f'При получении данных о корабле {_list[0]} возникли сбои. Предположительные координаты - {_list[1]-int(_list[2][0])}, {_list[1]-int(_list[2][1])}\n'


errors = []# десь будут храниться все найденные ошибки
with open('C:/Users/Kids01/Desktop/Нуруллин Тимур Булатович  1537/Вариант 9/space.csv', encoding='utf8') as f:#открытие и чтение файла
    name = f.readline()
    q = f.readlines()
for i in range(len(q)):
    q[i] = q[i][:-1]
    q[i] = q[i].split(',')
    a = error(q[i])
    if a is not None:
        errors.append(a)# добавляем в ошибки после выполнения алгоритма

with open('space new.txt', 'w', encoding='utf8') as f:# создание файла 
    for i in range(len(errors)):
        f.write(make_report(errors[i]))
