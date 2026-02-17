# 1stTest - 公历农历日历程序

## 项目描述

一个完整的日历应用程序，同时显示公历和中国农历，并标记重要节假日和传统节日。

提供两个版本：
- **Web 版本** - 基于 Flask 的浏览器应用（推荐）
- **GUI 版本** - 基于 tkinter 的桌面应用

## 功能特性

- ✅ 同时显示公历和农历
- ✅ 公历日期、星期显示
- ✅ 农历日期展示
- ✅ 节假日标记（春节、清明节、劳动节、端午节、中秋节、国庆节等）
- ✅ 农历传统节日标记（元宵节、中元节、重阳节、腊八节、除夕等）
- ✅ 月份导航（上月、下月、今天）
- ✅ 日期详细信息显示
- ✅ 美观的用户界面（Web 版）

## 项目结构

```
calendar_app/
├── main.py                  # GUI 应用入口
├── app.py                   # Web 应用入口
├── gui.py                   # GUI 界面模块
├── lunar_calendar.py        # 农历计算模块
├── holidays.py              # 节假日数据定义
├── templates/
│   └── index.html          # Web 应用 HTML 模板
├── requirements.txt         # GUI 依赖
└── web_requirements.txt     # Web 依赖
```

## 快速开始

### Web 版本（推荐）

#### 安装依赖

```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 安装 Flask
pip install Flask
```

#### 运行应用

```bash
# 激活虚拟环境后
cd calendar_app
python app.py

# 或使用虚拟环境的 Python
/path/to/venv/bin/python app.py
```

然后在浏览器中访问：**http://localhost:5000**

### GUI 版本

#### 安装依赖

```bash
# Linux/Ubuntu
sudo apt install python3-tk

# macOS
brew install python-tk

# Windows
# tkinter 已包含在 Python 安装中
```

#### 运行应用

```bash
cd calendar_app
python main.py
```

## 文件说明

### lunar_calendar.py
农历计算模块，提供以下功能：
- `solar_to_lunar()` - 公历转农历
- `lunar_to_solar()` - 农历转公历
- `format_lunar()` - 格式化农历日期显示
- 支持 1900-2100 年的转换

### holidays.py
节假日和传统节日数据定义：
- 公历节假日（元旦、春节、清明节等）
- 农历传统节日（元宵节、中元节、重阳节等）
- 节假日查询接口

### app.py（Web 版本）
Flask Web 应用程序：
- REST API 端点提供日历数据
- 与前端模板交互
- 支持 JSON 数据交换

### main.py（GUI 版本）
GUI 应用入口，启动 tkinter 日历界面。

### templates/index.html
Web 应用的前端页面：
- 响应式设计
- 动态日历显示
- 实时交互功能

## 使用说明

### Web 版本功能

1. **浏览日历**
   - 左侧显示完整的月份日历网格
   - 每个日期同时显示公历和农历
   - 节假日用红色背景高亮
   - 今天用黄色背景高亮

2. **导航月份**
   - 点击"◀ 上月"和"下月 ▶"导航
   - 或输入年份和月份，点击"跳转"
   - 点击"今天"快速回到当前日期

3. **查看日期详情**
   - 点击任意日期查看详细信息
   - 右侧面板显示：
     - 公历日期和星期
     - 农历日期
     - 节假日/传统节日标记

### GUI 版本功能

1. **导航月份**
   - 点击"◀ 上月"和"下月 ▶"按钮
   - 使用年份和月份输入框直接选择
   - 点击"今天"快速回到当前月份

2. **查看日期信息**
   - 点击日历网格中的任意日期
   - 右侧面板显示详细信息

## 节假日支持

**公历节假日：**
- 元旦（1月1日）
- 春节假期（2月10-16日）
- 清明节（4月4-6日）
- 劳动节（5月1-5日）
- 端午节（6月10日）
- 中秋节（9月15-17日）
- 国庆节（10月1-7日）

**农历传统节日：**
- 春节（正月初一）
- 元宵节（正月十五）
- 端午节（五月初五）
- 中元节（七月十五）
- 中秋节（八月十五）
- 重阳节（九月初九）
- 腊八节（十二月初八）
- 除夕（十二月三十）

## 技术细节

### 农历计算算法
使用标准的农历计算表（1900-2100年），基于农历月份数据进行公历和农历的相互转换。

### 前端技术（Web 版本）
- HTML5 + CSS3
- 原生 JavaScript（无需框架）
- 响应式设计
- 实时 AJAX 交互

### 后端技术（Web 版本）
- Flask Web 框架
- Python 3.6+
- RESTful API 设计

### 桌面应用（GUI 版本）
- Tkinter（Python 标准库）
- 跨平台兼容性

## 故障排除

### Web 版本
- **端口被占用**: 修改 app.py 中的 `port=5000` 为其他端口
- **导入错误**: 确保虚拟环境已激活，Flask 已安装
- **模板找不到**: 确保 templates 文件夹与 app.py 在同一目录

### GUI 版本
- **tkinter 找不到**: 在 Linux 上运行 `sudo apt install python3-tk`
- **no display**: 在无 GUI 环境使用 Web 版本

## 扩展功能建议

- [ ] 添加更多传统节日和纪念日
- [ ] 支持农历年份干支（生肖）显示
- [ ] 添加天气预报功能
- [ ] 实现日程提醒功能
- [ ] 导出日历数据（PDF、ICS 格式）
- [ ] 深色/浅色主题切换
- [ ] 多语言支持
- [ ] 移动应用版本

## 许可证

MIT License

## 开发时间

2026年2月16日
