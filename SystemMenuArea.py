from SystemMain import *

class SystemMenu:
    def __init__(self, win_obj):
        self.win = win_obj
        self.title_name = "视觉点胶2系统"
        self.auth = "管理人员权限"
        self.task_num = 1
        self.study_mode = "相机模式"
        self.running_mode = "单文件加工"
        self.win.title(f"{self.title_name:<50}操作权限：{self.auth:<30}当前加工任务：{self.task_num:<30}" \
                               f"示教模式：{self.study_mode:<30}运行模式: {self.running_mode}")
        self.menu_bar = Menu(self.win)
        self.system_menu = None
        self.workmanship_menu = None
        self.tools_menu = None
        self.help_menu = None
        self.system_menu_frame = None
        self.frame_heigth = int(4 * self.win.system_interval)
        self.button_palce_heigth = int(4.1 * self.win.system_interval)
    def system_menu_entry(self):
        self.system_menus_create()
        self.frame_and_widgets_create()
    def system_menus_create(self):
        self.__create_system_config_menu()
        self.__create_workmanship_config_menu()
        self.__create_tools_menu()
        self.__create_help_menu()
        self.win.config(menu=self.menu_bar)
    def frame_and_widgets_create(self):
        self.__create_system_menu_frame()
        self.__create_emergency_stop_button()
        self.__create_reset_button()
        self.__create_stop_button()
        self.__create_start_stop_box()
        self.__create_start_button()
        self.__create_number_box()
        self.__create_clear_alarms_button()
    def __create_system_menu_frame(self):
        self.system_menu_frame = \
            self.win.tool.create_frame_with_bg_and_layout(self.win, bg="lightblue", width=self.win.screen_width,
                                                          height=self.frame_heigth,
                                                          anchor="sw", y=self.win.system_interval*2)
    def __create_emergency_stop_button(self):
        self.win.tool.create_button_and_layout(self.system_menu_frame, text="急停", command="",
                                               width=self.win.button_width, height=self.win.button_heigth, anchor="sw",
                                               x=self.win.system_interval, y=self.button_palce_heigth)
    def __create_reset_button(self):
        self.win.tool.create_button_and_layout(self.system_menu_frame, text="复位", command="",
                                               width=self.win.button_width, height=self.win.button_heigth, anchor="sw",
                                               x=self.win.system_interval*6, y=self.button_palce_heigth)
    def __create_stop_button(self):
        self.win.tool.create_button_and_layout(self.system_menu_frame, text="停止", command="",
                                               width=self.win.button_width, height=self.win.button_heigth, anchor="sw",
                                               x=self.win.system_interval*11, y=self.button_palce_heigth)
    def __create_start_stop_box(self):
        self.win.tool.create_combobox_and_layout(self.system_menu_frame, values=("暂停", "继续"),
                                                 width=self.win.combox_width, anchor="sw",
                                                 x=self.win.system_interval*16, y=self.button_palce_heigth)
    def __create_start_button(self):
        self.win.tool.create_button_and_layout(self.system_menu_frame, text="启动", command="",
                                               width=self.win.button_width, height=self.win.button_heigth, anchor="sw",
                                               x=self.win.system_interval*27, y=self.button_palce_heigth)
    def __create_number_box(self):
        self.win.tool.create_combobox_and_layout(self.system_menu_frame, values=("1", "2", "3"),
                                                 width=self.win.combox_width, anchor="sw",
                                                 x=self.win.system_interval*32, y=self.button_palce_heigth)
    def __create_clear_alarms_button(self):
        self.win.tool.create_button_and_layout(self.system_menu_frame, text="报警清除", command="",
                                               width=self.win.button_width_ex, height=self.win.button_heigth, anchor="sw",
                                               x=self.win.screen_width-self.win.button_width*2,
                                               y=self.button_palce_heigth)
    def __create_system_config_menu(self):
        self.system_menu = Menu(self.menu_bar, tearoff=0)
        self.system_menu.add_command(label="操作权限配置", command='')
        self.system_menu.add_separator()
        self.system_menu.add_command(label="程序升级", command='')
        self.system_menu.add_command(label="系统配置", command='')
        self.system_menu.add_separator()
        self.system_menu.add_command(label="机械配置", command='')
        self.system_menu.add_command(label="I/O功能配置", command='')
        self.system_menu.add_separator()
        self.system_menu.add_command(label="相机光源配置", command='')
        self.system_menu.add_command(label="视觉功能配置", command='')
        self.system_menu.add_separator()
        self.system_menu.add_command(label="胶枪旋转配置", command='')
        self.system_menu.add_command(label="胶阀偏移配置", command='')
        self.system_menu.add_command(label="Z轴对针配置", command='')
        self.system_menu.add_command(label="自动对针配置", command='')
        self.system_menu.add_separator()
        self.system_menu.add_command(label="胶阀清洗配置", command='')
        self.system_menu.add_command(label="功能配置", command='')
        self.menu_bar.add_cascade(label="系统配置(C)", menu=self.system_menu)
    def __create_workmanship_config_menu(self):
        self.workmanship_menu = Menu(self.menu_bar, tearoff=0)
        self.workmanship_menu.add_command(label="复位配置", command='')
        self.workmanship_menu.add_command(label="速度配置", command='')
        self.workmanship_menu.add_command(label="延时配置", command='')
        self.workmanship_menu.add_command(label="I/O报警配置", command='')
        self.workmanship_menu.add_separator()
        self.workmanship_menu.add_command(label="加工速度模板", command='')
        self.workmanship_menu.add_separator()
        self.workmanship_menu.add_command(label="双Y配置", command='')
        self.workmanship_menu.add_separator()
        self.workmanship_menu.add_command(label="连续出胶参数模板", command='')
        self.workmanship_menu.add_command(label="打点出胶参数模板", command='')
        self.workmanship_menu.add_command(label="螺杆出胶参数模板", command='')
        self.workmanship_menu.add_command(label="出胶参数测试", command='')
        self.menu_bar.add_cascade(label="工艺配置(P)", menu=self.workmanship_menu)
    def __create_tools_menu(self):
        self.tools_menu = Menu(self.menu_bar, tearoff=0)
        self.tools_menu.add_command(label="状态监控", command='')
        self.tools_menu.add_command(label="IO监控", command='')
        self.tools_menu.add_command(label="点动面板", command='')
        self.tools_menu.add_command(label="参数导入导出", command='')
        self.tools_menu.add_separator()
        self.tools_menu.add_command(label="生产报表", command='')
        self.tools_menu.add_command(label="日志记录", command='')
        self.menu_bar.add_cascade(label="工具(T)", menu=self.tools_menu)
    def __create_help_menu(self):
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="帮助(H)", menu=self.help_menu)
