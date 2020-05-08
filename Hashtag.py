def generate_hashtag(s):
    res_string = '#'
    if s == '':
        return False
    elif len(s) >= 144:
        return False
    else:
        words = s.split( ' ' )
        words = list(filter(None, words))
        for word in words:
            res_string += word.capitalize()
        return res_string

def test_hashtag_1():
    assert generate_hashtag('Codewars') == '#Codewars'

def test_hashtag_2():
    assert generate_hashtag('Codewars       ') == '#Codewars'

def test_hashtag_3():
    assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'

def test_hashtag_4():
    assert generate_hashtag('Codewars is nice') == '#CodewarsIsNice'

def test_hashtag_5():
    assert generate_hashtag('Codewars   is  nice') == '#CodewarsIsNice'

def test_hashtag_6():
    assert generate_hashtag('Loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooool') == False

def test_hashtag_7():
    assert generate_hashtag('') == False