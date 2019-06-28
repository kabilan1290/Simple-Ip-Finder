#####################################
#   SIMPLE IP FINDER                #  
# BY Game0v3r Aka Kabilan           #
#          2019                     #
#####################################
import pyfiglet
from colorama import Fore
from datetime import date
import socket
today = date.today()
k = today.strftime("%d/%m/%y")
kabi = pyfiglet.figlet_format("Simple Ip Finder")
print(kabi)
print(Fore.RED+ "                      Welcome To Simple IP Finder     " + Fore.GREEN+ k)
print( Fore.RED+ "                          A Tool By Kabilan")   
print(Fore.GREEN + "1.Find your Ip address\n")
print("2.Find the Ip Adddress of the Domain\n")
print("3.Find the Ip Addrress of the list of domains\n")
a=input(Fore.RED+"Enter...............")
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
b=a
if(b==1):
    print(Fore.GREEN+"Your Computer Name is " +Fore.RED+ hostname)
    print(Fore.GREEN+"Your Computer Ip Address is " +Fore.RED+ ip)
elif(b==2):
    try:
        c = raw_input(Fore.GREEN+"Enter the domain Name :")
        ip2 = socket.gethostbyname(c)
        print("The Ip address Of the Domain " + Fore.RED + c + Fore.GREEN + " is " + Fore.RED + ip2)
    except socket.gaierror:
        print("Invalid Hostname " + Fore.RED +c)
elif(b==3):
	d =raw_input(Fore.GREEN+"Enter the Directory name(/root/Desktop/domainnames)\n")
	mak =[]
	with open(d) as f:
            for line in f:
                mak.append(line)
            n = len(mak)
            
            for i in range(0,n):
	       c = mak[i]
               xz = ''.join(c.split())
               try:
                   xu = socket.gethostbyname(xz)
                   print(Fore.GREEN +"\nThe Ip address Of the Domain " + Fore.RED + c + Fore.GREEN + " is " + Fore.RED + xu +"\n")
               except socket.gaierror:
                   print("Invalid Hostname " + Fore.RED +c)
	       
	      
else:
    print(Fore.RED+"Invalid Selection") 

