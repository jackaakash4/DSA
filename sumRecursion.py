#using recursion to add the sum of elements of list

def sum1(list1):
    #Base case
    if not list1:
        return 0

    if len(list1) == 1:
        return list1[1]

    #Divide
    mid = len(list1) // 2

    #Conquer
    left_sum = sum1(list1[ :mid])
    right_sum = sum1(list1[mid: ])

    return left_sum + right_sum

list11 = [3, 4, 5, 1, 2, 9]
print(f"The sum of list {list11} is {sum(list11)}")


