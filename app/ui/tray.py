from webbrowser import get

from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QTimer
from pathlib import Path
from threading import Thread
from app.config import load_config, save_config, get_icon
from app.core.mouse import jiggle_mouse
from app.ui.window import ConfigWindow


class TrayApp(QSystemTrayIcon):
    def __init__(self):
        self.config = load_config()
        self.theme = self.config.get("theme", {}).get("name", "default")

        self.icon_idle_path = get_icon(self.theme, "idle")
        self.icon_active_path = get_icon(self.theme, "active")
        self.interval = self.config.get("system", {}).get("mouse_interval", 30)
        
        self.window = None

        super().__init__(QIcon(self.icon_idle_path))

        self.setToolTip("CtrlAwake")

        # Estado
        self.running = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_tick)

        # Menú
        menu = QMenu()

        self.start_action = QAction("▶ Start")
        self.stop_action = QAction("⏹ Stop")
        self.exit_action = QAction("⏻ Exit")
        self.config_action = QAction("⚙️ Settings")

        self.start_action.triggered.connect(self.start)
        self.stop_action.triggered.connect(self.stop)
        self.exit_action.triggered.connect(self.exit_app)
        self.config_action.triggered.connect(self.open_config)

        self.stop_action.setEnabled(False)

        menu.addAction(self.start_action)
        menu.addAction(self.stop_action)
        menu.addSeparator()
        menu.addAction(self.config_action)
        menu.addAction(self.exit_action)

        self.setContextMenu(menu)

    def start(self):
        if self.running:
            return
        self.running = True
        self.timer.start(self.interval) * 1000 
        self.start_action.setEnabled(False)
        self.stop_action.setEnabled(True)
        self.setToolTip("CtrlAwake — Active")        
        self.setIcon(QIcon(self.icon_active_path))

    def stop(self):
        if not self.running:
            return
        self.running = False
        self.timer.stop()
        self.start_action.setEnabled(True)
        self.stop_action.setEnabled(False)
        self.setToolTip("CtrlAwake — Paused")
        self.setIcon(QIcon(self.icon_idle_path))

    def open_config(self):
        self.window = ConfigWindow(self)
        self.window.show()
        self.window.center()
        self.window.raise_()
        self.window.activateWindow()

    def on_tick(self):
        Thread(target=jiggle_mouse, daemon=True).start()
    
    def set_theme(self, theme: str):
        self.theme = theme
        self.icon_idle_path = get_icon(theme, "idle")
        self.icon_active_path = get_icon(theme, "active")

        # refrescar icono actual
        if self.running:
            self.setIcon(QIcon(self.icon_active_path))
        else:
            self.setIcon(QIcon(self.icon_idle_path))

    def exit_app(self):
        self.timer.stop()
        self.hide()
        from PySide6.QtWidgets import QApplication
        QApplication.quit()