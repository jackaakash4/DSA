
#self practice binary search

def binarySearch(arr, element):
    high = len(arr) - 1
    low = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid -1
    return None

print("The position of element is ", binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

