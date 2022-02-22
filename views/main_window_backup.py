# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainWindow(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName("main_window")
        main_window.resize(1061, 826)
        main_window.setStyleSheet('font: 12pt "Karla";')
        self.verticalLayout = QVBoxLayout(main_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QFrame(main_window)
        self.background_frame.setObjectName("background_frame")
        self.background_frame.setMinimumSize(QSize(0, 0))
        self.background_frame.setStyleSheet("background-color: rgb(28, 101, 140);")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.background_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName("shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.cental_widget_frame = QFrame(self.background_frame)
        self.cental_widget_frame.setObjectName("cental_widget_frame")
        self.cental_widget_frame.setMinimumSize(QSize(800, 340))
        self.cental_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.cental_widget_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.cental_widget_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.menu_frame = QFrame(self.cental_widget_frame)
        self.menu_frame.setObjectName("menu_frame")
        self.menu_frame.setMinimumSize(QSize(300, 50))
        self.menu_frame.setMaximumSize(QSize(16777215, 50))
        self.menu_frame.setStyleSheet("background-color: rgb(57, 138, 185);\n" "")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.menu_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.menu_title_label = QLabel(self.menu_frame)
        self.menu_title_label.setObjectName("menu_title_label")
        self.menu_title_label.setMinimumSize(QSize(0, 40))
        self.menu_title_label.setMaximumSize(QSize(16777215, 40))
        self.menu_title_label.setStyleSheet(
            'font: 63 24pt "Karla SemiBold";\n' "color: #EEEEEE"
        )

        self.horizontalLayout.addWidget(self.menu_title_label)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_button = QPushButton(self.menu_frame)
        self.add_button.setObjectName("add_button")
        self.add_button.setMinimumSize(QSize(0, 40))
        self.add_button.setMaximumSize(QSize(16777215, 40))
        self.add_button.setStyleSheet(
            'font: 63 16pt "Karla SemiBold";\n' "color: #EEEEEE"
        )

        self.horizontalLayout.addWidget(self.add_button)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.menu_btn_holder_frame = QFrame(self.menu_frame)
        self.menu_btn_holder_frame.setObjectName("menu_btn_holder_frame")
        self.menu_btn_holder_frame.setEnabled(True)
        self.menu_btn_holder_frame.setMinimumSize(QSize(110, 40))
        self.menu_btn_holder_frame.setMaximumSize(QSize(16777215, 40))
        self.menu_btn_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_btn_holder_frame.setFrameShadow(QFrame.Raised)
        self.close_tool_button = QToolButton(self.menu_btn_holder_frame)
        self.close_tool_button.setObjectName("close_tool_button")
        self.close_tool_button.setGeometry(QRect(80, 10, 30, 30))
        self.close_tool_button.setMinimumSize(QSize(0, 0))
        self.close_tool_button.setLayoutDirection(Qt.LeftToRight)
        self.close_tool_button.setAutoFillBackground(False)
        self.close_tool_button.setStyleSheet("")
        icon = QIcon()
        icon.addFile("./assets/close_icon.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.close_tool_button.setIcon(icon)
        self.close_tool_button.setIconSize(QSize(30, 30))
        self.maximize_button = QToolButton(self.menu_btn_holder_frame)
        self.maximize_button.setObjectName("maximize_button")
        self.maximize_button.setGeometry(QRect(40, 10, 30, 30))
        self.maximize_button.setMinimumSize(QSize(0, 0))
        self.maximize_button.setLayoutDirection(Qt.LeftToRight)
        self.maximize_button.setAutoFillBackground(False)
        self.maximize_button.setStyleSheet("")
        icon1 = QIcon()
        icon1.addFile("./assets/maximize_icon.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon1)
        self.maximize_button.setIconSize(QSize(30, 30))
        self.restore_button = QToolButton(self.menu_btn_holder_frame)
        self.restore_button.setObjectName("restore_button")
        self.restore_button.setGeometry(QRect(40, 10, 30, 30))
        self.restore_button.setMinimumSize(QSize(0, 0))
        self.restore_button.setLayoutDirection(Qt.LeftToRight)
        self.restore_button.setAutoFillBackground(False)
        self.restore_button.setStyleSheet("")
        icon2 = QIcon()
        icon2.addFile("./assets/restore_icon.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon2)
        self.restore_button.setIconSize(QSize(30, 30))
        self.minimize_button = QToolButton(self.menu_btn_holder_frame)
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.setGeometry(QRect(0, 10, 30, 30))
        self.minimize_button.setMinimumSize(QSize(0, 0))
        self.minimize_button.setLayoutDirection(Qt.LeftToRight)
        self.minimize_button.setAutoFillBackground(False)
        self.minimize_button.setStyleSheet("")
        icon3 = QIcon()
        icon3.addFile("./assets/minimize_icon.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon3)
        self.minimize_button.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.menu_btn_holder_frame)

        self.verticalLayout_2.addWidget(self.menu_frame)

        self.active_todos_frame = QFrame(self.cental_widget_frame)
        self.active_todos_frame.setObjectName("active_todos_frame")
        self.active_todos_frame.setMinimumSize(QSize(0, 0))
        self.active_todos_frame.setStyleSheet("background-color: rgb(216, 210, 203);")
        self.active_todos_frame.setFrameShape(QFrame.StyledPanel)
        self.active_todos_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.active_todos_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.active_menu_frame = QFrame(self.active_todos_frame)
        self.active_menu_frame.setObjectName("active_menu_frame")
        self.active_menu_frame.setMinimumSize(QSize(0, 60))
        self.active_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.active_menu_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.active_menu_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.active_label = QLabel(self.active_menu_frame)
        self.active_label.setObjectName("active_label")

        self.horizontalLayout_2.addWidget(self.active_label)

        self.active_estate_button = QPushButton(self.active_menu_frame)
        self.active_estate_button.setObjectName("active_estate_button")
        self.active_estate_button.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.active_estate_button)

        self.active_delete_button = QPushButton(self.active_menu_frame)
        self.active_delete_button.setObjectName("active_delete_button")
        self.active_delete_button.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.active_delete_button)

        self.active_modify_button = QPushButton(self.active_menu_frame)
        self.active_modify_button.setObjectName("active_modify_button")
        self.active_modify_button.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.active_modify_button)

        self.verticalLayout_3.addWidget(self.active_menu_frame)

        self.active_scroll_area = QScrollArea(self.active_todos_frame)
        self.active_scroll_area.setObjectName("active_scroll_area")
        self.active_scroll_area.setWidgetResizable(True)
        self.content_active_scroll_area = QWidget()
        self.content_active_scroll_area.setObjectName("content_active_scroll_area")
        self.content_active_scroll_area.setGeometry(QRect(0, 0, 989, 355))
        self.verticalLayout_5 = QVBoxLayout(self.content_active_scroll_area)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.active_list_widget = QListWidget(self.content_active_scroll_area)
        self.active_list_widget.setObjectName("active_list_widget")

        self.verticalLayout_5.addWidget(self.active_list_widget)

        self.active_scroll_area.setWidget(self.content_active_scroll_area)

        self.verticalLayout_3.addWidget(self.active_scroll_area)

        self.verticalLayout_2.addWidget(self.active_todos_frame)

        self.inactive_todos_frame = QFrame(self.cental_widget_frame)
        self.inactive_todos_frame.setObjectName("inactive_todos_frame")
        self.inactive_todos_frame.setStyleSheet("background-color: rgb(216, 210, 203);")
        self.inactive_todos_frame.setFrameShape(QFrame.StyledPanel)
        self.inactive_todos_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.inactive_todos_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.inactive_menu_frame = QFrame(self.inactive_todos_frame)
        self.inactive_menu_frame.setObjectName("inactive_menu_frame")
        self.inactive_menu_frame.setMinimumSize(QSize(0, 60))
        self.inactive_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.inactive_menu_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.inactive_menu_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.inactive_label = QLabel(self.inactive_menu_frame)
        self.inactive_label.setObjectName("inactive_label")

        self.horizontalLayout_3.addWidget(self.inactive_label)

        self.inactive_activate_all_button = QPushButton(self.inactive_menu_frame)
        self.inactive_activate_all_button.setObjectName("inactive_activate_all_button")
        self.inactive_activate_all_button.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_3.addWidget(self.inactive_activate_all_button)

        self.inactive_activate_selected_button = QPushButton(self.inactive_menu_frame)
        self.inactive_activate_selected_button.setObjectName(
            "inactive_activate_selected_button"
        )
        self.inactive_activate_selected_button.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_3.addWidget(self.inactive_activate_selected_button)

        self.verticalLayout_4.addWidget(self.inactive_menu_frame)

        self.inactive_scroll_area = QScrollArea(self.inactive_todos_frame)
        self.inactive_scroll_area.setObjectName("inactive_scroll_area")
        self.inactive_scroll_area.setWidgetResizable(True)
        self.content_inactive_scroll_area = QWidget()
        self.content_inactive_scroll_area.setObjectName("content_inactive_scroll_area")
        self.content_inactive_scroll_area.setGeometry(QRect(0, 0, 989, 175))
        self.verticalLayout_6 = QVBoxLayout(self.content_inactive_scroll_area)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.inactive_list_widget = QListWidget(self.content_inactive_scroll_area)
        self.inactive_list_widget.setObjectName("inactive_list_widget")

        self.verticalLayout_6.addWidget(self.inactive_list_widget)

        self.inactive_scroll_area.setWidget(self.content_inactive_scroll_area)

        self.verticalLayout_4.addWidget(self.inactive_scroll_area)

        self.verticalLayout_2.addWidget(self.inactive_todos_frame)

        self.verticalLayout_2.setStretch(1, 5)
        self.verticalLayout_2.setStretch(2, 3)

        self.shadow_layout.addWidget(self.cental_widget_frame)

        self.verticalLayout.addWidget(self.background_frame)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)

    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(
            QCoreApplication.translate("main_window", "Form", None)
        )
        self.menu_title_label.setText(
            QCoreApplication.translate("main_window", "LISTA TAREAS", None)
        )
        self.add_button.setText(
            QCoreApplication.translate("main_window", "Agregar Tarea", None)
        )
        self.close_tool_button.setText("")
        self.maximize_button.setText("")
        self.restore_button.setText("")
        self.minimize_button.setText("")
        self.active_label.setText(
            QCoreApplication.translate("main_window", "PENDIENTES", None)
        )
        self.active_estate_button.setText(
            QCoreApplication.translate("main_window", "Cambiar Estado", None)
        )
        self.active_delete_button.setText(
            QCoreApplication.translate("main_window", "Borrar Tarea", None)
        )
        self.active_modify_button.setText(
            QCoreApplication.translate("main_window", "Modificar Tarea", None)
        )
        self.inactive_label.setText(
            QCoreApplication.translate("main_window", "FINALIZADAS", None)
        )
        self.inactive_activate_all_button.setText(
            QCoreApplication.translate("main_window", "Activar Todas", None)
        )
        self.inactive_activate_selected_button.setText(
            QCoreApplication.translate("main_window", "Activar Seleccionadas", None)
        )

    # retranslateUi
