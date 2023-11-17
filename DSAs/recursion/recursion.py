from functools import wraps, cache
from time import time

### Timing function
def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap


### Factorial

# factorial (recursive): Time O(n) Memory O(n)
@timing
@cache
def factorial_rec(n):
    if n == 1 or n == 0 or isinstance(n, str):
        return 1
    elif isinstance(n, float):
        return 1
    elif n > 1 and isinstance(n, int):
        return n * factorial_rec(n-1)
    elif n < 0 and isinstance(n, int):
        return -abs(n * factorial_rec(n+1))

# factorial (iterative) - more efficient, memory O(1), closer to how Python implements factorial
@timing
def factorial_it(n):
    total = 1
    for i in range(2, n+1):
        total *= i
    return total

# print(factorial_rec(10))
# print(factorial_it(10))

# import math

# Python factorial
# print(math.factorial(5))

# Python gamma
# print(math.gamma(1.01))

### Fibonacci - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# Fibonacci sequence, where l is length of the sequence, and n is the current number in sequence
@timing
@cache
def fib_rec(l):
    seq = []
    def fib_num(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n > 1:
            return fib_num(n - 1) + fib_num(n - 2)

    for i in range(0, l):
        seq.append(fib_num(i))
    return seq

# Iterative Fibonacci solution
@timing
def fib_it(l):
    seq = []
    def fib_num(n):
        prev_num, prev_num2, cur_num = 1, 0, 0
        for i in range(n):
            cur_num = prev_num
            prev_num = prev_num + prev_num2
            prev_num2 = cur_num
        return cur_num

    for i in range(0, l):
        seq.append(fib_num(i))
    return seq




print(fib_rec(30))
print(fib_it(30))
