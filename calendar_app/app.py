#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web 版日历应用 - Flask 服务器
"""

from flask import Flask, render_template, request, jsonify
import datetime
import calendar as cal
from lunar_calendar import solar_to_lunar, format_lunar
from holidays import get_gregorian_holiday, get_lunar_holiday

app = Flask(__name__)


@app.route('/')
def index():
    """主页 - 显示当前月份的日历"""
    today = datetime.date.today()
    return render_template('index.html', 
                          year=today.year, 
                          month=today.month)


@app.route('/api/calendar/<int:year>/<int:month>')
def get_calendar(year, month):
    """获取指定月份的日历数据"""
    if month < 1 or month > 12 or year < 1900 or year > 2100:
        return jsonify({'error': '无效的年份或月份'}), 400
    
    # 获取该月的日历
    calendar_data = cal.monthcalendar(year, month)
    
    # 构建日期数据
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
                greg_holiday = get_gregorian_holiday(month, day)
                lunar_holiday = get_lunar_holiday(lunar_m, lunar_d)
                
                # 判断是否为今天
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
    """获取指定日期的详细信息"""
    try:
        date_obj = datetime.date(year, month, day)
    except ValueError:
        return jsonify({'error': '无效的日期'}), 400
    
    lunar_y, lunar_m, lunar_d = solar_to_lunar(year, month, day)
    
    # 获取星期
    weekday_names = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    weekday = weekday_names[date_obj.weekday()]
    
    luna_str = format_lunar(lunar_y, lunar_m, lunar_d)
    greg_holiday = get_gregorian_holiday(month, day)
    lunar_holiday = get_lunar_holiday(lunar_m, lunar_d)
    
    return jsonify({
        'gregorian': f'{year}年{month}月{day}日',
        'weekday': weekday,
        'lunar': luna_str,
        'lunar_full': f'{lunar_y}年{luna_str}',
        'greg_holiday': greg_holiday,
        'lunar_holiday': lunar_holiday
    })


if __name__ == '__main__':
    print("=" * 50)
    print("公历农历日历 Web 版本")
    print("=" * 50)
    print("\n访问地址: http://localhost:5000")
    print("\n按 Ctrl+C 停止服务器")
    print("=" * 50 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
