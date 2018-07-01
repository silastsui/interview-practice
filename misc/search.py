def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1

        while key < array[j] and j >= 0:
            array[j+1] = array[j]
            j = j-1
        
        array[j+1] = key
    
    return array

def heapify(array, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and array[l] > array[largest]:
        largest = l
    
    if r < n and array[r] > array[largest]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def heap_sort(array):
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, len(array), i)

    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)

    return array

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array)/2
    a = merge_sort(array[:mid])
    b = merge_sort(array[mid:])

    a_idx, b_idx = 0, 0
    array = []
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            array.append(a[a_idx])
            a_idx += 1
        else:
            array.append(b[b_idx])
            b_idx += 1

    array += a[a_idx:]
    array += b[b_idx:]

    return array

def quick_sort(array):
    if len(array) < 1:
        return array

    pivot_idx = len(array)/2
    pivot = array[pivot_idx]

    l_idx = 0
    r_idx = len(array)-1

    while l_idx < r_idx:
        while array[l_idx] < pivot:
            l_idx += 1
        while array[r_idx] > pivot:
            r_idx -= 1

        array[l_idx], array[r_idx] = array[r_idx], array[l_idx]

    return quick_sort(array[:r_idx]) + [pivot] + quick_sort(array[l_idx+1:])
