import os
import sys
import PyQt5
import csv
import datetime
import winsound
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from assignlist import assignmentObject
#from time import *
from mainmenu4 import today
#import threading


assignmentsObjectList = []
dirName = os.path.dirname(os.path.abspath(__file__))
csvName = os.path.join(dirName, 'daCSV.csv')

dueTomorrow = []
today = datetime.datetime.today()

if (os.path.exists(csvName)):
    with open(csvName,'r')as f:
        csvFile = csv.reader(f)
        next(csvFile,None)
        for lines in csvFile:
            csvName = lines[0]
            csvDays = datetime.datetime.strptime(lines[1], '%Y-%m-%d %H:%M:%S')
            assignmentsObjectList.append(assignmentObject(csvName,csvDays))

for x in assignmentsObjectList:
    targetDays = x.day - today
    #listString = x.name + ' - in ' + str(targetDays.days) +' day(s).' 
    if (int(targetDays.days) <= 2):
        dueTomorrow.append(x.name)



    
"""
def countdown():
    print (str(today.day))
    startCountdown()

def startCountdown():
    countdown_thread = threading.Timer(3, countdown)
    countdown_thread.daemon = True
    countdown_thread.start()

startCountdown()
"""
class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self,icon,parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self,icon,parent)
        self.setToolTip('TimeUp')
        menu = QtWidgets.QMenu(parent)

        exitApp = menu.addAction('Exit')
        #t.cancel()
        exitApp.triggered.connect(lambda:sys.exit())

        self.setContextMenu(menu)
        self.activated.connect(self.trayActivate)

    
    def trayActivate(self, reason):
        if reason == self.DoubleClick:
            window = startWindow()
    
def startWindow():
    from mainmenu4 import Ui_MainWindow
    import sys
    global daWindow
    global ui
    daWindow = QtWidgets.QMainWindow()

    daStyle="""
        QWidget{
            background: #fff280;
        }
        QListWidget#listAssignments{
            background: #fff7ad;
            border: 1px solid;
        }
        QLineEdit#lineName{
            background: #fff7ad;
            border: 1px solid;
        }
        QSpinBox#spinDays,QSpinBox#spinHour{
            background: #fff7ad;
            border: 1px solid;
            padding-right: 15px;
        }

        QPushButton#buttonAdd, QPushButton#buttonDelete, QPushButton#buttonAbout{
            background: #fff7ad;
            border: 1px solid;
        }
        QPushButton#buttonAdd:hover, QPushButton#buttonDelete:hover, QPushButton#buttonAbout:hover{
            background: #ffffff;
        }
        QPushButton#buttonAdd:pressed, QPushButton#buttonDelete:pressed, QPushButton#buttonAbout:pressed{
            color: white;
            background: #302d0b;
        }
        """
    daWindow.setStyleSheet(daStyle)

    ui = Ui_MainWindow()
    dirName = os.path.dirname(os.path.abspath(__file__))
    ui.csvName = os.path.join(dirName, 'daCSV.csv')
    ui.assignmentsObjectList = assignmentsObjectList
    ui.setupUi(daWindow)
    ui.refreshList()
    daWindow.show()

    return daWindow

def trayMain():
    trayApp = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    trayApp.setQuitOnLastWindowClosed(False)

    dirName=os.path.dirname(os.path.abspath(__file__))
    iconPath = os.path.join(dirName, 'icon.png')
    trayIcon = SystemTrayIcon(QtGui.QIcon(iconPath),w)
    trayIcon.show()
    """
    print ('setting up main window and hiding it.')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.refreshList()
    MainWindow.hide()
    """
    #mainmenu4.runMain()
    def threading_sound():
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

    def messageBox():
        msg = QtWidgets.QMessageBox()
        msgStyle = """
            QMessageBox{
                background: #fff7ad;
            }
            """
        msg.setStyleSheet(msgStyle)
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setText('Have you done these?')
        msg.setWindowTitle('TimeUp: Reminder')

        dirName=os.path.dirname(os.path.abspath(__file__))
        iconPath = os.path.join(dirName, 'icon.png')
        msg.setWindowIcon(QtGui.QIcon(iconPath)) 
        #msg.setMinimumSize(QtCore.QSize(940,240))
        tempText = ''
        for x in dueTomorrow:
            tempText = tempText + x + '\n'
        msg.setInformativeText(tempText)
        msg.setStandardButtons(QtWidgets.QMessageBox.Close)

        msgBox = msg.exec_()
    
    if (len(dueTomorrow) > 0):
        dialogSound =  threading.Thread(target=threading_sound)
        dialogSound.start()
        messageBox()
    
    sys.exit(trayApp.exec_())

if __name__ == '__main__':
    
    trayMain()

"""
xdate=datetime.today()
ydate=timedelta(0,10)

print (xdate)
print (ydate)
delta_t=xdate + ydate

print (delta_t)
secs= delta_t - xdate

def hello_world():
    print ('hello world')

#print (secs)

t = Timer(5,hello_world())
"""