# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test9.ui'
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
        Form.resize(1564, 941)
        self.img_label = QLabel(Form)
        self.img_label.setObjectName(u"img_label")
        self.img_label.setGeometry(QRect(500, 60, 711, 361))
        self.img_label.setAlignment(Qt.AlignCenter)
        self.startVideo = QPushButton(Form)
        self.startVideo.setObjectName(u"startVideo")
        self.startVideo.setGeometry(QRect(1340, 119, 180, 61))
        self.stopVideo = QPushButton(Form)
        self.stopVideo.setObjectName(u"stopVideo")
        self.stopVideo.setGeometry(QRect(1340, 200, 180, 61))
        self.exit_btn = QPushButton(Form)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(1340, 360, 180, 61))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1340, 70, 67, 17))
        self.Id = QTextEdit(Form)
        self.Id.setObjectName(u"Id")
        self.Id.setGeometry(QRect(1390, 60, 104, 30))
        self.poseLabel = QLabel(Form)
        self.poseLabel.setObjectName(u"poseLabel")
        self.poseLabel.setGeometry(QRect(470, 550, 541, 231))
        self.poseLabel.setAlignment(Qt.AlignCenter)
        self.frequenceLabel = QLabel(Form)
        self.frequenceLabel.setObjectName(u"frequenceLabel")
        self.frequenceLabel.setGeometry(QRect(30, 590, 361, 201))
        self.frequenceLabel.setAlignment(Qt.AlignCenter)
        self.deepLabel = QLabel(Form)
        self.deepLabel.setObjectName(u"deepLabel")
        self.deepLabel.setGeometry(QRect(40, 100, 351, 211))
        self.deepLabel.setAlignment(Qt.AlignCenter)
        self.analysisBtn = QPushButton(Form)
        self.analysisBtn.setObjectName(u"analysisBtn")
        self.analysisBtn.setGeometry(QRect(1340, 280, 180, 61))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 350, 201, 101))
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
        self.layoutWidget1.setGeometry(QRect(110, 810, 201, 111))
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

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(420, 0, 20, 981))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(420, 500, 1211, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 401, 71))
        self.label_8.setFont(font)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 500, 421, 71))
        self.label_7.setFont(font)
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(1280, 0, 20, 511))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(720, 0, 291, 61))
        self.label_20.setFont(font)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(1160, 10, 131, 51))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Round = QLabel(self.horizontalLayoutWidget)
        self.Round.setObjectName(u"Round")
        self.Round.setFont(font)

        self.horizontalLayout_5.addWidget(self.Round)

        self.round = QLabel(self.horizontalLayoutWidget)
        self.round.setObjectName(u"round")
        self.round.setFont(font)

        self.horizontalLayout_5.addWidget(self.round)

        self.armangle = QLabel(Form)
        self.armangle.setObjectName(u"armangle")
        self.armangle.setGeometry(QRect(480, 441, 161, 49))
        self.armangle.setFont(font)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(490, 830, 201, 82))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(126, 16777215))
        self.label_10.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.label_22 = QLabel(self.verticalLayoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_22)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_11)

        self.label_18 = QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_18)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(760, 830, 231, 82))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.postureLabel = QLabel(self.verticalLayoutWidget_2)
        self.postureLabel.setObjectName(u"postureLabel")
        self.postureLabel.setFont(font)

        self.horizontalLayout_8.addWidget(self.postureLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_13)

        self.label_17 = QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_17)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(1110, 540, 421, 51))
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(1040, 510, 20, 431))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.img_label_2 = QLabel(Form)
        self.img_label_2.setObjectName(u"img_label_2")
        self.img_label_2.setGeometry(QRect(1090, 620, 441, 281))
        self.img_label_2.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(650, 420, 79, 89))
        font2 = QFont()
        font2.setFamilies([u"Ubuntu Condensed"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.left_hand = QLabel(Form)
        self.left_hand.setObjectName(u"left_hand")
        self.left_hand.setGeometry(QRect(730, 430, 221, 71))
        self.left_hand.setFont(font2)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(960, 420, 79, 89))
        self.label_3.setFont(font2)
        self.right_hand = QLabel(Form)
        self.right_hand.setObjectName(u"right_hand")
        self.right_hand.setGeometry(QRect(1040, 420, 211, 89))
        self.right_hand.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"AI CPR ", None))
        self.img_label.setText(QCoreApplication.translate("Form", u"imgLabel", None))
        self.startVideo.setText(QCoreApplication.translate("Form", u"\u958b\u59cb\u9304\u5f71", None))
        self.stopVideo.setText(QCoreApplication.translate("Form", u"\u7d50\u675f\u9304\u5f71", None))
        self.exit_btn.setText(QCoreApplication.translate("Form", u"\u96e2\u958b", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7de8\u865f", None))
        self.poseLabel.setText(QCoreApplication.translate("Form", u"electrocardiogramLabel", None))
        self.frequenceLabel.setText(QCoreApplication.translate("Form", u"frequenceLabel", None))
        self.deepLabel.setText(QCoreApplication.translate("Form", u"deepLabel", None))
        self.analysisBtn.setText(QCoreApplication.translate("Form", u"\u5206\u6790", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6df1\u5ea6", None))
        self.depthLabel.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u983b\u7387", None))
        self.frequencyLabel.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Compression  Depth</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Compression  Rate</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">CPR Screen</span></p></body></html>", None))
        self.Round.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Round</span></p></body></html>", None))
        self.round.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">0</span></p></body></html>", None))
        self.armangle.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u624b\u81c2\u89d2\u5ea6:</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">Depth</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#000000;\">Normal</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">   Rate</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#000000;\">Normal</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">Posture</span></p></body></html>", None))
        self.postureLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#000000;\">Normal</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">Position</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#000000;\">Normal</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Compression Position</span></p></body></html>", None))
        self.img_label_2.setText(QCoreApplication.translate("Form", u"img_label_2", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5de6\u624b", None))
        self.left_hand.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\u5c1a\u672a\u958b\u59cb\u5075\u6e2c</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u53f3\u624b", None))
        self.right_hand.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\u5c1a\u672a\u958b\u59cb\u5075\u6e2c</span></p></body></html>", None))
    # retranslateUi

