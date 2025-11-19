#-*- coding:utf-8 -*-

import requests, json

URL = 'http://sldm.kt.com/dash/policyResultForAjax.do'

org_code = '442750'

data = {'majrCode':'B01','buseoIndc':'N','majrName':'%eb%b3%b4%ec%95%88%ec%9d%b8%ec%8b%9d%ec%a0%9c%ea%b3%a0%0d%0a','org_code':org_code,'searchType':'1','emp_no':'10149499','isSubOrg':'N','search_date':'2019-03-11'}
headers = {'Content-Type':'application/x-www-form-urlencoded; charset:UTF-8'}

cookies = {'_fbp':'fb.1.1550024007499.1321671954',' AMCV_BCC0678254F6278C0A4C98A5%40AdobeOrg':'-1330315163%7CMCIDTS%7C17941%7CMCMID%7C07230804356265173635567086487894521948%7CMCAID%7CNONE%7CMCOPTOUT-1550031318s%7CNONE','sldmJSSIONID':'F4A23E452DDB4150C6C6DEB2EC27C19C'}
res = requests.post(URL, headers=headers,cookies=cookies,data=data)

high_score = res.text.split('"tablebody":')[1]
c1 = high_score.count('100')
print c1



case = ['D01','E01','G01']

for i in case:
	data = {'majrCode':i,'buseoIndc':'N','majrName':'%EC%95%85%EC%84%B1%EC%BD%94%EB%93%9C+%EA%B0%90%EC%97%BC+%EB%8C%80%EC%9D%91','org_code':org_code,'searchType':'1','emp_no':'10149499','isSubOrg':'N','search_date':'2019-03-11'}
	
	res = requests.post(URL, headers=headers,cookies=cookies,data=data)

	c2 = res.text.split('"tablebody":')[1].count('100')
	if c1 == c2:
		print 'Same!!'
	else:
		print i
		print res.text
		

		