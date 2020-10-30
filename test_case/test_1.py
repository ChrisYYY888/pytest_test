# -*- coding: utf-8 -*-
import platform
import sys
import pytest  # 引入pytest包

# pytestmark = pytest.mark.webtest


@pytest.mark.aaa
def test_a():  # test开头的测试函数
    print("------->test_a")
    assert 1  # 断言成功


# @pytest.mark.flaky(reruns=3)
def test_b(bbb1, bbb2):
    print("------->test_b")
    assert bbb1 == 'leo'  # 断言成功
    assert bbb2 == 0  # 断言失败
    # pytest.assume(1 + 4 == 5)
    # pytest.assume(1 + 3 == 3)
    # pytest.assume(2 + 5 == 7)
    # pytest.assume(2 + 5 == 9)


@pytest.mark.ccc
def test_c(ccc):
    print("------->test_c")
    print(ccc)
    assert ccc == 2


@pytest.fixture()
def user():
    print("获取用户名")
    a = "yygirl"
    assert a == "yygirl123"
    return a


def test_d(user):
    assert user == "yygirl"


@pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
def test_f():
    print("我是测试用例f")


@pytest.mark.skipif(float(platform.python_version()[0:3]) > 3.6, reason="需要Python3.6版本以上")
def test_f2():
    print(sys.version)
    print("我是测试用例f2")


@pytest.mark.xfail()
def test_g():
    assert "abc" == "abc"


@pytest.mark.xfail(strict=True)
def test_e():
    assert 1 / 0


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_e():
    assert 1 / 0


@pytest.mark.parametrize("para1, para2", [(1, 2), (11, 22)])
def test_h(para1, para2):
    assert para1 == para2


if __name__ == '__main__':
    pytest.main("-v -s  test_1.py")  # 调用pytest的main函数执行测试