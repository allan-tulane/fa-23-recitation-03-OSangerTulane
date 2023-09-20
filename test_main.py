from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2

def test_multiply_3(self):
        x = BinaryNumber(['1', '0', '1', '0', '0', '1'])
        y = BinaryNumber(['1', '1', '0', '0', '1', '1'])
        result = quadratic_multiply(x, y)
        self.assertEqual(result, 1176)  # 101001 (41 in decimal) * 110011 (51 in decimal) = 1176 (in decimal)

def test_multiply_large_numbers(self):
        x = BinaryNumber(['1'] * 100)
        y = BinaryNumber(['1'] * 100)
        result = quadratic_multiply(x, y)
        self.assertEqual(result, int('1' * 200, 2))  # 111...111 (100 1s) * 111...111 (100 1s) = 111...111 (200 1s) in decimal
