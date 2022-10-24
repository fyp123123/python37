import unittest
class test(unittest.TestCase):
    def test01(self):
        a={"aa":1,"bb":2}
        b={"cc":1,"dd":3}
        self.assertEqual(a["aa"],b["cc"],msg="失败原因，a!=b")
if __name__ == '__main__':
 unittest.main()

