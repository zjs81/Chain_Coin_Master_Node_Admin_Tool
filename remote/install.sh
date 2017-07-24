#!/bin/bash

# TODO Logic for determining OS and choosing the right yum/atp commands

statusfile=~/hodladmin/status.log
touch $statusfile  
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
echo 'STEP 5' >> $statusfile
export CFLAGS="-fPIC"
./config --prefix=/opt/openssl --openssldir=/opt/openssl enable-ec enable-ecdh enable-ecdsa -fPIC shared
make all
make install
cd ~
mkdir chaincoin
echo 'STEP 6' >> $statusfile
cd ~/chaincoin
wget http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz
mkdir db4
cd db4
tar xvf ../db-4.8.30.NC.tar.gz
cd db-4.8.30.NC/build_unix/
../dist/configure --enable-cxx --disable-shared --with-pic --prefix=/root/chaincoin/db4/make
make install
echo 'STEP 7' >> $statusfile
cd ..
cd ..
cd ..
wget http://sourceforge.net/projects/boost/files/boost/1.55.0/boost_1_55_0.tar.bz2/download -O boost_1_55_0.tar.bz2
tar jxvf boost_1_55_0.tar.bz2
cd boost_1_55_0
./bootstrap.sh
./b2 --prefix=/root/chaincoin/deps link=static runtime-link=static install
cd ..
echo 'STEP 8' >> $statusfile
cd /usr/local/bin
rm chaincoind -rf
rm chaincoin-cli -rf
wget http://highoncoins.com/chaincoin/centos7/chaincoin-cli
wget http://highoncoins.com/chaincoin/centos7/chaincoind
chmod 700 chaincoin*
cd ~

echo 'STEP 9' >> $statusfile
cd ~
mkdir ~/.chaincoin/
cd ~/.chaincoin/
# TODO pull public ip address to populate the file
# Public methods
# wget -qO- http://ipecho.net/plain ; echo
# dig +short myip.opendns.com @resolver1.opendns.com

#ipaddress=LANG=c ifconfig eth0 | grep "inet addr" | awk -F: '{print $2}' | awk '{print $1}'
#echo 'IP=${ipaddress}'  >> $statusfile  
echo $'rpcuser=username\nrpcpassword=somepassword\nserver=1\nlisten=1\nmasternode=1\nmasternodeaddr=PutyourIPADDRESSHERE:11994' >chaincoin.conf
echo 'STEP 10' >> $statusfile    
cd ~/.chaincoin
wget http://downloadandroidrom.com/bootstrap.dat
chaincoind -loadblock=bootstrap.dat
chaincoind stop
echo 'STEP 11' >> $statusfile    
# set up firewall configurattion for 22 and 11994
# set up cron job for always keeping the masternode up..
