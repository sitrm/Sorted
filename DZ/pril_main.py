import time
import main_dz
import timed_sorter1 as metod_sort
import argparse
from random import randint

obj_TimedSorter = metod_sort.TimedSorter()
def sort_bubble():
    algorithm = 'Bubble_sort'
    for filename in args.list_files:
        data = main_dz.ReadHandle(filename, args.delimiter[0]).read_numbers()
        start_time = time.time()
        data_sort = obj_TimedSorter.bubble_sort(data)
        end_time = time.time()
        sorted_filename = filename.replace('.txt',
                                           '_sorted_{}_{}ms.txt'.format(algorithm, int((end_time - start_time) * 1000)))
        main_dz.WriteHandle(sorted_filename, args.delimiter[0]).write(data_sort)


def sort_insert():
    algorithm = 'Insert_sort'
    for filename in args.list_files:
        data = main_dz.ReadHandle(filename, args.delimiter[0]).read_numbers()
        start_time = time.time()
        data_sort = obj_TimedSorter.insertion_sort(data)
        end_time = time.time()
        sorted_filename = filename.replace('.txt',
                                           '_sorted_{}_{}ms.txt'.format(algorithm, int((end_time - start_time) * 1000)))
        main_dz.WriteHandle(sorted_filename, args.delimiter[0]).write(data_sort)


def quick_sort():
    algorithm = 'QuickSort'
    for filename in args.list_files:
        data = main_dz.ReadHandle(filename, args.delimiter[0]).read_numbers()
        start_time = time.time()
        data_sort = obj_TimedSorter.quicksort(data)
        end_time = time.time()
        sorted_filename = filename.replace('.txt',
                                           '_sorted_{}_{}ms.txt'.format(algorithm, int((end_time - start_time) * 1000)))
        main_dz.WriteHandle(sorted_filename, args.delimiter[0]).write(data_sort)


parser = argparse.ArgumentParser(epilog='Данный скрипт получает на вход список файлов, сортирует данные каждого файла\
                                        и записывает их  новые файлы с добавлением к навзанию файла- \
                                        _sorted_<алгоритм сортировки>_<время сортировки в мс>.\
                                        Также пользователь может выбрать один из трех алгоритмов и любой разделитель для чтения/записи файла'\
                                 , description='Сортировка данных из списка файлов в новые файлы с возможность выбора разделителя чтения/записи файлов')
parser.add_argument('list_files', nargs='+', help='Список путей к файлам')
parser.add_argument("-a", "--algoritm", nargs=1, type=int, help='Выбор метода сортировки: 1 - Bubble_sort, 2 - insertion_sort,\
                                                               3 - quicksort')
parser.add_argument('-d', '--delimiter', nargs=1, type=str, help='Разделитель, для чтения/записи файла. Например, ";", " ", ", "')
args = parser.parse_args()


if __name__ == '__main__':

    obj_write1 = main_dz.WriteHandle('test1.txt', args.delimiter[0])
    obj_write2 = main_dz.WriteHandle('test2.txt', args.delimiter[0])
    obj_write3 = main_dz.WriteHandle('test3.txt', args.delimiter[0])

    numbers1 = [randint(-100, 100) for _ in range(1000)]
    obj_write1.write(numbers1)
    numbers2 = [randint(-100, 100) for _ in range(1000)]
    obj_write2.write(numbers2)
    numbers3 = [randint(-100, 100) for _ in range(1000)]
    obj_write3.write(numbers3)

    if args.algoritm[0] == 1:
        sort_bubble()
    if args.algoritm[0] == 2:
        sort_insert()
    if args.algoritm[0] == 3:
        quick_sort()









