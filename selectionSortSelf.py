#self implementation of selection sort

def findSmallest(arr):
    #assume first element as smallest
    smallest = arr[0]
    smallest_index = 0

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#selection sort

def selectionsort(arr):
    copiedArr = list(arr)
    newArr = []
    for i in range(len(copiedArr)):
        small = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(small))

    return newArr

print("After applying selection sort: ", selectionsort([3,1,2,6,4]))

