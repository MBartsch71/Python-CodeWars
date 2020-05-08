def fib_3(signature,n):
    if n < 3:
        return signature
    else:
        signature.append(signature[-3] + signature[-2] + signature[-1])
        n -= 1
        return fib_3(signature,n)

print(fib_3([1,1,1],10))