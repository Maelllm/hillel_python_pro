import unittest
from datetime import datetime, timedelta
from task_20 import Fibonacci, formatted_name


class TestFibo(unittest.TestCase):

    def setUp(self):
        self.fibo = Fibonacci()

    def tearDown(self) -> None:
        self.fibo = None

    def test_extremum(self):
        self.assertEqual(self.fibo(0), 0)
        self.assertEqual(self.fibo(1), 1)
        self.assertEqual(self.fibo(480),
                         9216845717656874712980450562726202415567360565980794777111390850331644813674856981646960226192287360)
        with self.assertRaises(RecursionError):
            self.fibo(1000)

    def test_time(self):
        start = datetime.now()
        self.fibo(480)
        finish = datetime.now()
        self.assertLessEqual(finish - start, timedelta(milliseconds=900))

    def test_nonint(self):
        with self.assertRaises(ValueError):
            self.fibo("1")
        with self.assertRaises(ValueError):
            self.fibo([1, 2])
        with self.assertRaises(ValueError):
            self.fibo({1: 4})

    def test_negative(self):
        with self.assertRaises(ValueError):
            self.fibo(-5)

    def test_cache(self):
        self.fibo(7)
        self.assertEqual(self.fibo.cache, [0, 1, 1, 2, 3, 5, 8, 13])
        self.fibo(8)
        self.assertEqual(self.fibo.cache[8], 21)


class TestFormattedName(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(formatted_name('test_naMe', 'test_lAst_name', 'test_mIddlE_name'),
                         "Test_Name Test_Middle_Name Test_Last_Name")

    def test_empty(self):
        self.assertEqual(formatted_name("", ""), " ")
        self.assertEqual(formatted_name("", "", middle_name=" "), "   ")

    def test_nonstr(self):
        with self.assertRaises(TypeError):
            print(formatted_name(1, ["2"]))

    def test_symbol(self):
        self.assertEqual(formatted_name("Mike", "NotMike", "[]definely_not_Mike"), "Mike []Definely_Not_Mike Notmike")


if __name__ == '__main__':
    unittest.main()
