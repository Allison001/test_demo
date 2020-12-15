import allure

@allure.link("https://www.baidu.com",name="链接")
def test_with_link():
    print("这是一条加了链接得测试用例")
    pass

test_casedir="http://www.baidu.com"
@allure.testcase(test_casedir,"登录地址")
def test_with_testcase():
    print("这是一条测试用例，可以链接到测试地址")
    pass

@allure.issue("140","bug")
def test_issure():
    print("这是一条测试用例，链接到bug管理地址")
    pass

