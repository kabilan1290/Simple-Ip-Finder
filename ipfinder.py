#####################################
#   SIMPLE IP FINDER                #  
# BY  Game0v3r Aka Kabilan          #
#          2019                     #
#####################################
import pyfiglet
import os
import geoip2.database
import re
from datetime import date
import socket
today = date.today()
k = today.strftime("%d/%m/%y")
kabi = pyfiglet.figlet_format("Simple Ip Finder")
print(kabi)
print("                      Welcome To Simple IP Finder     " + k)
print( "                          A Tool By Kabilan")   
print("1.Find your Ip address\n")
print("2.Find the Ip Adddress of the Domain\n")
print("3.Find the Ip Addrress of the list of domains\n")
print("4.Enumerate Status code\n")
a=int(input("Enter..............."))
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
reader=geoip2.database.Reader('/root/Desktop/Simple-Ip-Finder/GeoLite2-City_20190709/GeoLite2-City.mmdb')
if (a==1):
    print("Your Computer Name is " +hostname)
    print("Your Computer Ip Address is " + ip)
      
    
elif (a==2):
    try:
        c = input("Enter the domain Name :")
        ip2 = socket.gethostbyname(c)
        print("The Ip address Of the Domain " +  " is " + ip2)
        response=reader.city(ip2)
        print("Latitude :",response.location.latitude)
        print("Longitude :",response.location.longitude)
    except socket.gaierror:
        print("Invalid Hostname " +c)
elif (a==3):
	d =raw_input("Enter the Directory name(/root/Desktop/domainnames)\n")
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
                   print("\nThe Ip address Of the Domain " + c +  " is " + xu +"\n")
               except socket.gaierror:
                   print("Invalid Hostname "  +c)
	       
elif (a==4):
    c = input("Enter The File Path\n")
    b=("done < " +c)
    def replace( filePath, text, subs, flags=0 ):
        with open( filePath, "r+" ) as file:
            fileContents = file.read()
            textPattern = re.compile( re.escape( text ), flags )
            fileContents = textPattern.sub( subs, fileContents )
            file.seek( 0 )
            file.truncate()
            file.write( fileContents )
    print(b)
    file = open('http.sh', 'a')
    replace("http.sh", "done < url.txt", b, flags=0)

    a = 'bash http.sh'
    os.system(a)	      
else:
    print("Invalid Selection") 

