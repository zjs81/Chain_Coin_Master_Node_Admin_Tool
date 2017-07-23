from appJar import gui
import os
keyfilename = ""
keyfileinuse = False
app = gui("HODLER ADMIN")
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        ip = app.getEntry("IP")
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        port = app.getEntry("Port")
        command = ("python t.py ") + ip +" " + usr + " " + pwd + " " + port
        #app.okBox("alert", "Trying to connect to the server.")
        os.system(command)

def keyfile(button):
    global keyfilename
    global keyfileinuse
    keyfilename = app.openBox(title=None, dirName=None, fileTypes=None, asFile=False)
    if(keyfilename == ""):
        pass
    else:
        keyfileinuse = True
    print keyfileinuse
    print keyfilename
app = gui("Login Window")


app.setSticky("ew")
app.setFont(20)

app.startLabelFrame("Remote Login Details")
app.addLabel("l1", "IP", 0, 0)
app.addEntry("IP", 0, 1)
app.addLabel("l2", "Port", 1, 0)
app.addEntry("Port", 1, 1)
app.addLabel("l4", "Username", 2, 0)
app.addEntry("Username", 2, 1)
app.addLabel("l3", "Password", 3, 0)
app.addSecretEntry("Password", 3, 1)
app.addButtons(["Submit", "Cancel"], press, 4, 0, 4)
#app.addButtons(["Add ssh key file"], keyfile, 5, 0, 5)
app.stopLabelFrame()
app.go()
