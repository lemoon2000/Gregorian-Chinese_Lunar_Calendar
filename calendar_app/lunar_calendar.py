# Lunar calendar calculation module
from lunarcalendar import Converter, Solar, Lunar


def solar_to_lunar(year, month, day):
    """
    Convert Gregorian calendar to Lunar calendar
    
    Args:
        year: Gregorian year
        month: Gregorian month
        day: Gregorian day
        
    Returns:
        (Lunar year, Lunar month, Lunar day)
    """
    try:
        solar = Solar(year, month, day)
        lunar = Converter.Solar2Lunar(solar)
        return lunar.year, lunar.month, lunar.day
    except Exception as e:
        print(f"Conversion failed {year}-{month}-{day}: {e}")
        return None


def lunar_to_solar(year, month, day):
    """
    Convert Lunar calendar to Gregorian calendar
    
    Args:
        year: Lunar year
        month: Lunar month  
        day: Lunar day
        
    Returns:
        (Gregorian year, Gregorian month, Gregorian day)
    """
    try:
        lunar = Lunar(year, month, day)
        solar = Converter.Lunar2Solar(lunar)
        return solar.year, solar.month, solar.day
    except Exception as e:
        print(f"Conversion failed {year}-{month}-{day}: {e}")
        return None


def format_lunar(lunar_year, lunar_month, lunar_day):
    """Format Lunar date for display"""
    # Lunar numbers
    lunar_numbers = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    lunar_months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    lunar_day_prefixes = ["", "10", "20", "30"]
    
    # Format month
    if lunar_month <= 12:
        month_str = lunar_months[lunar_month]
    else:
        month_str = "Leap " + lunar_months[lunar_month - 12]
    
    # Format day
    if lunar_day <= 10:
        day_str = "Day " + lunar_numbers[lunar_day]
    elif lunar_day == 20:
        day_str = "Day 20"
    elif lunar_day < 30:
        day_str = "Day " + lunar_numbers[lunar_day - 20]
    else:
        day_str = "Day 30"
    
    return f"{month_str} {day_str}"

