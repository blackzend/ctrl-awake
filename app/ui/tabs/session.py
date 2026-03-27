from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QComboBox, QSpinBox
)


class SessionTab(QWidget):
    def __init__(self, config):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Duración"))

        self.duration = QComboBox()
        self.duration.addItems([
            "Infinito", "5m", "10m", "15m", "30m",
            "1h", "2h", "3h", "24h", "Otro"
        ])

        layout.addWidget(self.duration)

        self.custom = QSpinBox()
        self.custom.setRange(1, 1440)
        self.custom.setSuffix(" min")
        layout.addWidget(self.custom)

        layout.addWidget(QLabel(
            "Click izquierdo inicia sesión default\nClick derecho muestra menú"
        ))

        self.setLayout(layout)