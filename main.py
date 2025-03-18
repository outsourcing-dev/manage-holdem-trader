#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import traceback
from PyQt6.QtWidgets import QApplication, QMessageBox
from ui.main_window import UserManagementWindow

def main():
    app = QApplication(sys.argv)
    
    try:
        window = UserManagementWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        error_msg = f"프로그램 실행 중 오류가 발생했습니다:\n{str(e)}\n\n{traceback.format_exc()}"
        print(error_msg)
        
        # 그래픽 인터페이스가 작동하지 않을 수 있으므로 터미널에도 출력
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Critical)
        msgBox.setWindowTitle("오류")
        msgBox.setText("프로그램 실행 오류")
        msgBox.setDetailedText(error_msg)
        msgBox.exec()

if __name__ == '__main__':
    main()