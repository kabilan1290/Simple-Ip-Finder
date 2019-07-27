import os
c = input("Enter The File Path\n")
b=("done < " +c)
import re
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