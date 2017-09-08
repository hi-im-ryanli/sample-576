# Quick Sort
def printArray(arr):
    print ' '.join(str(i) for i in arr)

def quicksort(arr, i, j):
    if i < j:
        pos = partition(arr, i, j)
        quicksort(arr, i, pos - 1)
        quicksort(arr, pos + 1, j)

def partition(arr, i, j):
    pivot = arr[j]
    small = i - 1
    for k in range(i, j):
        if arr[k] <= pivot:
            small += 1
            swap(arr, k, small)

    swap(arr, j, small + 1)
    print "Pivot = " + str(arr[small + 1])
    printArray(arr)
    return small + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

arr = [9, 4, 8, 3, 1, 2, 5]
print "Initial Array :",
printArray(arr)
quicksort(arr, 0, len(arr) - 1)
