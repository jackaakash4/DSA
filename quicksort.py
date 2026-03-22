#quick sort is done using D&C algorithm

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        less = [i for i in arr[1:] if i <= pivot]

        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print("Sorted array using quick sort is ", quicksort([4, 3, 5, 6, 8, 0]))

