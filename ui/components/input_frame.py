# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QDateEdit, QFrame, QGridLayout
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
        self.setMinimumHeight(250)  # 높이 증가
        
        # 메인 레이아웃 설정 - 여백 최소화
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # # 정보 입력 타이틀
        # input_title = QLabel("사용자 정보 입력")
        # input_title.setStyleSheet(INPUT_TITLE_STYLE)
        # input_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # main_layout.addWidget(input_title)
        
        # 그리드 레이아웃 사용 - 2행 3열 구조
        grid_layout = QGridLayout()
        grid_layout.setSpacing(15)
        
        # 1행: ID, 이름, 전화번호
        # ID 입력
        id_label = QLabel('아이디')
        id_label.setStyleSheet("background-color: #e6f2ff; border-radius: 4px; padding: 5px; font-weight: bold; color: #333; border: 1px solid #cce0ff;")
        id_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        id_label.setFixedHeight(30)  # 레이블 높이 고정
        
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText('사용자 ID 입력')
        self.id_input.setMinimumWidth(150)
        self.id_input.setMinimumHeight(35)
        self.id_input.setStyleSheet(INPUT_FIELD_STYLE)
        
        grid_layout.addWidget(id_label, 0, 0)
        grid_layout.addWidget(self.id_input, 1, 0)
        
        # 이름 입력
        name_label = QLabel('이름')
        name_label.setStyleSheet("background-color: #e6f2ff; border-radius: 4px; padding: 5px; font-weight: bold; color: #333; border: 1px solid #cce0ff;")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setFixedHeight(30)  # 레이블 높이 고정
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('이름 입력')
        self.name_input.setMinimumWidth(150)
        self.name_input.setMinimumHeight(35)
        self.name_input.setStyleSheet(INPUT_FIELD_STYLE)
        
        grid_layout.addWidget(name_label, 0, 1)
        grid_layout.addWidget(self.name_input, 1, 1)
        
        # 전화번호 입력
        phone_label = QLabel('전화번호')
        phone_label.setStyleSheet("background-color: #e6f2ff; border-radius: 4px; padding: 5px; font-weight: bold; color: #333; border: 1px solid #cce0ff;")
        phone_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        phone_label.setFixedHeight(30)  # 레이블 높이 고정
        
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText('전화번호 입력')
        self.phone_input.setMinimumWidth(150)
        self.phone_input.setMinimumHeight(35)
        self.phone_input.setStyleSheet(INPUT_FIELD_STYLE)
        
        grid_layout.addWidget(phone_label, 0, 2)
        grid_layout.addWidget(self.phone_input, 1, 2)
        
        # 2행: 비밀번호, 추천인, 사용기간
        # 비밀번호 입력
        pw_label = QLabel('비밀번호')
        pw_label.setStyleSheet("background-color: #e6f2ff; border-radius: 4px; padding: 5px; font-weight: bold; color: #333; border: 1px solid #cce0ff;")
        pw_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pw_label.setFixedHeight(30)  # 레이블 높이 고정
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('비밀번호 입력')
        self.password_input.setMinimumWidth(150)
        self.password_input.setMinimumHeight(35)
        self.password_input.setStyleSheet(INPUT_FIELD_STYLE)
        
        grid_layout.addWidget(pw_label, 2, 0)
        grid_layout.addWidget(self.password_input, 3, 0)
        
        # 추천인 입력
        referrer_label = QLabel('추천인')
        referrer_label.setStyleSheet("background-color: #e6f2ff; border-radius: 4px; padding: 5px; font-weight: bold; color: #333; border: 1px solid #cce0ff;")
        referrer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        referrer_label.setFixedHeight(30)  # 레이블 높이 고정
        
        self.referrer_input = QLineEdit()
        self.referrer_input.setPlaceholderText('추천인 입력')
        self.referrer_input.setMinimumWidth(150)
        self.referrer_input.setMinimumHeight(35)
        self.referrer_input.setStyleSheet(INPUT_FIELD_STYLE)
        
        grid_layout.addWidget(referrer_label, 2, 1)
        grid_layout.addWidget(self.referrer_input, 3, 1)
        
        # 사용 기간 입력
        expiry_label = QLabel('사용 기간 (종료일)')
        expiry_label.setStyleSheet("background-color: #e6f2ff; border-radius: 4px; padding: 5px; font-weight: bold; color: #333; border: 1px solid #cce0ff;")
        expiry_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        expiry_label.setFixedHeight(30)  # 레이블 높이 고정
        
        self.expiry_input = QDateEdit()
        self.expiry_input.setCalendarPopup(True)
        self.expiry_input.setDate(QDate.currentDate().addDays(APP_SETTINGS['default_expiry_days']))
        self.expiry_input.setMinimumWidth(150)
        self.expiry_input.setMinimumHeight(35)
        self.expiry_input.setStyleSheet(INPUT_FIELD_STYLE)
        
        grid_layout.addWidget(expiry_label, 2, 2)
        grid_layout.addWidget(self.expiry_input, 3, 2)
        
        # 그리드 레이아웃을 메인 레이아웃에 추가
        main_layout.addLayout(grid_layout)
    
    def get_user_input(self):
        """사용자 입력 값 반환"""
        return {
            'user_id': self.id_input.text().strip(),
            'password': self.password_input.text(),
            'expiry_date': self.expiry_input.date().toString('yyyy-MM-dd'),
            'name': self.name_input.text().strip(),
            'phone': self.phone_input.text().strip(),
            'referrer': self.referrer_input.text().strip()
        }
    
    def clear_inputs(self):
        """입력 필드 초기화"""
        self.id_input.clear()
        self.password_input.clear()
        self.name_input.clear()
        self.phone_input.clear()
        self.referrer_input.clear()
        self.expiry_input.setDate(QDate.currentDate().addDays(APP_SETTINGS['default_expiry_days']))
    
    def set_user_info(self, user_id, password, expiry_date_str, name='', phone='', referrer=''):
        """사용자 정보 설정"""
        self.id_input.setText(user_id)
        self.password_input.setText(password)
        self.name_input.setText(name)
        self.phone_input.setText(phone)
        self.referrer_input.setText(referrer)
        
        expiry_date = QDate.fromString(expiry_date_str, 'yyyy-MM-dd')
        self.expiry_input.setDate(expiry_date)