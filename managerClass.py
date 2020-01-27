from parentClass.employmentClass import *

class Manager(Employment):

	def __init__(self,first_name,last_name,pay=30000,sex='male',married=False, emps_list=[]):
		super().__init__(first_name,last_name,pay,sex,married)
		self.emps_list = emps_list

	def add_emp(self,*args):
		for i in args:
			if i not in self.emps_list:
				self.emps_list.append(i)

	def remove_emp(self,*args):
		for i in args:
			if i not in self.emps_list:
				print(f"{self.full_name()} doesn't manage {i}")
			else:
				self.emps_list.remove(i)

	def __str__(self):
		return f"{self.full_name()} manages " + ', '.join(self.emps_list)