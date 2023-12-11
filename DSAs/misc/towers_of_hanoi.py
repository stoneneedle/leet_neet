def toh(n):
    return 1 if n ==1 else  2*toh(n-1) + 1
print(toh(10))