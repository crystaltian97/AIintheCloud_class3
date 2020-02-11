import unittest
import class_example

class TestMyModule(unittest.TestCase):
	
	def setUp(self):
		return 


	def do_divide(first_arg, sec_arg):

		first_arg = 4
		sec_arg = 2

		result = class_example.do_divide(first_arg,sec_arg)
		expected_result = 2

		self.assertEqual(result, expected_result)

