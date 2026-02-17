# GUI interface module
import tkinter as tk
from tkinter import ttk
import datetime
import calendar
from lunar_calendar import solar_to_lunar, lunar_to_solar, format_lunar
from holidays import get_holiday_mark, get_gregorian_holiday, get_lunar_holiday


class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gregorian and Lunar Calendar")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        # Current displayed date
        self.current_date = datetime.date.today()
        self.year = self.current_date.year
        self.month = self.current_date.month
        
        # Create UI
        self.setup_ui()
        self.update_calendar()
    
    def setup_ui(self):
        """Set up user interface"""
        # Top control bar
        control_frame = ttk.Frame(self.root)
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # Previous month button
        ttk.Button(control_frame, text="◀ Previous", command=self.prev_month).pack(side=tk.LEFT, padx=5)
        
        # Year and month display and selection
        ttk.Label(control_frame, text="Year:").pack(side=tk.LEFT, padx=5)
        self.year_var = tk.StringVar(value=str(self.year))
        year_spinbox = ttk.Spinbox(control_frame, from_=1900, to=2100, textvariable=self.year_var,
                                    width=8, command=self.on_year_changed)
        year_spinbox.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(control_frame, text="Month:").pack(side=tk.LEFT, padx=5)
        self.month_var = tk.StringVar(value=str(self.month))
        month_spinbox = ttk.Spinbox(control_frame, from_=1, to=12, textvariable=self.month_var,
                                     width=4, command=self.on_month_changed)
        month_spinbox.pack(side=tk.LEFT, padx=5)
        
        # Today button
        ttk.Button(control_frame, text="Today", command=self.go_to_today).pack(side=tk.LEFT, padx=5)
        
        # Next month button
        ttk.Button(control_frame, text="Next ▶", command=self.next_month).pack(side=tk.LEFT, padx=5)
        
        # Main container - divided into left and right sections
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left section: Gregorian calendar
        left_frame = ttk.LabelFrame(main_frame, text="Gregorian Calendar", padding=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        self.gregorian_calendar_widget = self.create_gregorian_calendar(left_frame)
        
        # Right section: Lunar calendar and detailed information
        right_frame = ttk.LabelFrame(main_frame, text="Lunar Calendar Info", padding=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        # Date selection dropdown menu
        ttk.Label(right_frame, text="Select Date:").pack(anchor=tk.W, pady=5)
        self.day_var = tk.StringVar()
        self.day_combo = ttk.Combobox(right_frame, textvariable=self.day_var, state="readonly", width=20)
        self.day_combo.pack(anchor=tk.W, fill=tk.X, pady=5)
        self.day_combo.bind("<<ComboboxSelected>>", self.on_day_selected)
        
        # Detailed information display area
        self.info_text = tk.Text(right_frame, height=20, width=30, wrap=tk.WORD, state=tk.DISABLED)
        self.info_text.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.info_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.info_text.config(yscrollcommand=scrollbar.set)
    
    def create_gregorian_calendar(self, parent):
        """Create Gregorian calendar display section"""
        # Create table frame
        cal_frame = ttk.Frame(parent)
        cal_frame.pack(fill=tk.BOTH, expand=True)
        
        # Week header
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            label = ttk.Label(cal_frame, text=day, relief=tk.RAISED, borderwidth=1,
                            justify=tk.CENTER, anchor=tk.CENTER)
            label.grid(row=0, column=i, sticky="nsew", padx=1, pady=1)
        
        # Create date button grid
        self.day_buttons = {}
        for week in range(6):
            for day in range(7):
                btn = tk.Button(cal_frame, text="", relief=tk.RAISED, borderwidth=1,
                              font=("Arial", 10), height=5, width=12)
                btn.grid(row=week + 1, column=day, sticky="nsew", padx=1, pady=1)
                self.day_buttons[(week, day)] = btn
                btn.bind("<Button-1>", self.on_day_clicked)
        
        # Set grid weights
        for i in range(7):
            cal_frame.grid_columnconfigure(i, weight=1)
        for i in range(7):
            cal_frame.grid_rowconfigure(i, weight=1)
        
        return cal_frame
    
    def update_calendar(self):
        """Update calendar display"""
        try:
            self.year = int(self.year_var.get())
            self.month = int(self.month_var.get())
        except ValueError:
            return
        
        # Get calendar for the month
        cal = calendar.monthcalendar(self.year, self.month)
        
        # Clear date list
        days_in_month = calendar.monthrange(self.year, self.month)[1]
        day_list = []
        
        # Fill date buttons
        for week_num, week in enumerate(cal):
            for day_num, day in enumerate(week):
                button = self.day_buttons[(week_num, day_num)]
                if day == 0:
                    button.config(text="", state=tk.DISABLED, bg="lightgray")
                else:
                    day_list.append(day)
                    lunar_y, lunar_m, lunar_d = solar_to_lunar(self.year, self.month, day)
                    lunar_str = format_lunar(lunar_y, lunar_m, lunar_d)
                    holiday = get_holiday_mark(self.month, day, lunar_m, lunar_d, self.year)
                    
                    # Set button text
                    text = f"{day}\n{lunar_str}"
                    if holiday:
                        text += f"\n【{holiday}】"
                    
                    button.config(text=text, command=lambda d=day: self.select_day(d),
                                state=tk.NORMAL, bg="white", fg="black")
                    
                    # Highlight today
                    if (self.year == self.current_date.year and
                        self.month == self.current_date.month and
                        day == self.current_date.day):
                        button.config(bg="yellow")
        
        # Update date dropdown
        self.day_combo.config(values=[f"{d}" for d in day_list])
        if day_list:
            self.day_combo.current(0)
            self.select_day(day_list[0])
    
    def select_day(self, day):
        """Select a day"""
        if day == 0:
            return
        
        lunar_y, lunar_m, lunar_d = solar_to_lunar(self.year, self.month, day)
        self.display_day_info(self.year, self.month, day, lunar_y, lunar_m, lunar_d)
    
    def display_day_info(self, g_year, g_month, g_day, l_year, l_month, l_day):
        """Display detailed information for specified date"""
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        
        # Get weekday
        date_obj = datetime.date(g_year, g_month, g_day)
        days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        weekday = days_of_week[date_obj.weekday()]
        
        # Build information text
        info = f"Gregorian Date\n{'='*20}\n"
        info += f"{g_year}-{g_month:02d}-{g_day:02d}\n"
        info += f"{weekday}\n\n"
        
        info += f"Lunar Date\n{'='*20}\n"
        info += f"{l_year}\n"
        info += format_lunar(l_year, l_month, l_day) + "\n\n"
        
        # Display holidays
        greg_holiday = get_gregorian_holiday(g_month, g_day, g_year)
        lunar_holiday = get_lunar_holiday(l_month, l_day)
        
        info += f"Holiday Info\n{'='*20}\n"
        if greg_holiday or lunar_holiday:
            if greg_holiday:
                info += f"Gregorian: {greg_holiday}\n"
            if lunar_holiday:
                info += f"Lunar: {lunar_holiday}\n"
        else:
            info += "No holidays\n"
        
        self.info_text.insert(tk.END, info)
        self.info_text.config(state=tk.DISABLED)
    
    def on_day_clicked(self, event):
        """Handle date button click event"""
        widget = event.widget
        text = widget.cget("text")
        if text and text.split("\n")[0].isdigit():
            day = int(text.split("\n")[0])
            self.select_day(day)
            self.day_var.set(f"{day}")
    
    def on_day_selected(self, event):
        """Handle date dropdown selection"""
        selected = self.day_combo.get()
        if selected:
            day = int(selected)
            self.select_day(day)
    
    def on_year_changed(self):
        """Handle year change"""
        self.update_calendar()
    
    def on_month_changed(self):
        """Handle month change"""
        self.update_calendar()
    
    def prev_month(self):
        """Previous month"""
        if self.month == 1:
            self.year -= 1
            self.month = 12
        else:
            self.month -= 1
        self.year_var.set(str(self.year))
        self.month_var.set(str(self.month))
        self.update_calendar()
    
    def next_month(self):
        """Next month"""
        if self.month == 12:
            self.year += 1
            self.month = 1
        else:
            self.month += 1
        self.year_var.set(str(self.year))
        self.month_var.set(str(self.month))
        self.update_calendar()
    
    def go_to_today(self):
        """Go to today"""
        self.year = self.current_date.year
        self.month = self.current_date.month
        self.year_var.set(str(self.year))
        self.month_var.set(str(self.month))
        self.update_calendar()


def run_app():
    """Run the application"""
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_app()
