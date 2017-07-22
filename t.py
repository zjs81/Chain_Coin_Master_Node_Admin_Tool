from appJar import gui
import sys
import paramiko

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
app = gui("HODLER ADMIN", "400x200")


app.setFont(10)
app.addLabelOptionBox("Options", ["File","Install MasterNode"])

print port, ip, username, password
app.go()
