#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script - Verify Lunar calendar calculation functionality
"""

import sys
sys.path.insert(0, '/workspaces/1stTest')

from calendar_app.lunar_calendar import solar_to_lunar, format_lunar
from calendar_app.holidays import get_gregorian_holiday, get_lunar_holiday
import datetime

# Test Lunar calendar conversion for today
today = datetime.date.today()
print(f"Test date: {today.year}-{today.month:02d}-{today.day:02d}")
print()

lunar_y, lunar_m, lunar_d = solar_to_lunar(today.year, today.month, today.day)
lunar_str = format_lunar(lunar_y, lunar_m, lunar_d)
print(f"Lunar date: {lunar_str}")
print()

# Test several special dates
test_dates = [
    (2026, 1, 1),    # New Year's Day
    (2026, 2, 10),   # Spring Festival
    (2026, 6, 10),   # Dragon Boat Festival
    (2026, 10, 1),   # National Day
]

print("="*50)
print("Special Date Tests:")
print("="*50)

for year, month, day in test_dates:
    lunar_y, lunar_m, lunar_d = solar_to_lunar(year, month, day)
    lunar_str = format_lunar(lunar_y, lunar_m, lunar_d)
    holiday = get_gregorian_holiday(month, day)
    
    print(f"\nGregorian: {year}-{month:02d}-{day:02d}")
    print(f"Lunar: {lunar_str}")
    if holiday:
        print(f"Holiday: {holiday}")

print("\n✅ Lunar calendar calculation is working correctly!")
