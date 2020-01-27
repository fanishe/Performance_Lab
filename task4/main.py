"""
В течении дня  в  банк заходят  люди,  для каждого  посещения  фиксируется время  захода в банк и время  выхода. 

Банк работает с 8:00  до 20:00. 
Написать программу, которая определяет периоды  времени, когда  в  банке  было максимальное количество посетителей. 

Файл содержит  информацию о времени  посещения  банка  каждым посетителем, округленном  до минут. 
Время  входа  посетителя  меньше  либо равно времени  выхода . 
Выведите интервалы времени, когда  в  банке  было  максимальное число посетителей. Начало и конец интервала разделяются  пробелом. 
В случае  необходимости  вывести  несколько периодов, в  качестве  разделителя между  ними  следует использовать символ перевода строки. 

Пример 
Входные  данные: 
8:00 8:30 
8:15 8:45 
8:45 9:00 
8:30 9:00 
9:00 9:30 
9:10 9:20 

Вывод: 
8:15 9:00 
9:10 9:20
"""
work_day_start = 8
work_day_end = 20


def make_list(file):
    persons = {}
    num = 1
    with open(file, 'r',  encoding = 'utf-8') as f:
        for line in f:
            line = line.split(' ')
            line = [ l.rstrip() for l in line ]
            p = {f'p{num}' : line}
            num += 1
            persons.update(p)

    return persons

persons = make_list('input.txt')
#for p in persons:
#    print(p, ' - ', persons[p])

def search_max(persons):
    counter = 0
    visitors = {}
    for h in range(work_day_start, work_day_end):
        for m in range(0, 55, 5):
            if m == 0:
                m = '00'
            elif m == 5:
                m = '05'

            time = f'{h}:{m}'
            for p in persons:
                #print(p)
                if time == persons[p][0]:
                    counter += 1
                    visitors[time] = counter 
                    #visitors.append(time)
                    #visitors.append(counter)
                    print(f'{time} +1')
            for p in persons:
                if time == persons[p][1]:
                    counter -= 1
                    print(f'{time} -1')

    maximum = max(visitors.values())
    new_list = []
    for vis in visitors:
        if visitors[vis] == maximum:
            new_list.append(vis)
    return f'{new_list[0]} {new_list[-1]}'


