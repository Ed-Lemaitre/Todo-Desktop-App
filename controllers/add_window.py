from PySide2.QtWidgets import (
    QWidget,
)
from views.add_window import AddWindow

from database import todo


class AddWindowForm(QWidget, AddWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.agregar_button.clicked.connect(self.agregar_button_action)
        self.cancelar_button.clicked.connect(self.cancelar_button_action)

    def agregar_button_action(self):
        self.insert_todo()

    def cancelar_button_action(self):
        self.close()

    def insert_todo(self):
        # todo.insert(("hacerse amigo de juan", False))
        tarea = self.input_text.toPlainText()
        estado = False
        data = (tarea, estado)
        if tarea != "":
            if todo.insert(data):
                self.creation_msg_label.setText("Registro creado!!")
            else:
                self.creation_msg_label.setText("Error: no se pudo crear un registro")
        else:
            self.creation_msg_label.setText(
                "Registro no valido. Debe ingresar un texto"
            )
