import os
import getpass
from zipfile import ZipFile
#os.system("proxy.bat")
print("Thanx for choosing BIGMAE")
print("Note : Please close all chrome windows before starting!")
b=getpass.getuser()
l=input("Please enter the installation directory,Note: Directory should have minimum 2 gb free space \t")
k=open("C:\\Users\\"+b+"\\BIGMAE_dir.txt","w")
k.write(l)
k.close()
os.system('mkdir "'+l+':\\BIGMAE"')
a=open(l+":/BIGMAE/gchrome_profile.txt","w")
o=input("Is IIITA profile is Default(y/n)?, Type 'chrome://version/' in chrome address bar and from profile path see whether it is default or Profile 1,2...n\t")
print(o)
if o=="y" or o=="Y":
    a.write("Default")
else:
    a.write("Profile "+ input("Please Enter Google Chrome IIITA profile number\t"))
a.close()
try:
    o=os.listdir("C:\\Program Files (x86)\\Google\\Chrome\\Application")
except(FileNotFoundError):
    o=os.listdir("C:\\Program Files\\Google\\Chrome\\Application")
for i in o:  
    if "106" in i:
        os.system('curl -o "'+l+':\\BIGMAE\\chromedriver_win32.zip" "https://chromedriver.storage.googleapis.com/106.0.5249.21/chromedriver_win32.zip"')
    elif "105" in i:
        os.system('curl -o "'+l+':\\BIGMAE\\chromedriver_win32.zip" "https://chromedriver.storage.googleapis.com/105.0.5195.52/chromedriver_win32.zip"')
    elif "104" in i:
        os.system('curl -o "'+l+':\\BIGMAE\\chromedriver_win32.zip" "https://chromedriver.storage.googleapis.com/104.0.5112.79/chromedriver_win32.zip"')
with ZipFile(l+":\\BIGMAE\\chromedriver_win32.zip","r") as zip:
    zip.extractall(l+":\\BIGMAE")
list = ["selenium","datetime"]   #libraries name to be use in main program
for i in list:
    os.system("pip install "+ i)
a=open(l+":/BIGMAE/gchrome_profile.txt","r")
x=a.read()
a.close()
c=open(l+":/BIGMAE/gmeet_links.txt","w")
c.write("https://meet.google.com/ufi-asyn-uxa\nhttps://classroom.google.com/c/NDAzMjE0OTI1OTg3\nhttps://classroom.google.com/u/1/c/NDAwNTg0MTA0NjY1\nhttps://classroom.google.com/c/NDA0ODk3NTkzMDU5?cjc=zej722x\nhttp://meet.google.com/spy-vvrh-fko")
c.close()
y='xcopy /E "C:\\Users\\'+b+'\\AppData\\Local\\Google\\Chrome\\USER DATA\\'  #/E to copy directory and subdirectory   /H to copy hidden and system files
for i in os.listdir("C:/Users/"+b+"/AppData/Local/Google/Chrome/USER DATA"):
    if i==x:
        os.system(y+i+'\\" ' +'"'+l+':\\BIGMAE\\'+i+'\\"'+' /y')
    elif i=="Local State":
        os.system(y+i+'" ' +'"'+l+':\\BIGMAE\\'+'"')
    elif i=="Safe Browsing Channel IDs":
        os.system(y+i+'" ' +'"'+l+':\\BIGMAE\\'+'"')

