def firstDigit(n):
    n = abs(n)
    if n == 0:
        return 0
    while n >= 10:
        n //= 10
    return n