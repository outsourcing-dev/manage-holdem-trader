import pymysql

conn = pymysql.connect(
    host='svc.sel4.cloudtype.app',
    port=32481,
    user='root',
    password='!hanapf1121@',
    db='manager',  # 직접 DB 이름 지정
    connect_timeout=10
)

try:
    with conn.cursor() as cursor:
        print("컬럼 추가 시도 중...")
        
        # 컬럼 추가
        try:
            cursor.execute("ALTER TABLE hol_user ADD COLUMN name VARCHAR(50)")
            print("name 컬럼 추가됨")
        except Exception as e:
            print(f"name 컬럼 추가 실패: {str(e)}")
        
        try:
            cursor.execute("ALTER TABLE hol_user ADD COLUMN phone VARCHAR(20)")
            print("phone 컬럼 추가됨")
        except Exception as e:
            print(f"phone 컬럼 추가 실패: {str(e)}")
        
        try:
            cursor.execute("ALTER TABLE hol_user ADD COLUMN referrer VARCHAR(50)")
            print("referrer 컬럼 추가됨")
        except Exception as e:
            print(f"referrer 컬럼 추가 실패: {str(e)}")
        
        # 변경사항 커밋
        conn.commit()
        print("변경사항 커밋 완료")
        
        # 테이블 구조 확인
        print("\n=== 수정 후 hol_user 테이블 구조 ===")
        cursor.execute("DESCRIBE hol_user")
        columns = cursor.fetchall()
        for col in columns:
            print(col)
            
except Exception as e:
    print(f"오류 발생: {e}")

finally:
    conn.close()
    print("\n데이터베이스 연결이 종료되었습니다.")