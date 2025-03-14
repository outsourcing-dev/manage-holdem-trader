# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QDateEdit, QFrame
from PyQt6.QtCore import QDate, Qt
from config.settings import APP_SETTINGS
from ui.styles import (INPUT_FRAME_STYLE, INPUT_TITLE_STYLE, 
                       INPUT_LABEL_STYLE, INPUT_FIELD_STYLE)

class InputFrame(QWidget):
    """사용자 정보 입력 프레임"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        # 스타일 설정
        self.setStyleSheet(INPUT_FRAME_STYLE)
        self.setMinimumHeight(180)
        
        # 메인 레이아웃 설정 - 여백 최소화
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(5, 5, 5, 5)
        
        # 정보 입력 타이틀
        input_title = QLabel("사용자 정보 입력")
        input_title.setStyleSheet(INPUT_TITLE_STYLE)
        input_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(input_title)
        
        # 입력 필드 레이아웃 (중앙 정렬)
        fields_layout = QHBoxLayout()
        fields_layout.setSpacing(30)
        fields_layout.setContentsMargins(0, 0, 0, 0)
        
        # 왼쪽 여백
        fields_layout.addStretch(1)
        
        # ID 입력 - 직접 레이아웃에 추가
        id_layout = QVBoxLayout()
        id_layout.setSpacing(5)  # 간격 축소
        id_layout.setContentsMargins(0, 0, 0, 0)
        
        id_label = QLabel('아이디')
        id_label.setStyleSheet(INPUT_LABEL_STYLE)
        id_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText('사용자 ID 입력')
        self.id_input.setMinimumWidth(180)
        self.id_input.setMinimumHeight(35)
        self.id_input.setStyleSheet(INPUT_FIELD_STYLE)
        
        id_layout.addWidget(id_label)
        id_layout.addWidget(self.id_input)
        fields_layout.addLayout(id_layout)  # 레이아웃 직접 추가
        
        # 비밀번호 입력 - 직접 레이아웃에 추가
        pw_layout = QVBoxLayout()
        pw_layout.setSpacing(5)  # 간격 축소
        pw_layout.setContentsMargins(0, 0, 0, 0)
        
        pw_label = QLabel('비밀번호')
        pw_label.setStyleSheet(INPUT_LABEL_STYLE)
        pw_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('비밀번호 입력')
        self.password_input.setMinimumWidth(180)
        self.password_input.setMinimumHeight(35)
        self.password_input.setStyleSheet(INPUT_FIELD_STYLE)
        
        pw_layout.addWidget(pw_label)
        pw_layout.addWidget(self.password_input)
        fields_layout.addLayout(pw_layout)  # 레이아웃 직접 추가
        
        # 사용 기간 입력 - 직접 레이아웃에 추가
        expiry_layout = QVBoxLayout()
        expiry_layout.setSpacing(5)  # 간격 축소
        expiry_layout.setContentsMargins(0, 0, 0, 0)
        
        expiry_label = QLabel('사용 기간 (종료일)')
        expiry_label.setStyleSheet(INPUT_LABEL_STYLE)
        expiry_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.expiry_input = QDateEdit()
        self.expiry_input.setCalendarPopup(True)
        self.expiry_input.setDate(QDate.currentDate().addDays(APP_SETTINGS['default_expiry_days']))
        self.expiry_input.setMinimumWidth(180)
        self.expiry_input.setMinimumHeight(35)
        self.expiry_input.setStyleSheet(INPUT_FIELD_STYLE)
        
        expiry_layout.addWidget(expiry_label)
        expiry_layout.addWidget(self.expiry_input)
        fields_layout.addLayout(expiry_layout)  # 레이아웃 직접 추가
        
        # 오른쪽 여백
        fields_layout.addStretch(1)
        
        # 필드 레이아웃을 메인 레이아웃에 추가
        main_layout.addLayout(fields_layout)
    
    def get_user_input(self):
        """사용자 입력 값 반환"""
        return {
            'user_id': self.id_input.text().strip(),
            'password': self.password_input.text(),
            'expiry_date': self.expiry_input.date().toString('yyyy-MM-dd')
        }
    
    def clear_inputs(self):
        """입력 필드 초기화"""
        self.id_input.clear()
        self.password_input.clear()
        self.expiry_input.setDate(QDate.currentDate().addDays(APP_SETTINGS['default_expiry_days']))
    
    def set_user_info(self, user_id, password, expiry_date_str):
        """사용자 정보 설정"""
        self.id_input.setText(user_id)
        self.password_input.setText(password)
        
        expiry_date = QDate.fromString(expiry_date_str, 'yyyy-MM-dd')
        self.expiry_input.setDate(expiry_date)