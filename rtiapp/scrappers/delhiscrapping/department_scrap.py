import requests
import lxml.html as lh
import lxml
import json 

def get_departments():
	url = 'http://delhigovt.nic.in/rti/spio/search_ques.asp'
	response = requests.get(url)
	tree = lh.fromstring(response.text)

	departments = tree.xpath('//select[@name="comb_dept"]/option')

	department_list = []
	for dp in departments[1:]:
		# if dp.get('value') == '1':
		department_list.append({
			'dep_id' : dp.get('value'),
			'dep_name' : dp.text
			})

	
	dep_json = {}
	for dl in department_list:
		dep_json[dl['dep_name']] = []
	
	json_file = open('delhi_data.json', 'w')
	json_file.write(json.dumps(dep_json))
	json_file.close()

	return department_list