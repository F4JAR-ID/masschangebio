try:
	import requests as r, os

	from bs4 import BeautifulSoup as parser
	ses = r.Session()
	
	os.system("clear")
	h = '\033[92m'
	m = '\033[91m'
	p = '\033[0m'
	
	print h + "Mass Change Bio Facebook\nCoded by: SalisM3\n" + p
	
	file = raw_input('[?] File Facebook List (use sparator email|pass): ')
	open = open(file).read().splitlines()
	baru = raw_input('[?] Bio Baru: ')
	print ""
	for s in open:
		u = s.split('|')[0]
		pw = s.split('|')[1]
		oh = ses.post('https://mbasic.facebook.com/login', data={'email':u, 'pass':pw, 'login':'submit'})
		a = ses.get('https://mbasic.facebook.com/profile/basic/intro/bio').text
		soup = parser(a, "html.parser")
		fb_dtsg = soup.find_all('input')[4].get('value')
		jazoest = soup.find_all('input')[5].get('value')
		b = ses.post('https://mbasic.facebook.com/profile/intro/bio/save/', data={'fb_dtsg':fb_dtsg, 'jazoest':jazoest, 'bio':baru}).content
		if baru in b:
			print h + "[OK] " + p + u
		else:
			print m + "[FL] " + p + u

except:
	print m + "[+] Terjadi Error!" + p
