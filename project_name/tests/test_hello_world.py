import pytest  # noqa
from package_name import foo


def test_foo():
    assert(foo.bar() == 'Hello World')
