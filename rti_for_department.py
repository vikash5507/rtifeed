import requests
import lxml.html as lh
import lxml

def get_rtis_for_department(department):
	dep_id = department['dep_id']
	base_url = "http://delhigovt.nic.in/rti/spio/search_ques.asp?page=" + dep_id + "&comb_dept=1&comb_cat=00&txt_ques="
	response = requests.get(base_url)
	tree = lh.fromstring(response.text)

	pages_xpath = tree.xpath('//center/a')
	dep_hosts = []
	for page_xpath in pages_xpath:
		dep_hosts.append(page_xpath.get('href'))

	print dep_hosts

get_rtis_for_department({'dep_id' : 1})
