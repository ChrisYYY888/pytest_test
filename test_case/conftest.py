import pytest


@pytest.fixture()
def bbb1():
    b = 'leo'
    return b


@pytest.fixture()
def bbb2():
    b = 'leo'
    return b


@pytest.fixture(params=[0, 1, 2, 3])
def ccc(request):
    param = request.param
    return param

