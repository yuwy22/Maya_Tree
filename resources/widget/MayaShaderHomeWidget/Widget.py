# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Peipei/PycharmProjects/Shaders/resources/widget/MayaShaderHomeWidget/Widget.ui'
#
# Created: Mon Mar  9 22:48:37 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class PySideUiFileSetup(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(608, 422)
        Form.horizontalLayout = QtGui.QHBoxLayout(Form)
        Form.horizontalLayout.setObjectName("horizontalLayout")
        Form.widget_2 = QtGui.QWidget(Form)
        Form.widget_2.setObjectName("widget_2")
        Form.verticalLayout = QtGui.QVBoxLayout(Form.widget_2)
        Form.verticalLayout.setContentsMargins(0, 0, 0, 0)
        Form.verticalLayout.setObjectName("verticalLayout")
        Form.assignment4Btn = QtGui.QPushButton(Form.widget_2)
        Form.assignment4Btn.setObjectName("assignment4Btn")
        Form.verticalLayout.addWidget(Form.assignment4Btn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        Form.verticalLayout.addItem(spacerItem)
        Form.horizontalLayout.addWidget(Form.widget_2)
        spacerItem1 = QtGui.QSpacerItem(438, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        Form.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        Form.assignment4Btn.setText(QtGui.QApplication.translate("Form", "Assignment 4", None, QtGui.QApplication.UnicodeUTF8))

