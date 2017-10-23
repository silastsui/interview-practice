def find_sum_of_multiples(num):
    return sum([x for x in range(num) if x%3 == 0 or x%5 == 0])

print(find_sum_of_multiples(1000))
