# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Demo.ui'
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
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1201, 852)
        self.startVideo = QPushButton(Form)
        self.startVideo.setObjectName(u"startVideo")
        self.startVideo.setGeometry(QRect(990, 129, 180, 61))
        self.stopVideo = QPushButton(Form)
        self.stopVideo.setObjectName(u"stopVideo")
        self.stopVideo.setGeometry(QRect(990, 220, 180, 61))
        self.exit_btn = QPushButton(Form)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(990, 310, 180, 61))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1000, 60, 67, 17))
        self.Id = QTextEdit(Form)
        self.Id.setObjectName(u"Id")
        self.Id.setGeometry(QRect(1050, 50, 104, 30))
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 410, 1641, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(1320, 0, 20, 511))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(330, 0, 301, 81))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_20.setFont(font)
        self.armangle = QLabel(Form)
        self.armangle.setObjectName(u"armangle")
        self.armangle.setGeometry(QRect(110, 440, 191, 71))
        self.armangle.setFont(font)
        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(940, 0, 20, 421))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(50, 580, 79, 61))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu Condensed"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.left_hand = QLabel(Form)
        self.left_hand.setObjectName(u"left_hand")
        self.left_hand.setGeometry(QRect(120, 570, 311, 81))
        self.left_hand.setFont(font1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 710, 79, 51))
        self.label_3.setFont(font1)
        self.right_hand = QLabel(Form)
        self.right_hand.setObjectName(u"right_hand")
        self.right_hand.setGeometry(QRect(120, 700, 311, 81))
        self.right_hand.setFont(font1)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(480, 530, 271, 71))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_6.addWidget(self.label)

        self.depthLabel = QLabel(self.layoutWidget)
        self.depthLabel.setObjectName(u"depthLabel")
        self.depthLabel.setFont(font)

        self.horizontalLayout_6.addWidget(self.depthLabel)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(480, 600, 271, 71))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.frequencyLabel = QLabel(self.layoutWidget1)
        self.frequencyLabel.setObjectName(u"frequencyLabel")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.frequencyLabel.setFont(font2)

        self.horizontalLayout_7.addWidget(self.frequencyLabel)

        self.layoutWidget2 = QWidget(Form)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(480, 670, 271, 71))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.postureLabel = QLabel(self.layoutWidget2)
        self.postureLabel.setObjectName(u"postureLabel")
        self.postureLabel.setFont(font)

        self.horizontalLayout_8.addWidget(self.postureLabel)

        self.layoutWidget3 = QWidget(Form)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(480, 740, 271, 71))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_13)

        self.label_17 = QLabel(self.layoutWidget3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_17)

        self.img_label_1 = QLabel(Form)
        self.img_label_1.setObjectName(u"img_label_1")
        self.img_label_1.setGeometry(QRect(90, 70, 771, 311))
        self.img_label_1.setAlignment(Qt.AlignCenter)
        self.armangle_2 = QLabel(Form)
        self.armangle_2.setObjectName(u"armangle_2")
        self.armangle_2.setGeometry(QRect(520, 440, 191, 71))
        self.armangle_2.setFont(font)
        self.line_5 = QFrame(Form)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(780, 420, 20, 441))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(740, 30, 101, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(910, 450, 191, 41))
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(870, 550, 67, 17))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"AI CPR ", None))
        self.startVideo.setText(QCoreApplication.translate("Form", u"\u958b\u59cb\u5075\u6e2c", None))
        self.stopVideo.setText(QCoreApplication.translate("Form", u"\u7d50\u675f\u5075\u6e2c", None))
        self.exit_btn.setText(QCoreApplication.translate("Form", u"\u96e2\u958b", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7de8\u865f", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">CPR Screen</span></p></body></html>", None))
        self.armangle.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u624b\u81c2\u89d2\u5ea6 </p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5de6\u624b", None))
        self.left_hand.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400;\">\u5c1a\u672a\u958b\u59cb\u5075\u6e2c</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u53f3\u624b", None))
        self.right_hand.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400;\">\u5c1a\u672a\u958b\u59cb\u5075\u6e2c</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6df1\u5ea6", None))
        self.depthLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400;\">\u5c1a\u672a\u958b\u59cb\u5075\u6e2c</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u983b\u7387", None))
        self.frequencyLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:400;\">\u5c1a\u672a\u958b\u59cb\u5075\u6e2c</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">Posture</span></p></body></html>", None))
        self.postureLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#000000;\">Normal</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">Position</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#000000;\">Normal</span></p></body></html>", None))
        self.img_label_1.setText(QCoreApplication.translate("Form", u"img_label_1", None))
        self.armangle_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6309\u58d3\u8cc7\u8a0a</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Round</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">1</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700;\">Test result</span></p></body></html>", None))
        self.label_9.setText("")
    # retranslateUi

