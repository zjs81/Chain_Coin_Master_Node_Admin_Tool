from appJar import gui
import random
import sys
import paramiko
past = ["1","2"]
#Def Func
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
    cmd='echo installing\n' + ';yum -y install wget;yum -y install epel-release;yum -y install system-config-firewall-tui bzip2 git clone autoconf automake gcc-c++ boost-devel openssl-devel;yum -y update;cd /usr/src;wget https://www.openssl.org/source/openssl-1.0.2-latest.tar.gz;tar -zxf openssl-1.0.2-latest.tar.gz;cd openssl-1.0.2l;export CFLAGS="-fPIC";./config --prefix=/opt/openssl --openssldir=/opt/openssl enable-ec enable-ecdh enable-ecdsa -fPIC shared;make all;make install;cd ~;mkdir chaincoin;cd ~/chaincoin;wget http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz;mkdir db4;cd db4;tar xvf ../db-4.8.30.NC.tar.gz;cd db-4.8.30.NC/build_unix/;../dist/configure --enable-cxx --disable-shared --with-pic --prefix=/root/chaincoin/db4/;make;make install;cd ..;cd ..;cd ..;wget http://sourceforge.net/projects/boost/files/boost/1.55.0/boost_1_55_0.tar.bz2/download -O boost_1_55_0.tar.bz2;tar jxvf boost_1_55_0.tar.bz2;cd boost_1_55_0;./bootstrap.sh;./b2 --prefix=/root/chaincoin/deps link=static runtime-link=static install;cd ..;cd /usr/local/bin;rm chaincoind -rf; rm chaincoin-cli -rf;wget http://highoncoins.com/chaincoin/centos7/chaincoin-cli; wget http://highoncoins.com/chaincoin/centos7/chaincoind;chmod 700 chaincoin*;cd ~'
    # TODO pull masternode public IP address
    cmd2='echo creating conf file\n' + ';mkdir ~/.chaincoin/;cd ~/.chaincoin/;echo $"rpcuser=username\nrpcpassword=somepassword\nserver=1\nlisten=1\nmasternode=1\nmasternodeaddr=PutyourIPADDRESSHERE:11994" >chaincoin.conf'
    cmd3='cd ~/.chaincoin;' + 'echo \'downloading bootstrap\n' + ';wget http://downloadandroidrom.com/bootstrap.dat;'+ 'echo initializing wallet with bootstrap\n' + ';chaincoind -loadblock=bootstrap.dat;chaincoind stop'
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    stdin,stdout,stderr=ssh.exec_command(cmd2)
    stdin,stdout,stderr=ssh.exec_command(cmd3)    
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
app = gui()
app.setFont(10)
app.addButton("Start masternode", startmaster)
app.addButton("Start masternode wallet", startwallet)
app.addButton("restart server", restart)
app.addButton("Send chc from masternode", send)
app.addButton("Refresh Balance", refresh)
app.addButton("open setup", setup)
app.infoBox("Alert", "Its recomended that you start your masternode wallet first then wait about 3 minutes before sending from or starting the masternode. So It can sync")
def updatelist():
    app.addListBox("list", past)
app.go()
