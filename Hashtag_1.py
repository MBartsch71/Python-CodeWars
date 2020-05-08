def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
        

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