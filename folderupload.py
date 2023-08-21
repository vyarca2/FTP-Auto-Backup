import ftplib
import os

filename1=open(r'directory.txt',"r")
filename2=open(r'serverip.txt',"r")
filename3=open(r'username.txt',"r")
filename4=open(r'password.txt',"r")

server = filename2.read()
username =filename3.read()
password = filename4.read()
myFTP = ftplib.FTP(server, username, password)
mypath=filename1.read()

def uploadThis(mypath):
    files = os.listdir(mypath)
    os.chdir(mypath)
    if '/' in mypath:
        for f in files:
            if os.path.isfile(mypath + r'/{}'.format(f)):
                fh = open(f, 'rb')
                myFTP.storbinary('STOR %s' % f, fh)
                fh.close()
            elif os.path.isdir(mypath + r'/{}'.format(f)):
                myFTP.mkd(f)
                myFTP.cwd(f)
                uploadThis(mypath + r'/{}'.format(f))
    if '\\' in mypath:
        for f in files:
            if os.path.isfile(mypath + r'\{}'.format(f)):
                 fh = open(f, 'rb')
                 myFTP.storbinary('STOR %s' % f, fh)
                 fh.close()
            elif os.path.isdir(mypath + r'\{}'.format(f)):
                myFTP.mkd(f)
                myFTP.cwd(f)
                uploadThis(mypath + r'\{}'.format(f))
                
    myFTP.cwd('..')
    os.chdir('..')
uploadThis(mypath)
