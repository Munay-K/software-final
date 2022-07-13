from main import is_old_enough
import unittest

class TestIsOldEnough(unittest.TestCase):
	def test_is_old_enough(self):
		self.assertEqual(is_old_enough("2000/01/01","2020/01/01"), True)
		self.assertEqual(is_old_enough("2000/01/01","2003/01/01"), False)
		with self.assertRaises(Exception):
			is_old_enough("2000/01/01","1940/01/01")#DateException
		with self.assertRaises(Exception):
			is_old_enough("2000-01-01","2000-01-01")#DateFormatException
