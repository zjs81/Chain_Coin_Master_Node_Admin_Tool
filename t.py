from appJar import gui
import sys
import paramiko

#Def Func
def startmaster(button):
    cmd='chaincoind masternode start'
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    ssh.exit()
def send(button):
    cmd='chaincoind masternode start'
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    ssh.exit()
def restart(button):
    cmd='restart'
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    ssh.exit()
def startwallet(button):
    cmd='chaincoind --daemon'
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    ssh.exit()
def setup(button):
    pass
def refresh(button):
    cmd='chaincoind listtransactions'
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    ssh.exit()
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
ssh.close()
#ssh connection end
app = gui()
app.setFont(10)
app.addButton("Start masternode", startmaster)
app.addButton("Start masternode wallet", startwallet)
app.addButton("restart server", restart)
app.addButton("Send chc from masternode", send)
app.addButton("Refresh Balance", refresh)
app.addButton("open setup", setup)
app.infoBox("Alert", "Its recomended that you start your masternode wallet first then wait about 3 minutes before sending from or starting the masternode. So It can sync")

app.go()
