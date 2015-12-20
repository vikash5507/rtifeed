import requests
import lxml.html as lh
import grequests 
import json 
# def gender_genie(text, genre):

def get_rtis_for_department(department):
	url = 'http://delhigovt.nic.in/rti/spio/search_ques.asp'
	# caption = 'The Gender Genie thinks the author of this passage is:'
	 
	form_data = {
	    'comb_dept': str(department['dep_id']),
	    'txt_ques': "",
	    'comb_cat' : '00',
	    'Search': 'Search',
	}


	response = requests.post(url, data=form_data)
	tree = lh.fromstring(response.text)
	pages = tree.xpath('//center/a')
	print len(pages)

	hosts = []
	for i in range(0, len(pages)):
		url = "http://delhigovt.nic.in/rti/spio/search_ques.asp?page=" + str(i+1) + "&comb_dept=1&comb_cat=00&txt_ques="
		hosts.append(url)
	
	all_hosts = list(chunks(hosts, 20))
	print "all_pag_hossts", len(all_hosts)
	responses = []
	for hosts in all_hosts:
		rs=(grequests.post(u, data=form_data) for u in hosts)
		responses += grequests.map(rs)
		print len(responses)

	fetched_rti_links = []
	rti_attr_list = []

	for response in responses:
		tree = lh.fromstring(response.text)
		rti_links = tree.xpath('//table[@id="AutoNumber1"]/tr/td/a')
		
		for rti_link in rti_links:
			raw_link = rti_link.get('href')
			link = raw_link[raw_link.find("(")+1:raw_link.find(")")]
			link = link.replace("'", "")
			attrs = link.split(',')
			if not attrs in rti_attr_list:
				rti_attr_list.append(attrs)
			else:
				pass
		response.close()
	print len(rti_attr_list)
	rti_data = get_data_for_rtis(rti_attr_list)

	json_file = open('delhi_data.json', 'r')
	dep_json = json.loads(json_file.read())
	json_file.close()
	# pprint.pprint(dep_json)
	dep_json[department['dep_name']] = rti_data
	
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
	responses = []
	all_hosts = list(chunks(hosts, 50))

	rti_data = []
	for hosts in all_hosts:
		rs=(grequests.get(u, stream=False) for u in hosts)
		responses = grequests.map(rs)
		
		print "responses", len(responses)
		
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
			response.close()
		
		print "rtis_fetched", len(rti_data)
			
	return rti_data

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]
# get_rtis_for_department({'dep_id' : 1})