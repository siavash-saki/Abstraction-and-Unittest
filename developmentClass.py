from parentClass.employmentClass import *

class Development(Employment):

	def __init__(self,first_name,last_name,pay=30000,sex='male',married=False,prog_lan='Java'):
		super().__init__(first_name,last_name,pay,sex,married)
		# Employment.__init__(self,first_name,last_name,pay,sex,married)
		self.prog_lan = prog_lan

		if self.prog_lan.lower() == 'python':
			raise_amount = 1.20
		else:
			raise_amount = 1.15

	def __str__(self):
		return f"{self.full_name()}'s programming language is: {self.prog_lan}."

