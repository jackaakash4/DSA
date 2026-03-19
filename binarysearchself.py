
#self practice binary search

def binarySearch(arr, element):
    low = arr[0]
    high = arr[len(arr) - 1]
    guess = element

    while low <= high:
        mid = (low + high) // 2

        if guess == arr[mid]:
            return mid
        elif guess < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


print("The position of element is ", binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

