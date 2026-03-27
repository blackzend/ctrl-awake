from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QCheckBox,
    QLabel, QComboBox
)


class SystemTab(QWidget):
    def __init__(self, config):
        super().__init__()

        layout = QVBoxLayout()

        self.mouse_enabled = QCheckBox("Mover mouse")
        self.mouse_enabled.setChecked(
            config["system"].get("mouse_enabled", True)
        )

        layout.addWidget(self.mouse_enabled)

        layout.addWidget(QLabel("Cada:"))

        self.interval = QComboBox()
        self.interval.addItems(["5s", "10s", "15s", "30s", "1m", "2m"])
        layout.addWidget(self.interval)

        layout.addWidget(QLabel("Después de inactividad:"))

        self.idle = QComboBox()
        self.idle.addItems(["30s", "1m", "2m", "5m"])
        layout.addWidget(self.idle)

        self.setLayout(layout)