# only 5 lines!
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i-1
        while j >= 0 and arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1