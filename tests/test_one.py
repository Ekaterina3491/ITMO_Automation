def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


# def test_fail():
#     assert 'test' == 'testing'

# функция для проверка на несоотвествие
def test_not():
    a = 'test'
    b = 'testing'
    assert not a == b

def test_list():
    x = ["a", "b", "c"]
    y = [1, 2, 3]

    asser not x == y
    assert x !=y