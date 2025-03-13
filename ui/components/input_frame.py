# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QDateEdit
from PyQt6.QtCore import QDate
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
        
        # 레이아웃 설정
        input_layout = QVBoxLayout(self)
        input_layout.setSpacing(15)
        
        # 정보 입력 타이틀
        input_title = QLabel("사용자 정보 입력")
        input_title.setStyleSheet(INPUT_TITLE_STYLE)
        input_layout.addWidget(input_title)
        
        # 필드 컨테이너 (행 형태로 정렬)
        fields_container = QWidget()
        fields_layout = QHBoxLayout(fields_container)
        fields_layout.setSpacing(30)
        
        # ID 입력
        id_container = QWidget()
        id_layout = QVBoxLayout(id_container)
        id_layout.setSpacing(8)
        id_label = QLabel('아이디')
        id_label.setStyleSheet(INPUT_LABEL_STYLE)
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText('사용자 ID 입력')
        self.id_input.setMinimumWidth(180)
        self.id_input.setMinimumHeight(35)
        self.id_input.setStyleSheet(INPUT_FIELD_STYLE)
        id_layout.addWidget(id_label)
        id_layout.addWidget(self.id_input)
        fields_layout.addWidget(id_container)
        
        # 비밀번호 입력
        pw_container = QWidget()
        pw_layout = QVBoxLayout(pw_container)
        pw_layout.setSpacing(8)
        pw_label = QLabel('비밀번호')
        pw_label.setStyleSheet(INPUT_LABEL_STYLE)
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('비밀번호 입력')
        self.password_input.setMinimumWidth(180)
        self.password_input.setMinimumHeight(35)
        self.password_input.setStyleSheet(INPUT_FIELD_STYLE)
        pw_layout.addWidget(pw_label)
        pw_layout.addWidget(self.password_input)
        fields_layout.addWidget(pw_container)
        
        # 사용 기간 입력
        expiry_container = QWidget()
        expiry_layout = QVBoxLayout(expiry_container)
        expiry_layout.setSpacing(8)
        expiry_label = QLabel('사용 기간 (종료일)')
        expiry_label.setStyleSheet(INPUT_LABEL_STYLE)
        self.expiry_input = QDateEdit()
        self.expiry_input.setCalendarPopup(True)
        # 기본값: 현재 날짜로부터 APP_SETTINGS에 정의된 일수만큼
        self.expiry_input.setDate(QDate.currentDate().addDays(APP_SETTINGS['default_expiry_days']))
        self.expiry_input.setMinimumWidth(180)
        self.expiry_input.setMinimumHeight(35)
        self.expiry_input.setStyleSheet(INPUT_FIELD_STYLE)
        expiry_layout.addWidget(expiry_label)
        expiry_layout.addWidget(self.expiry_input)
        fields_layout.addWidget(expiry_container)
        
        # 여백 추가
        fields_layout.addStretch(1)
        
        # 컨테이너를 메인 레이아웃에 추가
        input_layout.addWidget(fields_container)
    
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