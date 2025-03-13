# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QTableWidget, QTableWidgetItem, QHeaderView)
from PyQt6.QtCore import Qt, pyqtSignal, QSize
from config.settings import TABLE_SETTINGS, STATUS_SETTINGS
from ui.styles import (TABLE_FRAME_STYLE, TABLE_LABEL_STYLE, USER_COUNT_STYLE,
                       TABLE_STYLE, TABLE_HEADER_STYLE)

class TableFrame(QWidget):
    """사용자 목록 테이블 프레임"""
    
    # 시그널 정의
    row_clicked = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        # 테이블 프레임 스타일 설정
        self.setStyleSheet(TABLE_FRAME_STYLE + '''
            QWidget {
                border-radius: 8px;
                border: 1px solid #ddd;
                overflow: hidden;
            }
        ''')
        
        # 레이아웃 설정
        table_layout = QVBoxLayout(self)
        table_layout.setContentsMargins(15, 15, 15, 15)
        table_layout.setSpacing(0)  # 간격 제거하여 일체감 있게
        
        # 테이블 헤더 컨테이너
        table_header = QWidget()
        table_header_layout = QHBoxLayout(table_header)
        table_header_layout.setContentsMargins(0, 0, 0, 10)
        
        # 테이블 라벨
        table_label = QLabel('사용자 목록')
        table_label.setStyleSheet(TABLE_LABEL_STYLE)
        table_header_layout.addWidget(table_label)
        
        # 유저 카운트 표시 (우측 정렬)
        self.user_count_label = QLabel('총 0명')
        self.user_count_label.setStyleSheet(USER_COUNT_STYLE)
        table_header_layout.addStretch(1)
        table_header_layout.addWidget(self.user_count_label)
        
        table_layout.addWidget(table_header)
        
        # 테이블 컨테이너 - 테이블을 감싸는 컨테이너
        table_container = QWidget()
        table_container.setStyleSheet('''
            background-color: white;
            border-radius: 8px;
            border: 1px solid #0078d7;
            padding: 0;
            margin: 0;
        ''')
        table_container_layout = QVBoxLayout(table_container)
        table_container_layout.setContentsMargins(0, 0, 0, 0)
        table_container_layout.setSpacing(0)
        
        # 테이블 위젯 설정
        self.user_table = QTableWidget()
        self.user_table.setColumnCount(4)
        self.user_table.setHorizontalHeaderLabels(TABLE_SETTINGS['headers'])
        
        # 테이블 전체 스타일
        self.user_table.setStyleSheet(TABLE_STYLE)
        
        # 헤더 스타일 직접 설정
        header = self.user_table.horizontalHeader()
        header.setStyleSheet(TABLE_HEADER_STYLE)
        
        # 테이블과 헤더 사이의 간격 제거 및 테두리 스타일 맞추기
        self.user_table.setStyleSheet(TABLE_STYLE)
        
        # 수직 헤더도 스타일 적용 (행 번호 표시)
        vertical_header = self.user_table.verticalHeader()
        vertical_header.setStyleSheet("""
            QHeaderView::section {
                background-color: #0078d7;
                color: white;
                border: none;
                font-weight: bold;
                padding: 5px;
                min-width: 25px;
            }
        """)
        
        # 아이콘 크기 설정 - 작게 조정
        self.user_table.setIconSize(QSize(16, 16))
        
        # 헤더 설정 - 고정 크기 사용
        column_widths = TABLE_SETTINGS['column_widths']
        self.user_table.setColumnWidth(0, column_widths['id'])
        self.user_table.setColumnWidth(1, column_widths['password'])
        self.user_table.setColumnWidth(2, column_widths['expiry_date'])
        self.user_table.setColumnWidth(3, column_widths['days_left'])
        
        # 헤더 텍스트 중앙 정렬
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # 헤더 높이 설정
        header.setMinimumHeight(40)
        
        # 테이블 행 설정
        self.user_table.setAlternatingRowColors(True)
        self.user_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        
        # 행 번호 표시 설정
        vertical_header = self.user_table.verticalHeader()
        vertical_header.setVisible(True)  # 행 번호 표시
        vertical_header.setDefaultSectionSize(45)  # 행 높이와 동일하게 설정
        vertical_header.setStyleSheet("""
            QHeaderView::section {
                background-color: #0078d7;
                color: white;
                border: none;
                padding: 5px;
                font-weight: bold;
            }
        """)
        
        self.user_table.clicked.connect(self._handle_click)
        
        # 테이블 기본 설정
        self.user_table.setShowGrid(True)
        self.user_table.setGridStyle(Qt.PenStyle.SolidLine)
        self.user_table.setSortingEnabled(True)  # 정렬 기능 활성화
        
        table_layout.addWidget(self.user_table)
    
    def update_table(self, users):
        """사용자 목록 업데이트"""
        # 테이블 설정 변경
        self.user_table.setUpdatesEnabled(False)  # 업데이트 일시 중지
        
        # 사용자 수 업데이트
        self.user_count_label.setText(f'총 {len(users)}명')
        
        # 테이블 업데이트
        self.user_table.setRowCount(len(users))
        for row, user in enumerate(users):
            # ID 항목 생성
            id_item = QTableWidgetItem(user['id'])
            id_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.user_table.setItem(row, 0, id_item)
            
            # 비밀번호 항목 생성
            pw_item = QTableWidgetItem(user['password'])
            pw_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.user_table.setItem(row, 1, pw_item)
            
            # 만료일 항목 생성
            expiry_item = QTableWidgetItem(user['expiry_date_str'])
            expiry_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.user_table.setItem(row, 2, expiry_item)
            
            # 남은 일수 항목 생성
            days_left = user['days_left']
            days_text = f"{days_left}일"
            days_item = QTableWidgetItem(days_text)
            days_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            # 상태에 따른 아이콘만 적용 (배경색 없음)
            if days_left < 0:
                # 만료됨
                days_item.setForeground(Qt.GlobalColor.red)
                days_item.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_MessageBoxCritical))
                days_item.setToolTip("사용 기간이 만료되었습니다!")
            elif days_left < 7:
                # 곧 만료
                days_item.setForeground(Qt.GlobalColor.darkYellow)
                days_item.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_MessageBoxWarning))
                days_item.setToolTip("사용 기간이 7일 이내로 남았습니다.")
            else:
                # 정상
                days_item.setForeground(Qt.GlobalColor.darkGreen)
                days_item.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_DialogApplyButton))
            
            self.user_table.setItem(row, 3, days_item)
            
            # 행 높이 설정
            self.user_table.setRowHeight(row, 30)
        
        # 테이블 정렬 - 기본적으로 만료일 임박순(남은 일수 적은 순)으로 정렬
        self.user_table.sortItems(3, Qt.SortOrder.AscendingOrder)
        
        self.user_table.setUpdatesEnabled(True)  # 업데이트 다시 활성화
    
    def _apply_status_style(self, item, status):
        """상태에 따른 스타일 적용"""
        if status == 'expired':
            # 만료됨 - 빨간색 배경
            item.setBackground(Qt.GlobalColor.red)
            item.setForeground(Qt.GlobalColor.white)  # 흰색 텍스트
            item.setToolTip(STATUS_SETTINGS['expired']['tooltip'])
            item.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_MessageBoxCritical))
        elif status == 'warning':
            # 곧 만료 - 노란색 배경
            item.setBackground(Qt.GlobalColor.yellow)
            item.setForeground(Qt.GlobalColor.black)  # 검정색 텍스트
            item.setToolTip(STATUS_SETTINGS['warning']['tooltip'])
            item.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_MessageBoxWarning))
        else:
            # 정상 - 초록색 배경
            item.setBackground(Qt.GlobalColor.darkGreen)
            item.setForeground(Qt.GlobalColor.white)  # 흰색 텍스트
            item.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_DialogApplyButton))
        
        # 폰트 크기 및 스타일 설정하여 가독성 향상
        font = item.font()
        font.setBold(True)
        font.setPointSize(10)  # 폰트 크기 설정
        item.setFont(font)
    
    def _handle_click(self):
        """테이블 행 클릭 처리"""
        selected_row = self.user_table.currentRow()
        if selected_row >= 0:
            self.row_clicked.emit(selected_row)
    
    def get_selected_user_id(self):
        """선택된 사용자 ID 반환"""
        selected_rows = self.user_table.selectedItems()
        if not selected_rows:
            return None
        
        row = selected_rows[0].row()
        return self.user_table.item(row, 0).text()