from rtiapp import models
import os
my_dir = os.path.dirname(__file__)

department = open(os.path.join(my_dir, 'rtidepartment.csv'))
department = department.read()
department = department.split('\n')
for row in department[2:]:
	# print row
	row = row.split(',')
	dep_name = row[2]
	website = row[3]
	dept = models.Department()
	dept.department_name = dep_name
	dept.website = website
	dept.department_type = 'centre'	
	dept.save()
	print dep_name, website
