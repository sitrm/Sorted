import os
import time
import timed_sorter1 as metod_sort

class Files:
    def __init__(self, filenames):
        self.filenames = filenames
        self.file_status = {}

    def check_files(self):#ок
        for filename in self.filenames:
            self.file_status[filename] = os.path.exists(filename)
        return self.file_status

class ReadHandle:
    def __init__(self, filename, delimiter=' '):
        self.filename = filename
        self.delimiter = delimiter
        self.file_handle = open(self.filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file_handle.readline()
        if line:
            return line.strip().split(self.delimiter)
        else:#если файл пустой то закрываем
            self.file_handle.close()
            raise StopIteration

    def read_numbers(self):
        with open(self.filename, 'r') as f:
            numbers = f.read().strip().split(self.delimiter)
            return [str(num) for num in numbers]

class FilesReader(Files):
    def __init__(self, filenames, delimiter=' '):
        super().__init__(filenames)
        self.delimiter = delimiter
        self.read_handles = {}

    def read(self):
        for filename in self.filenames:
            if filename not in self.file_status or not self.file_status[filename]:#если имя не совпадает с ключем(названием) и значение этого файла Fslse
                continue
            self.read_handles[filename] = ReadHandle(filename, self.delimiter)
        return self.read_handles

    def stop_reading(self, filenames: list):
        # if filenames is None:
        #     filenames = self.read_handles.keys()#все открытые файлы
        for filename in filenames:
            # if filename in self.read_handles:
            with open(filename, 'r') as f:
                f.close()
                # self.read_handles[filename].file_handle.close()
                # del self.read_handles[filename]



#деструктор

class WriteHandle:
    def __init__(self, filename, delimiter=' '):
        self.filename = filename
        self.delimiter = delimiter
        self.file_handle = open(self.filename, 'w')

    def write(self, data):
        with open(self.filename, 'w') as f:
            line = self.delimiter.join(str(x) for x in data)
            f.write(line)

    def close(self):
        self.file_handle.close()


class FilesWriter(Files):
    def __init__(self, filenames, delimiter=' '):
        super().__init__(filenames)
        self.delimiter = delimiter
        self.write_handles = {}

    def get_write_handle(self, filename):
        if filename not in self.write_handles:
            self.write_handles[filename] = WriteHandle(filename, self.delimiter)
        return self.write_handles[filename]
    #
    # def get_write_handle1(self):#ок
    #     for filename in self.filenames:
    #         self.write_handles[filename] = WriteHandle(filename, self.delimiter)
    #     return self.write_handles

    def write_sorted_files_bubble(self):
        obj_TimedSorter = metod_sort.TimedSorter()
        for filename in self.filenames:
            # if filename not in self.file_status or not self.file_status[filename]:#если нет то скипаем
            #     continue
            data = ReadHandle(filename).read_numbers()
            print(data)
            start_time = time.time()
            data_sort = obj_TimedSorter.bubble_sort(data)
            end_time = time.time()
            sorted_filename = filename.replace('.txt', '_sorted_{}_{}ms.txt'.format('bubble_sort', int(( start_time - end_time) * 1000)))
            WriteHandle(sorted_filename, ' ').write(data_sort)



if __name__ == '__main__':
    filenames = ['test1.txt', 'test2.txt', 'test3.txt']
    files_reader = FilesReader(filenames)
    files_writer = FilesWriter(filenames)

    file_status = files_reader.check_files()#ок
    print(file_status)
    #print(files_writer.get_write_handle('test1.txt'))#ок
    print(files_reader.read())#словарь файл - объект ReadHandle

    # write_handle = WriteHandle('testtest.txt', ';')#ок
    # write_handle.write([1,2,3,4])#ок


    read_handles = files_reader.read()#ок

    for filename, read_handle in read_handles.items():#по списоку пар (key, value)
        for line in read_handle:
            print(f"{filename}: {line}")

    files_writer.write_sorted_files_bubble()#ооооокккккк
    print(ReadHandle('file1.txt').__next__())

