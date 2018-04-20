# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\swb\Documents\Projects\py\Crypto Messaging.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 510)
        Dialog.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Dialog.setAcceptDrops(False)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.pushButtonSendEncryptedMessage = QtWidgets.QPushButton(Dialog)
        self.pushButtonSendEncryptedMessage.setGeometry(QtCore.QRect(40, 120, 151, 23))
        self.pushButtonSendEncryptedMessage.setObjectName("pushButtonSendEncryptedMessage")
        self.pushButtonReceiveDecryptedMessage = QtWidgets.QPushButton(Dialog)
        self.pushButtonReceiveDecryptedMessage.setGeometry(QtCore.QRect(40, 420, 151, 23))
        self.pushButtonReceiveDecryptedMessage.setObjectName("pushButtonReceiveDecryptedMessage")
        self.lineTop = QtWidgets.QFrame(Dialog)
        self.lineTop.setGeometry(QtCore.QRect(30, 150, 341, 20))
        self.lineTop.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineTop.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineTop.setObjectName("lineTop")
        self.textEditEncryptedCommunicationHistory = QtWidgets.QTextEdit(Dialog)
        self.textEditEncryptedCommunicationHistory.setGeometry(QtCore.QRect(40, 190, 321, 81))
        self.textEditEncryptedCommunicationHistory.setObjectName("textEditEncryptedCommunicationHistory")
        self.lineBottom = QtWidgets.QFrame(Dialog)
        self.lineBottom.setGeometry(QtCore.QRect(30, 280, 341, 20))
        self.lineBottom.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineBottom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineBottom.setObjectName("lineBottom")
        self.labelCipherTextLog = QtWidgets.QLabel(Dialog)
        self.labelCipherTextLog.setGeometry(QtCore.QRect(170, 170, 91, 20))
        self.labelCipherTextLog.setObjectName("labelCipherTextLog")
        self.textEditSendEncryptedMessage = QtWidgets.QTextEdit(Dialog)
        self.textEditSendEncryptedMessage.setGeometry(QtCore.QRect(40, 30, 321, 81))
        self.textEditSendEncryptedMessage.setObjectName("textEditSendEncryptedMessage")
        self.textEditReceiveDecryptedMessage = QtWidgets.QTextEdit(Dialog)
        self.textEditReceiveDecryptedMessage.setGeometry(QtCore.QRect(40, 330, 321, 81))
        self.textEditReceiveDecryptedMessage.setObjectName("textEditReceiveDecryptedMessage")
        self.labelSendEncrypted = QtWidgets.QLabel(Dialog)
        self.labelSendEncrypted.setGeometry(QtCore.QRect(40, 10, 81, 16))
        self.labelSendEncrypted.setObjectName("labelSendEncrypted")
        self.labelReceiveDecrypted = QtWidgets.QLabel(Dialog)
        self.labelReceiveDecrypted.setGeometry(QtCore.QRect(40, 310, 91, 16))
        self.labelReceiveDecrypted.setObjectName("labelReceiveDecrypted")
        self.pushButtonQuitApplication = QtWidgets.QPushButton(Dialog)
        self.pushButtonQuitApplication.setGeometry(QtCore.QRect(274, 480, 101, 23))
        self.pushButtonQuitApplication.setObjectName("pushButtonQuitApplication")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cryptographic Messaging Tool  by Jonathan Herrera"))
        self.pushButtonSendEncryptedMessage.setText(_translate("Dialog", "Send Encrypted Message"))
        self.pushButtonReceiveDecryptedMessage.setText(_translate("Dialog", "Receive Decrypted Message"))
        self.labelCipherTextLog.setText(_translate("Dialog", "Cipher Log"))
        self.labelSendEncrypted.setText(_translate("Dialog", "Send Encrypted"))
        self.labelReceiveDecrypted.setText(_translate("Dialog", "Receive Decrypted"))
        self.pushButtonQuitApplication.setText(_translate("Dialog", "Quit Application"))

