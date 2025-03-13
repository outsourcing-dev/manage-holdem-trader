#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import UserManagementWindow

def main():
    app = QApplication(sys.argv)
    window = UserManagementWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()