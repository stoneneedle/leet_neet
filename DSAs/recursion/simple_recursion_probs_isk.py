# sum nums recursively
def sum_recursive(nums):
    if not nums:
        return 0

    # return nums[0] + sum_recursive(nums[1:])
    return nums[len(nums)-1] + sum_recursive(nums[:len(nums)-1])

print(sum_recursive([1,2,3]))




# check if str is palindrome - abba returns True; abab False


def palindrome_recursive(str):
    if not str or len(str) == 1:
        return True

    if str[0] == str[len(str)-1]:
        return palindrome_recursive(str[1:len(str)-1])
    return False

print(palindrome_recursive("bba"))



# Reverse a string
# abcd - dcba

def reverse(str):
    if not str or len(str) == 1:
        return str

    return str[len(str)-1] + reverse(str[1:len(str)-1]) + str[0]

print(reverse('abcd'))

# calculate power of a number
# 2^3 = 8
# 2,3
# identify the base case

def power(num, p):
    if p == 0:
        return 1
    if p == 1:
        return num

    return num * power(num, p-1)

print(power(2,3))