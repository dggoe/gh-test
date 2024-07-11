from ghtests.sample import convert


def setup_module(module):
    print("\n==== setting up ====\n")


def teardown_module(module):
    print("\n==== tearing down ====\n")


def test_conversion():
    assert convert("hello world") == "<HELLO WORLD>"
    assert True == True