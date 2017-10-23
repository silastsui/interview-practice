def find_smallest_multiple(num):
    product = 1
    factors = []
    for x in range(1, num+1):
        x_factors = prime(x)
        temp = product
        for y in x_factors:
            if temp % y == 0:
                temp //= y
            else:
                product *= y

    return product

def prime(n):
    factors = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

print(find_smallest_multiple(20))
