# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dxf2gcode_pyQt4_ui.ui'
#
# Created: Tue Oct 23 12:47:21 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1146, 895)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.mytabWidget = QtGui.QTabWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mytabWidget.sizePolicy().hasHeightForWidth())
        self.mytabWidget.setSizePolicy(sizePolicy)
        self.mytabWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.mytabWidget.setObjectName("mytabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.blocksCollapsePushButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blocksCollapsePushButton.sizePolicy().hasHeightForWidth())
        self.blocksCollapsePushButton.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/collapse-all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blocksCollapsePushButton.setIcon(icon)
        self.blocksCollapsePushButton.setIconSize(QtCore.QSize(24, 24))
        self.blocksCollapsePushButton.setObjectName("blocksCollapsePushButton")
        self.horizontalLayout_5.addWidget(self.blocksCollapsePushButton)
        self.blocksExpandPushButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blocksExpandPushButton.sizePolicy().hasHeightForWidth())
        self.blocksExpandPushButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/expand-all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blocksExpandPushButton.setIcon(icon1)
        self.blocksExpandPushButton.setIconSize(QtCore.QSize(24, 24))
        self.blocksExpandPushButton.setObjectName("blocksExpandPushButton")
        self.horizontalLayout_5.addWidget(self.blocksExpandPushButton)
        spacerItem = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.entitiesTreeView = MyTreeView(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entitiesTreeView.sizePolicy().hasHeightForWidth())
        self.entitiesTreeView.setSizePolicy(sizePolicy)
        self.entitiesTreeView.setObjectName("entitiesTreeView")
        self.verticalLayout_3.addWidget(self.entitiesTreeView)
        self.mytabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setMargin(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.layersCollapsePushButton = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layersCollapsePushButton.sizePolicy().hasHeightForWidth())
        self.layersCollapsePushButton.setSizePolicy(sizePolicy)
        self.layersCollapsePushButton.setIcon(icon)
        self.layersCollapsePushButton.setIconSize(QtCore.QSize(24, 24))
        self.layersCollapsePushButton.setObjectName("layersCollapsePushButton")
        self.horizontalLayout_4.addWidget(self.layersCollapsePushButton)
        self.layersExpandPushButton = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layersExpandPushButton.sizePolicy().hasHeightForWidth())
        self.layersExpandPushButton.setSizePolicy(sizePolicy)
        self.layersExpandPushButton.setIcon(icon1)
        self.layersExpandPushButton.setIconSize(QtCore.QSize(24, 24))
        self.layersExpandPushButton.setObjectName("layersExpandPushButton")
        self.horizontalLayout_4.addWidget(self.layersExpandPushButton)
        spacerItem1 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.layersGoUpPushButton = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layersGoUpPushButton.sizePolicy().hasHeightForWidth())
        self.layersGoUpPushButton.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/go-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.layersGoUpPushButton.setIcon(icon2)
        self.layersGoUpPushButton.setIconSize(QtCore.QSize(24, 24))
        self.layersGoUpPushButton.setObjectName("layersGoUpPushButton")
        self.horizontalLayout_4.addWidget(self.layersGoUpPushButton)
        self.layersGoDownPushButton = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layersGoDownPushButton.sizePolicy().hasHeightForWidth())
        self.layersGoDownPushButton.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/go-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.layersGoDownPushButton.setIcon(icon3)
        self.layersGoDownPushButton.setIconSize(QtCore.QSize(24, 24))
        self.layersGoDownPushButton.setObjectName("layersGoDownPushButton")
        self.horizontalLayout_4.addWidget(self.layersGoDownPushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.layersShapesTreeView = MyTreeView(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layersShapesTreeView.sizePolicy().hasHeightForWidth())
        self.layersShapesTreeView.setSizePolicy(sizePolicy)
        self.layersShapesTreeView.setObjectName("layersShapesTreeView")
        self.verticalLayout_5.addWidget(self.layersShapesTreeView)
        self.millSettingsFrame = QtGui.QFrame(self.tab_2)
        self.millSettingsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.millSettingsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.millSettingsFrame.setLineWidth(0)
        self.millSettingsFrame.setObjectName("millSettingsFrame")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.millSettingsFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setMargin(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolDiameterComboBox = QtGui.QComboBox(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolDiameterComboBox.sizePolicy().hasHeightForWidth())
        self.toolDiameterComboBox.setSizePolicy(sizePolicy)
        self.toolDiameterComboBox.setMaxVisibleItems(20)
        self.toolDiameterComboBox.setObjectName("toolDiameterComboBox")
        self.horizontalLayout_3.addWidget(self.toolDiameterComboBox)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtGui.QLabel(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.toolDiameterLabel = QtGui.QLabel(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolDiameterLabel.sizePolicy().hasHeightForWidth())
        self.toolDiameterLabel.setSizePolicy(sizePolicy)
        self.toolDiameterLabel.setObjectName("toolDiameterLabel")
        self.horizontalLayout.addWidget(self.toolDiameterLabel)
        self.label_12 = QtGui.QLabel(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.toolSpeedLabel = QtGui.QLabel(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolSpeedLabel.sizePolicy().hasHeightForWidth())
        self.toolSpeedLabel.setSizePolicy(sizePolicy)
        self.toolSpeedLabel.setObjectName("toolSpeedLabel")
        self.horizontalLayout.addWidget(self.toolSpeedLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_13 = QtGui.QLabel(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.startRadiusLabel = QtGui.QLabel(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startRadiusLabel.sizePolicy().hasHeightForWidth())
        self.startRadiusLabel.setSizePolicy(sizePolicy)
        self.startRadiusLabel.setObjectName("startRadiusLabel")
        self.horizontalLayout_2.addWidget(self.startRadiusLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(self.millSettingsFrame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.startAtXLineEdit = QtGui.QLineEdit(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startAtXLineEdit.sizePolicy().hasHeightForWidth())
        self.startAtXLineEdit.setSizePolicy(sizePolicy)
        self.startAtXLineEdit.setObjectName("startAtXLineEdit")
        self.gridLayout.addWidget(self.startAtXLineEdit, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.millSettingsFrame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.startAtYLineEdit = QtGui.QLineEdit(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startAtYLineEdit.sizePolicy().hasHeightForWidth())
        self.startAtYLineEdit.setSizePolicy(sizePolicy)
        self.startAtYLineEdit.setObjectName("startAtYLineEdit")
        self.gridLayout.addWidget(self.startAtYLineEdit, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.millSettingsFrame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.zRetractionArealLineEdit = QtGui.QLineEdit(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zRetractionArealLineEdit.sizePolicy().hasHeightForWidth())
        self.zRetractionArealLineEdit.setSizePolicy(sizePolicy)
        self.zRetractionArealLineEdit.setObjectName("zRetractionArealLineEdit")
        self.gridLayout.addWidget(self.zRetractionArealLineEdit, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.millSettingsFrame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.zSafetyMarginLineEdit = QtGui.QLineEdit(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zSafetyMarginLineEdit.sizePolicy().hasHeightForWidth())
        self.zSafetyMarginLineEdit.setSizePolicy(sizePolicy)
        self.zSafetyMarginLineEdit.setObjectName("zSafetyMarginLineEdit")
        self.gridLayout.addWidget(self.zSafetyMarginLineEdit, 3, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.millSettingsFrame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.zInfeedDepthLineEdit = QtGui.QLineEdit(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zInfeedDepthLineEdit.sizePolicy().hasHeightForWidth())
        self.zInfeedDepthLineEdit.setSizePolicy(sizePolicy)
        self.zInfeedDepthLineEdit.setObjectName("zInfeedDepthLineEdit")
        self.gridLayout.addWidget(self.zInfeedDepthLineEdit, 4, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.millSettingsFrame)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 0, 1, 1)
        self.zInitialMillDepthLineEdit = QtGui.QLineEdit(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zInitialMillDepthLineEdit.sizePolicy().hasHeightForWidth())
        self.zInitialMillDepthLineEdit.setSizePolicy(sizePolicy)
        self.zInitialMillDepthLineEdit.setObjectName("zInitialMillDepthLineEdit")
        self.gridLayout.addWidget(self.zInitialMillDepthLineEdit, 5, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.millSettingsFrame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.zFinalMillDepthLineEdit = QtGui.QLineEdit(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zFinalMillDepthLineEdit.sizePolicy().hasHeightForWidth())
        self.zFinalMillDepthLineEdit.setSizePolicy(sizePolicy)
        self.zFinalMillDepthLineEdit.setObjectName("zFinalMillDepthLineEdit")
        self.gridLayout.addWidget(self.zFinalMillDepthLineEdit, 6, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.millSettingsFrame)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.g1FeedXYLineEdit = QtGui.QLineEdit(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g1FeedXYLineEdit.sizePolicy().hasHeightForWidth())
        self.g1FeedXYLineEdit.setSizePolicy(sizePolicy)
        self.g1FeedXYLineEdit.setObjectName("g1FeedXYLineEdit")
        self.gridLayout.addWidget(self.g1FeedXYLineEdit, 7, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.millSettingsFrame)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.g1FeedZLineEdit = QtGui.QLineEdit(self.millSettingsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g1FeedZLineEdit.sizePolicy().hasHeightForWidth())
        self.g1FeedZLineEdit.setSizePolicy(sizePolicy)
        self.g1FeedZLineEdit.setObjectName("g1FeedZLineEdit")
        self.gridLayout.addWidget(self.g1FeedZLineEdit, 8, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_5.addWidget(self.millSettingsFrame)
        self.mytabWidget.addTab(self.tab_2, "")
        self.MyGraphicsView = MyGraphicsView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MyGraphicsView.sizePolicy().hasHeightForWidth())
        self.MyGraphicsView.setSizePolicy(sizePolicy)
        self.MyGraphicsView.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.MyGraphicsView.setObjectName("MyGraphicsView")
        self.verticalLayout.addWidget(self.splitter)
        self.myMessageBox = myMessageBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.myMessageBox.sizePolicy().hasHeightForWidth())
        self.myMessageBox.setSizePolicy(sizePolicy)
        self.myMessageBox.setMaximumSize(QtCore.QSize(16777215, 120))
        self.myMessageBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.myMessageBox.setObjectName("myMessageBox")
        self.verticalLayout.addWidget(self.myMessageBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1146, 25))
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionShow_WP_Zero = QtGui.QAction(MainWindow)
        self.actionShow_WP_Zero.setCheckable(True)
        self.actionShow_WP_Zero.setChecked(True)
        self.actionShow_WP_Zero.setEnabled(False)
        self.actionShow_WP_Zero.setObjectName("actionShow_WP_Zero")
        self.actionShow_path_directions = QtGui.QAction(MainWindow)
        self.actionShow_path_directions.setCheckable(True)
        self.actionShow_path_directions.setChecked(False)
        self.actionShow_path_directions.setEnabled(False)
        self.actionShow_path_directions.setObjectName("actionShow_path_directions")
        self.actionShow_disabled_paths = QtGui.QAction(MainWindow)
        self.actionShow_disabled_paths.setCheckable(True)
        self.actionShow_disabled_paths.setChecked(False)
        self.actionShow_disabled_paths.setEnabled(False)
        self.actionShow_disabled_paths.setObjectName("actionShow_disabled_paths")
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
        self.actionOptimize_Shape = QtGui.QAction(MainWindow)
        self.actionOptimize_Shape.setObjectName("actionOptimize_Shape")
        self.actionExport_Shapes = QtGui.QAction(MainWindow)
        self.actionExport_Shapes.setObjectName("actionExport_Shapes")
        self.menuFile.addAction(self.actionLoad_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuExport.addSeparator()
        self.menuExport.addAction(self.actionOptimize_Shape)
        self.menuExport.addAction(self.actionExport_Shapes)
        self.menuView.addAction(self.actionShow_WP_Zero)
        self.menuView.addAction(self.actionShow_path_directions)
        self.menuView.addAction(self.actionShow_disabled_paths)
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
        self.mytabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.layersCollapsePushButton, QtCore.SIGNAL("clicked()"), self.layersShapesTreeView.collapseAll)
        QtCore.QObject.connect(self.layersExpandPushButton, QtCore.SIGNAL("clicked()"), self.layersShapesTreeView.expandAll)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.blocksCollapsePushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Collapse all items", None, QtGui.QApplication.UnicodeUTF8))
        self.blocksExpandPushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Expand all items", None, QtGui.QApplication.UnicodeUTF8))
        self.mytabWidget.setTabText(self.mytabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Entities", None, QtGui.QApplication.UnicodeUTF8))
        self.layersCollapsePushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Collapse all items", None, QtGui.QApplication.UnicodeUTF8))
        self.layersExpandPushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Expand all items", None, QtGui.QApplication.UnicodeUTF8))
        self.layersGoUpPushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Move-up the selected shape/layer", None, QtGui.QApplication.UnicodeUTF8))
        self.layersGoDownPushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Move-down the selected shape/layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "⌀", None, QtGui.QApplication.UnicodeUTF8))
        self.toolDiameterLabel.setText(QtGui.QApplication.translate("MainWindow", "[mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "/ speed ", None, QtGui.QApplication.UnicodeUTF8))
        self.toolSpeedLabel.setText(QtGui.QApplication.translate("MainWindow", "[rpm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "start radius (comp) ", None, QtGui.QApplication.UnicodeUTF8))
        self.startRadiusLabel.setText(QtGui.QApplication.translate("MainWindow", "[mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Start at X [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Start at Y [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Z retraction area [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Z safety margin [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Z infeed depth [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Z initial mill depth [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Z final mill depth [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "G1 feed XY-directions [mm/min]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "G1 feed Z-direction [mm/min]", None, QtGui.QApplication.UnicodeUTF8))
        self.mytabWidget.setTabText(self.mytabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.MyGraphicsView.setToolTip(QtGui.QApplication.translate("MainWindow", "Graphic Area for drawing\n"
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
        self.actionShow_WP_Zero.setStatusTip(QtGui.QApplication.translate("MainWindow", "Show the Workpiece Zero symbol in the plot.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_path_directions.setText(QtGui.QApplication.translate("MainWindow", "Show path directions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_path_directions.setStatusTip(QtGui.QApplication.translate("MainWindow", "Always shows the path direction in the plot (not only while selected)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_disabled_paths.setText(QtGui.QApplication.translate("MainWindow", "Show disabled paths", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAutoscale.setText(QtGui.QApplication.translate("MainWindow", "Autoscale", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_G0_paths.setText(QtGui.QApplication.translate("MainWindow", "Delete G0 paths", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTolerances.setText(QtGui.QApplication.translate("MainWindow", "Tolerances", None, QtGui.QApplication.UnicodeUTF8))
        self.actionScale_all.setText(QtGui.QApplication.translate("MainWindow", "Scale all", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRotate_all.setText(QtGui.QApplication.translate("MainWindow", "Rotate all", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove_WP_zero.setText(QtGui.QApplication.translate("MainWindow", "Move WP zero", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOptimize_Shape.setText(QtGui.QApplication.translate("MainWindow", "Optimize Shape ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_Shapes.setText(QtGui.QApplication.translate("MainWindow", "Export Shapes", None, QtGui.QApplication.UnicodeUTF8))

from Gui.myCanvasClass import MyGraphicsView
from Gui.myTreeView import MyTreeView
from Gui.myMessageBox import myMessageBox
import dxf2gcode_images_rc
