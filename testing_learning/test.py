def test_1():
    x=10
    y=10
    assert x==y

def test_2():
    name = "subhasish"
    title = "subhasish is a good men"
    assert name in title

def test_3():
    name = "suhasini"
    title = "Simi is a good woman"
    assert name is title,"Name should not be in title"