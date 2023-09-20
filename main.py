"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    #1
    xvec = x.binary_vec
    yvec = y.binary_vec

    #2 Pad binary vectors to have the same length
    max_len = max(len(xvec), len(yvec))
    xvec = ['0'] * (max_len - len(xvec)) + xvec
    yvec = ['0'] * (max_len - len(yvec)) + yvec

    #3 Base case: If both x and y are <= 1, return their product
    if len(xvec) == 1 and len(yvec) == 1:
        return BinaryNumber([str(int(xvec[0]) * int(yvec[0]))])

    #4 Split xvec and yvec into two halves
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)

    #5 Recursive calls for multiplication
    xlyl = _quadratic_multiply(x_left, y_left)
    xlyr = _quadratic_multiply(x_left, y_right)
    xryl = _quadratic_multiply(x_right, y_left)
    xryr = _quadratic_multiply(x_right, y_right)

    #6&7 Perform additions and shifts to compute the final result
    part1 = bit_shift(bit_shift(xlyl, len(xvec)), len(xvec))
    part2 = bit_shift(_quadratic_multiply(x_left + x_right, y_left + y_right), len(xvec) // 2)
    part3 = xlyr + xryl

    result = part1 + part2 + part3 + xryr

    return result

    
    
#def test_quadratic_multiply(x, y, f):
  # start = time.time()
    # multiply two numbers x, y using function f
    
   # return (time.time() - start)*1000

def test_multiply_1(self):
        x = BinaryNumber(['1', '0', '1'])
        y = BinaryNumber(['1', '1', '0'])
        result = quadratic_multiply(x, y)
        self.assertEqual(result, 6)  # 101 (5 in decimal) * 110 (6 in decimal) = 30 (in decimal)

def test_multiply_2(self):
        x = BinaryNumber(['1', '0', '1', '0', '0'])
        y = BinaryNumber(['1', '1', '0', '0', '1'])
        result = quadratic_multiply(x, y)
        self.assertEqual(result, 52)  # 10100 (20 in decimal) * 11001 (25 in decimal) = 520 (in decimal)



    
    

