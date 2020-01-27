class Employment():
	
	company = 'man-energy'
	raise_amount = 1.05
	num_emps = 0
	list_of_emploees = []

	def __init__(self,first_name,last_name,pay=30000,sex='male',married=False):
		self.first_name = first_name.capitalize()
		self.last_name = last_name.capitalize()
		self.pay = int(pay)
		self.sex = sex
		self.married = married
		Employment.num_emps +=1
		Employment.list_of_emploees.append(self)

	def full_name(self):
		return self.first_name + ' ' + self.last_name

	def email(self):
		return self.first_name + '.' + self.last_name + '@' + Employment.company + '.de'

	def apply_raise(self):

		self.pay = int(self.raise_amount * self.pay)

	def __str__(self):

		if self.married == True:
			mar='Yes'
		else:
			mar='No'

		spaces_s = 11 - len(self.sex)
		spaces_n = 22 - len(self.full_name())

		return self.full_name() + spaces_n*' ' + str(self.pay) + '$' + ' '*5 + self.sex + spaces_s*' ' + 'Married: ' + mar  
