from ghtests.sample import convert


def test_conversion():
    assert convert("hello world") == "HELLO WORLD"