# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Kun\Documents\maya\2016\scripts\jumpPad\ui.ui'
#
# Created: Thu Aug 25 13:56:49 2016
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DlgGridJump(object):
    def setupUi(self, DlgGridJump):
        DlgGridJump.setObjectName("DlgGridJump")
        DlgGridJump.resize(219, 226)
        self.gridLayout_2 = QtGui.QGridLayout(DlgGridJump)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtGui.QGroupBox(DlgGridJump)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_6.setContentsMargins(9, 3, -1, 3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 3, 0, 1, 1)
        self.cmbPresetSel = QtGui.QComboBox(self.groupBox)
        self.cmbPresetSel.setMinimumSize(QtCore.QSize(110, 0))
        self.cmbPresetSel.setEditable(False)
        self.cmbPresetSel.setObjectName("cmbPresetSel")
        self.gridLayout_6.addWidget(self.cmbPresetSel, 3, 1, 1, 1)
        self.txtUnitValue = QtGui.QTextEdit(self.groupBox)
        self.txtUnitValue.setEnabled(False)
        self.txtUnitValue.setMinimumSize(QtCore.QSize(0, 20))
        self.txtUnitValue.setMaximumSize(QtCore.QSize(60, 16777215))
        self.txtUnitValue.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtUnitValue.setObjectName("txtUnitValue")
        self.gridLayout_6.addWidget(self.txtUnitValue, 3, 2, 1, 1)
        self.rdbMoveMode = QtGui.QRadioButton(self.groupBox)
        self.rdbMoveMode.setChecked(True)
        self.rdbMoveMode.setObjectName("rdbMoveMode")
        self.gridLayout_6.addWidget(self.rdbMoveMode, 1, 0, 1, 3)
        self.rdbAttachMode = QtGui.QRadioButton(self.groupBox)
        self.rdbAttachMode.setChecked(False)
        self.rdbAttachMode.setObjectName("rdbAttachMode")
        self.gridLayout_6.addWidget(self.rdbAttachMode, 0, 0, 1, 3)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(DlgGridJump)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.btnZPlus = QtGui.QPushButton(self.groupBox_2)
        self.btnZPlus.setMinimumSize(QtCore.QSize(40, 40))
        self.btnZPlus.setObjectName("btnZPlus")
        self.gridLayout.addWidget(self.btnZPlus, 0, 1, 1, 1)
        self.btnXPlus = QtGui.QPushButton(self.groupBox_2)
        self.btnXPlus.setMinimumSize(QtCore.QSize(40, 40))
        self.btnXPlus.setObjectName("btnXPlus")
        self.gridLayout.addWidget(self.btnXPlus, 1, 0, 1, 1)
        self.btnZMinus = QtGui.QPushButton(self.groupBox_2)
        self.btnZMinus.setMinimumSize(QtCore.QSize(40, 40))
        self.btnZMinus.setObjectName("btnZMinus")
        self.gridLayout.addWidget(self.btnZMinus, 1, 1, 1, 1)
        self.btnXMinus = QtGui.QPushButton(self.groupBox_2)
        self.btnXMinus.setMinimumSize(QtCore.QSize(40, 40))
        self.btnXMinus.setObjectName("btnXMinus")
        self.gridLayout.addWidget(self.btnXMinus, 1, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 0, 1, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnCW = QtGui.QPushButton(self.groupBox_2)
        self.btnCW.setMinimumSize(QtCore.QSize(40, 40))
        self.btnCW.setObjectName("btnCW")
        self.gridLayout_3.addWidget(self.btnCW, 0, 0, 1, 1)
        self.btnCCW = QtGui.QPushButton(self.groupBox_2)
        self.btnCCW.setMinimumSize(QtCore.QSize(40, 40))
        self.btnCCW.setObjectName("btnCCW")
        self.gridLayout_3.addWidget(self.btnCCW, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.retranslateUi(DlgGridJump)
        QtCore.QMetaObject.connectSlotsByName(DlgGridJump)

    def retranslateUi(self, DlgGridJump):
        DlgGridJump.setWindowTitle(QtGui.QApplication.translate("DlgGridJump", "Jump Pad", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DlgGridJump", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.rdbMoveMode.setText(QtGui.QApplication.translate("DlgGridJump", "Move", None, QtGui.QApplication.UnicodeUTF8))
        self.rdbAttachMode.setText(QtGui.QApplication.translate("DlgGridJump", "Attach to Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DlgGridJump", "JumpPad", None, QtGui.QApplication.UnicodeUTF8))
        self.btnZPlus.setText(QtGui.QApplication.translate("DlgGridJump", "+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.btnXPlus.setText(QtGui.QApplication.translate("DlgGridJump", "+X", None, QtGui.QApplication.UnicodeUTF8))
        self.btnZMinus.setText(QtGui.QApplication.translate("DlgGridJump", "-Z", None, QtGui.QApplication.UnicodeUTF8))
        self.btnXMinus.setText(QtGui.QApplication.translate("DlgGridJump", "-X", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCW.setText(QtGui.QApplication.translate("DlgGridJump", "CW", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCCW.setText(QtGui.QApplication.translate("DlgGridJump", "CCW", None, QtGui.QApplication.UnicodeUTF8))

