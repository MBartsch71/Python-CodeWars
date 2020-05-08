def find_outlier(integers):
    odds = []
    evens = []
    for number in integers:
        if number % 2:
            evens.append(number)
        else:
            odds.append(number)
    print(odds)
    print(evens)
    if len(odds) == 1:
        return odds[0]
    elif len(evens) == 1:
        return evens[0]

def test_outliers_1():
    assert find_outlier([2,4,6,8,10,3]) == 3

def test_outliers_2():
    assert find_outlier([2,4,0,100,4,11,2602,36]) == 11

def test_outliers_3():
    assert find_outlier([160,3,1719,19,11,13,-21]) == 160