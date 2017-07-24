from appJar import gui
import random
import sys
import paramiko

app = gui()
past = []
installstarted = True

#Def Func
def updateMessage(x):
    #past.append(x)
    app.setMessage("list", x)

def checkStatus():
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

def installmasternode(button):
    
    #TODO support creation of a non-root masternode user with password set by the admin user

    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    
    updateMessage("Installing")
    cmd='mkdir hodladmin;cd hodladmin;curl -O https://raw.githubusercontent.com/zjs81/Chain_Coin_Master_Node_Admin_Tool/master/remote/checkstatus.sh;chmod +x checkstatus.sh;curl -O https://raw.githubusercontent.com/zjs81/Chain_Coin_Master_Node_Admin_Tool/master/remote/install.sh;chmod +x install.sh;./install.sh &'
    stdin,stdout,stderr=ssh.exec_command(cmd)
    exit_status = stdout.channel.recv_exit_status()
    if exit_status == 0:
        installstarted = True
        updateMessage("Install started")
    else
        installstarted = False
        updateMessage("Install error")

    if installstarted:
        app.registerEvent(checkStatus)
        app.setPollTime(1000)

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
app.setFont(10)
app.addButton("Start masternode", startmaster)
app.addButton("Start masternode wallet", startwallet)
app.addButton("restart server", restart)
app.addButton("Send chc from masternode", send)
app.addButton("Refresh Balance", refresh)
app.addButton("Install masternode", installmasternode)
app.addEmptyMessage("list")
updateMessage("Ready")
app.infoBox("Alert", "Its recomended that you start your masternode wallet first then wait about 3 minutes before sending from or starting the masternode. So It can sync") 
app.go()
