from itertools import permutations as perm
def permutations(string):
    chars = []
    resultlist = []
    result = ''
    for char in string:
        if char != ',':
            chars.append(char)
    startlist = list(range(0,len(chars)))
    charlist = list(perm(startlist))
    for pairs in charlist:
        for number in pairs:
            result += chars[int(number)]
        if result not in resultlist:
            resultlist.append(result)
        result = ''
    return resultlist

def test_permut_1():
    assert permutations('a') == ['a']

def test_permut_2():
    assert permutations('a,b') == ['ab', 'ba']

def test_permut_3():
    assert permutations('aabb') == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']  