# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dxf2gcode_pyQt4_ui.ui'
#
# Created: Sun Dec 04 21:00:42 2011
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 799)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mytabWidget = QtGui.QTabWidget(self.centralwidget)
        self.mytabWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.mytabWidget.setObjectName("mytabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableView_2 = QtGui.QTableView(self.tab)
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout_4.addWidget(self.tableView_2)
        self.treeView_2 = QtGui.QTreeView(self.tab)
        self.treeView_2.setObjectName("treeView_2")
        self.verticalLayout_4.addWidget(self.treeView_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.mytabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.treeView = QtGui.QTreeView(self.tab_2)
        self.treeView.setMinimumSize(QtCore.QSize(0, 250))
        self.treeView.setObjectName("treeView")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.treeView)
        self.tableView = QtGui.QTableView(self.tab_2)
        self.tableView.setObjectName("tableView")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.tableView)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.mytabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.mytabWidget)
        self.mygraphicsView = MyGraphicsView(self.centralwidget)
        self.mygraphicsView.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.mygraphicsView.setObjectName("mygraphicsView")
        self.horizontalLayout.addWidget(self.mygraphicsView)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.myMessageBox = QtGui.QTextBrowser(self.centralwidget)
        self.myMessageBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.myMessageBox.setObjectName("myMessageBox")
        self.verticalLayout.addWidget(self.myMessageBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport = QtGui.QMenu(self.menubar)
        self.menuExport.setEnabled(True)
        self.menuExport.setObjectName("menuExport")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTolerances = QtGui.QMenu(self.menubar)
        self.menuTolerances.setObjectName("menuTolerances")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_File = QtGui.QAction(MainWindow)
        self.actionLoad_File.setObjectName("actionLoad_File")
        self.actionExit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName("actionExit")
        self.actionShow_WP_Zero = QtGui.QAction(MainWindow)
        self.actionShow_WP_Zero.setCheckable(True)
        self.actionShow_WP_Zero.setChecked(True)
        self.actionShow_WP_Zero.setEnabled(False)
        self.actionShow_WP_Zero.setObjectName("actionShow_WP_Zero")
        self.actionShow_path_directions = QtGui.QAction(MainWindow)
        self.actionShow_path_directions.setCheckable(True)
        self.actionShow_path_directions.setChecked(True)
        self.actionShow_path_directions.setEnabled(False)
        self.actionShow_path_directions.setObjectName("actionShow_path_directions")
        self.actionShow_hiden_paths = QtGui.QAction(MainWindow)
        self.actionShow_hiden_paths.setCheckable(True)
        self.actionShow_hiden_paths.setChecked(True)
        self.actionShow_hiden_paths.setEnabled(False)
        self.actionShow_hiden_paths.setObjectName("actionShow_hiden_paths")
        self.actionAutoscale = QtGui.QAction(MainWindow)
        self.actionAutoscale.setEnabled(False)
        self.actionAutoscale.setObjectName("actionAutoscale")
        self.actionDelete_G0_paths = QtGui.QAction(MainWindow)
        self.actionDelete_G0_paths.setEnabled(False)
        self.actionDelete_G0_paths.setObjectName("actionDelete_G0_paths")
        self.actionTolerances = QtGui.QAction(MainWindow)
        self.actionTolerances.setObjectName("actionTolerances")
        self.actionScale_all = QtGui.QAction(MainWindow)
        self.actionScale_all.setEnabled(False)
        self.actionScale_all.setObjectName("actionScale_all")
        self.actionRotate_all = QtGui.QAction(MainWindow)
        self.actionRotate_all.setEnabled(False)
        self.actionRotate_all.setObjectName("actionRotate_all")
        self.actionMove_WP_zero = QtGui.QAction(MainWindow)
        self.actionMove_WP_zero.setEnabled(False)
        self.actionMove_WP_zero.setObjectName("actionMove_WP_zero")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionLoad_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionShow_WP_Zero)
        self.menuView.addAction(self.actionShow_path_directions)
        self.menuView.addAction(self.actionShow_hiden_paths)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionAutoscale)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionDelete_G0_paths)
        self.menuTolerances.addAction(self.actionTolerances)
        self.menuTolerances.addSeparator()
        self.menuTolerances.addAction(self.actionScale_all)
        self.menuTolerances.addAction(self.actionRotate_all)
        self.menuTolerances.addSeparator()
        self.menuTolerances.addAction(self.actionMove_WP_zero)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTolerances.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.mytabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.mytabWidget.setTabText(self.mytabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Entities", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Linie 1 Edit Feld", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Linie 2 Edit Feld", None, QtGui.QApplication.UnicodeUTF8))
        self.mytabWidget.setTabText(self.mytabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.mygraphicsView.setToolTip(QtGui.QApplication.translate("MainWindow", "Graphic Area for drawing\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExport.setStatusTip(QtGui.QApplication.translate("MainWindow", "Export the current project to G-Code", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExport.setTitle(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTolerances.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_File.setText(QtGui.QApplication.translate("MainWindow", "Load File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_File.setStatusTip(QtGui.QApplication.translate("MainWindow", "Load DXF or other supportet document", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_File.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Exit DXF2GCODE and close window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_WP_Zero.setText(QtGui.QApplication.translate("MainWindow", "Show WP zero", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_path_directions.setText(QtGui.QApplication.translate("MainWindow", "Show path directions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_hiden_paths.setText(QtGui.QApplication.translate("MainWindow", "Show hiden paths", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAutoscale.setText(QtGui.QApplication.translate("MainWindow", "Autoscale", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_G0_paths.setText(QtGui.QApplication.translate("MainWindow", "Delete G0 paths", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTolerances.setText(QtGui.QApplication.translate("MainWindow", "Tolerances", None, QtGui.QApplication.UnicodeUTF8))
        self.actionScale_all.setText(QtGui.QApplication.translate("MainWindow", "Scale all", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRotate_all.setText(QtGui.QApplication.translate("MainWindow", "Rotate all", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove_WP_zero.setText(QtGui.QApplication.translate("MainWindow", "Move WP zero", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

from myCanvasClass import MyGraphicsView
import dxf2gcode_images_rc
