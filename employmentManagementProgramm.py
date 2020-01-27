
from parentClass.employmentClass import Employment
from developmentClass import Development
from managerClass import *

emp_1 = Employment('christian','mohr',80000,'male',True)
emp_2 = Employment('pia','Bohr',40000,'female',True)
emp_3 = Employment('kerstin','schurmann',60000,'female',False)
emp_4 = Employment('Test','User' )

dev_1 = Development('elnaz','Bezdoodeh',50000,'female',False,'Python')
dev_2 = Development('Bahark','heydari',50000,'female',False,'c++')
	
man_1 = Manager('Mathias', 'Stark', 90000, 'male', True)



def main():

	# emp_1 = Employment('christian','mohr',80000,'male',True)
	# emp_2 = Employment('pia','Bohr',40000,'female',True)
	# emp_3 = Employment('kerstin','schurmann',60000,'female',False)
	# emp_4 = Employment('Test','User' )


	# dev_1 = Development('elnaz','Bezdoodeh',50000,'female',False,'Python')
	# dev_2 = Development('Bahark','heydari',50000,'female',False,'c++')
	
	# man_1 = Manager('Mathias', 'Stark', 90000, 'male', True)

	print(emp_1)
	print(emp_4)
	print(dev_1)
	print(dev_2)
	print(man_1)

	print('\n')

	# print(emp_1.email())
	# print(emp_2.email())
	# print(emp_3.email())
	# print(emp_4.email())

	emp_4.apply_raise()
	dev_1.apply_raise()
	dev_2.apply_raise()
	print(emp_4)
	print(dev_1)
	print(dev_2)
	print('\n')

	# print(f'{dev_1.full_name()}:     '+dev_1.prog_lan)
	# print(f'{dev_2.full_name()}:      '+dev_2.prog_lan)

	print('\n')
	print(Employment.num_emps)

	print('\n')
	print(man_1.emps_list)
	man_1.add_emp(emp_1.full_name(),emp_2.full_name(),emp_3.full_name(),emp_4.full_name())
	print(man_1.emps_list)
	man_1.remove_emp(emp_1.full_name(),emp_2.full_name(),dev_1.full_name())
	print(man_1.emps_list)

	print('\n')
	# print(Employment.list_of_emploees)

	for x in Employment.list_of_emploees:
		print(x)

	### Useful Informations

	# print(emp_1.__dict__)
	# print(dev_1.__dict__)
	# print(Employment.__dict__)

	# class info
	# **Method Resoluiton Order
	# print(help(Development))

if __name__=='__main__':
	main()

