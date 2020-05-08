def move_zeros(string):
    print(string)
    for item in string:
        if item == 0:
            string.remove(item)
            string.append(item)
    print(string)
    return string

def test_move_zeros_1():
    assert move_zeros([0,1,2,0,3,4,8]) == [1,2,3,4,8,0,0]

def test_move_zeros_2():
    assert move_zeros([false,1,0,1,2,0,1,3,"a"]) == [false,1,1,2,1,3,"a",0,0]