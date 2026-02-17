# Gregorian and Lunar Calendar Program

## Project Description

A complete calendar application that displays both Gregorian calendar and Chinese Lunar calendar, and marks important holidays and traditional festivals.

Two versions are provided:
- **Web Version** - Flask-based browser application (recommended)
- **GUI Version** - tkinter-based desktop application

## Features

- ✅ Display both Gregorian and Lunar calendars
- ✅ Gregorian date and weekday display
- ✅ Lunar date display
- ✅ Holiday marking (Spring Festival, Qingming Festival, Labor Day, Dragon Boat Festival, Mid-Autumn Festival, National Day, etc.)
- ✅ Lunar traditional festival marking (Lantern Festival, Ghost Festival, Double Ninth Festival, Laba Festival, New Year's Eve, etc.)
- ✅ Month navigation (previous month, next month, today)
- ✅ Detailed date information display
- ✅ Beautiful user interface (Web version)

## Project Structure

```
calendar_app/
├── main.py                  # GUI application entry point
├── app.py                   # Web application entry point
├── gui.py                   # GUI interface module
├── lunar_calendar.py        # Lunar calendar calculation module
├── holidays.py              # Holiday data definitions
├── templates/
│   └── index.html          # Web application HTML template
├── requirements.txt         # GUI dependencies
└── web_requirements.txt     # Web dependencies
```

## Quick Start

### Web Version (Recommended)

#### Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

# Install Flask
pip install Flask
```

#### Run Application

```bash
# After activating virtual environment
cd calendar_app
python app.py

# Or use Python from virtual environment
/path/to/venv/bin/python app.py
```

Then access in browser: **http://localhost:5000**

### GUI Version

#### Install Dependencies

```bash
# Linux/Ubuntu
sudo apt install python3-tk

# macOS
brew install python-tk

# Windows
# tkinter is included in Python installation
```

#### Run Application

```bash
cd calendar_app
python main.py
```

## File Description

### lunar_calendar.py
Lunar calendar calculation module, providing the following functions:
- `solar_to_lunar()` - Convert Gregorian to Lunar
- `lunar_to_solar()` - Convert Lunar to Gregorian
- `format_lunar()` - Format Lunar date display
- Support conversion for years 1900-2100

### holidays.py
Holiday and traditional festival data definitions:
- Gregorian holidays (New Year's Day, Spring Festival, Qingming Festival, etc.)
- Lunar traditional festivals (Lantern Festival, Ghost Festival, Double Ninth Festival, etc.)
- Holiday query interface

### app.py (Web Version)
Flask Web application:
- REST API endpoints provide calendar data
- Interact with frontend templates
- Support JSON data exchange

### main.py (GUI Version)
GUI application entry point, launches tkinter calendar interface.

### templates/index.html
Frontend page of web application:
- Responsive design
- Dynamic calendar display
- Real-time interaction features

## Usage Guide

### Web Version Features

1. **Browse Calendar**
   - Left side displays complete monthly calendar grid
   - Each date shows both Gregorian and Lunar calendars
   - Holidays highlighted with red background
   - Today highlighted with yellow background

2. **Navigate Months**
   - Click "◀ Previous Month" and "Next Month ▶" to navigate
   - Or input year and month, click "Jump"
   - Click "Today" to quickly return to current date

3. **View Date Details**
   - Click any date to view detailed information
   - Right panel shows:
     - Gregorian date and weekday
     - Lunar date
     - Holiday/traditional festival marks

### GUI Version Features

1. **Navigate Months**
   - Click "◀ Previous" and "Next ▶" buttons
   - Use year and month input boxes to select directly
   - Click "Today" to quickly return to current month

2. **View Date Information**
   - Click any date in the calendar grid
   - Right panel displays detailed information

## Holiday Support

**Gregorian Holidays:**
- New Year's Day (January 1)
- Spring Festival (February 10-16)
- Qingming Festival (April 4-6)
- Labor Day (May 1-5)
- Dragon Boat Festival (June 10)
- Mid-Autumn Festival (September 15-17)
- National Day (October 1-7)

**Lunar Traditional Festivals:**
- Spring Festival (1st day of 1st lunar month)
- Lantern Festival (15th day of 1st lunar month)
- Dragon Boat Festival (5th day of 5th lunar month)
- Ghost Festival (15th day of 7th lunar month)
- Mid-Autumn Festival (15th day of 8th lunar month)
- Double Ninth Festival (9th day of 9th lunar month)
- Laba Festival (8th day of 12th lunar month)
- New Year's Eve (30th day of 12th lunar month)

## Technical Details

### Lunar Calendar Calculation Algorithm
Uses standard lunar calendar calculation tables (1900-2100), based on lunar month data for inter-conversion between Gregorian and Lunar calendars.

### Frontend Technology (Web Version)
- HTML5 + CSS3
- Native JavaScript (no framework needed)
- Responsive design
- Real-time AJAX interaction

### Backend Technology (Web Version)
- Flask Web framework
- Python 3.6+
- RESTful API design

### Desktop Application (GUI Version)
- Tkinter (Python standard library)
- Cross-platform compatibility

## Troubleshooting

### Web Version
- **Port in use**: Modify `port=5000` in app.py to another port
- **Import error**: Ensure virtual environment is activated, Flask is installed
- **Template not found**: Ensure templates folder is in same directory as app.py

### GUI Version
- **tkinter not found**: Run `sudo apt install python3-tk` on Linux
- **No display**: Use web version in GUI-less environment

## Extension Feature Suggestions

- [ ] Add more traditional holidays and commemorative days
- [ ] Support Lunar zodiac (animal year) display
- [ ] Add weather forecast feature
- [ ] Implement schedule reminder functionality
- [ ] Export calendar data (PDF, ICS format)
- [ ] Dark/light theme toggle
- [ ] Multi-language support
- [ ] Mobile application version

## License

MIT License

## Development Time

February 16, 2026
