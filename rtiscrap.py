import re
from mechanize import Browser

browser = Browser()
browser.open("http://delhigovt.nic.in/rti/spio/search_ques.asp")
print "form"

browser.select_form(nr=0)
print browser.form
browser.form['comb_dept'] = ['1',]
browser.form['txt_ques'] = ""
browser.form['comb_cat'] = ['00',]


response = browser.submit()

content = response.read()

print content

# print result[0]