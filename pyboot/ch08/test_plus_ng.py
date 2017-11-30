import unittest

#테스트 대상 plus 함수
def plus(a,b):
    return a + b

class PlusTest(unittest.TestCase):
    #테스트 프로그램
    def test_plus(self):
        self.assertEqual(10, plus(2,8))
        self.assertEqual(20, plus(2,8))

if __name__ == "__main__":
    unittest.main()
