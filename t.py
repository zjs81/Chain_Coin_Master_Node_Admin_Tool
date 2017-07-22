from appJar import gui
import sys

keyfilename = ""
keyfileinuse = False
port = sys.argv[4]
ip = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
#The stuff above takes args from login.py
balance = 0
#Gets balance
app = gui("HODLER ADMIN", "400x200")


app.setFont(10)
app.addLabelOptionBox("Options", ["File","Install MasterNode"])

print port, ip, username, password
app.go()
