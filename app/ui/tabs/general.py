from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox


class GeneralTab(QWidget):
    def __init__(self, config):
        super().__init__()

        layout = QVBoxLayout()

        self.start_login = QCheckBox("Iniciar al login")
        self.start_login.setChecked(config.get("start_on_login", False))

        self.auto_start = QCheckBox("Iniciar sesión al iniciar")
        self.auto_start.setChecked(config.get("auto_start_session", False))

        layout.addWidget(self.start_login)
        layout.addWidget(self.auto_start)

        self.setLayout(layout)