import unittest


class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_a(self):
        print("test a got executed")

    @unittest.skip("testing skip in unittest")
    def test_b(self):
        print("test b got executed")

    @unittest.skipIf(1 == 1, "meri marzi")
    def test_c(self):
        print("test c got executed")

    def test_d(self):
        print("test d got executed")

    def test_e(self):
        print("test e got executed")

    def test_f(self):
        print("test f got executed")

if __name__ == "__main__":
    unittest.main()