# HODL Admin - Chaincoin Masternode manager
HODL Admin is a tool that helps you manage your Chaincoin masternodes. Install your masternode, monitor your masternode, and most importantly, HODL.


## Features
* Provides easy to run commands to install, manage, monitor and maintain your masternode, saving you time and learning required to set up.
* No additional software needs to be installed on the masternode reducing the potential for attack so it's more secure.
* No additional ports needs to be opened, it uses the SSH port just like you need to use anyway, reducing the potential for attack so it's more secure.
* No confidential information is stored on the masternode, making it more secure.

## Prequeuisties
1. Spin up a VPS server on Vultr, Linode, Digital Ocean, AWS, or any other reputable provider - link to instructions elsewhere?
 * Make sure you get at least XXGB space and XXCPU - typically $5 per month
 * Also choose automatic daily backups. Typically $1 per month
2. Once you have the IP address and the root password, test ssh into the machine

 `ssh root@<insert-your-ip-here>`

3. Enter your password when promped. You should see a message after you successfully login
Welcome to Ubuntu 14.04.5 LTS (GNU/Linux 3.13.0-123-generic x86_64)
[root@hostname ~]


## HODL Admin Installation
1. Install Python 2.7.13 on your Mac or Windows machine, this is the basic framework that supports the admin tool.

  [Mac OS X](https://www.python.org/ftp/python/2.7.13/python-2.7.13-macosx10.6.pkg)

  [Windows 32 bit](https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi)

  [Windows 64 bit](https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi)

2. Open up the terminal and run the admin executable by running the following commands (need to change to not install libraries if already installed)

  **Mac OS X**
  ```
  mkdir hodladmin
  cd hodladmin
  curl -O https://raw.githubusercontent.com/zjs81/Chain_Coin_Master_Node_Admin_Tool/master/hodl.sh
  curl -O https://raw.githubusercontent.com/zjs81/Chain_Coin_Master_Node_Admin_Tool/master/t.py
  curl -O https://raw.githubusercontent.com/zjs81/Chain_Coin_Master_Node_Admin_Tool/master/login.py
 chmod +x ./hodl.sh
  ./hodl.sh
  ```
  
  *Enter password when prompted*

  **Windows**

  To be written
  download this XXX
  double click hodl.bat

3. When you run this command again, run

  **Mac OS X**

  ```
  cd hodladmin
  .//hodl.sh
  ```