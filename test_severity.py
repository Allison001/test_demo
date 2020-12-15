import allure
import pytest

@allure.severity(allure.severity_level.BLOCKER)
def test_severity_a():
    print("这是一条阻塞级别的Bug")

@allure.severity(allure.severity_level.CRITICAL)
def test_severity_b():
    print("这是一条优先级高的Bug")

@allure.severity(allure.severity_level.NORMAL)
def test_severity_c():
    print("这是一条正常的bug")

@allure.severity(allure.severity_level.MINOR)
def test_severity_d():
    print("这是一条优先级低的Bug")

@allure.severity(allure.severity_level.TRIVIAL)
def test_severity_e():
    print("这是一条优先级最低的Bug")


if __name__ == '__main__':
    pytest.main()