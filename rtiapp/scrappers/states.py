from rtiapp import models
import os
my_dir = os.path.dirname(__file__)

statelist = open(os.path.join(my_dir, 'states.csv'))
statelist = statelist.read()
statelist = statelist.split('\n')
for st in statelist[2:]:
	st = st.split(',')
	if st[1] != '':
		state = models.State()
		state.state_name = st[1]
		state.save()
		print st[1]

	