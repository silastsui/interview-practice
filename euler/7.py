from math import sqrt


def find_nth_prime(n):
    count = 1
    num = 1
    while count < n:
        num += 2
        if is_prime(num):
            count += 1
    return num

def is_prime(n):
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    for x in range(5, int(sqrt(n))+1, 6):
        if n % x == 0:
            return False
        elif n % (x+2) == 0:
            return False
    return True

print(find_nth_prime(6))
print(find_nth_prime(10001))
