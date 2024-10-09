# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1159, 698)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layers_windows = QWidget(self.splitter)
        self.layers_windows.setObjectName(u"layers_windows")
        self.layers_windows.setEnabled(True)
        self.layers_windows.setStyleSheet(u"")
        self.splitter.addWidget(self.layers_windows)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.model_builder_tab = QWidget()
        self.model_builder_tab.setObjectName(u"model_builder_tab")
        self.tabWidget.addTab(self.model_builder_tab, "")
        self.training_tab = QWidget()
        self.training_tab.setObjectName(u"training_tab")
        self.tabWidget.addTab(self.training_tab, "")
        self.splitter.addWidget(self.tabWidget)
        self.config_windows = QTabWidget(self.splitter)
        self.config_windows.setObjectName(u"config_windows")
        self.config_windows.setStyleSheet(u"")
        self.data_tab = QWidget()
        self.data_tab.setObjectName(u"data_tab")
        self.config_windows.addTab(self.data_tab, "")
        self.train_settings_tab = QWidget()
        self.train_settings_tab.setObjectName(u"train_settings_tab")
        self.config_windows.addTab(self.train_settings_tab, "")
        self.test_tab = QWidget()
        self.test_tab.setObjectName(u"test_tab")
        self.config_windows.addTab(self.test_tab, "")
        self.splitter.addWidget(self.config_windows)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1159, 22))
        self.menubar.setStyleSheet(u"background-color: #BFBFBF;")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.config_windows.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.model_builder_tab), QCoreApplication.translate("MainWindow", u"Model Builder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.training_tab), QCoreApplication.translate("MainWindow", u"Training", None))
        self.config_windows.setTabText(self.config_windows.indexOf(self.data_tab), QCoreApplication.translate("MainWindow", u"Data", None))
        self.config_windows.setTabText(self.config_windows.indexOf(self.train_settings_tab), QCoreApplication.translate("MainWindow", u"Train", None))
        self.config_windows.setTabText(self.config_windows.indexOf(self.test_tab), QCoreApplication.translate("MainWindow", u"Test", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

