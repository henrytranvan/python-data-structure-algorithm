def buble_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp


my_array = [4,8,2,3,9]
buble_sort(my_array)
print(my_array)


def select_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                min_index = j
        if min_index > i:
            tmp = array[i]
            array[i] = array[min_index]
            array[min_index] = tmp


my_array = [6,3,8,5,1,9]
buble_sort(my_array)
print(my_array)


def insert_sort(array):
    for i in range(1, len(array)):
        tmp = array[i]
        j = i - 1
        while tmp < array[j] and j > -1:
            array[j + 1] = array[j]
            array[j] = tmp
            j -= 1


my_array = [7,3,4,5,1,9]
insert_sort(my_array)
print(my_array)


def merger_sorted_list(arr1, arr2):
    results = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            results.append(arr1[i])
            i += 1
        else:
            results.append(arr2[j])
            j += 1
    if i < len(arr1):
        for ind in range(i, len(arr1)):
            results.append(arr1[ind])

    if j < len(arr2):
        for ind in range(j, len(arr2)):
            results.append(arr2[ind])

    return results


arr1 = [3,4,5]
arr2 = [2,6,8]
arr3 = merger_sorted_list(arr1, arr2)
print(arr3)


def merger_sort(array):
    if len(array) == 1:
        return array
    mid_index = int(len(array)/2)
    left_list = merger_sort(array[:mid_index])
    right_list = merger_sort(array[mid_index:])
    return merger_sorted_list(left_list, right_list)


my_array = [10,39,40,50,14,90]
insert_sort(my_array)
print(my_array)
