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
        self.startVideo.setGeometry(QRect(990, 150, 180, 61))
        self.stopVideo = QPushButton(Form)
        self.stopVideo.setObjectName(u"stopVideo")
        self.stopVideo.setGeometry(QRect(990, 240, 180, 61))
        self.exit_btn = QPushButton(Form)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(990, 340, 180, 61))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(990, 66, 71, 21))
        self.Id = QTextEdit(Form)
        self.Id.setObjectName(u"Id")
        self.Id.setGeometry(QRect(1040, 60, 121, 31))
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 460, 1641, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(1320, 0, 20, 511))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(320, 0, 301, 81))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_20.setFont(font)
        self.armangle = QLabel(Form)
        self.armangle.setObjectName(u"armangle")
        self.armangle.setGeometry(QRect(110, 490, 191, 71))
        self.armangle.setFont(font)
        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(940, 0, 20, 471))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(50, 600, 79, 61))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu Condensed"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.left_hand = QLabel(Form)
        self.left_hand.setObjectName(u"left_hand")
        self.left_hand.setGeometry(QRect(90, 590, 311, 81))
        self.left_hand.setFont(font1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 730, 79, 51))
        self.label_3.setFont(font1)
        self.right_hand = QLabel(Form)
        self.right_hand.setObjectName(u"right_hand")
        self.right_hand.setGeometry(QRect(90, 720, 311, 71))
        self.right_hand.setFont(font1)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(450, 590, 271, 71))
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
        self.layoutWidget1.setGeometry(QRect(450, 720, 271, 71))
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

        self.img_label_1 = QLabel(Form)
        self.img_label_1.setObjectName(u"img_label_1")
        self.img_label_1.setGeometry(QRect(40, 70, 861, 381))
        self.img_label_1.setAlignment(Qt.AlignCenter)
        self.armangle_2 = QLabel(Form)
        self.armangle_2.setObjectName(u"armangle_2")
        self.armangle_2.setGeometry(QRect(490, 490, 191, 71))
        self.armangle_2.setFont(font)
        self.line_5 = QFrame(Form)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(760, 470, 20, 391))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(780, 20, 101, 41))
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
        self.label_8.setGeometry(QRect(890, 490, 191, 51))
        font3 = QFont()
        font3.setPointSize(24)
        font3.setItalic(True)
        self.label_8.setFont(font3)
        self.horizontalLayoutWidget_2 = QWidget(Form)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(840, 570, 281, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)

        self.deep_result = QLabel(self.horizontalLayoutWidget_2)
        self.deep_result.setObjectName(u"deep_result")

        self.horizontalLayout_2.addWidget(self.deep_result)

        self.horizontalLayoutWidget_3 = QWidget(Form)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(840, 633, 281, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.horizontalLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.frequency_result = QLabel(self.horizontalLayoutWidget_3)
        self.frequency_result.setObjectName(u"frequency_result")

        self.horizontalLayout_3.addWidget(self.frequency_result)

        self.horizontalLayoutWidget_4 = QWidget(Form)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(840, 700, 281, 54))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.horizontalLayoutWidget_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.poseture_result = QLabel(self.horizontalLayoutWidget_4)
        self.poseture_result.setObjectName(u"poseture_result")

        self.horizontalLayout_4.addWidget(self.poseture_result)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(870, 770, 231, 71))
        self.line_6 = QFrame(Form)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(380, 470, 20, 391))
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

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
        self.img_label_1.setText(QCoreApplication.translate("Form", u"img_label_1", None))
        self.armangle_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6309\u58d3\u8cc7\u8a0a</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Round</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">1</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; font-style:normal;\">CPR\u6e2c\u9a57\u7d50\u679c</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">\u6df1\u5ea6</span></p></body></html>", None))
        self.deep_result.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">\u983b\u7387</span></p></body></html>", None))
        self.frequency_result.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">\u59ff\u52e2</span></p></body></html>", None))
        self.poseture_result.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

