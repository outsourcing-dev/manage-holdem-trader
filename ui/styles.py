# -*- coding: utf-8 -*-

# 애플리케이션 전체 스타일
APP_STYLE = '''
    QMainWindow {
        background-color: #f5f5f5;
    }
    QLabel {
        font-weight: bold;
        font-size: 13px;
        color: #333;
    }
    QPushButton {
        background-color: #0078d7;
        color: white;
        border: none;
        padding: 6px 12px;
        font-weight: bold;
        font-size: 12px;
        border-radius: 2px;
    }
    QPushButton:hover {
        background-color: #005fa3;
    }
    QPushButton:pressed {
        background-color: #004c82;
    }
    QLineEdit, QDateEdit {
        padding: 6px;
        border: 1px solid #ccc;
        border-radius: 2px;
        background-color: white;
    }
    QCalendarWidget {
        background-color: white;
    }
    QCalendarWidget QToolButton {
        color: black;
        background-color: #f0f0f0;
        font-weight: bold;
    }
    QCalendarWidget QMenu {
        color: black;
    }
    QCalendarWidget QSpinBox {
        color: black;
        background-color: white;
    }
'''

# 제목 스타일
TITLE_STYLE = '''
    font-size: 18px;
    font-weight: bold;
    color: #0078d7;
    padding: 10px 0;
    border-bottom: 2px solid #0078d7;
    margin-bottom: 15px;
'''

# 입력 프레임 스타일
INPUT_FRAME_STYLE = '''
    background-color: white;
    border: 1px solid #d0d0d0;
    padding: 10px;
'''

# 입력 타이틀 스타일
INPUT_TITLE_STYLE = '''
    font-size: 16px;
    font-weight: bold;
    color: #333;
    margin-bottom: 10px;
    border-bottom: 1px solid #ddd;
    padding-bottom: 5px;
'''

# 입력 필드 레이블 스타일
INPUT_LABEL_STYLE = '''
    font-size: 14px;
    font-weight: bold;
    color: #555;
'''

# 입력 필드 스타일
INPUT_FIELD_STYLE = '''
    font-size: 13px;
    padding: 8px 12px;
'''

# 삭제 버튼 스타일
DELETE_BUTTON_STYLE = '''
    background-color: #d9534f;
    font-size: 13px;
    font-weight: bold;
'''

# 일반 버튼 스타일
BUTTON_STYLE = '''
    font-size: 13px;
    font-weight: bold;
'''

# 테이블 프레임 스타일
TABLE_FRAME_STYLE = '''
    background-color: white;
    padding: 0;
    border: none;
'''

# 테이블 라벨 스타일
TABLE_LABEL_STYLE = '''
    font-size: 15px;
    font-weight: bold;
    color: #333;
'''

# 사용자 수 라벨 스타일
USER_COUNT_STYLE = '''
    font-size: 14px;
    color: #666;
'''

# 테이블 스타일 - 엑셀 스타일로 단순화
TABLE_STYLE = '''
    QTableWidget {
        border: 1px solid #d0d0d0;
        gridline-color: #d0d0d0;
        background-color: white;
        selection-background-color: #e6f3ff;
        selection-color: black;
        font-size: 13px;
    }
    QTableWidget::item {
        padding: 5px;
        border: 0px;
    }
    QTableWidget::item:selected {
        background-color: #e6f3ff;
        color: black;
    }
'''

# 테이블 헤더 스타일 - 엑셀 스타일
TABLE_HEADER_STYLE = '''
    QHeaderView::section {
        background-color: #0078d7;
        color: white;
        padding: 10px;
        font-weight: bold;
        border: 0px;
        border-right: 1px solid white;
        border-bottom: 1px solid white;
        font-size: 14px;
    }
    QHeaderView::section:last {
        border-right: 0px;
    }
'''