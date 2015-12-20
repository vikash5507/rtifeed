import requests
import lxml.html as lh
import lxml 
from mechanize import Browser
# def gender_genie(text, genre):
# url = 'http://delhigovt.nic.in/rti/spio/search_ques.asp'
# # caption = 'The Gender Genie thinks the author of this passage is:'
 
# form_data = {
#     'comb_dept': '1',
#     'txt_ques': "",
#     'comb_cat' : '00',
#     'Search': 'Search',
#     # 'page' : 2,
# }
 
# response = requests.post(url, data=form_data)
browser = Browser()
browser.open("http://delhigovt.nic.in/rti/spio/search_ques.asp?page=2&comb_dept=2&comb_cat=00&txt_ques=")
browser.select_form(nr=0)
browser.form['comb_dept'] = ['1',]
browser.form['txt_ques'] = ""
browser.form['comb_cat'] = ['00',]
# browser.form['page'] = '2'

response = browser.submit()

content = response.read()
tree = lh.fromstring(content)
tables = tree.xpath('//table[@id="AutoNumber1"]/tr/td/a')
for tb in tables:
	print tb.get('href')
