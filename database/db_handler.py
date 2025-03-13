# -*- coding: utf-8 -*-

import pymysql
from config.settings import DB_CONFIG

class DatabaseHandler:
    """데이터베이스 연결 및 쿼리 처리를 담당하는 클래스"""
    
    def __init__(self):
        self.conn = None
        self.connect()
        self.init_table()
    
    def connect(self):
        """데이터베이스 연결"""
        try:
            self.conn = pymysql.connect(
                host=DB_CONFIG['host'],
                port=DB_CONFIG['port'],
                user=DB_CONFIG['user'],
                password=DB_CONFIG['password'],
                db=DB_CONFIG['db'],
                charset=DB_CONFIG['charset']
            )
            return True
        except Exception as e:
            raise ConnectionError(f"데이터베이스 연결 실패: {str(e)}")
    
    def init_table(self):
        """사용자 테이블 초기화"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS hol_user (
                        no INT AUTO_INCREMENT PRIMARY KEY,
                        id VARCHAR(50) UNIQUE NOT NULL,
                        pw VARCHAR(100) NOT NULL,
                        end_date DATE NOT NULL
                    )
                ''')
                self.conn.commit()
            return True
        except Exception as e:
            raise Exception(f"테이블 초기화 실패: {str(e)}")
    
    def get_all_users(self):
        """모든 사용자 조회"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT id, pw, end_date FROM hol_user')
                return cursor.fetchall()
        except Exception as e:
            raise Exception(f"사용자 조회 실패: {str(e)}")
    
    def get_user(self, user_id):
        """특정 사용자 조회"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT id, pw, end_date FROM hol_user WHERE id = %s', (user_id,))
                return cursor.fetchone()
        except Exception as e:
            raise Exception(f"사용자 조회 실패: {str(e)}")
    
    def user_exists(self, user_id):
        """사용자 ID 존재 여부 확인"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT id FROM hol_user WHERE id = %s', (user_id,))
                return cursor.fetchone() is not None
        except Exception as e:
            raise Exception(f"사용자 확인 실패: {str(e)}")
    
    def add_user(self, user_id, password, expiry_date):
        """사용자 추가"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO hol_user (id, pw, end_date) VALUES (%s, %s, %s)',
                    (user_id, password, expiry_date)
                )
                self.conn.commit()
            return True
        except Exception as e:
            raise Exception(f"사용자 추가 실패: {str(e)}")
    
    def update_user(self, user_id, password, expiry_date):
        """사용자 정보 업데이트"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    'UPDATE hol_user SET pw = %s, end_date = %s WHERE id = %s',
                    (password, expiry_date, user_id)
                )
                self.conn.commit()
            return True
        except Exception as e:
            raise Exception(f"사용자 업데이트 실패: {str(e)}")
    
    def reset_password(self, user_id, new_password):
        """사용자 비밀번호 초기화"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    'UPDATE hol_user SET pw = %s WHERE id = %s',
                    (new_password, user_id)
                )
                self.conn.commit()
            return True
        except Exception as e:
            raise Exception(f"비밀번호 초기화 실패: {str(e)}")
    
    def delete_user(self, user_id):
        """사용자 삭제"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('DELETE FROM hol_user WHERE id = %s', (user_id,))
                self.conn.commit()
            return True
        except Exception as e:
            raise Exception(f"사용자 삭제 실패: {str(e)}")
    
    def close(self):
        """데이터베이스 연결 종료"""
        if self.conn:
            self.conn.close()