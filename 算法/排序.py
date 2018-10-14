list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element = 7


# 查找算法：
# 顺序查找
def ord_sear(list, element):
    for i in range(0, len(list)):
        if list[i] == element:
            print('list[{0}]={1}'.format(i, element))
            return i
    else:
        print('not found')


# 二分查找
def middle(list, element):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = (low + high) // 2
        if element == list[mid]:
            return mid
        elif element > list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


list1 = [3, 1, 5, 7, 8, 6, 2, 0, 4, 9]


# 排序算法：
# 冒泡排序：
def bubble(list):
    high = len(list) - 1
    while high > 0:
        for i in range(0, high):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        high -= 1
    return list


# 选择排序
def choice(list):
    for i in range(0, len(list)):
        min_loc = i
        for j in range(i + 1, len(list)):
            if list[min_loc] > list[j]:
                min_loc = j
        list[min_loc], list[i] = list[i], list[min_loc]
    return list


# 插入排序
def cut(list):
    for i in range(1, len(list)):
        temp = list[i]
        for j in range(i - 1, -1, -1):
            if list[j] > temp:
                list[j + 1] = list[j]
                list[j] = temp
    return list


# 快速排序
def QuickSort(arr, firstIndex, lastIndex):
    if firstIndex < lastIndex:
        divIndex = Partition(arr, firstIndex, lastIndex)

        QuickSort(arr, firstIndex, divIndex)
        QuickSort(arr, divIndex + 1, lastIndex)
    else:
        return
def Partition(arr, firstIndex, lastIndex):
    i = firstIndex - 1
    for j in range(firstIndex, lastIndex):
        if arr[j] <= arr[lastIndex]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[lastIndex] = arr[lastIndex], arr[i + 1]
    return i
QuickSort(list1, 0, len(list1) - 1)
print(list1)
