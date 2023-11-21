# low = 1, high = 100

# Binary search on some range of values
def binary_search(low, high, guess):

    while low <= high:
        mid = (low + high) // 2

        if is_correct(mid, guess) > 0:
            high = mid - 1
        elif is_correct(mid, guess) < 0:
            low = mid + 1
        else:
            return mid
    return -1

# Return 1 if n is too big, -1 if too small, 0 if correct
def is_correct(n, g):
    if n > g:
        return 1
    elif n < g:
        return -1
    else:
        return 0

print(binary_search(1, 100, 10))
