from appJar import gui
import sys
import paramiko

#Def Func
def startmaster():
    print "lol"
def send():
    pass
def restart():
    pass
def startwallet():
    pass
def setup():
    pass
def refresh():
    pass
#Done Def Func
#Starts takeing args
keyfilename = ""
keyfileinuse = False
port = int(sys.argv[4])
ip = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
#The stuff above takes args from login.py
balance = 0
#Gets balance
#ssh connection start
cmd='uptime'
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)
stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)

#ssh connection end
app = gui()
app.setFont(10)
app.addButton("Start masternode", startmaster)
app.addButton("Send chc from masternode", send)
app.addButton("restart server", restart)
app.addButton("Start masternode wallet", startwallet)
app.addButton("open setup", setup)
app.addButton("Refresh Balance", refresh)
app.infoBox("Alert", "Its recomended that you start your masternode wallet first then wait about 3 minutes before sending from or starting the masternode. So It can sync")

app.go()
