from ghtests.sample import convert


def test_conversion():
    assert convert("hello1 world") == "HELLO WORLD"