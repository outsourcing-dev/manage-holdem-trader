import pymysql

# 데이터베이스 연결
conn = pymysql.connect(
    host='svc.sel4.cloudtype.app',
    port=32481,
    user='admin',  # 또는 root 계정
    password='hanapf1121'  # 실제 비밀번호
)

try:
    with conn.cursor() as cursor:
        # 데이터베이스 목록 조회
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        
        print("=== 데이터베이스 목록 ===")
        for db in databases:
            print(db[0])
            
        # 첫 번째 데이터베이스의 테이블 목록 조회 (선택 사항)
        if databases:
            selected_db = databases[2][0]
            print(f"\n=== '{selected_db}' 데이터베이스의 테이블 목록 ===")
            cursor.execute(f"USE `{selected_db}`")
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            
            if tables:
                for table in tables:
                    print(table[0])
            else:
                print("테이블이 없습니다.")
            
except Exception as e:
    print(f"오류 발생: {e}")

finally:
    conn.close()
    print("\n데이터베이스 연결이 종료되었습니다.")