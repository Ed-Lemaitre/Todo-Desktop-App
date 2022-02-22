# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class AddWindow(object):
    def setupUi(self, AddWindow):
        if not AddWindow.objectName():
            AddWindow.setObjectName("AddWindow")
        AddWindow.resize(648, 540)
        AddWindow.setMinimumSize(QSize(648, 540))
        AddWindow.setMaximumSize(QSize(648, 540))
        self.background_frame = QFrame(AddWindow)
        self.background_frame.setObjectName("background_frame")
        self.background_frame.setGeometry(QRect(0, 0, 648, 540))
        self.background_frame.setMinimumSize(QSize(648, 540))
        self.background_frame.setMaximumSize(QSize(750, 540))
        self.background_frame.setStyleSheet("background-color: rgb(28, 101, 140);")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.central_frame = QFrame(self.background_frame)
        self.central_frame.setObjectName("central_frame")
        self.central_frame.setGeometry(QRect(12, 12, 624, 516))
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.title_frame = QFrame(self.central_frame)
        self.title_frame.setObjectName("title_frame")
        self.title_frame.setGeometry(QRect(12, 12, 600, 80))
        self.title_frame.setMinimumSize(QSize(600, 80))
        self.title_frame.setMaximumSize(QSize(600, 80))
        self.title_frame.setLayoutDirection(Qt.LeftToRight)
        self.title_frame.setStyleSheet("background-color: #398AB9;")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.title_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title_label = QLabel(self.title_frame)
        self.title_label.setObjectName("title_label")
        self.title_label.setStyleSheet(
            "color: rgb(216, 210, 203);\n" 'font: 81 22pt "Karla ExtraBold";'
        )
        self.title_label.setScaledContents(False)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.title_label)

        self.buton_frame = QFrame(self.central_frame)
        self.buton_frame.setObjectName("buton_frame")
        self.buton_frame.setGeometry(QRect(10, 400, 600, 40))
        self.buton_frame.setMinimumSize(QSize(600, 40))
        self.buton_frame.setMaximumSize(QSize(600, 40))
        self.buton_frame.setFrameShape(QFrame.StyledPanel)
        self.buton_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.buton_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.agregar_button = QPushButton(self.buton_frame)
        self.agregar_button.setObjectName("agregar_button")
        self.agregar_button.setMinimumSize(QSize(100, 30))
        self.agregar_button.setMaximumSize(QSize(100, 30))
        self.agregar_button.setStyleSheet(
            "QPushButton{\n"
            "color: rgb(216, 210, 203);\n"
            "}\n"
            "QPushButton:hover{\n"
            "color: rgb(0,0,0);\n"
            "background-color: rgb(216, 210, 203);\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.agregar_button)

        self.cancelar_button = QPushButton(self.buton_frame)
        self.cancelar_button.setObjectName("cancelar_button")
        self.cancelar_button.setMinimumSize(QSize(100, 30))
        self.cancelar_button.setMaximumSize(QSize(100, 30))
        self.cancelar_button.setStyleSheet(
            "QPushButton{\n"
            "color: rgb(216, 210, 203);\n"
            "}\n"
            "QPushButton:hover{\n"
            "color: rgb(0,0,0);\n"
            "background-color: rgb(216, 210, 203);\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.cancelar_button)

        self.text_frame = QFrame(self.central_frame)
        self.text_frame.setObjectName("text_frame")
        self.text_frame.setGeometry(QRect(12, 99, 600, 290))
        self.text_frame.setMinimumSize(QSize(600, 290))
        self.text_frame.setMaximumSize(QSize(600, 290))
        self.text_frame.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.text_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_text = QPlainTextEdit(self.text_frame)
        self.input_text.setObjectName("input_text")

        self.horizontalLayout.addWidget(self.input_text)

        self.creation_msg_label = QLabel(self.central_frame)
        self.creation_msg_label.setObjectName("creation_msg_label")
        self.creation_msg_label.setGeometry(QRect(20, 470, 591, 20))
        self.creation_msg_label.setStyleSheet("color: rgb(255, 255, 0);")
        self.creation_msg_label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(AddWindow)

        QMetaObject.connectSlotsByName(AddWindow)

    # setupUi

    def retranslateUi(self, AddWindow):
        AddWindow.setWindowTitle(QCoreApplication.translate("AddWindow", "Form", None))
        self.title_label.setText(
            QCoreApplication.translate("AddWindow", "AGREGAR TAREA", None)
        )
        self.agregar_button.setText(
            QCoreApplication.translate("AddWindow", "AGREGAR", None)
        )
        self.cancelar_button.setText(
            QCoreApplication.translate("AddWindow", "CANCELAR", None)
        )
        self.creation_msg_label.setText("")

    # retranslateUi
