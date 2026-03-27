from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QSpinBox, QComboBox, QPushButton, QTabWidget
)
from PySide6.QtGui import QGuiApplication

#load tabs
from app.ui.tabs.general import GeneralTab
from app.ui.tabs.session import SessionTab
from app.ui.tabs.system import SystemTab
from app.ui.tabs.theme import ThemeTab

from app.config import save_config


class ConfigWindow(QWidget):
    def __init__(self, tray):
        super().__init__()

        self.tray = tray
        self.config = tray.config

        self.setWindowTitle("⚙️ CtrlAwake Settings")
        self.setFixedSize(500,200)

        layout = QVBoxLayout()

        self.tabs = QTabWidget()


        self.general_tab = GeneralTab(self.config)
        self.session_tab = SessionTab(self.config)
        self.system_tab = SystemTab(self.config)
        self.theme_tab = ThemeTab(self.config)

        self.tabs.addTab(self.general_tab, "🛠️ General")
        self.tabs.addTab(self.session_tab, "⏱️ Session")
        self.tabs.addTab(self.system_tab, "💻 System")
        self.tabs.addTab(self.theme_tab, "🎨 Theme")

        layout.addWidget(self.tabs)

        self.setLayout(layout)
    
    def center(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        window = self.frameGeometry()
        window.moveCenter(screen.center())
        self.move(window.topLeft())

    def save(self):
        new_config = {
            "interval": self.interval_input.value(),
            "mouse_move": self.mouse_move_input.value(),
            "theme": self.theme_select.currentText()
        }

        save_config(new_config)

        # aplicar en caliente
        self.tray.config = new_config
        self.tray.interval = new_config["interval"]
        self.tray.mouse_move = new_config["mouse_move"]
        self.tray.set_theme(new_config["theme"])

        if self.tray.running:
            self.tray.timer.stop()
            self.tray.timer.start(self.tray.interval * 1000)

        self.close()