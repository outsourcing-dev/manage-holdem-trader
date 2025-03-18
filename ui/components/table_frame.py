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
        
        # 컬럼 수 설정 - 번호 컬럼도 포함하여 8개로 증가
        self.user_table.setColumnCount(8)
        
        # 모든 헤더 레이블 설정 - 번호 컬럼 추가
        header_labels = ['NO'] + TABLE_SETTINGS['headers']
        self.user_table.setHorizontalHeaderLabels(header_labels)
        
        # 테이블 전체 스타일
        self.user_table.setStyleSheet(TABLE_STYLE)
        
        # 헤더 스타일 직접 설정
        header = self.user_table.horizontalHeader()
        
        # 모든 컬럼을 Stretch로 설정 (기본 설정)
        for i in range(self.user_table.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
            
        # 번호 컬럼 너비 고정
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        self.user_table.setColumnWidth(0, 60)  # 번호 컬럼 너비를 60으로 고정
        
        # 컬럼 너비 설정 (고정 너비가 있는 경우만 Interactive로 설정) - 인덱스 조정
        column_names = ['id', 'name', 'phone', 'referrer', 'password', 'expiry_date', 'days_left']
        for idx, col_name in enumerate(column_names):
            if col_name in TABLE_SETTINGS['column_widths']:
                width = TABLE_SETTINGS['column_widths'][col_name]
                self.user_table.setColumnWidth(idx + 1, width)  # +1 for NO column
                header.setSectionResizeMode(idx + 1, QHeaderView.ResizeMode.Interactive)
        
        # 마지막 컬럼(days_left)는 stretch 모드로 설정하여 남은 공간을 활용
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.Stretch)  # 7 = 인덱스 조정
        
        header.setStyleSheet(TABLE_HEADER_STYLE)
        
        # 수직 헤더 숨기기 (행 번호를 직접 첫 번째 컬럼에 표시할 것이므로)
        self.user_table.verticalHeader().setVisible(False)
        
        # 아이콘 크기 설정 - 작게 조정
        self.user_table.setIconSize(QSize(16, 16))
        
        # 헤더 텍스트 중앙 정렬
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # 헤더 높이 설정
        header.setMinimumHeight(40)
        
        # 테이블 행 설정
        self.user_table.setAlternatingRowColors(True)
        self.user_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        
        # 테이블 셀 편집 비활성화
        self.user_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        self.user_table.clicked.connect(self._handle_click)
        
        # 테이블 기본 설정
        self.user_table.setShowGrid(True)
        self.user_table.setGridStyle(Qt.PenStyle.SolidLine)
        self.user_table.setSortingEnabled(True)  # 정렬 기능 활성화
        
        table_container_layout.addWidget(self.user_table)
        table_layout.addWidget(table_container)
    
    def _handle_click(self):
        """테이블 행 클릭 처리"""
        selected_row = self.user_table.currentRow()
        if selected_row >= 0:
            self.row_clicked.emit(selected_row)
    
    def get_selected_user_id(self):
        """선택된 사용자 ID 반환"""
        selected_items = self.user_table.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            # ID는 이제 두 번째 컬럼(인덱스 1)에 있음
            return self.user_table.item(row, 1).text()
        return None
            
    def update_table(self, users):
        """사용자 목록 업데이트"""
        # 테이블 설정 변경
        self.user_table.setUpdatesEnabled(False)  # 업데이트 일시 중지
        
        # 사용자 수 업데이트
        self.user_count_label.setText(f'총 {len(users)}명')
        
        # 테이블 업데이트
        self.user_table.setRowCount(len(users))
        for row, user in enumerate(users):
            # 번호 컬럼 추가 (1부터 시작)
            no_item = QTableWidgetItem(str(row + 1))
            no_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.user_table.setItem(row, 0, no_item)
            
            # ID 항목 생성 (1번 컬럼으로 이동)
            id_item = QTableWidgetItem(user['id'])
            id_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.user_table.setItem(row, 1, id_item)
            
            # 이름 항목 생성
            name_item = QTableWidgetItem(user['name'])
            name_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.user_table.setItem(row, 2, name_item)
            
            # 전화번호 항목 생성
            phone_item = QTableWidgetItem(user['phone'])
            phone_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.user_table.setItem(row, 3, phone_item)
            
            # 추천인 항목 생성
            referrer_item = QTableWidgetItem(user['referrer'])
            referrer_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.user_table.setItem(row, 4, referrer_item)
            
            # 비밀번호 항목 생성
            pw_item = QTableWidgetItem(user['password'])
            pw_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.user_table.setItem(row, 5, pw_item)
            
            # 만료일 항목 생성
            expiry_item = QTableWidgetItem(user['expiry_date_str'])
            expiry_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.user_table.setItem(row, 6, expiry_item)
            
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
            
            self.user_table.setItem(row, 7, days_item)
            
            # 행 높이 설정
            self.user_table.setRowHeight(row, 30)
        
        # 테이블 정렬 - 기본적으로 만료일 임박순(남은 일수 적은 순)으로 정렬
        self.user_table.sortItems(7, Qt.SortOrder.AscendingOrder)  # 7로 인덱스 조정
        
        self.user_table.setUpdatesEnabled(True)  # 업데이트 다시 활성화