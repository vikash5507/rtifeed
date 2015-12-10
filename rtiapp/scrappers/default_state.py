from rtiapp import models

states = models.State.objects.all()

default_departments = ['Dep1', 'Dep2', 'Dep3']

for state in states:
	for dep_text in default_departments:
		dp = models.Department()
		dp.department_name = dep_text + " " + state.state_name
		dp.department_type = 'state'
		dp.save()
		sd = models.State_department()
		sd.department = dp
		sd.state = state
		sd.save()


