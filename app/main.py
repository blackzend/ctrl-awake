import sys
from PySide6.QtWidgets import QApplication
from app.ui.tray import TrayApp

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    tray = TrayApp()
    tray.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()