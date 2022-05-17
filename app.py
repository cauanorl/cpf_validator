import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
)

import validate_cpf as f_cpf
from design import Ui_MainWindow


class ValidarCPF(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.color_green = "color: green;"
        self.color_red = 'color: red;'
        self.style_label = f"border: 1px solid black;\n" \
                            "border-radius: 5px;\n" \
                            "background-color: white;\n" \
                            "font-size: 35px;\n"

        self.btnValidate.clicked.connect(self.validar)
        self.btnGenerator.clicked.connect(self.gerar)
        self.setFixedSize(700, 150)
    
    def validar(self):
        cpf_bool = f_cpf.validateCPF(self.inputCpf.text())
        if cpf_bool:
            self.labelCpf.setStyleSheet(
                self.style_label + self.color_green)
            self.labelCpf.setText('Válido')
        else:
            self.labelCpf.setText('Inválido')
            self.labelCpf.setStyleSheet(
                self.style_label + self.color_red)
    
    def gerar(self):
        self.labelCpf.setStyleSheet(self.style_label + self.color_green)
        self.labelCpf.setText(f_cpf.generatorCPF())


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = ValidarCPF()
    app.show()
    qt.exec_()
