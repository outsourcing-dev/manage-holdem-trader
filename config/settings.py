# -*- coding: utf-8 -*-

# 데이터베이스 설정
DB_CONFIG = {
    'host': 'svc.sel4.cloudtype.app',
    'port': 32481,
    'user': 'admin',
    'password': 'hanapf1121',  # 실제 비밀번호 입력 필요
    'db': 'manager',  # 사용할 데이터베이스 이름
    'charset': 'utf8mb4'
}

# 애플리케이션 설정
APP_SETTINGS = {
    'window_title': '사용자 관리 프로그램',
    'window_geometry': (100, 100, 1100, 900),  # 가로 길이 증가
    'default_expiry_days': 30,  # 기본 사용 기간 (일)
}

# 테이블 설정
TABLE_SETTINGS = {
    'column_widths': {
        'id': 120,
        'name': 100,
        'phone': 290,
        'referrer': 100,
        'password': 120,
        'expiry_date': 150,
        'days_left': 100
    },
    'headers': ['ID', '이름', '전화번호', '추천인', '비밀번호', '사용 기간', '남은 일수']
}

# 알림 메시지
MESSAGES = {
    'input_error': '아이디와 비밀번호를 모두 입력해주세요.',
    'user_updated': '사용자 정보가 업데이트되었습니다.',
    'user_added': '새 사용자가 추가되었습니다.',
    'selection_error': '작업할 사용자를 선택해주세요.',
    'password_reset': '사용자 {user_id}의 비밀번호가 초기화되었습니다.\n새 비밀번호: {new_password}',
    'delete_confirm': '사용자 {user_id}를 정말 삭제하시겠습니까?',
    'user_deleted': '사용자 {user_id}가 삭제되었습니다.',
    'db_connect_error': '데이터베이스 연결 실패: {error}',
    'db_load_error': '사용자 목록 로딩 실패: {error}',
    'db_save_error': '사용자 저장 실패: {error}',
    'db_reset_error': '비밀번호 초기화 실패: {error}',
    'db_delete_error': '사용자 삭제 실패: {error}',
    'db_password_error': '비밀번호 조회 실패: {error}'
}

# 상태 설정
STATUS_SETTINGS = {
    'expired': {
        'tooltip': '사용 기간이 만료되었습니다!',
        'days': 0
    },
    'warning': {
        'tooltip': '사용 기간이 7일 이내로 남았습니다.',
        'days': 7
    }
}