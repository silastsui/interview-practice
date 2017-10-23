from math import sqrt


def find_highest_prime(num):
    is_prime = True
    prime = num
    if num % 2 == 0:
        return find_highest_prime(num/2)
    for x in range(int(sqrt(num)) + 1, 2, -1):
        if num % x == 0:
            prime = x
            is_prime = False

    if is_prime:
        return num
    return find_highest_prime(num/prime)

print(find_highest_prime(600851475143))
