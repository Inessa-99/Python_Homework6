'''Задача 30: Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''

def arith_progress (first_element: int, difference_num: int, count_elements: int):
    lst1 = []
    for i in range(count_elements):
        element = first_element + i * difference_num
        lst1.append(element)
    lst1 = ' '.join(map(str, lst1))
    return lst1
#
first_element = int(input('Введите первый элемент: '))
difference_num = int(input('Введите разность: '))
count_elements = int(input('Введите количество элементов: '))

print(arith_progress(first_element, difference_num, count_elements))


