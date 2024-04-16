from my_package.app import Demo


def test_app():
    x = Demo(name="kobi", age=5)
    assert x.age==5
    assert x.name=="kobi"