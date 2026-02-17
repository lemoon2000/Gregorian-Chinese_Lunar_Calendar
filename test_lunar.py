#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本 - 验证农历计算功能
"""

import sys
sys.path.insert(0, '/workspaces/1stTest')

from calendar_app.lunar_calendar import solar_to_lunar, format_lunar
from calendar_app.holidays import get_gregorian_holiday, get_lunar_holiday
import datetime

# 测试当前日期的农历转换
today = datetime.date.today()
print(f"测试日期: {today.year}年{today.month}月{today.day}日")
print()

lunar_y, lunar_m, lunar_d = solar_to_lunar(today.year, today.month, today.day)
lunar_str = format_lunar(lunar_y, lunar_m, lunar_d)
print(f"农历日期: {lunar_str}")
print()

# 测试几个特殊日期
test_dates = [
    (2026, 1, 1),    # 元旦
    (2026, 2, 10),   # 春节
    (2026, 6, 10),   # 端午节
    (2026, 10, 1),   # 国庆节
]

print("="*50)
print("特殊日期测试:")
print("="*50)

for year, month, day in test_dates:
    lunar_y, lunar_m, lunar_d = solar_to_lunar(year, month, day)
    lunar_str = format_lunar(lunar_y, lunar_m, lunar_d)
    holiday = get_gregorian_holiday(month, day)
    
    print(f"\n公历: {year}年{month}月{day}日")
    print(f"农历: {lunar_str}")
    if holiday:
        print(f"节假日: {holiday}")

print("\n✅ 农历计算功能正常！")
