# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background: rgb(201, 255, 254)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.program_title = QLabel(self.centralwidget)
        self.program_title.setObjectName(u"program_title")
        self.program_title.setGeometry(QRect(270, 50, 201, 21))
        self.program_title.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.program_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(670, 120, 101, 21))
        self.label.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(490, 110, 171, 41))
        self.lineEdit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lineEdit.setStyleSheet(u"background: rgb(255, 255, 255);  \n"
"border: 2px solid #005A9C;\n"
"        padding: 10px;         \n"
"        border-radius: 8px;    ")
        self.lineEdit.setLocale(QLocale(QLocale.Hebrew, QLocale.Israel))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(490, 170, 171, 41))
        self.comboBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.comboBox.setStyleSheet(u"background: rgb(255, 255, 255);  \n"
"border: 2px solid #005A9C;\n"
"        padding: 10px;         \n"
"        border-radius: 8px;    ")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(660, 180, 121, 21))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.listWidget = QListWidget(self.centralwidget)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem8 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem9 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem10 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem11 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem12 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem13 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(410, 230, 256, 192))
        self.listWidget.setStyleSheet(u"background: rgb(255, 255, 255);  \n"
"border: 2px solid #005A9C;\n"
"        padding: 10px;         \n"
"        border-radius: 8px;    ")
        self.listWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(670, 230, 101, 20))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(410, 430, 100, 32))
        self.pushButton.setStyleSheet(u"background:rgb(143, 178, 255)\n"
"")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 230, 361, 191))
        self.textEdit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.textEdit.setStyleSheet(u"background: rgb(255, 255, 255);  \n"
"border: 2px solid #005A9C;\n"
"        padding: 10px;         \n"
"        border-radius: 8px;    ")
        self.textEdit.setReadOnly(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 200, 271, 31))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 430, 361, 32))
        self.pushButton_2.setStyleSheet(u"background:rgb(143, 178, 255)\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.program_title.setText(QCoreApplication.translate("MainWindow", u"\u05de\u05d2\u05e0\u05f3\u05e8\u05d8 \u05d4\u05de\u05d9\u05d9\u05dc\u05d9\u05dd \u05e9\u05dc \u05de\u05d5\u05e9\u05dc", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u05e9\u05dd \u05d4\u05de\u05d5\u05e2\u05de\u05d3/\u05ea:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u05d4\u05d6\u05d9\u05e0\u05d5 \u05d0\u05ea \u05e9\u05dd \u05d4\u05de\u05d5\u05e2\u05de\u05d3/\u05ea...", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u05d4\u05e4\u05d5\u05e2\u05dc\u05d9\u05dd", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u05dc\u05d0 \u05d1\u05d8\u05d5\u05d7/\u05d4", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u05dc\u05d0\u05d5\u05de\u05d9", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u05e4\u05e4\u05e8", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u05de\u05d6\u05e8\u05d7\u05d9 \u05d8\u05e4\u05d7\u05d5\u05ea", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u05d1\u05e0\u05e7 \u05d4\u05d3\u05d5\u05d0\u05e8", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u05d4\u05d1\u05d9\u05e0\u05dc\u05d0\u05d5\u05de\u05d9", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"\u05d3\u05d9\u05e1\u05e7\u05d5\u05e0\u05d8/\u05de\u05e8\u05db\u05e0\u05ea\u05d9\u05dc", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u05d1\u05d7\u05e8\u05d5 \u05d1\u05e0\u05e7...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u05d1\u05e0\u05e7 \u05d4\u05de\u05d5\u05e2\u05de\u05d3/\u05ea:", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u05de\u05e2\u05de\u05d3 \u05dc\u05d0 \u05e2\u05d5\u05d1\u05d3", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u05d9\u05ea\u05e8\u05ea \u05e4\u05d9\u05e7\u05d3\u05d5\u05df \u05e6\u05d1\u05d0\u05d9", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u05e4\u05d9\u05e8\u05d5\u05d8 \u05d0\u05e9\u05e8\u05d0\u05d9", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u05e4\u05d9\u05e8\u05d5\u05d8 \u05e2\u05d5\u05f4\u05e9", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u05d3\u05d5\u05d7 \u05e8\u05d9\u05db\u05d5\u05d6 \u05d9\u05ea\u05e8\u05d5\u05ea", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u05ea\u05e9\u05dc\u05d5\u05dd \u05e7\u05e6\u05d1\u05d4/ \u05d0\u05e1\u05de\u05db\u05ea\u05d0 \u05dc\u05e7\u05e6\u05d1\u05d4", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u05d2\u05d9\u05dc\u05d9\u05d5\u05df \u05e6\u05d9\u05d5\u05e0\u05d9 \u05d1\u05d2\u05e8\u05d5\u05ea", None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u05e6\u05d9\u05d5\u05df \u05e4\u05e1\u05d9\u05db\u05d5\u05de\u05d8\u05e8\u05d9/ \u05d2\u05dc\u05d9\u05d5\u05df \u05e6\u05d9\u05d5\u05e0\u05d9\u05dd/ \u05de\u05d1\u05d7\u05df \u05d9\u05e2\u05dc", None));
        ___qlistwidgetitem8 = self.listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u05e4\u05d9\u05e8\u05d5\u05d8 \u05d7\u05d5\u05d1\u05d5\u05ea/\u05d4\u05dc\u05d5\u05d5\u05d0\u05d5\u05ea", None));
        ___qlistwidgetitem9 = self.listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u05de\u05e1\u05de\u05da \u05dc\u05e1\u05d9\u05dc\u05d5\u05e7 \u05de\u05e9\u05db\u05e0\u05ea\u05d0", None));
        ___qlistwidgetitem10 = self.listWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u05ea\u05dc\u05d5\u05e9 \u05e9\u05db\u05e8 \u05d4\u05d5\u05e8\u05d4", None));
        ___qlistwidgetitem11 = self.listWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u05d0\u05e1\u05de\u05db\u05ea\u05d0 \u05dc\u05e0\u05d9\u05ea\u05d5\u05e7 \u05e7\u05e9\u05e8 \u05de\u05d4\u05d5\u05e8\u05d4", None));
        ___qlistwidgetitem12 = self.listWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u05d9\u05ea\u05e8\u05ea \u05e4\u05d9\u05e7\u05d3\u05d5\u05df \u05e6\u05d1\u05d0\u05d9", None));
        ___qlistwidgetitem13 = self.listWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u05e9\u05d5\u05de\u05ea \u05de\u05e1 \u05dc\u05e9\u05e0\u05d4 \u05d4\u05e0\u05d5\u05db\u05d7\u05d9\u05ea", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u05de\u05e1\u05de\u05db\u05d9\u05dd \u05d7\u05e1\u05e8\u05d9\u05dd:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u05d2\u05f3\u05e0\u05e8\u05d8", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u05db\u05d0\u05df \u05d9\u05d5\u05e4\u05d9\u05e2 \u05d4\u05de\u05d9\u05d9\u05dc \u05d4\u05de\u05d2\u05f3\u05d5\u05e0\u05e8\u05d8...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u05d4\u05de\u05d9\u05d9\u05dc \u05d4\u05de\u05d2\u05f3\u05d5\u05e0\u05e8\u05d8:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u05d4\u05e2\u05ea\u05e7 \u05d8\u05e7\u05e1\u05d8", None))
    # retranslateUi

