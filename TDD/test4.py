import unittest

# 테스트 코드
class TestAdd(unittest.TestCase):
  def test_add(self):
    self.assertEqual(1 + 2, 3)
    self.assertTrue(True == (1<5)) # 이렇게도 사용 가능 물론!
    self.assertFalse(1 == 10)
    self.assertGreater(10, 1) # 앞에 것이 뒤에 것보다 큰지
    self.assertLess(1, 10) # 앞에 것이 뒤에 것보다 작은지
    self.assertIn(1, [1, 2, 3, 4, 5]) # 포함하고 있는지
    self.assertIsInstance('a', str) # 인스턴스인지

if __name__ == '__main__':
    unittest.main()