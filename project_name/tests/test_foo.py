import pytest  # noqa
from package_name.foo import bar


def test_bar():
    assert(bar() == 'Hello World')
