#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Calendar Application - Flask Server
"""

from flask import Flask, render_template, request, jsonify
import datetime
import calendar as cal
from lunar_calendar import solar_to_lunar, format_lunar
from holidays import get_gregorian_holiday, get_lunar_holiday

app = Flask(__name__)


@app.route('/')
def index():
    """Home page - Display calendar for current month"""
    today = datetime.date.today()
    return render_template('index.html', 
                          year=today.year, 
                          month=today.month)


@app.route('/api/calendar/<int:year>/<int:month>')
def get_calendar(year, month):
    """Get calendar data for specified month"""
    if month < 1 or month > 12 or year < 1900 or year > 2100:
        return jsonify({'error': 'Invalid year or month'}), 400
    
    # Get calendar for the month
    calendar_data = cal.monthcalendar(year, month)
    
    # Build date data
    days_data = []
    days_in_month = cal.monthrange(year, month)[1]
    
    for week in calendar_data:
        week_data = []
        for day in week:
            if day == 0:
                week_data.append(None)
            else:
                lunar_y, lunar_m, lunar_d = solar_to_lunar(year, month, day)
                lunar_str = format_lunar(lunar_y, lunar_m, lunar_d)
                greg_holiday = get_gregorian_holiday(month, day, year)
                lunar_holiday = get_lunar_holiday(lunar_m, lunar_d)
                
                # Determine if it's today
                today = datetime.date.today()
                is_today = (year == today.year and 
                           month == today.month and 
                           day == today.day)
                
                week_data.append({
                    'day': day,
                    'lunar': lunar_str,
                    'lunar_month': lunar_m,
                    'lunar_day': lunar_d,
                    'greg_holiday': greg_holiday,
                    'lunar_holiday': lunar_holiday,
                    'is_today': is_today
                })
        days_data.append(week_data)
    
    return jsonify({
        'year': year,
        'month': month,
        'days': days_data
    })


@app.route('/api/date/<int:year>/<int:month>/<int:day>')
def get_date_info(year, month, day):
    """Get detailed information for specified date"""
    try:
        date_obj = datetime.date(year, month, day)
    except ValueError:
        return jsonify({'error': 'Invalid date'}), 400
    
    lunar_y, lunar_m, lunar_d = solar_to_lunar(year, month, day)
    
    # Get weekday
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday = weekday_names[date_obj.weekday()]
    
    luna_str = format_lunar(lunar_y, lunar_m, lunar_d)
    greg_holiday = get_gregorian_holiday(month, day, year)
    lunar_holiday = get_lunar_holiday(lunar_m, lunar_d)
    
    return jsonify({
        'gregorian': f'{year}-{month:02d}-{day:02d}',
        'weekday': weekday,
        'lunar': luna_str,
        'lunar_full': f'{lunar_y} {luna_str}',
        'greg_holiday': greg_holiday,
        'lunar_holiday': lunar_holiday
    })


if __name__ == '__main__':
    print("=" * 50)
    print("Gregorian-Lunar Calendar Web Version")
    print("=" * 50)
    print("\nAccess at: http://localhost:5000")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 50 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
