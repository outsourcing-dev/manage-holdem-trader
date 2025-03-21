# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal
from ui.styles import BUTTON_STYLE, DELETE_BUTTON_STYLE

class ButtonFrame(QWidget):
    """버튼 프레임 컴포넌트"""
    
    # 시그널 정의
    save_clicked = pyqtSignal()
    reset_clicked = pyqtSignal()
    delete_clicked = pyqtSignal()
    force_logout_clicked = pyqtSignal()  # 새로운 시그널 추가

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        # 레이아웃 설정
        button_layout = QHBoxLayout(self)
        button_layout.setContentsMargins(0, 5, 0, 5)
        button_layout.setSpacing(10)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # 저장 버튼
        self.save_button = QPushButton('저장')
        self.save_button.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_DialogSaveButton))
        self.save_button.setMinimumHeight(50)
        self.save_button.setFixedWidth(120)
        self.save_button.clicked.connect(self.save_clicked.emit)
        button_layout.addWidget(self.save_button)
        
        # 비밀번호 초기화 버튼
        self.reset_password_button = QPushButton('비밀번호 초기화')
        self.reset_password_button.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_BrowserReload))
        self.reset_password_button.setMinimumHeight(50)
        self.reset_password_button.setFixedWidth(140)
        self.reset_password_button.clicked.connect(self.reset_clicked.emit)
        button_layout.addWidget(self.reset_password_button)
        
        # 사용자 삭제 버튼
        self.delete_button = QPushButton('사용자 삭제')
        self.delete_button.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_TrashIcon))
        self.delete_button.setMinimumHeight(50)
        self.delete_button.setFixedWidth(120)
        self.delete_button.setStyleSheet('background-color: #d9534f;')
        self.delete_button.clicked.connect(self.delete_clicked.emit)
        button_layout.addWidget(self.delete_button)
        
        self.force_logout_button = QPushButton('강제 로그아웃')
        self.force_logout_button.setMinimumHeight(50)
        self.force_logout_button.setFixedWidth(120)
        # button_frame.py에서 스타일시트 수정
        self.force_logout_button.setStyleSheet("""
            QPushButton {
                background-color: #FF6B6B;
                color: white;
                border: none;
                padding: 6px 12px;
                font-weight: bold;
                border-radius: 2px;
            }
            QPushButton:hover {
                background-color: #FF5252;
            }
        """)
        self.force_logout_button.clicked.connect(self.force_logout_clicked.emit)
        button_layout.addWidget(self.force_logout_button)