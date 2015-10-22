import requests
from lxml import html

postdata = {
	'val' : 'Com',
	'val_l' : '',
	'firstflag' : 'search',
	'user_id' : '',
	'val_1' : 'Com',
	'search_id' : 3,
	'complaint_id' : 32422432,
	'name_id' : '',
	'mail_id' : ''
}
r = requests.post("http://rti.india.gov.in/cic_gov_check_status.php", data=postdata)
print(r.status_code, r.reason)
# print(r.text + '...')
tree=html.fromstring(r.text)
resp=tree.xpath('//*[@id="mainContentWrapper2"]//text()')
print resp