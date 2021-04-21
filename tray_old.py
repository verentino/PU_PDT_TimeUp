import os
import sys
from PyQt5 import QtGui, QtWidgets

"""
from datetime import datetime,timedelta
from threading import Timer
"""
print('poggo')
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
    ui = Ui_MainWindow()
    ui.setupUi(daWindow)
    ui.refreshList()
    daWindow.show()

    return daWindow

def trayMain():
    from mainmenu4 import Ui_MainWindow
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