# Chain_Coin_Master_Node_Admin_Tool
Chain coin masternode manager 


*Features of the admin tool*
* Provides easy to run install process and monitoring for your masternode saving you time and learning required to set up.
* Everything runs from the your client PC/MAC using SSH. No extra ports need to be open such as webserver port 80/993. Only masternode 11994 and SSH 22 are required to be open. More secure.
* No extra software to install on the masternode. This makes the potential for attack much lower. More secure.
* No personal information is stored in a database or locally on the filesystem. More secure.

*Prequeuisties*
1. Set up a VPS server on Vultr, Linode, Digital Ocean, AWS, or any other reputable provider
* Make sure you get at least XXGB space and XXCPU - typically $5 per month
* Also choose automatic backups.
2. Once you have the IP address and the root password, test ssh into the machine

example here

3. Optional - set up ssh key based access.


HODL Admin Installation
1. Install python on your Mac or Windows machine, this is the basic framework that supports the admin tool.

Mac OS X
https://www.python.org/ftp/python/2.7.13/python-2.7.13-macosx10.6.pkg

Windows - 32bit
https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi

Windows - 64bit
https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi

2. Run the HODL Admin (note this will install a python GUI framework if not installed the first time)
_Note we could put this in a script and bat file_
curl -O https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo pip install appJar

