import unittest

def search():
    print("search")

class TestSuit(unittest.TestCase):
    def setUp(self) -> None:
        print("start")

    def tearDown(self) -> None:
        print("end")

    def test_001(self):
        print("test001")
        self.sear = search()
        print(self.sear)

    def test_002(self):
        print("test002")

if __name__ == '__main__':
    #执行全部的测试用例
    # unittest.main()
    #执行指定的测试用例
    suit = unittest.TestSuite()
    suit.addTest(TestSuit("test_002"))
    unittest.TextTestRunner().run(suit)