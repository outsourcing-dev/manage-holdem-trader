# -*- coding: utf-8 -*-

from datetime import datetime

def calculate_days_left(expiry_date):
    """만료일까지 남은 일수 계산"""
    today = datetime.now().date()
    days_left = (expiry_date - today).days
    return days_left