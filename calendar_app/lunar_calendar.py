# 农历计算模块
from lunarcalendar import Converter, Solar, Lunar


def solar_to_lunar(year, month, day):
    """
    公历转农历
    
    Args:
        year: 公历年份
        month: 公历月份
        day: 公历日期
        
    Returns:
        (农历年, 农历月, 农历日)
    """
    try:
        solar = Solar(year, month, day)
        lunar = Converter.Solar2Lunar(solar)
        return lunar.year, lunar.month, lunar.day
    except Exception as e:
        print(f"转换失败 {year}-{month}-{day}: {e}")
        return None


def lunar_to_solar(year, month, day):
    """
    农历转公历
    
    Args:
        year: 农历年份
        month: 农历月份  
        day: 农历日期
        
    Returns:
        (公历年, 公历月, 公历日)
    """
    try:
        lunar = Lunar(year, month, day)
        solar = Converter.Lunar2Solar(lunar)
        return solar.year, solar.month, solar.day
    except Exception as e:
        print(f"转换失败 {year}-{month}-{day}: {e}")
        return None


def format_lunar(lunar_year, lunar_month, lunar_day):
    """格式化农历日期显示"""
    # 农历数字
    lunar_numbers = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    lunar_months = ["", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十", "冬", "腊"]
    lunar_days = ["初", "十", "廿", "三"]
    
    # 格式化月份
    if lunar_month <= 12:
        month_str = lunar_months[lunar_month]
    else:
        month_str = "闰" + lunar_months[lunar_month - 12]
    
    # 格式化日期
    if lunar_day <= 10:
        day_str = lunar_days[0] + lunar_numbers[lunar_day]
    elif lunar_day == 20:
        day_str = "二十"
    elif lunar_day < 30:
        day_str = lunar_days[2] + lunar_numbers[lunar_day - 20]
    else:
        day_str = "三十"
    
    return f"{month_str}月{day_str}"


def lunar_to_solar(lunar_year, lunar_month, lunar_day):
    """农历转公历"""
    if lunar_year < 1900 or lunar_year > 2100:
        return None
    
    # 计算从农历1900年1月初一到指定日期的天数
    days = 0
    
    for y in range(1900, lunar_year):
        for m in range(1, 13):
            days += get_lunar_month_days(y, m)
    
    for m in range(1, lunar_month):
        days += get_lunar_month_days(lunar_year, m)
    
    days += lunar_day
    
    # 从公历1900年1月31日开始计算（农历1900年1月初一对应的公历日期）
    date = datetime.date(1900, 1, 31)
    date = date + datetime.timedelta(days=days)
    
    return date.year, date.month, date.day


def format_lunar(lunar_year, lunar_month, lunar_day):
    """格式化农历日期"""
    # 农历数字
    lunar_numbers = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    lunar_months = ["", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十", "冬", "腊"]
    lunar_days = ["初", "十", "廿", "三"]
    
    # 格式化月份
    if lunar_month <= 12:
        month_str = lunar_months[lunar_month]
    else:
        month_str = "闰" + lunar_months[lunar_month - 12]
    
    # 格式化日期
    if lunar_day <= 10:
        day_str = lunar_days[0] + lunar_numbers[lunar_day]
    elif lunar_day == 20:
        day_str = "二十"
    elif lunar_day < 30:
        day_str = lunar_days[2] + lunar_numbers[lunar_day - 20]
    else:
        day_str = "三十"
    
    return f"{month_str}月{day_str}"
