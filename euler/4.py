def find_largest_palindrome():
    for x in range(999, 899, -1):
        for y in range(999, 899, -1):
            if isPal(x*y):
                return x*y


def isPal(num):
    num = str(num)
    if len(num) <= 1:
        return True
    if num[0] != num[-1]:
        return False
    return isPal(num[1:len(num)-1])

print(find_largest_palindrome())
