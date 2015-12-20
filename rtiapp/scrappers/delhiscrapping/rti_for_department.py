import requests
import lxml.html as lh
import lxml
import grequests
from mechanize import Browser
import json
import pprint

def get_rtis_for_department(department):
	dep_id = department['dep_id']
	print department
	browser = Browser()
	browser.open("http://delhigovt.nic.in/rti/spio/search_ques.asp")
	browser.select_form(nr=0)
	browser.form['comb_dept'] = [str(dep_id),]
	browser.form['txt_ques'] = ""
	browser.form['comb_cat'] = ['00',]
	
	response = browser.submit()

	content = response.read()
	tree = lh.fromstring(content)
	
	rti_links = tree.xpath('//table[@id="AutoNumber1"]/tr/td/a')
	rti_attr_list = []
	for rti_link in rti_links:
		raw_link = rti_link.get('href')
		link = raw_link[raw_link.find("(")+1:raw_link.find(")")]
		link = link.replace("'", "")
		attrs = link.split(',')
		rti_attr_list.append(attrs)

	rti_data = get_data_for_rtis(rti_attr_list)

	json_file = open('delhi_data.json', 'r')
	dep_json = json.loads(json_file.read())
	json_file.close()
	# pprint.pprint(dep_json)
	dep_json[department['dep_name']].append(rti_data)
	
	json_file = open('delhi_data.json', 'w')
	json_file.write(json.dumps(dep_json))
	json_file.close()

def get_data_for_rtis(rti_attr_list):
	hosts = []
	# print "att len", len(rti_attr_list)
	for attr_list in rti_attr_list:
		url = ('http://delhigovt.nic.in/rti/spio/show_ans.asp?id_no='+str(attr_list[0])
		+'&user_code='+str(attr_list[1])+'&ques_id='+str(attr_list[2])+'&status='+str(attr_list[3]))
		hosts.append(url)

	print 'hosts', len(hosts)
	rs=(grequests.get(u) for u in hosts)
	responses=grequests.map(rs)
	# print "responses", len(responses)
	rti_data = []
	counter = 0
	for response in responses:
		rti = {}
		tree = lh.fromstring(response.text)
		response_tree = tree.xpath('//tr/td[@width="90%"]')
		if len(response_tree) >= 1:
			rti['category'] = response_tree[0].text
		if len(response_tree) >= 2:
			rti['query'] = response_tree[1].text
		if len(response_tree) == 3:
			rti['response'] = response_tree[2].text
		rti['url'] = hosts[counter]
		counter += 1
		rti_data.append(rti)

	return rti_data