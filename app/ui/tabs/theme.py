from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QComboBox, QCheckBox
)


class ThemeTab(QWidget):
    def __init__(self, config):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Tema"))

        self.theme = QComboBox()
        self.theme.addItems(["default", "eye", "ghost"])
        self.theme.setCurrentText(config["theme"].get("name", "default"))

        layout.addWidget(self.theme)

        self.show_time = QCheckBox("Mostrar tiempo transcurrido")
        self.show_time.setChecked(
            config["theme"].get("show_elapsed", False)
        )

        layout.addWidget(self.show_time)

        self.setLayout(layout)