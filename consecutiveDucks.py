def consec(n):
    while n % 2 == 0 and n > 1:
        n //= 2
    if n > 1:
        return True
    elif n == 1:
        return False


print(consec(382131))
