# -*- coding: utf-8 -*-
# python 3.8.7

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import economy


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.namn = QtWidgets.QLabel(self.centralwidget)
        self.namn.setGeometry(QtCore.QRect(340, 10, 41, 31))
        self.namn.setObjectName("namn")
        self.profilNamn = QtWidgets.QLabel(self.centralwidget)
        self.profilNamn.setGeometry(QtCore.QRect(390, 10, 131, 31))
        self.profilNamn.setObjectName("profilNamn")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 521, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.sparaDatum = QtWidgets.QPushButton(self.tab)
        self.sparaDatum.setGeometry(QtCore.QRect(184, 350, 81, 23))
        self.sparaDatum.setObjectName("sparaDatum")
        self.nyUtgift = QtWidgets.QLabel(self.tab)
        self.nyUtgift.setGeometry(QtCore.QRect(20, 240, 71, 20))
        self.nyUtgift.setObjectName("nyUtgift")
        self.nastaLon = QtWidgets.QLabel(self.tab)
        self.nastaLon.setGeometry(QtCore.QRect(90, 320, 61, 20))
        self.nastaLon.setObjectName("nastaLon")
        self.nastaLonEdit = QtWidgets.QDateEdit(self.tab)
        self.nastaLonEdit.setGeometry(QtCore.QRect(164, 320, 111, 22))

        # get year, month and day before setting them when opening the application
        nSDYear, nSDMonth, nSDDay = self.read_nSD(person)

        self.nastaLonEdit.setDate(QtCore.QDate(nSDYear, nSDMonth, nSDDay))
        self.nastaLonEdit.setObjectName("nastaLonEdit")
        self.inkomstWidget = QtWidgets.QTreeWidget(self.tab)
        self.inkomstWidget.setGeometry(QtCore.QRect(20, 20, 261, 111))
        self.inkomstWidget.setObjectName("inkomstWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.inkomstWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.inkomstWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.inkomstWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.inkomstWidget)
        self.utgiftEdit = QtWidgets.QLineEdit(self.tab)
        self.utgiftEdit.setGeometry(QtCore.QRect(92, 240, 81, 20))
        self.utgiftEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.utgiftEdit.setObjectName("utgiftEdit")
        self.inkomstEdit = QtWidgets.QLineEdit(self.tab)
        self.inkomstEdit.setGeometry(QtCore.QRect(92, 160, 81, 20))
        self.inkomstEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.inkomstEdit.setObjectName("inkomstEdit")
        self.sparaInkomst = QtWidgets.QPushButton(self.tab)
        self.sparaInkomst.setGeometry(QtCore.QRect(190, 190, 81, 23))
        self.sparaInkomst.setObjectName("sparaInkomst")
        self.utgiftKategori = QtWidgets.QComboBox(self.tab)
        self.utgiftKategori.setGeometry(QtCore.QRect(180, 240, 101, 22))
        self.utgiftKategori.setObjectName("utgiftKategori")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.utgiftKategori.addItem("")
        self.nyInkomst = QtWidgets.QLabel(self.tab)
        self.nyInkomst.setGeometry(QtCore.QRect(20, 160, 71, 20))
        self.nyInkomst.setObjectName("nyInkomst")
        self.utgiftWidget = QtWidgets.QTreeWidget(self.tab)
        self.utgiftWidget.setGeometry(QtCore.QRect(290, 20, 211, 361))
        self.utgiftWidget.setObjectName("utgiftWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.utgiftWidget)
        self.inkomstKategori = QtWidgets.QComboBox(self.tab)
        self.inkomstKategori.setGeometry(QtCore.QRect(180, 160, 101, 22))
        self.inkomstKategori.setObjectName("inkomstKategori")
        self.inkomstKategori.addItem("")
        self.inkomstKategori.addItem("")
        self.inkomstKategori.addItem("")
        self.inkomstKategori.addItem("")
        self.sparaUtgift = QtWidgets.QPushButton(self.tab)
        self.sparaUtgift.setGeometry(QtCore.QRect(190, 270, 81, 23))
        self.sparaUtgift.setObjectName("sparaUtgift")
        self.totalUtgift = QtWidgets.QLabel(self.tab)
        self.totalUtgift.setGeometry(QtCore.QRect(290, 390, 81, 31))
        self.totalUtgift.setObjectName("totalUtgift")
        self.totUtg = QtWidgets.QLabel(self.tab)
        self.totUtg.setGeometry(QtCore.QRect(370, 390, 81, 31))
        self.totUtg.setObjectName("totUtg")
        self.totalInkomst = QtWidgets.QLabel(self.tab)
        self.totalInkomst.setGeometry(QtCore.QRect(20, 390, 81, 31))
        self.totalInkomst.setObjectName("totalInkomst")
        self.totInk = QtWidgets.QLabel(self.tab)
        self.totInk.setGeometry(QtCore.QRect(110, 390, 81, 31))
        self.totInk.setObjectName("totInk")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.kvarAvLon = QtWidgets.QLabel(self.tab_2)
        self.kvarAvLon.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.kvarAvLon.setObjectName("kvarAvLon")
        self.kvarAvLonProcent = QtWidgets.QProgressBar(self.tab_2)
        self.kvarAvLonProcent.setGeometry(QtCore.QRect(10, 40, 231, 21))
        self.kvarAvLonProcent.setProperty("value", 24)
        self.kvarAvLonProcent.setObjectName("kvarAvLonProcent")
        self.kvarPerDag = QtWidgets.QLabel(self.tab_2)
        self.kvarPerDag.setGeometry(QtCore.QRect(10, 80, 121, 21))
        self.kvarPerDag.setObjectName("kvarPerDag")
        self.kvarPerDag_2 = QtWidgets.QLabel(self.tab_2)
        self.kvarPerDag_2.setGeometry(QtCore.QRect(140, 80, 91, 21))
        self.kvarPerDag_2.setObjectName("kvarPerDag_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menyOpen = QtWidgets.QMenu(self.menuFile)
        self.menyOpen.setStatusTip("")
        self.menyOpen.setObjectName("menyOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSpara = QtWidgets.QAction(MainWindow)
        self.actionSpara.setObjectName("actionSpara")
        self.actionAvsluta = QtWidgets.QAction(MainWindow)
        self.actionAvsluta.setObjectName("actionAvsluta")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionJasmine = QtWidgets.QAction(MainWindow)
        self.actionJasmine.setObjectName("actionJasmine")
        self.actionAll = QtWidgets.QAction(MainWindow)
        self.actionAll.setObjectName("actionAll")
        self.actionNy = QtWidgets.QAction(MainWindow)
        self.actionNy.setObjectName("actionNy")
        self.actionJasmine = QtWidgets.QAction(MainWindow)
        self.actionJasmine.setObjectName("actionJasmine")
        self.actionSamuel = QtWidgets.QAction(MainWindow)
        self.actionSamuel.setObjectName("actionSamuel")
        self.actionNytt = QtWidgets.QAction(MainWindow)
        self.actionNytt.setObjectName("actionNytt")
        self.menyOpen.addAction(self.actionAll)
        self.menyOpen.addAction(self.actionJasmine)
        self.menyOpen.addAction(self.actionSamuel)
        self.menuFile.addAction(self.actionSpara)
        self.menuFile.addAction(self.actionNytt)
        self.menuFile.addAction(self.menyOpen.menuAction())
        self.menuFile.addAction(self.actionAvsluta)
        self.menubar.addAction(self.menuFile.menuAction())

        # connect button to function
        self.sparaDatum.pressed.connect(lambda: self.save_nSD(economy.read_line('person.txt', 0)))
        self.actionSamuel.triggered.connect(lambda: self.setPerson('Samuel'))
        self.actionJasmine.triggered.connect(lambda: self.setPerson('Jasmine'))

        self.sparaInkomst.pressed.connect(lambda: self.save_income(economy.read_line('person.txt', 0)))
        self.sparaUtgift.pressed.connect(lambda: self.save_expense(economy.read_line('person.txt', 0)))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.inkomstEdit)
        MainWindow.setTabOrder(self.inkomstEdit, self.inkomstKategori)
        MainWindow.setTabOrder(self.inkomstKategori, self.sparaInkomst)
        MainWindow.setTabOrder(self.sparaInkomst, self.utgiftEdit)
        MainWindow.setTabOrder(self.utgiftEdit, self.utgiftKategori)
        MainWindow.setTabOrder(self.utgiftKategori, self.sparaUtgift)
        MainWindow.setTabOrder(self.sparaUtgift, self.nastaLonEdit)
        MainWindow.setTabOrder(self.nastaLonEdit, self.sparaDatum)
        MainWindow.setTabOrder(self.sparaDatum, self.inkomstWidget)
        MainWindow.setTabOrder(self.inkomstWidget, self.utgiftWidget)

        self.show_income(economy.read_line('person.txt', 0))
        self.show_expense(economy.read_line('person.txt', 0))
        self.show_totIncome(economy.read_line('person.txt', 0))
        self.show_totExpense(economy.read_line('person.txt', 0))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Min Ekonomi"))
        self.namn.setText(_translate("MainWindow", "Namn:"))
        self.profilNamn.setText(_translate("MainWindow", person))
        self.sparaDatum.setText(_translate("MainWindow", "Spara Datum"))
        self.nyUtgift.setText(_translate("MainWindow", "Ny Utgift:"))
        self.nastaLon.setText(_translate("MainWindow", "Nästa Lön:"))
        self.inkomstWidget.headerItem().setText(0, _translate("MainWindow", "Kategorier"))
        self.inkomstWidget.headerItem().setText(1, _translate("MainWindow", "Inkomster"))
        __sortingEnabled = self.inkomstWidget.isSortingEnabled()
        self.inkomstWidget.setSortingEnabled(False)
        self.inkomstWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Lön"))
        self.inkomstWidget.topLevelItem(0).setText(1, _translate("MainWindow", "0000"))
        self.inkomstWidget.topLevelItem(1).setText(0, _translate("MainWindow", "CSN"))
        self.inkomstWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Presenter"))
        self.inkomstWidget.topLevelItem(3).setText(0, _translate("MainWindow", "Annat"))
        self.inkomstWidget.setSortingEnabled(__sortingEnabled)
        self.sparaInkomst.setText(_translate("MainWindow", "Lägg till"))
        self.utgiftKategori.setItemText(0, _translate("MainWindow", "Hyra"))
        self.utgiftKategori.setItemText(1, _translate("MainWindow", "Abonnemang"))
        self.utgiftKategori.setItemText(2, _translate("MainWindow", "Resor - Långa"))
        self.utgiftKategori.setItemText(3, _translate("MainWindow", "Resor - Korta"))
        self.utgiftKategori.setItemText(4, _translate("MainWindow", "Mat - Mat"))
        self.utgiftKategori.setItemText(5, _translate("MainWindow", "Mat - Mat ute"))
        self.utgiftKategori.setItemText(6, _translate("MainWindow", "Mat - Sötsug"))
        self.utgiftKategori.setItemText(7, _translate("MainWindow", "Skolrelaterat"))
        self.utgiftKategori.setItemText(8, _translate("MainWindow", "Inredning"))
        self.utgiftKategori.setItemText(9, _translate("MainWindow", "Kläder"))
        self.utgiftKategori.setItemText(10, _translate("MainWindow", "Spel"))
        self.utgiftKategori.setItemText(11, _translate("MainWindow", "Elektronik"))
        self.utgiftKategori.setItemText(12, _translate("MainWindow", "Smink/Bad"))
        self.utgiftKategori.setItemText(13, _translate("MainWindow", "Medicin"))
        self.utgiftKategori.setItemText(14, _translate("MainWindow", "Alkohol"))
        self.utgiftKategori.setItemText(15, _translate("MainWindow", "Sparande"))
        self.utgiftKategori.setItemText(16, _translate("MainWindow", "Presenter"))
        self.utgiftKategori.setItemText(17, _translate("MainWindow", "Övrigt"))
        self.nyInkomst.setText(_translate("MainWindow", "Ny Inkomst:"))
        self.utgiftWidget.headerItem().setText(0, _translate("MainWindow", "Kategorier"))
        self.utgiftWidget.headerItem().setText(1, _translate("MainWindow", "Utgifter"))
        __sortingEnabled = self.utgiftWidget.isSortingEnabled()
        self.utgiftWidget.setSortingEnabled(False)
        self.utgiftWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Hyra"))
        self.utgiftWidget.topLevelItem(0).setText(1, _translate("MainWindow", "0000"))
        self.utgiftWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Abonnemang"))
        self.utgiftWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Resor"))
        self.utgiftWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "Långa"))
        self.utgiftWidget.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "Korta"))
        self.utgiftWidget.topLevelItem(3).setText(0, _translate("MainWindow", "Mat"))
        self.utgiftWidget.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "Mat"))
        self.utgiftWidget.topLevelItem(3).child(1).setText(0, _translate("MainWindow", "Mat ute"))
        self.utgiftWidget.topLevelItem(3).child(2).setText(0, _translate("MainWindow", "Sötsug"))
        self.utgiftWidget.topLevelItem(4).setText(0, _translate("MainWindow", "Skolrelaterat"))
        self.utgiftWidget.topLevelItem(5).setText(0, _translate("MainWindow", "Inredning"))
        self.utgiftWidget.topLevelItem(6).setText(0, _translate("MainWindow", "Kläder"))
        self.utgiftWidget.topLevelItem(7).setText(0, _translate("MainWindow", "Spel"))
        self.utgiftWidget.topLevelItem(8).setText(0, _translate("MainWindow", "Elektronik"))
        self.utgiftWidget.topLevelItem(9).setText(0, _translate("MainWindow", "Smink/Bad"))
        self.utgiftWidget.topLevelItem(10).setText(0, _translate("MainWindow", "Medicin"))
        self.utgiftWidget.topLevelItem(11).setText(0, _translate("MainWindow", "Alkohol"))
        self.utgiftWidget.topLevelItem(12).setText(0, _translate("MainWindow", "Sparande"))
        self.utgiftWidget.topLevelItem(13).setText(0, _translate("MainWindow", "Presenter"))
        self.utgiftWidget.topLevelItem(14).setText(0, _translate("MainWindow", "Övrigt"))
        self.utgiftWidget.setSortingEnabled(__sortingEnabled)
        self.inkomstKategori.setItemText(0, _translate("MainWindow", "Lön"))
        self.inkomstKategori.setItemText(1, _translate("MainWindow", "CSN"))
        self.inkomstKategori.setItemText(2, _translate("MainWindow", "Presenter"))
        self.inkomstKategori.setItemText(3, _translate("MainWindow", "Annat"))
        self.sparaUtgift.setText(_translate("MainWindow", "Lägg till"))
        self.totalUtgift.setText(_translate("MainWindow", "Totala utgifter:"))
        self.totUtg.setText(_translate("MainWindow", "0000"))
        self.totalInkomst.setText(_translate("MainWindow", "Totala inkomster:"))
        self.totInk.setText(_translate("MainWindow", "0000"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Huvudtab"))
        self.kvarAvLon.setText(_translate("MainWindow", "Kvar av lön:"))
        self.kvarPerDag.setText(_translate("MainWindow", "Kvar per dag till ny lön:"))
        self.kvarPerDag_2.setText(_translate("MainWindow", "240 kr/dag"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Grafer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menyOpen.setTitle(_translate("MainWindow", "Öppna"))
        self.actionSpara.setText(_translate("MainWindow", "Spara"))
        self.actionSpara.setStatusTip(_translate("MainWindow", "Spara fil"))
        self.actionSpara.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAvsluta.setText(_translate("MainWindow", "Avsluta"))
        self.actionAvsluta.setStatusTip(_translate("MainWindow", "Avsluta program"))
        self.actionDelete.setText(_translate("MainWindow", "Radera"))
        self.actionDelete.setStatusTip(_translate("MainWindow", "Delete current file"))
        self.actionAll.setText(_translate("MainWindow", "All"))
        self.actionNy.setText(_translate("MainWindow", "Ny"))
        self.actionJasmine.setText(_translate("MainWindow", "Jasmine"))
        self.actionSamuel.setText(_translate("MainWindow", "Samuel"))
        self.actionNytt.setText(_translate("MainWindow", "Ny person"))
    

    def save_nSD(self, person):
        # save new salary date from ui
        newDate = self.nastaLonEdit.date()
        newDate = newDate.toPyDate()      
        economy.add_newSalaryDate(person, newDate)


    def read_nSD(self, person):
        # get date from database, unless person is new. Then set to 1970-01-01.
        nSD = economy.read_newSalaryDate(person)
        nSD = nSD[0].split('-')
        try:
            nSDYear = int(nSD[0])
            nSDMonth = int(nSD[1])
            nSDDay = int(nSD[2])
        except:
            nSDYear = 1970
            nSDMonth = 1
            nSDDay = 1
        return nSDYear, nSDMonth, nSDDay


    def setPerson(self, person):
        economy.create_table(person)
        self.profilNamn.setText(person)

        # correct dates
        nSDYear, nSDMonth, nSDDay = self.read_nSD(person)
        self.nastaLonEdit.setDate(QtCore.QDate(nSDYear, nSDMonth, nSDDay))

        # write name to textfile
        economy.write_line('person.txt', person)

        # update income and expense
        self.show_income(person)
        self.show_expense(person)
        self.show_totIncome(person)
        self.show_totExpense(person)


    def save_income(self, person):
        income = self.inkomstEdit.text()
        if income.isdecimal():
            incomeCat = self.inkomstKategori.currentText()
            economy.add_income(person, incomeCat, income)
            print(person, incomeCat, income)
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Inkomsten kunde inte sparas!')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        self.show_income(person)
        self.show_totIncome(person)
        self.inkomstEdit.setText('')


    def save_expense(self, person):
        expense = self.utgiftEdit.text()
        if expense.isdecimal():
            expenseCat = self.utgiftKategori.currentText()
            economy.add_expense(person, expenseCat, expense)
            print(person, expenseCat, expense)
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Utgiften kunde inte sparas!')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        self.show_expense(person)
        self.show_totExpense(person) 
        self.utgiftEdit.setText('')   

    
    def show_income(self, person):
        incomeList = economy.read_incomeCat(person)
        lön = 0
        csn = 0
        presenter = 0
        annat = 0
        for each in incomeList:
            if each[0] == 'Lön':
                lön += int(each[1])
            elif each[0] == 'CSN':
                csn += int(each[1])
            elif each[0] == 'Presenter':
                presenter += int(each[1])
            elif each[0] == 'Annat':
                annat += int(each[1])
            
        _translate = QtCore.QCoreApplication.translate
        self.inkomstWidget.topLevelItem(0).setText(1, _translate("MainWindow", str(lön)))
        self.inkomstWidget.topLevelItem(1).setText(1, _translate("MainWindow", str(csn)))
        self.inkomstWidget.topLevelItem(2).setText(1, _translate("MainWindow", str(presenter)))
        self.inkomstWidget.topLevelItem(3).setText(1, _translate("MainWindow", str(annat)))


    def show_totIncome(self, person):
        allIncome = economy.read_income(person)
        _translate = QtCore.QCoreApplication.translate
        self.totInk.setText(_translate("MainWindow", str(int(allIncome))))
    

    def show_expense(self, person):
        expenseList = economy.read_expenseCat(person)

        # all categories
        hyra = 0
        abonnemang = 0
        resorLånga = 0
        resorKorta = 0
        matMat = 0
        matMatute = 0
        matSötsug = 0
        skolrelaterat = 0
        inredning = 0
        kläder = 0
        spel = 0
        elektronik = 0
        sminkBad = 0
        medicin = 0
        alkohol = 0
        sparande = 0
        presenter = 0
        övrigt = 0

        totResor = 0
        totMat = 0

        # create total for all categories
        for each in expenseList:
            if each[0] == 'Hyra':
                hyra += int(each[1])
            elif each[0] == 'Abonnemang':
                abonnemang += int(each[1])
            elif each[0] == 'Skolrelaterat':
                skolrelaterat += int(each[1])
            elif each[0] == 'Resor - Långa':
                resorLånga += int(each[1])
            elif each[0] == 'Resor - Korta':
                resorKorta += int(each[1])
            elif each[0] == 'Mat - Mat':
                matMat += int(each[1])
            elif each[0] == 'Mat - Mat ute':
                matMatute += int(each[1])
            elif each[0] == 'Mat - Sötsug':
                matSötsug += int(each[1])
            elif each[0] == 'Inredning':
                inredning += int(each[1])
            elif each[0] == 'Kläder':
                kläder += int(each[1])   
            elif each[0] == 'Spel':
                spel += int(each[1])   
            elif each[0] == 'Elektronik':
                elektronik += int(each[1])   
            elif each[0] == 'Smink/Bad':
                sminkBad += int(each[1])   
            elif each[0] == 'Medicin':
                medicin += int(each[1])   
            elif each[0] == 'Alkohol':
                alkohol += int(each[1])   
            elif each[0] == 'Sparande':
                sparande += int(each[1])       
            elif each[0] == 'Presenter':
                presenter += int(each[1])
            elif each[0] == 'Övrigt':
                övrigt += int(each[1])
            
        totResor = resorLånga + resorKorta
        totMat = matMat + matMatute + matSötsug

        # update UI
        _translate = QtCore.QCoreApplication.translate
        self.utgiftWidget.topLevelItem(0).setText(1, _translate("MainWindow", str(hyra)))
        self.utgiftWidget.topLevelItem(1).setText(1, _translate("MainWindow", str(abonnemang)))
        self.utgiftWidget.topLevelItem(2).setText(1, _translate("MainWindow", str(totResor)))
        self.utgiftWidget.topLevelItem(2).child(0).setText(1, _translate("MainWindow", str(resorLånga)))
        self.utgiftWidget.topLevelItem(2).child(1).setText(1, _translate("MainWindow", str(resorKorta)))
        self.utgiftWidget.topLevelItem(3).setText(1, _translate("MainWindow", str(totMat)))
        self.utgiftWidget.topLevelItem(3).child(0).setText(1, _translate("MainWindow", str(matMat)))
        self.utgiftWidget.topLevelItem(3).child(1).setText(1, _translate("MainWindow", str(matMatute)))
        self.utgiftWidget.topLevelItem(3).child(2).setText(1, _translate("MainWindow", str(matSötsug)))
        self.utgiftWidget.topLevelItem(4).setText(1, _translate("MainWindow", str(skolrelaterat)))
        self.utgiftWidget.topLevelItem(5).setText(1, _translate("MainWindow", str(inredning)))
        self.utgiftWidget.topLevelItem(6).setText(1, _translate("MainWindow", str(kläder)))
        self.utgiftWidget.topLevelItem(7).setText(1, _translate("MainWindow", str(spel)))
        self.utgiftWidget.topLevelItem(8).setText(1, _translate("MainWindow", str(elektronik)))
        self.utgiftWidget.topLevelItem(9).setText(1, _translate("MainWindow", str(sminkBad)))
        self.utgiftWidget.topLevelItem(10).setText(1, _translate("MainWindow", str(medicin)))
        self.utgiftWidget.topLevelItem(11).setText(1, _translate("MainWindow", str(alkohol)))
        self.utgiftWidget.topLevelItem(12).setText(1, _translate("MainWindow", str(sparande)))
        self.utgiftWidget.topLevelItem(13).setText(1, _translate("MainWindow", str(presenter)))
        self.utgiftWidget.topLevelItem(14).setText(1, _translate("MainWindow", str(övrigt)))


    def show_totExpense(self, person):
        allExpense = economy.read_expense(person)
        _translate = QtCore.QCoreApplication.translate
        self.totUtg.setText(_translate("MainWindow", str(int(allExpense))))


if __name__ == "__main__":
    import sys

    person = economy.read_line('person.txt', 0)

    # create table unless it already exists
    economy.create_table(person)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
