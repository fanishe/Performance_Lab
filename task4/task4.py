import sys

var = sys.argv[1:]
work_day_start = 8
work_day_end = 20


def make_list(file):
    """ Принимает файл с данными и возвращает словарь"""
    persons = {}
    num = 1
    with open(file, 'r',  encoding = 'utf-8') as f:
        for line in f:
            line = line.split(' ')
            line = [ l.rstrip() for l in line ]
            # rstrip() удаляет символ "\n" от данных
            p = {f'p{num}' : line}
            num += 1
            persons.update(p)

    return persons

# {'p1': ['8:00', '8:30'], 
# 'p2': ['8:15', '8:45'], 
# 'p3': ['8:45', '9:00'], 
# 'p4': ['8:30', '9:00'], 
# 'p5': ['9:00', '9:30'], 
# 'p6': ['9:10', '9:20']}

def search_max(persons):
    """Принимает словарь
        Формирует рабочий день с 9 до 20
        минуты просматривает через каждые 5 минут
        после формирования времени просматривает входы и выходы посетителей
    """
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
                if time == persons[p][0]:
                    # Если время соответствует времени входа
                        # Увеличиваю счетчик посетителей
                    counter += 1
                    visitors[time] = counter 
                    
            for p in persons:
                if time == persons[p][1]:
                    # Если соответствует времени выхода
                        # Кол-во посетителей уменьшается на одного
                    counter -= 1
                    

    maximum = max(visitors.values())
    # Нахожу максимальное Кол-во посетителей
    new_list = []
    for vis in visitors:
        if visitors[vis] == maximum:
            new_list.append(vis)
        # Создаю список с "горячим временем"
    return f'{new_list[0]} {new_list[-1]}'
    # возвращаю начало и конец списка



def main():
    persons = make_list(var[0])
    result = search_max(persons)
    print(result)
    # несколько диапазонов найти не получилось
    # из-за нехватки опыта, надеюсь, что все решил верно

if __name__ == '__main__':
    main()