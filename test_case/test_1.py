# -*- coding: utf-8 -*-
import pytest  # 引入pytest包


@pytest.mark.aaa
def test_a():  # test开头的测试函数
    print("------->test_a")
    assert 1  # 断言成功


# @pytest.mark.flaky(reruns=3)
def test_b(bbb):
    print("------->test_b")
    assert bbb == 0  # 断言失败
    # pytest.assume(1 + 4 == 5)
    # pytest.assume(1 + 3 == 3)
    # pytest.assume(2 + 5 == 7)
    # pytest.assume(2 + 5 == 9)


def test_c():
    print("------->test_b")
    assert 1 + 1 == 2  # 断言成功


@pytest.fixture()
def user():
    print("获取用户名")
    a = "yygirl"
    assert a == "yygirl123"
    return a


def test_d(user):
    assert user == "yygirl"


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_e():
    assert 1 / 0


@pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
def test_f():
    print("我是测试用例22222")


@pytest.mark.xfail()
def test_g():
    assert "abc" == "abc"


if __name__ == '__main__':
    pytest.main("-v -s  test_1.py")  # 调用pytest的main函数执行测试