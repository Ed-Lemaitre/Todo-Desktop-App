from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QHBoxLayout,
    QFrame,
)
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QGraphicsDropShadowEffect
from views.main_window import MainWindow
from controllers.add_window import AddWindowForm


class MainWindowForm(QWidget, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.remove_default_title_bar()
        self.menu_frame.mouseMoveEvent = self.move_window_with_mouse
        self.set_central_widget_shadow()
        self.title_buttons_actions()
        self.form_buttons_actions()

    def remove_default_title_bar(self):
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlag(Qt.FramelessWindowHint)

    def mousePressEvent(self, event):
        self.drag_pos = event.globalPos()

    def move_window_with_mouse(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() + self.pos() - self.drag_pos)
            self.drag_pos = event.globalPos()

    def set_central_widget_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor("#000000")
        self.cental_widget_frame.setGraphicsEffect(shadow)

    def minimize_button_action(self):
        self.showMinimized()

    def maximize_button_action(self):
        self.showNormal()
        self.restore_button.setVisible(True)

    def restore_button_action(self):
        self.showMaximized()
        self.restore_button.setVisible(False)

    def close_button_action(self):
        self.close()

    def add_button_action(self):
        self.active_list_widget.addItem("add_button_action")
        self.window = AddWindowForm()
        self.window.show()

    def title_buttons_actions(self):
        self.restore_button.clicked.connect(self.restore_button_action)
        self.maximize_button.clicked.connect(self.maximize_button_action)
        self.minimize_button.clicked.connect(self.minimize_button_action)
        self.close_button.clicked.connect(self.close_button_action)
        self.add_button.clicked.connect(self.add_button_action)

    def form_buttons_actions(self):
        self.active_estate_button.clicked.connect(self.active_estate_button_action)
        self.active_delete_button.clicked.connect(self.active_delete_button_action)
        self.active_modify_button.clicked.connect(self.active_modify_button_action)
        self.inactive_activate_all_button.clicked.connect(
            self.inactive_activate_all_button_action
        )
        self.inactive_activate_selected_button.clicked.connect(
            self.inactive_activate_selected_button_action
        )

    def active_estate_button_action(self):
        self.active_list_widget.addItem("active_estate_button")

    def active_delete_button_action(self):
        valor = self.active_list_widget.takeItem(self.active_list_widget.currentRow())
        print(repr(valor))

    def active_modify_button_action(self):
        self.active_list_widget.addItem("active_modify_button")

    def inactive_activate_all_button_action(self):
        self.inactive_list_widget.addItem("inactive_activate_all_button")

    def inactive_activate_selected_button_action(self):
        self.inactive_list_widget.addItem("inactive_activate_selected_button")
