import random
import timeit


class Sorter:

    def bubble_sort(self, list):
        # Мы можем остановить итерацию, как только обмен будет выполнен
        has_swapped = True
        # Мы можем предотвратить ненужную оценку, используя логический флаг и проверяя,
        # были ли сделаны какие-либо свопы в предыдущем разделе.
        while (has_swapped):
            has_swapped = False
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    # Swap
                    list[i], list[i + 1] = list[i + 1], list[i]
                    has_swapped = True
        return list

    def insertion_sort(self, list):
        for i in range(1, len(list)):
            temp = list[i]
            j = i - 1
            while j >= 0 and temp < list[j]:
                list[j + 1] = list[j]
                j = j - 1
            list[j + 1] = temp
        return list

    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            q = random.choice(nums)
            s_nums = []
            m_nums = []
            e_nums = []
            for n in nums:
                if n < q:
                    s_nums.append(n)
                elif n > q:
                    m_nums.append(n)
                else:
                    e_nums.append(n)
            return self.quicksort(s_nums) + e_nums + self.quicksort(m_nums)


class TimedSorter(Sorter):
    def timed(func):
        def wrapper(*args, **kwargs):
            start_time = timeit.default_timer()
            result = func(*args, **kwargs)
            end_time = timeit.default_timer()
            print(f"Время выполнения сортировки методом {func.__name__}: {end_time - start_time:.7f}")
            return result

        return wrapper

    @timed
    def bubble_sort_time(self, list):
        obj = TimedSorter()
        return obj.bubble_sort(list)

    @timed
    def insertion_sort_time(self, list):
        obj = TimedSorter()
        return obj.insertion_sort(list)

    @timed
    def quicksort_time(self, list):
        obj = TimedSorter()
        return obj.quicksort(list)


if __name__ == '__main__':
    list_1 = random.sample(range(-100, 100), 30)
    obj1 = TimedSorter()
    print("Неотсортированный массив: ", list_1)
    print("Отсортированный массив(bubble_sort): ", obj1.bubble_sort_time(list_1))

    random.shuffle(list_1)
    print("Неотсортированный массив: ", list_1)
    print("Отсортированный массив(insertion_sort): ", obj1.insertion_sort_time(list_1))

    random.shuffle(list_1)
    print("Неотсортированный массив: ", list_1)
    print("Отсортированный массив(quicksort): ", obj1.quicksort_time(list_1))
