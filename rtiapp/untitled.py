from rtiapp import models

states = models.State.objects.all()

default_departments = []

for state in states:
	for dep_text in default_departments:
		dp = models.Department()
		dp.department_name = dep_text
		dp.department_type = 'state'

