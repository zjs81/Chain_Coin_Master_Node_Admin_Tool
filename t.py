from appJar import gui
import random
import sys
import paramiko
from ftplib import FTP
app = gui()
past = []
installstarted = True

#Def Func
def updateMessage(x):
    #past.append(x)
    app.setMessage("list", x)

def checkStatus():

    #TODO add handling for a network connection drop.
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)

    updateMessage("Checking status")
    cmd='cd hodladmin;./checkstatus.sh'
    stdin,stdout,stderr=ssh.exec_command(cmd)
    for line in stdout:
        updateMessage(line)

def startmaster(button):
    global port
    global ip
    global username
    global password
    cmd='chaincoind masternode start'
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    outlines=stdout.readlines()
    resp=''.join(outlines)
    print(resp)
    ssh.close()

def send(button):
    global port
    global ip
    global username
    global password
    cmd='chaincoind masternode start'
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    outlines=stdout.readlines()
    resp=''.join(outlines)
    print(resp)
    ssh.close()

def restart(button):
    global port
    global ip
    global username
    global password
    cmd='restart'
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    outlines=stdout.readlines()
    resp=''.join(outlines)
    print(resp)
    ssh.close()

def startwallet(button):
    global port
    global ip
    global username
    global password
    cmd='chaincoind --daemon'
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    outlines=stdout.readlines()
    resp=''.join(outlines)
    print(resp)
    ssh.close()

def bootstrapAdmin(button):

    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)

    updateMessage("Bootstrapping admin")
    cmd='test -d "hodladmin" && { ./hodladmin/bootstrap.sh; } || { mkdir hodladmin;cd hodladmin;curl -O https://raw.githubusercontent.com/zjs81/Chain_Coin_Master_Node_Admin_Tool/master/remote/bootstrap.sh;chmod +x bootstrap.sh;./bootstrap.sh; }'
    stdin,stdout,stderr=ssh.exec_command(cmd)
    outlines=stdout.readlines()
    resp=''.join(outlines)
    print(resp)
    ssh.close()

    #TODO pull status of masternode installation to detrmine what still needs to be done and what to show in the UI

def installMasternode(button):

    #TODO support creation of a non-root masternode user with password set by the admin user

    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)

    updateMessage("Installing masternode software")
    cmd='./hodladmin/install.sh &'
    stdin,stdout,stderr=ssh.exec_command(cmd)
    exit_status = stdout.channel.recv_exit_status()
    if exit_status == 0:
        installstarted = True
        updateMessage("Install started")
    else:
        installstarted = False
        updateMessage("Install error")

    if installstarted:
        app.registerEvent(checkStatus)
        app.setPollTime(5000)

    ssh.close()

#TODO need a genkey function and wallet creation command. genkey needs to append to chaincoin.conf

def refresh(button):
    global port
    global ip
    global username
    global password
    cmd='chaincoind listtransactions'
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    outlines=stdout.readlines()
    resp=''.join(outlines)
    print(resp)
    ssh.close()
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
#Gets balance doesnt work yet
#ssh connection start
cmd='yum -y install vsftpd'
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)
stdin,stdout,stderr=ssh.exec_command(cmd)
resp = stdout.readlines()

print(resp)
ssh.close()
def check():
    cmd = "touch serverlog.txt"
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    ssh.exec_command(cmd)

    stdin,stdout,stderr=ssh.exec_command("cat serverlog.txt | xargs echo")

    outlines=stdout.readlines()

    print outlines
    showStartMasternode()
    if "[u'installed" in outlines:
        print("dank")
    if "statuson" in outlines:
        print ("Danker")
#ssh connection end
app.setFont(10)
def showStartMasternode():
    app.addButton("Start masternode", startmaster)
app.addButton("Start masternode wallet", startwallet)
app.addButton("restart server", restart)
app.addButton("Send chc from masternode", send)
app.addButton("Refresh Balance", refresh)
app.addButton("Initialize Tool", bootstrapAdmin)
app.addButton("Install Masternode", installMasternode)

app.addEmptyMessage("list")
app.addEmptyMessage("status")
updateMessage("Ready")
app.infoBox("Alert", "Its recomended that you start your masternode wallet first then wait about 3 minutes before sending from or starting the masternode. So It can sync")
check()
app.go()
