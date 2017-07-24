#!/bin/bash

#TODO check status of the masternode to determine what needs to be done.

cd ~/hodladmin
curl -O https://raw.githubusercontent.com/zjs81/Chain_Coin_Master_Node_Admin_Tool/master/remote/install.sh
curl -O https://raw.githubusercontent.com/zjs81/Chain_Coin_Master_Node_Admin_Tool/master/remote/checkstatus.sh
chmod +x checkstatus.sh
chmod +x install.sh

# check for admin tool status file and check the status 
# create a status file if needed
# return the status of the bootstrap process to the client so it can show the correct UI
