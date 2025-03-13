# -*- coding: utf-8 -*-

from datetime import datetime
from database.db_handler import DatabaseHandler
from utils.date_utils import calculate_days_left

class UserModel:
    """사용자 모델 및 관련 비즈니스 로직 처리"""
    
    def __init__(self):
        self.db = DatabaseHandler()
    
    def get_all_users(self):
        """모든 사용자 정보를 가져와 처리"""
        users = self.db.get_all_users()
        
        # 각 사용자에 대해 남은 일수 계산하여 정보 확장
        processed_users = []
        for user in users:
            user_id, password, expiry_date = user
            days_left = calculate_days_left(expiry_date)
            
            processed_users.append({
                'id': user_id,
                'password': password,
                'expiry_date': expiry_date,
                'expiry_date_str': expiry_date.strftime('%Y-%m-%d'),
                'days_left': days_left,
                'days_left_str': f"{days_left}일",
                'status': self._get_status(days_left)
            })
        
        return processed_users
    
    def save_user(self, user_id, password, expiry_date):
        """사용자 저장 (추가 또는 업데이트)"""
        if not user_id or not password:
            raise ValueError("아이디와 비밀번호는 필수 입력값입니다.")
        
        if self.db.user_exists(user_id):
            self.db.update_user(user_id, password, expiry_date)
            return {'success': True, 'is_new': False}
        else:
            self.db.add_user(user_id, password, expiry_date)
            return {'success': True, 'is_new': True}
    
    def reset_password(self, user_id):
        """사용자 비밀번호 초기화"""
        # 현재 날짜를 포함한 기본 비밀번호 생성
        default_password = f"reset{datetime.now().strftime('%Y%m%d')}"
        
        self.db.reset_password(user_id, default_password)
        
        return {'success': True, 'new_password': default_password}
    
    def delete_user(self, user_id):
        """사용자 삭제"""
        self.db.delete_user(user_id)
        return {'success': True}
    
    def _get_status(self, days_left):
        """남은 일수에 따른 상태 반환"""
        if days_left < 0:
            return 'expired'
        elif days_left < 7:
            return 'warning'
        else:
            return 'normal'
    
    def close(self):
        """리소스 정리"""
        if self.db:
            self.db.close()