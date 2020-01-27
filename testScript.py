import unittest
from employmentManagementProgramm import *

class test_employmentManagementProgramm(unittest.TestCase):

	def test_fullname(self):
		result=emp_1.full_name()
		self.assertEqual(result,'Christian Mohr')

	def test_email(self):
		result=emp_1.email().lower()
		self.assertEqual(result,'christian.mohr@man-energy.de')

	def test_apllyraise(self):
		emp_1.apply_raise()
		result=emp_1.pay
		self.assertEqual(result,84000)

	def test_str_emp(self):
		result = str(emp_1)
		self.assertEqual(result,'Christian Mohr        84000$     male       Married: Yes')




if __name__=='__main__':
	unittest.main()