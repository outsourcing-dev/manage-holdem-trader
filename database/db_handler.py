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
            print("데이터베이스 연결 시도 중...")  # 디버깅용 메시지 추가
            self.conn = pymysql.connect(
                host=DB_CONFIG['host'],
                port=DB_CONFIG['port'],
                user=DB_CONFIG['user'],
                password=DB_CONFIG['password'],
                db=DB_CONFIG['db'],
                charset=DB_CONFIG['charset'],
                connect_timeout=5  # 5초 타임아웃 추가
            )
            print("데이터베이스 연결 성공!")  # 디버깅용 메시지 추가
            return True
        except Exception as e:
            error_msg = f"데이터베이스 연결 실패: {str(e)}"
            print(error_msg)  # 콘솔에 오류 출력
            raise ConnectionError(error_msg)
    
    def init_table(self):
        """사용자 테이블 초기화"""
        try:
            print("테이블 초기화 시작...")
            with self.conn.cursor() as cursor:
                print("테이블 존재 여부 확인 중...")
                # 테이블이 존재하는지만 확인 (ALTER TABLE 시도 없음)
                cursor.execute("SHOW TABLES LIKE 'hol_user'")
                table_exists = cursor.fetchone() is not None
                
                if not table_exists:
                    print("테이블 생성 중...")
                    cursor.execute('''
                        CREATE TABLE hol_user (
                            no INT AUTO_INCREMENT PRIMARY KEY,
                            id VARCHAR(50) UNIQUE NOT NULL,
                            pw VARCHAR(100) NOT NULL,
                            end_date DATE NOT NULL
                        )
                    ''')
                
                # ALTER TABLE 명령은 일단 주석 처리
                '''
                # 컬럼 추가 시도는 건너뜁니다
                try:
                    cursor.execute("ALTER TABLE hol_user ADD COLUMN name VARCHAR(50) AFTER end_date")
                    print("name 컬럼 추가됨")
                except Exception as e:
                    print(f"name 컬럼 추가 실패: {str(e)}")
                
                try:
                    cursor.execute("ALTER TABLE hol_user ADD COLUMN phone VARCHAR(20) AFTER name")
                    print("phone 컬럼 추가됨")
                except Exception as e:
                    print(f"phone 컬럼 추가 실패: {str(e)}")
                
                try:
                    cursor.execute("ALTER TABLE hol_user ADD COLUMN referrer VARCHAR(50) AFTER phone")
                    print("referrer 컬럼 추가됨")
                except Exception as e:
                    print(f"referrer 컬럼 추가 실패: {str(e)}")
                '''
                
                print("변경사항 커밋 중...")
                self.conn.commit()
                
            print("테이블 초기화 완료!")
            return True
        except Exception as e:
            error_msg = f"테이블 초기화 실패: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)
        
    def get_all_users(self):
        """모든 사용자 조회"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT id, pw, end_date, name, phone, referrer FROM hol_user')
                # cursor.execute('SELECT id, pw, end_date FROM hol_user')
                return cursor.fetchall()
        except Exception as e:
            raise Exception(f"사용자 조회 실패: {str(e)}")
    
    def get_user(self, user_id):
        """특정 사용자 조회"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT id, pw, end_date, name, phone, referrer FROM hol_user WHERE id = %s', (user_id,))
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
    
    def add_user(self, user_id, password, expiry_date, name='', phone='', referrer=''):
        """사용자 추가"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO hol_user (id, pw, end_date, name, phone, referrer) VALUES (%s, %s, %s, %s, %s, %s)',
                    (user_id, password, expiry_date, name, phone, referrer)
                )
                self.conn.commit()
            return True
        except Exception as e:
            raise Exception(f"사용자 추가 실패: {str(e)}")
    
    def update_user(self, user_id, password, expiry_date, name='', phone='', referrer=''):
        """사용자 정보 업데이트"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(
                    'UPDATE hol_user SET pw = %s, end_date = %s, name = %s, phone = %s, referrer = %s WHERE id = %s',
                    (password, expiry_date, name, phone, referrer, user_id)
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
