# Chinese holidays and festivals data by year
# Based on official China State Council holiday announcements

# Year-specific Gregorian holidays (month, day): holiday_name
GREGORIAN_HOLIDAYS_BY_YEAR = {
    2023: {
        # New Year's Day holiday span: 2022-12-31 to 2023-01-02 (include Jan 1-2 in 2023)
        (1, 1): "New Year's Day",
        (1, 2): "New Year's Day",
        # Spring Festival: Jan 21 - Jan 27, 2023 (7 days)
        (1, 21): "Spring Festival",
        (1, 22): "Spring Festival",
        (1, 23): "Spring Festival",
        (1, 24): "Spring Festival",
        (1, 25): "Spring Festival",
        (1, 26): "Spring Festival",
        (1, 27): "Spring Festival",
        # Qingming: Apr 5, 2023
        (4, 5): "Qingming Festival",
        # Labor Day: Apr 29 - May 3, 2023
        (4, 29): "Labor Day",
        (4, 30): "Labor Day",
        (5, 1): "Labor Day",
        (5, 2): "Labor Day",
        (5, 3): "Labor Day",
        # Dragon Boat: Jun 22 - Jun 24, 2023
        (6, 22): "Dragon Boat Festival",
        (6, 23): "Dragon Boat Festival",
        (6, 24): "Dragon Boat Festival",
        # Mid-Autumn & National Day combined: Sep 29 - Oct 6, 2023
        (9, 29): "National Day",
        (9, 30): "National Day",
        (10, 1): "National Day",
        (10, 2): "National Day",
        (10, 3): "National Day",
        (10, 4): "National Day",
        (10, 5): "National Day",
        (10, 6): "National Day",
    },
    2024: {
        (1, 1): "New Year's Day",
        (2, 10): "Spring Festival",
        (2, 11): "Spring Festival",
        (2, 12): "Spring Festival",
        (2, 13): "Spring Festival",
        (2, 14): "Spring Festival",
        (2, 15): "Spring Festival",
        (2, 16): "Spring Festival",
        (2, 17): "Spring Festival",
        (4, 4): "Qingming Festival",
        (4, 5): "Qingming Festival",
        (4, 6): "Qingming Festival",
        (5, 1): "Labor Day",
        (5, 2): "Labor Day",
        (5, 3): "Labor Day",
        (5, 4): "Labor Day",
        (5, 5): "Labor Day",
        (6, 10): "Dragon Boat Festival",
        (9, 15): "Mid-Autumn Festival",
        (9, 16): "Mid-Autumn Festival",
        (9, 17): "Mid-Autumn Festival",
        (10, 1): "National Day",
        (10, 2): "National Day",
        (10, 3): "National Day",
        (10, 4): "National Day",
        (10, 5): "National Day",
        (10, 6): "National Day",
        (10, 7): "National Day",
    },
    2025: {
        (1, 1): "New Year's Day",
        # Spring Festival: Jan 28 - Feb 4, 2025 (8 days)
        (1, 28): "Spring Festival",
        (1, 29): "Spring Festival",
        (1, 30): "Spring Festival",
        (1, 31): "Spring Festival",
        (2, 1): "Spring Festival",
        (2, 2): "Spring Festival",
        (2, 3): "Spring Festival",
        (2, 4): "Spring Festival",
        (4, 4): "Qingming Festival",
        (4, 5): "Qingming Festival",
        (4, 6): "Qingming Festival",
        (5, 1): "Labor Day",
        (5, 2): "Labor Day",
        (5, 3): "Labor Day",
        (5, 4): "Labor Day",
        (5, 5): "Labor Day",
        # Dragon Boat (端午): May 31 - Jun 2, 2025
        (5, 31): "Dragon Boat Festival",
        (6, 1): "Dragon Boat Festival",
        (6, 2): "Dragon Boat Festival",
        # Mid-Autumn and National Day combined holiday: Oct 1 - Oct 8, 2025
        (10, 1): "National Day",
        (10, 2): "National Day",
        (10, 3): "National Day",
        (10, 4): "National Day",
        (10, 5): "National Day",
        (10, 6): "National Day",
        (10, 7): "National Day",
        (10, 8): "National Day",
    },
    2026: {
        (1, 1): "New Year's Day",
        (1, 2): "New Year's Day",
        (1, 3): "New Year's Day",
        # Spring Festival: Feb 15 - Feb 23, 2026 (9 days)
        (2, 15): "Spring Festival",
        (2, 16): "Spring Festival",
        (2, 17): "Spring Festival",
        (2, 18): "Spring Festival",
        (2, 19): "Spring Festival",
        (2, 20): "Spring Festival",
        (2, 21): "Spring Festival",
        (2, 22): "Spring Festival",
        (2, 23): "Spring Festival",
        (4, 4): "Qingming Festival",
        (4, 5): "Qingming Festival",
        (4, 6): "Qingming Festival",
        (5, 1): "Labor Day",
        (5, 2): "Labor Day",
        (5, 3): "Labor Day",
        (5, 4): "Labor Day",
        (5, 5): "Labor Day",
        # Dragon Boat: Jun 19 - Jun 21, 2026
        (6, 19): "Dragon Boat Festival",
        (6, 20): "Dragon Boat Festival",
        (6, 21): "Dragon Boat Festival",
        # Mid-Autumn: Sep 25 - Sep 27, 2026
        (9, 25): "Mid-Autumn Festival",
        (9, 26): "Mid-Autumn Festival",
        (9, 27): "Mid-Autumn Festival",
        (10, 1): "National Day",
        (10, 2): "National Day",
        (10, 3): "National Day",
        (10, 4): "National Day",
        (10, 5): "National Day",
        (10, 6): "National Day",
        (10, 7): "National Day",
    },
}

# Lunar holidays and traditional festivals
LUNAR_HOLIDAYS = {
    (1, 1): "Spring Festival",
    (1, 15): "Lantern Festival",
    (5, 5): "Dragon Boat Festival",
    (7, 15): "Ghost Festival",
    (8, 15): "Mid-Autumn Festival",
    (9, 9): "Double Ninth Festival",
    (12, 8): "Laba Festival",
    (12, 30): "New Year's Eve",
}

# Twenty-four Solar Terms
SOLAR_TERMS_CN = {
    "Spring Begins", "Rain Water", "Insects Awakened", "Spring Equinox", "Pure Brightness", "Grain Rain",
    "Summer Begins", "Grain Fill", "Grain in Ear", "Summer Solstice", "Minor Heat", "Major Heat",
    "Autumn Begins", "Heat Ends", "White Dew", "Autumn Equinox", "Cold Dew", "Frost Descent",
    "Winter Begins", "Minor Snow", "Major Snow", "Winter Solstice", "Minor Cold", "Major Cold"
}

def get_gregorian_holiday(month, day, year=None):
    """Get Gregorian holiday for a specific date
    
    Args:
        month: Month (1-12)
        day: Day of month
        year: Year (optional, defaults to current year if not provided)
    
    Returns:
        Holiday name string or empty string if not a holiday
    """
    if year is None:
        from datetime import date
        year = date.today().year
    
    # Get holidays for the year, default to current year's structure if year not in data
    holidays = GREGORIAN_HOLIDAYS_BY_YEAR.get(year, GREGORIAN_HOLIDAYS_BY_YEAR.get(2026, {}))
    return holidays.get((month, day), "")

def get_lunar_holiday(lunar_month, lunar_day):
    """Get Lunar holiday"""
    return LUNAR_HOLIDAYS.get((lunar_month, lunar_day), "")

def get_holiday_mark(month, day, lunar_month, lunar_day, year=None):
    """Get holiday mark for the date
    
    Args:
        month: Gregorian month
        day: Gregorian day
        lunar_month: Lunar month
        lunar_day: Lunar day
        year: Year (optional)
    
    Returns:
        Holiday name string or empty string
    """
    greg_holiday = get_gregorian_holiday(month, day, year)
    lunar_holiday = get_lunar_holiday(lunar_month, lunar_day)
    
    if greg_holiday:
        return greg_holiday
    elif lunar_holiday:
        return lunar_holiday
    else:
        return ""
