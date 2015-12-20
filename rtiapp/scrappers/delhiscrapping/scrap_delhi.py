import requests
import lxml.html as lh
import lxml
import department_scrap
import rti_for_department_v2


department_list = department_scrap.get_departments()


for dep in department_list:
	print "-------"
	print dep
	rti_for_department_v2.get_rtis_for_department(dep)