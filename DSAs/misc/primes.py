def is_prime(x):
    return all(x % i for i in range(2, x))

# def next_prime(x):
#     return min([a for a in range(x+1, 2*x) if is_prime(a)])

def next_prime(x):
    return min([a for a in range(x + 1, 2 * x) if all(a % i for i in range(2, a))])