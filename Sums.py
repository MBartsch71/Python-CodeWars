def get_sum(a,b):
    sum = 0
    ordered_list = list((a,b))
    ordered_list.sort()
    i = ordered_list[0]
    while i <= ordered_list[1]:
        sum += i
        i+=1
    return sum

def test_get_sum_1():
    assert get_sum(0,1) == 1

def test_get_sum_2():
    assert get_sum(0,-1) == -1

def test_get_sum_3():
    assert get_sum(1,2) == 3
