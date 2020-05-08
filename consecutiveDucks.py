def consec(n):
    sum = 0
    start = 1
    end = n
    found = False
    while found == False:
        if start == n:
            break
        for number in range(start, end):
            printf('start: {0}', start)
            found = False
            sum += number
            if sum > n:
                print(sum)
                break
            elif sum == n:
                found = True
        if found == True:
            print(start, number)
        else:
            start += 1
            sum = 0
            print(start)


print(consec(42))
