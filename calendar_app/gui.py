# GUI界面模块
import tkinter as tk
from tkinter import ttk
import datetime
import calendar
from lunar_calendar import solar_to_lunar, lunar_to_solar, format_lunar
from holidays import get_holiday_mark, get_gregorian_holiday, get_lunar_holiday


class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("公历农历日历")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        # 当前显示的日期
        self.current_date = datetime.date.today()
        self.year = self.current_date.year
        self.month = self.current_date.month
        
        # 创建UI
        self.setup_ui()
        self.update_calendar()
    
    def setup_ui(self):
        """设置用户界面"""
        # 顶部控制栏
        control_frame = ttk.Frame(self.root)
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # 上一个月按钮
        ttk.Button(control_frame, text="◀ 上月", command=self.prev_month).pack(side=tk.LEFT, padx=5)
        
        # 年月显示和选择
        ttk.Label(control_frame, text="年份:").pack(side=tk.LEFT, padx=5)
        self.year_var = tk.StringVar(value=str(self.year))
        year_spinbox = ttk.Spinbox(control_frame, from_=1900, to=2100, textvariable=self.year_var,
                                    width=8, command=self.on_year_changed)
        year_spinbox.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(control_frame, text="月份:").pack(side=tk.LEFT, padx=5)
        self.month_var = tk.StringVar(value=str(self.month))
        month_spinbox = ttk.Spinbox(control_frame, from_=1, to=12, textvariable=self.month_var,
                                     width=4, command=self.on_month_changed)
        month_spinbox.pack(side=tk.LEFT, padx=5)
        
        # 今天按钮
        ttk.Button(control_frame, text="今天", command=self.go_to_today).pack(side=tk.LEFT, padx=5)
        
        # 下一个月按钮
        ttk.Button(control_frame, text="下月 ▶", command=self.next_month).pack(side=tk.LEFT, padx=5)
        
        # 主容器 - 分为左右两部分
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 左部分：公历日历
        left_frame = ttk.LabelFrame(main_frame, text="公历日历", padding=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        self.gregorian_calendar_widget = self.create_gregorian_calendar(left_frame)
        
        # 右部分：农历和详细信息
        right_frame = ttk.LabelFrame(main_frame, text="农历信息", padding=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        # 日期选择下拉菜单
        ttk.Label(right_frame, text="选择日期:").pack(anchor=tk.W, pady=5)
        self.day_var = tk.StringVar()
        self.day_combo = ttk.Combobox(right_frame, textvariable=self.day_var, state="readonly", width=20)
        self.day_combo.pack(anchor=tk.W, fill=tk.X, pady=5)
        self.day_combo.bind("<<ComboboxSelected>>", self.on_day_selected)
        
        # 详细信息显示区域
        self.info_text = tk.Text(right_frame, height=20, width=30, wrap=tk.WORD, state=tk.DISABLED)
        self.info_text.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 添加滚动条
        scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.info_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.info_text.config(yscrollcommand=scrollbar.set)
    
    def create_gregorian_calendar(self, parent):
        """创建公历日历显示部分"""
        # 创建表格框架
        cal_frame = ttk.Frame(parent)
        cal_frame.pack(fill=tk.BOTH, expand=True)
        
        # 周头
        days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        for i, day in enumerate(days):
            label = ttk.Label(cal_frame, text=day, relief=tk.RAISED, borderwidth=1,
                            justify=tk.CENTER, anchor=tk.CENTER)
            label.grid(row=0, column=i, sticky="nsew", padx=1, pady=1)
        
        # 创建日期按钮网格
        self.day_buttons = {}
        for week in range(6):
            for day in range(7):
                btn = tk.Button(cal_frame, text="", relief=tk.RAISED, borderwidth=1,
                              font=("Arial", 10), height=5, width=12)
                btn.grid(row=week + 1, column=day, sticky="nsew", padx=1, pady=1)
                self.day_buttons[(week, day)] = btn
                btn.bind("<Button-1>", self.on_day_clicked)
        
        # 设置网格权重
        for i in range(7):
            cal_frame.grid_columnconfigure(i, weight=1)
        for i in range(7):
            cal_frame.grid_rowconfigure(i, weight=1)
        
        return cal_frame
    
    def update_calendar(self):
        """更新日历显示"""
        try:
            self.year = int(self.year_var.get())
            self.month = int(self.month_var.get())
        except ValueError:
            return
        
        # 获取该月的日历
        cal = calendar.monthcalendar(self.year, self.month)
        
        # 清空日期列表
        days_in_month = calendar.monthrange(self.year, self.month)[1]
        day_list = []
        
        # 填充日期按钮
        for week_num, week in enumerate(cal):
            for day_num, day in enumerate(week):
                button = self.day_buttons[(week_num, day_num)]
                if day == 0:
                    button.config(text="", state=tk.DISABLED, bg="lightgray")
                else:
                    day_list.append(day)
                    lunar_y, lunar_m, lunar_d = solar_to_lunar(self.year, self.month, day)
                    lunar_str = format_lunar(lunar_y, lunar_m, lunar_d)
                    holiday = get_holiday_mark(self.month, day, lunar_m, lunar_d)
                    
                    # 设置按钮文本
                    text = f"{day}\n{lunar_str}"
                    if holiday:
                        text += f"\n【{holiday}】"
                    
                    button.config(text=text, command=lambda d=day: self.select_day(d),
                                state=tk.NORMAL, bg="white", fg="black")
                    
                    # 高亮今天
                    if (self.year == self.current_date.year and
                        self.month == self.current_date.month and
                        day == self.current_date.day):
                        button.config(bg="yellow")
        
        # 更新日期下拉框
        self.day_combo.config(values=[f"{d}日" for d in day_list])
        if day_list:
            self.day_combo.current(0)
            self.select_day(day_list[0])
    
    def select_day(self, day):
        """选择某一天"""
        if day == 0:
            return
        
        lunar_y, lunar_m, lunar_d = solar_to_lunar(self.year, self.month, day)
        self.display_day_info(self.year, self.month, day, lunar_y, lunar_m, lunar_d)
    
    def display_day_info(self, g_year, g_month, g_day, l_year, l_month, l_day):
        """显示指定日期的详细信息"""
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        
        # 获取星期
        date_obj = datetime.date(g_year, g_month, g_day)
        weekday = ["一", "二", "三", "四", "五", "六", "日"][date_obj.weekday()]
        
        # 构建信息文本
        info = f"公历日期\n{'='*20}\n"
        info += f"{g_year}年{g_month}月{g_day}日\n"
        info += f"星期{weekday}\n\n"
        
        info += f"农历日期\n{'='*20}\n"
        info += f"{l_year}年\n"
        info += format_lunar(l_year, l_month, l_day) + "\n\n"
        
        # 显示节假日
        greg_holiday = get_gregorian_holiday(g_month, g_day)
        lunar_holiday = get_lunar_holiday(l_month, l_day)
        
        info += f"节假日信息\n{'='*20}\n"
        if greg_holiday or lunar_holiday:
            if greg_holiday:
                info += f"公历: {greg_holiday}\n"
            if lunar_holiday:
                info += f"农历: {lunar_holiday}\n"
        else:
            info += "无节假日\n"
        
        self.info_text.insert(tk.END, info)
        self.info_text.config(state=tk.DISABLED)
    
    def on_day_clicked(self, event):
        """处理日期按钮点击事件"""
        widget = event.widget
        text = widget.cget("text")
        if text and text.split("\n")[0].isdigit():
            day = int(text.split("\n")[0])
            self.select_day(day)
            self.day_var.set(f"{day}日")
    
    def on_day_selected(self, event):
        """处理日期下拉框选择"""
        selected = self.day_combo.get()
        if selected:
            day = int(selected.replace("日", ""))
            self.select_day(day)
    
    def on_year_changed(self):
        """处理年份变化"""
        self.update_calendar()
    
    def on_month_changed(self):
        """处理月份变化"""
        self.update_calendar()
    
    def prev_month(self):
        """上一个月"""
        if self.month == 1:
            self.year -= 1
            self.month = 12
        else:
            self.month -= 1
        self.year_var.set(str(self.year))
        self.month_var.set(str(self.month))
        self.update_calendar()
    
    def next_month(self):
        """下一个月"""
        if self.month == 12:
            self.year += 1
            self.month = 1
        else:
            self.month += 1
        self.year_var.set(str(self.year))
        self.month_var.set(str(self.month))
        self.update_calendar()
    
    def go_to_today(self):
        """回到今天"""
        self.year = self.current_date.year
        self.month = self.current_date.month
        self.year_var.set(str(self.year))
        self.month_var.set(str(self.month))
        self.update_calendar()


def run_app():
    """运行应用程序"""
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_app()
