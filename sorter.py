import random


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

    def quicksort(self, list):
        if len(list) <= 1:
            return list
        else:
            q = random.choice(list)
            s_nums = []
            m_nums = []
            e_nums = []
            for n in list:
                if n < q:
                    s_nums.append(n)
                elif n > q:
                    m_nums.append(n)
                else:
                    e_nums.append(n)
            return self.quicksort(s_nums) + e_nums + self.quicksort(m_nums)


if __name__ == '__main__':
    list_1 = random.sample(range(1, 50), 20)
    obj1 = Sorter()
    print("The unsorted list is: ", list_1)
    print("The sorted list is(bubble_sort): ", obj1.bubble_sort(list_1))

    random.shuffle(list_1)
    print("The unsorted list is: ", list_1)
    print("The sorted list is(insertion_sort): ", obj1.insertion_sort(list_1))

    random.shuffle(list_1)
    print("The unsorted list is: ", list_1)
    print("The sorted list is(quicksort): ", obj1.quicksort(list_1))
