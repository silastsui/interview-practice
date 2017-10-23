
def find_sum_of_even_fib(num):
    fib_prev = 1
    fib = 2
    total = 0

    while fib < num:
        if fib % 2 == 0:
            total += fib

        temp = fib
        fib += fib_prev
        fib_prev = temp

    return total

def find_sum_of_even_fib_recursive(num):
    n = 3
    while n < num:
        n = fib(n-2) + fib(n-1)

    return 4*n-3 + n-6

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
