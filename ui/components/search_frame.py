# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon

class SearchFrame(QWidget):
    """사용자 검색 컴포넌트"""
    
    # 검색 신호 정의
    search_triggered = pyqtSignal(str, str)  # 검색어, 검색 타입
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        # 레이아웃 설정
        search_layout = QHBoxLayout(self)
        search_layout.setContentsMargins(0, 0, 0, 0)
        search_layout.setSpacing(10)
        
        # 검색 필드 레이블
        search_label = QLabel("검색:")
        search_label.setFixedWidth(40)
        search_layout.addWidget(search_label)
        
        # 검색 타입 선택 (ID 또는 이름)
        self.search_type = QComboBox()
        self.search_type.addItems(["ID", "이름"])
        self.search_type.setFixedWidth(80)
        self.search_type.setStyleSheet("""
            QComboBox {
                border: 1px solid #ccc;
                border-radius: 2px;
                padding: 5px;
                background-color: white;
            }
            QComboBox::drop-down {
                border: 0px;
            }
            QComboBox::down-arrow {
                image: url(down_arrow.png);
                width: 12px;
                height: 12px;
            }
        """)
        search_layout.addWidget(self.search_type)
        
        # 검색 입력 필드
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("검색어 입력...")
        self.search_input.setMinimumHeight(35)
        self.search_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 2px;
                padding: 5px 10px;
                background-color: white;
            }
            QLineEdit:focus {
                border: 1px solid #0078d7;
            }
        """)
        
        # 엔터 키로 검색 실행
        self.search_input.returnPressed.connect(self.trigger_search)
        
        search_layout.addWidget(self.search_input)
        
        # 검색 버튼
        self.search_button = QPushButton("검색")
        self.search_button.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_FileDialogContentsView))
        self.search_button.setMinimumHeight(35)
        self.search_button.setFixedWidth(80)
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #0078d7;
                color: white;
                border: none;
                padding: 6px 12px;
                font-weight: bold;
                border-radius: 2px;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
            QPushButton:pressed {
                background-color: #004c82;
            }
        """)
        self.search_button.clicked.connect(self.trigger_search)
        search_layout.addWidget(self.search_button)
        
        # 초기화 버튼 (검색 필터 해제)
        self.reset_button = QPushButton("초기화")
        self.reset_button.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_DialogResetButton))
        self.reset_button.setMinimumHeight(35)
        self.reset_button.setFixedWidth(80)
        self.reset_button.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                color: #333;
                border: 1px solid #ccc;
                padding: 6px 12px;
                font-weight: bold;
                border-radius: 2px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)
        self.reset_button.clicked.connect(self.reset_search)
        search_layout.addWidget(self.reset_button)
        
        # 우측 여백 조정
        search_layout.addStretch(1)
    
    def trigger_search(self):
        """검색 실행"""
        search_text = self.search_input.text().strip()
        search_type_idx = self.search_type.currentIndex()
        search_type = "id" if search_type_idx == 0 else "name"
        
        self.search_triggered.emit(search_text, search_type)
    
    def reset_search(self):
        """검색 초기화"""
        self.search_input.clear()
        # 빈 검색어로 검색 트리거하여 전체 목록 표시
        self.search_triggered.emit("", "")