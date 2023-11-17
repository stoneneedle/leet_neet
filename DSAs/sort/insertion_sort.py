# test_list = [8, 3, 5, 4, 2]
#
#
# def insertionSort(s_list):
#     for i in range(len(s_list)):
#         next = i + 1 if i < len(s_list)-1 else i
#         #print(next)
#         s_list[i], s_list[next] = s_list[next], s_list[i]


# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# print(arr)
# for i in range(len(arr)):
#     print("% d" % arr[i])

nums = [12, 11, 13, 5, 6]

for i in range(1, len(nums)):
    k = nums[i]
    #print(k)
    j = i - 1  # pointer to next elem
    while j >= 0 and k < nums[j]:
        nums[j + 1] = nums[j]
        # print(j)
        j -= 1
    nums[j + 1] = k

print(nums)



