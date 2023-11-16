import unittest

# 우리가 구현한 코드
def add(x, y):
    return x+y

def sub(x, y):
    return x - y

def mul(x,y):
    return x*y

#테스트 코드
class TestAdd(unittest.TestCase):
    def test_add(self):
        print('더하기 테스트')
        self.assertEqual(add(1, 2), 3)

    def test_sub(self):
        print('그냥 테스트')
        self.assertEqual(sub(3-1), 2)

    def test_mul(self):
        print('빼기 테스트')
        self.assertEqual(mul(2,3), 6)
    
    def ko(self):
        '''
        test이름은 자유롭게 작성 가능
        '''
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()