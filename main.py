import argparse
from random import randint
import timed_sorter as sort


parser = argparse.ArgumentParser(epilog='Скрипт получает на вход список путей к файлам, содержащим массивы чисел.\
                                        Сортирует их и выводит в консоль отсортированный массивы и время выполнения\
                                        сортировки. Пути к файлам вводите через пробелы. Выбор метода через флаг -m',
                                 description='Сортировка')
parser.add_argument('list_files', nargs='+', help='список путей к файлам')
parser.add_argument('-m', '--metod', nargs=1, type=int, help='Выбор метода сортировки: 1 - Bubble_sort, 2 - insertion_sort,\
                                                               3 - quicksort')
args = parser.parse_args()

if __name__ == '__main__':
    numbers1 = [randint(-100, 100) for _ in range(25)]
    numbers_str1 = ' '.join(map(str, numbers1))
    with open('file1.txt', 'w') as file_write:
        # Записываем строку с числами в файл
        file_write.write(numbers_str1)

    numbers2 = [randint(-100, 100) for _ in range(25)]
    numbers_str2 = ' '.join(map(str, numbers2))
    with open('file2.txt', 'w') as file_write:
        # Записываем строку с числами в файл
        file_write.write(numbers_str2)

    numbers3 = [randint(-100, 100) for _ in range(25)]
    numbers_str3 = ' '.join(map(str, numbers3))
    with open('file3.txt', 'w') as file_write:
        # Записываем строку с числами в файл
        file_write.write(numbers_str3)

    obj_TimedSorted = sort.TimedSorter()

    if args.metod[0] == 1:
        print(f'//BUBBLE SORTING//')
    if args.metod[0] == 2:
        print(f'//SORTING BY INSERT//')
    if args.metod[0] == 3:
        print(f'//QUICK SORTING//')

    # Чтение каждого файла и добавление его содержимого в список arr. затем применяем методы сортировок
    for file_path in args.list_files:
        if args.metod[0] == 1:
            with open(file_path) as file_read1:
                arr_temp = file_read1.read().split()
                if any(c.isalpha() for c in arr_temp):
                    raise TypeError(f'Массив в файле {file_path} введен некорректно. Должны быть введены тольок числа!')
                # переобразовали элементы массива в числа, так как методы сортируют именно списки c числами, а не строками
                arr = list(map(float, arr_temp))

                arr_sort_bubble = obj_TimedSorted.bubble_sort_time(arr)
                print(f'Сортировка файла {file_path}. Отсортированный массив:  {arr_sort_bubble}')
                print()
        if args.metod[0] == 2:
            with open(file_path) as file_read2:
                arr_temp = file_read2.read().split()
                if any(c.isalpha() for c in arr_temp):
                    raise TypeError(f'Массив в файле {file_path} введен некорректно. Должны быть введены тольок числа!')

                arr = list(map(float, arr_temp))
                arr_sort_insert = obj_TimedSorted.insertion_sort_time(arr)
                print(f'Сортировка файла {file_path}. Отсортированный массив:  {arr_sort_insert}')
                print()
        if args.metod[0] == 3:
            with open(file_path) as file_read3:
                arr_temp = file_read3.read().split()
                if any(c.isalpha() for c in arr_temp):
                    raise TypeError(f'Массив в файле {file_path} введен некорректно. Должны быть введены тольок числа!')

                arr = list(map(float, arr_temp))
                arr_sort_insert = obj_TimedSorted.quicksort_time(arr)
                print(f'Сортировка файла {file_path}. Отсортированный массив: {arr_sort_insert}')
                print()
