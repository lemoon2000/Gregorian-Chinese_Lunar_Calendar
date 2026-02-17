# 中国节假日数据

# 公历节假日 (包括周末)
GREGORIAN_HOLIDAYS = {
    (1, 1): "元旦",
    (2, 10): "春节",
    (2, 11): "春节",
    (2, 12): "春节",
    (2, 13): "春节",
    (2, 14): "春节",
    (2, 15): "春节",
    (2, 16): "春节",
    (4, 4): "清明节",
    (4, 5): "清明节",
    (4, 6): "清明节",
    (5, 1): "劳动节",
    (5, 2): "劳动节",
    (5, 3): "劳动节",
    (5, 4): "劳动节",
    (5, 5): "劳动节",
    (6, 10): "端午节",
    (9, 15): "中秋节",
    (9, 16): "中秋节",
    (9, 17): "中秋节",
    (10, 1): "国庆节",
    (10, 2): "国庆节",
    (10, 3): "国庆节",
    (10, 4): "国庆节",
    (10, 5): "国庆节",
    (10, 6): "国庆节",
    (10, 7): "国庆节",
}

# 农历节假日和传统节日
LUNAR_HOLIDAYS = {
    (1, 1): "春节",
    (1, 15): "元宵节",
    (5, 5): "端午节",
    (7, 15): "中元节",
    (8, 15): "中秋节",
    (9, 9): "重阳节",
    (12, 8): "腊八节",
    (12, 30): "除夕",
}

# 二十四节气
SOLAR_TERMS_CN = {
    "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
    "立夏", "小满", "芒种", "夏至", "小暑", "大暑",
    "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
    "立冬", "小雪", "大雪", "冬至", "小寒", "大寒"
}

def get_gregorian_holiday(month, day):
    """获取公历节假日"""
    return GREGORIAN_HOLIDAYS.get((month, day), "")

def get_lunar_holiday(lunar_month, lunar_day):
    """获取农历节假日"""
    return LUNAR_HOLIDAYS.get((lunar_month, lunar_day), "")

def get_holiday_mark(month, day, lunar_month, lunar_day):
    """获取该日期的节假日标记"""
    greg_holiday = get_gregorian_holiday(month, day)
    lunar_holiday = get_lunar_holiday(lunar_month, lunar_day)
    
    if greg_holiday:
        return greg_holiday
    elif lunar_holiday:
        return lunar_holiday
    else:
        return ""
