# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QMessageBox
from PyQt6.QtCore import QDate

from config.settings import APP_SETTINGS, MESSAGES
from models.user import UserModel
from ui.styles import APP_STYLE, TITLE_STYLE
from ui.components.input_frame import InputFrame
from ui.components.button_frame import ButtonFrame
from ui.components.table_frame import TableFrame

class UserManagementWindow(QMainWindow):
    """사용자 관리 프로그램 메인 윈도우"""
    
    def __init__(self):
        super().__init__()
        self.user_model = UserModel()
        self.initUI()
        self.loadUsers()
    
    def initUI(self):
        # 메인 윈도우 설정
        self.setWindowTitle(APP_SETTINGS['window_title'])
        self.setGeometry(*APP_SETTINGS['window_geometry'])
        self.setStyleSheet(APP_STYLE)
        self.setMinimumWidth(900)  # 최소 너비 설정
        self.setMinimumHeight(700)  # 최소 높이 설정 추가
        
        # 중앙 위젯 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)  # 간격 축소
        main_layout.setContentsMargins(5, 5, 5, 5)  # 여백 최소화
        
        # 타이틀 레이블
        title_label = QLabel('사용자 관리 시스템')
        title_label.setStyleSheet(TITLE_STYLE)
        main_layout.addWidget(title_label)
        
        # 입력 프레임
        self.input_frame = InputFrame()
        main_layout.addWidget(self.input_frame)
        
        # 버튼 프레임
        self.button_frame = ButtonFrame()
        self.button_frame.save_clicked.connect(self.saveUser)
        self.button_frame.reset_clicked.connect(self.resetPassword)
        self.button_frame.delete_clicked.connect(self.deleteUser)
        main_layout.addWidget(self.button_frame)
        
        # 테이블 프레임 - 나머지 공간을 최대한 사용하도록 설정
        self.table_frame = TableFrame()
        self.table_frame.row_clicked.connect(self.tableRowClicked)
        main_layout.addWidget(self.table_frame, 1)  # 스트레치 팩터 1 추가하여 확장되도록 함
    
    def loadUsers(self):
        """사용자 목록 로드"""
        try:
            users = self.user_model.get_all_users()
            self.table_frame.update_table(users)
        except Exception as e:
            QMessageBox.critical(self, '오류', MESSAGES['db_load_error'].format(error=str(e)))
    
    def saveUser(self):
        """사용자 저장"""
        user_input = self.input_frame.get_user_input()
        
        if not user_input['user_id'] or not user_input['password']:
            QMessageBox.warning(self, '입력 오류', MESSAGES['input_error'])
            return
        
        try:
            result = self.user_model.save_user(
                user_input['user_id'], 
                user_input['password'], 
                user_input['expiry_date']
            )
            
            message = MESSAGES['user_added'] if result['is_new'] else MESSAGES['user_updated']
            QMessageBox.information(self, '성공', message)
            
            # 입력 필드 초기화
            self.input_frame.clear_inputs()
            
            # 테이블 새로고침
            self.loadUsers()
            
        except Exception as e:
            QMessageBox.critical(self, '오류', MESSAGES['db_save_error'].format(error=str(e)))
    
    def resetPassword(self):
        """비밀번호 초기화"""
        user_id = self.table_frame.get_selected_user_id()
        if not user_id:
            QMessageBox.warning(self, '선택 오류', MESSAGES['selection_error'])
            return
        
        try:
            result = self.user_model.reset_password(user_id)
            
            QMessageBox.information(
                self, 
                '성공', 
                MESSAGES['password_reset'].format(
                    user_id=user_id, 
                    new_password=result['new_password']
                )
            )
            
            # 테이블 새로고침
            self.loadUsers()
            
        except Exception as e:
            QMessageBox.critical(self, '오류', MESSAGES['db_reset_error'].format(error=str(e)))
    
    def deleteUser(self):
        """사용자 삭제"""
        user_id = self.table_frame.get_selected_user_id()
        if not user_id:
            QMessageBox.warning(self, '선택 오류', MESSAGES['selection_error'])
            return
        
        # 삭제 확인
        reply = QMessageBox.question(
            self, 
            '삭제 확인', 
            MESSAGES['delete_confirm'].format(user_id=user_id),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.user_model.delete_user(user_id)
                
                QMessageBox.information(
                    self, 
                    '성공', 
                    MESSAGES['user_deleted'].format(user_id=user_id)
                )
                
                # 테이블 새로고침
                self.loadUsers()
                
            except Exception as e:
                QMessageBox.critical(self, '오류', MESSAGES['db_delete_error'].format(error=str(e)))
    
    def tableRowClicked(self, row):
        """테이블 행 클릭 이벤트 처리"""
        user_id = self.table_frame.user_table.item(row, 0).text()
        expiry_date_str = self.table_frame.user_table.item(row, 2).text()
        
        try:
            user = self.user_model.db.get_user(user_id)
            if user:
                self.input_frame.set_user_info(
                    user_id=user[0],
                    password=user[1],
                    expiry_date_str=expiry_date_str
                )
        except Exception as e:
            QMessageBox.critical(self, '오류', MESSAGES['db_password_error'].format(error=str(e)))
    
    def closeEvent(self, event):
        """프로그램 종료 시 리소스 정리"""
        if hasattr(self, 'user_model'):
            self.user_model.close()
        event.accept()