#!/bin/bash

# TODO Logic for determining OS and choosing the right yum/atp commands

#TODO create function to write status to file

statusfile=~/hodladmin/status.log
ipaddressfile=~/hodladmin/ipaddress.log

# Pull additional remote scripts
touch $statusfile  

cd ~
echo 'STEP 1' >> $statusfile
yum -y install wget
echo 'STEP 2' >> $statusfile
yum -y install epel-release
echo 'STEP 3' >> $statusfile
yum -y install system-config-firewall-tui bzip2 git clone autoconf automake gcc-c++ boost-devel openssl-devel
echo 'STEP 4' >> $statusfile
yum -y update
echo 'STEP 5' >> $statusfile
cd /usr/src
wget https://www.openssl.org/source/openssl-1.0.2-latest.tar.gz
tar -zxf openssl-1.0.2-latest.tar.gz
cd openssl-1.0.2l
echo 'STEP 6' >> $statusfile
export CFLAGS="-fPIC"
./config --prefix=/opt/openssl --openssldir=/opt/openssl enable-ec enable-ecdh enable-ecdsa -fPIC shared
make all
make install
cd ~
mkdir chaincoin
echo 'STEP 7' >> $statusfile
cd ~/chaincoin
wget http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz
mkdir db4
cd db4
tar xvf ../db-4.8.30.NC.tar.gz
cd db-4.8.30.NC/build_unix/
../dist/configure --enable-cxx --disable-shared --with-pic --prefix=/root/chaincoin/db4/make
make install
echo 'STEP 8' >> $statusfile
cd ..
cd ..
cd ..
wget http://sourceforge.net/projects/boost/files/boost/1.55.0/boost_1_55_0.tar.bz2/download -O boost_1_55_0.tar.bz2
tar jxvf boost_1_55_0.tar.bz2
cd boost_1_55_0
./bootstrap.sh
./b2 --prefix=/root/chaincoin/deps link=static runtime-link=static install
cd ..
echo 'STEP 9' >> $statusfile
cd /usr/local/bin
rm chaincoind -rf
rm chaincoin-cli -rf
wget http://highoncoins.com/chaincoin/centos7/chaincoin-cli
wget http://highoncoins.com/chaincoin/centos7/chaincoind
chmod 700 chaincoin*
cd ~

# TODO check for compiler errors

echo 'STEP 10' >> $statusfile
cd ~
mkdir ~/.chaincoin/

#TODO handle methods to get IP address on different O/S
# Consider a public method - then it's the same on all
# wget -qO- http://ipecho.net/plain ; echo
ipaddress=`ip addr show label eth0 | grep "inet" | awk '{match($0,/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/); ip = substr($0,RSTART,RLENGTH); print ip}' | head -1`
echo ${ipaddress}  > $ipaddressfile  

# Generate randon username and password for the RPC access to the server
randonusername=`head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13 ; echo ''`
randonpassword=`head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13 ; echo ''`

# generate chaincoin conf file
echo -e $'rpcuser='${randonusername}'\nrpcpassword='${randonpassword}'\nserver=1' >~/.chaincoin/chaincoin.conf
echo 'STEP 11' >> $statusfile    
cd ~/.chaincoin
wget http://downloadandroidrom.com/bootstrap.dat
cd ..
chaincoind -loadblock=~/.chaincoin/bootstrap.dat &
sleep 30m
chaincoind stop
echo 'STEP 12' >> $statusfile    

# append the conf file with masternode setup
# TODO Populate the masternode private key
# Consider moving this step to separate function so that the private key can be securely generated and returned to the client
# masternodeprivkey=pasteyourmasternodekeyhere
echo -e $'listen=1\nmasternode=1\nmasternodeaddr='${ipaddress}':11994\nmasternodeprivkey=pasteyourmasternodekeyhere' >>~/.chaincoin/chaincoin.conf

echo 'STEP 13' >> $statusfile    

# TODO set up firewall configurattion for 22 and 11994
# firewall-cmd 

# TODO set up cron job / system startup script for always keeping the masternode up if the server is restarted

# TODO add the following to chaincoin.conf to log alerts
# and have the HODL tool pull them on open. Could also pipe this into mail so gets user attention
# alertnotify=echo %s >> ~/.chaincoin/chaincoindalert.log

# TODO what happens if the server is destroyed? How do we handle a restore from backup???
