def dirReduc(arr):
    combo_found = False
    dir_combos = { 'one': ("NORTH", "SOUTH"),
                   'two': ("SOUTH", "NORTH"),
                   'three': ("EAST", "WEST"),
                   'four': ("WEST", "EAST"), }
    for item in dir_combos:
        for i in range(len(arr)-1):
            if arr[i] != '' and arr[i] == dir_combos[item][0] and arr[i+1] and arr[i+1] == dir_combos[item][1]:
                    arr[i] = ''
                    arr[i+1] = ''
                    combo_found = True
    arr = list(filter(None, arr))
    if combo_found == True:
        return dirReduc(arr)
    return arr

def test_directions():
    arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    assert dirReduc(arr) == ["WEST"]

def test_dir1():
    arr=["NORTH", "WEST", "SOUTH", "EAST"]
    assert dirReduc(arr) ==  ["NORTH", "WEST", "SOUTH", "EAST"]

def test_dir2():
    arr = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'NORTH', 'WEST', 'EAST']
    assert dirReduc(arr) == ['NORTH', 'NORTH']