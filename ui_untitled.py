# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSplitter, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(419, 474)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.splitter.addWidget(self.label)
        self.tuess = QLineEdit(self.splitter)
        self.tuess.setObjectName(u"tuess")
        self.splitter.addWidget(self.tuess)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 2)

        self.splitter_3 = QSplitter(Form)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_3 = QLabel(self.splitter_3)
        self.label_3.setObjectName(u"label_3")
        self.splitter_3.addWidget(self.label_3)
        self.times = QLineEdit(self.splitter_3)
        self.times.setObjectName(u"times")
        self.splitter_3.addWidget(self.times)

        self.gridLayout.addWidget(self.splitter_3, 2, 0, 1, 2)

        self.splitter_5 = QSplitter(Form)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.label_5 = QLabel(self.splitter_5)
        self.label_5.setObjectName(u"label_5")
        self.splitter_5.addWidget(self.label_5)
        self.result = QLineEdit(self.splitter_5)
        self.result.setObjectName(u"result")
        self.splitter_5.addWidget(self.result)

        self.gridLayout.addWidget(self.splitter_5, 8, 0, 1, 2)

        self.splitter_4 = QSplitter(Form)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(self.splitter_4)
        self.label_4.setObjectName(u"label_4")
        self.splitter_4.addWidget(self.label_4)
        self.people = QLineEdit(self.splitter_4)
        self.people.setObjectName(u"people")
        self.splitter_4.addWidget(self.people)

        self.gridLayout.addWidget(self.splitter_4, 7, 0, 1, 2)

        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.splitter_2.addWidget(self.label_2)
        self.end = QLineEdit(self.splitter_2)
        self.end.setObjectName(u"end")
        self.splitter_2.addWidget(self.end)

        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 2)

        self.begin = QPushButton(Form)
        self.begin.setObjectName(u"begin")

        self.gridLayout.addWidget(self.begin, 9, 0, 1, 1)

        self.exit = QPushButton(Form)
        self.exit.setObjectName(u"exit")

        self.gridLayout.addWidget(self.exit, 9, 1, 1, 1)

        self.sure = QPushButton(Form)
        self.sure.setObjectName(u"sure")

        self.gridLayout.addWidget(self.sure, 4, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u731c\u731c\u770b", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8bd5\u731c\u6b21\u6570", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6e38\u620f\u7ed3\u679c", None))
        self.result.setText(QCoreApplication.translate("Form", u"\u7b49\u5f85\u6e38\u620f\u5f00\u59cb", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u4eba\u6570", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u731c\u6570\u7684\u7ed3\u679c", None))
        self.end.setText(QCoreApplication.translate("Form", u"\u7b49\u5f85\u6e38\u620f\u5f00\u59cb", None))
        self.begin.setText(QCoreApplication.translate("Form", u"\u6e38\u620f\u5f00\u59cb", None))
        self.exit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.sure.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
    # retranslateUi

