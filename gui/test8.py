# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test8.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1564, 956)
        self.img_label = QLabel(Form)
        self.img_label.setObjectName(u"img_label")
        self.img_label.setGeometry(QRect(450, 90, 841, 321))
        self.startVideo = QPushButton(Form)
        self.startVideo.setObjectName(u"startVideo")
        self.startVideo.setGeometry(QRect(1360, 180, 180, 50))
        self.stopVideo = QPushButton(Form)
        self.stopVideo.setObjectName(u"stopVideo")
        self.stopVideo.setGeometry(QRect(1360, 250, 180, 50))
        self.exit_btn = QPushButton(Form)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(1360, 390, 181, 51))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1350, 80, 71, 31))
        self.Id = QTextEdit(Form)
        self.Id.setObjectName(u"Id")
        self.Id.setGeometry(QRect(1420, 80, 104, 30))
        self.frequenceLabel = QLabel(Form)
        self.frequenceLabel.setObjectName(u"frequenceLabel")
        self.frequenceLabel.setGeometry(QRect(40, 600, 351, 211))
        self.deepLabel = QLabel(Form)
        self.deepLabel.setObjectName(u"deepLabel")
        self.deepLabel.setGeometry(QRect(50, 100, 331, 221))
        self.generalcomment_btn = QPushButton(Form)
        self.generalcomment_btn.setObjectName(u"generalcomment_btn")
        self.generalcomment_btn.setGeometry(QRect(1360, 320, 181, 51))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 370, 361, 101))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.depthLabel = QLabel(self.layoutWidget)
        self.depthLabel.setObjectName(u"depthLabel")
        self.depthLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.depthLabel)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(70, 820, 351, 101))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.frequencyLabel = QLabel(self.layoutWidget1)
        self.frequencyLabel.setObjectName(u"frequencyLabel")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.frequencyLabel.setFont(font1)

        self.horizontalLayout_4.addWidget(self.frequencyLabel)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 510, 421, 71))
        self.label_7.setFont(font)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 421, 71))
        self.label_8.setFont(font)
        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(710, 0, 331, 99))
        self.label_20.setFont(font)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(410, 0, 20, 981))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(420, 490, 1211, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(1190, 10, 131, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Round = QLabel(self.horizontalLayoutWidget)
        self.Round.setObjectName(u"Round")
        self.Round.setFont(font)

        self.horizontalLayout.addWidget(self.Round)

        self.round = QLabel(self.horizontalLayoutWidget)
        self.round.setObjectName(u"round")
        self.round.setFont(font)

        self.horizontalLayout.addWidget(self.round)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(1310, 0, 20, 501))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(1010, 500, 20, 491))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.img_label_2 = QLabel(Form)
        self.img_label_2.setObjectName(u"img_label_2")
        self.img_label_2.setGeometry(QRect(1060, 610, 461, 311))
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(1100, 520, 411, 51))
        self.label_15.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 540, 521, 261))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(470, 850, 191, 82))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(126, 16777215))
        self.label_10.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.label_22 = QLabel(self.verticalLayoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_22)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.label_18 = QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_18)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(740, 850, 231, 82))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.label_21 = QLabel(self.verticalLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_21)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.label_17 = QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_17)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayoutWidget_2 = QWidget(Form)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(680, 430, 191, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Left = QLabel(self.horizontalLayoutWidget_2)
        self.Left.setObjectName(u"Left")
        self.Left.setFont(font)

        self.horizontalLayout_2.addWidget(self.Left)

        self.left = QLabel(self.horizontalLayoutWidget_2)
        self.left.setObjectName(u"left")
        self.left.setFont(font)

        self.horizontalLayout_2.addWidget(self.left)

        self.horizontalLayoutWidget_3 = QWidget(Form)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(910, 430, 191, 41))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Right = QLabel(self.horizontalLayoutWidget_3)
        self.Right.setObjectName(u"Right")
        self.Right.setFont(font)

        self.horizontalLayout_9.addWidget(self.Right)

        self.right = QLabel(self.horizontalLayoutWidget_3)
        self.right.setObjectName(u"right")
        self.right.setFont(font)

        self.horizontalLayout_9.addWidget(self.right)

        self.armangle = QLabel(Form)
        self.armangle.setObjectName(u"armangle")
        self.armangle.setGeometry(QRect(470, 430, 181, 49))
        self.armangle.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"AI CPR ", None))
        self.img_label.setText(QCoreApplication.translate("Form", u"imgLabel", None))
        self.startVideo.setText(QCoreApplication.translate("Form", u"\u958b\u59cb\u9304\u5f71", None))
        self.stopVideo.setText(QCoreApplication.translate("Form", u"\u7d50\u675f\u9304\u5f71", None))
        self.exit_btn.setText(QCoreApplication.translate("Form", u"\u96e2\u958b", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">\u7de8\u865f</span></p></body></html>", None))
        self.frequenceLabel.setText(QCoreApplication.translate("Form", u"frequenceLabel", None))
        self.deepLabel.setText(QCoreApplication.translate("Form", u"deepLabel", None))
        self.generalcomment_btn.setText(QCoreApplication.translate("Form", u"\u7e3d\u8a55", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Depth</p></body></html>", None))
        self.depthLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>0.0</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Rate</p></body></html>", None))
        self.frequencyLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>0.0</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Compression  Rate</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Compression  Depth</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">CPR Screen</span></p></body></html>", None))
        self.Round.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Round</span></p></body></html>", None))
        self.round.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt;\">0</span></p></body></html>", None))
        self.img_label_2.setText(QCoreApplication.translate("Form", u"imgYOLOLabel", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Compression Position</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"electrocardiogramLabel", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">Depth</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">Abnormal</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">   Rate</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">Abnormal</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">Posture</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">Abnormal</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">Position</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ef2929;\">Abnormal</span></p></body></html>", None))
        self.Left.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Left</p><p align=\"center\"><br/></p></body></html>", None))
        self.left.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">0</span></p></body></html>", None))
        self.Right.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Right</p><p align=\"center\"><br/></p></body></html>", None))
        self.right.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">0</span></p></body></html>", None))
        self.armangle.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Arm angle :</p><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi

