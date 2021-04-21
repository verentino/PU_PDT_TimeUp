# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os.path

from assignlist import assignmentObject
import csv
import datetime

today = datetime.datetime.today()
"""
assignmentsObjectList = []


dirName = os.path.dirname(os.path.abspath(__file__))
csvName = os.path.join(dirName, 'daCSV.csv')

if (os.path.exists(csvName)):
    with open(csvName,'r')as f:
        csvFile = csv.reader(f)
        next(csvFile,None)
        for lines in csvFile:
            csvName = lines[0]
            csvDays = datetime.datetime.strptime(lines[1], '%Y-%m-%d').date()
            assignmentsObjectList.append(assignmentObject(csvName,csvDays))
"""
class Ui_MainWindow(object):
    def __init__(self):
        self.selectedRow = 0
    def clickAbout(self):
        dialog = QtWidgets.QMessageBox()
        diaStyle = """
            QMessageBox{
                background: #fff7ad;
            }
            """
        dirName=os.path.dirname(os.path.abspath(__file__))
        iconPath = os.path.join(dirName, 'icon.png')
        dialog.setWindowIcon(QtGui.QIcon(iconPath)) 

        dialog.setStyleSheet(diaStyle)
        dialog.setText('Made for PDT; by Bayu, Kevin, Fitra and Reinardus')
        dialog.setWindowTitle('About')
        dialog.exec()

    def clickAdd(self):
        tempDays = today + datetime.timedelta(days=self.spinDays.value())
        #, hours=self.spinHour.value()
        combinedDate = datetime.datetime.combine(tempDays.date(),datetime.time(self.spinHour.value(),0))
        self.assignmentsObjectList.append(assignmentObject(self.lineName.text(),combinedDate))

        self.lineName.setText('')
        self.spinDays.setValue(1)
        self.spinHour.setValue(0)
        self.refreshList()

    def refreshList(self):
        self.listAssignments.clear()
        assFields = ['Name','Days']
        assRows = []

        for x in self.assignmentsObjectList:
            targetDays = x.day - today
            if targetDays.days < 0:
                listString = x.name + ' - late.'
            elif targetDays.days < 1:
                
                diffDatetime = x.day - today
                hoursLeft = diffDatetime.seconds//3600
                minutesLeft = (diffDatetime.seconds%3600)//60
                
                listString = x.name + ' - in ' + str(hoursLeft) +' hour(s), '+str(minutesLeft)+' minute(s).'
            else:
                listString = x.name + ' - in ' + str(targetDays.days) +' day(s).'
            tempList = [x.name,x.day]
            assRows.append(tempList)
            self.listAssignments.addItem(listString)
        
        
        with open(self.csvName, 'w', newline='') as g:
            write = csv.writer(g)

            write.writerow(assFields)
            write.writerows(assRows)
        #assDF = pd.DataFrame(assDict)
        #assDF.to_csv('daCSV.csv')

    def listSelected(self,item):
        self.selectedRow = self.listAssignments.row(item)
        #self.listAssignments.

    def clickDelete(self):
        if len(self.assignmentsObjectList) != 0:
            self.assignmentsObjectList.pop(self.selectedRow)
            self.selectedRow = 0
            self.refreshList()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setFixedSize(498, 385)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listAssignments = QtWidgets.QListWidget(self.centralwidget)
        self.listAssignments.setGeometry(QtCore.QRect(10, 120, 371, 221))
        self.listAssignments.setObjectName("listAssignments")
        
        self.buttonDelete = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDelete.setGeometry(QtCore.QRect(390, 120, 101, 41))
        self.buttonDelete.setObjectName("buttonDelete")

        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAdd.setGeometry(QtCore.QRect(390, 30, 101, 41))
        self.buttonAdd.setObjectName("buttonAdd")

        self.lineName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineName.setGeometry(QtCore.QRect(10, 30, 231, 41))
        self.lineName.setObjectName("lineName")

        self.spinDays = QtWidgets.QSpinBox(self.centralwidget)
        self.spinDays.setGeometry(QtCore.QRect(251, 30, 61, 41))
        self.spinDays.setMinimum(1)
        self.spinDays.setMaximum(255)
        self.spinDays.setObjectName("spinDays")

        self.spinHour = QtWidgets.QSpinBox(self.centralwidget)
        self.spinHour.setGeometry(QtCore.QRect(321, 30, 61, 41))
        self.spinHour.setMinimum(0)
        self.spinHour.setMaximum(23)
        self.spinHour.setObjectName("spinHour")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 5, 301, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 5, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 371, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 5, 61, 21))
        self.label_4.setObjectName("label_4")
        self.buttonAbout = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAbout.setGeometry(QtCore.QRect(390, 300, 101, 41))
        self.buttonAbout.setObjectName("buttonAbout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #my code
        self.buttonAbout.clicked.connect(self.clickAbout)
        self.buttonAdd.clicked.connect(self.clickAdd)
        self.listAssignments.itemClicked.connect(self.listSelected)
        self.buttonDelete.clicked.connect(self.clickDelete)
        #end code

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TimeUp"))
        
        dirName=os.path.dirname(os.path.abspath(__file__))
        iconPath = os.path.join(dirName, 'icon.png')
        MainWindow.setWindowIcon(QtGui.QIcon(iconPath)) 
        
        self.buttonDelete.setText(_translate("MainWindow", "Delete"))
        self.buttonAdd.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "Assignment Name"))
        self.label_2.setText(_translate("MainWindow", "Days"))
        self.label_3.setText(_translate("MainWindow", "Assignment List"))
        self.label_4.setText(_translate("MainWindow", "Hour"))
        self.buttonAbout.setText(_translate("MainWindow", "About"))

def runMain():
    """
    import sys
    print ('safe')
    app = QtWidgets.QApplication(sys.argv)
    print ('victory.')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.refreshList()
    MainWindow.show()
    sys.exit(app.exec_())
    """


if __name__ == "__main__":
    import sys

    assignmentsObjectList = []


    dirName = os.path.dirname(os.path.abspath(__file__))
    csvName = os.path.join(dirName, 'daCSV.csv')

    if (os.path.exists(csvName)):
        with open(csvName,'r')as f:
            csvFile = csv.reader(f)
            next(csvFile,None)
            for lines in csvFile:
                csvName = lines[0]
                csvDays = datetime.datetime.strptime(lines[1], '%Y-%m-%d %H:%M:%S')
                assignmentsObjectList.append(assignmentObject(csvName,csvDays))

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    dirName = os.path.dirname(os.path.abspath(__file__))
    ui.csvName = os.path.join(dirName, 'daCSV.csv')
    ui.assignmentsObjectList = assignmentsObjectList
    ui.setupUi(MainWindow)
    ui.refreshList()
    MainWindow.show()
    sys.exit(app.exec_())
