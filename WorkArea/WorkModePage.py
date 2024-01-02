from SystemMain import *


class WorkModePage:
    def __init__(self, win_obj):
        self.win = win_obj
        self.main_frame = None
        self.main_frame_width = int(self.win.screen_width * 2 / 7)
        self.main_frame_heigth = int(self.win.screen_heigth * 11 / 16)
        self.main_frame_place_y = self.win.system_interval * 2
    def work_mode_page_entry(self):
        self.frame_and_widgets_create()
    def frame_and_widgets_create(self):
        self.__create_main_frame()
        self.__create_work_set_label()
        self.__create_mode_and_speed_label()
        self.__create_running_mode_label_and_combox()
        self.__create_process_time_label_and_entry()
        self.__create_output_mode_label_and_combox()
        self.__create_speed_rate_label_and_entry()
        self.__create_step_mode_label_and_combox()
        self.__create_idle_speed_label_and_entry()
        self.__create_function_choice_label_and_combox()
        self.__create_work_mode_label_and_combox()
        self.__create_file_array_label_and_combox()
        self.__create_location_and_offset_label()
        self.__create_idle_x_y_z_r()
        self.__create_record_and_locate_button()
        self.__create_axis_offset_label_and_entry()
        self.__create_search_failed_mark_label()
        self.__create_search_failed_processing_radio_button()
        self.__create_before_working_label()
        self.__create_widgets_using_before_working()
    def __create_main_frame(self):
        self.main_frame = \
            self.win.tool.create_frame_with_bg_and_layout(self.win, bg="lightblue", width=self.main_frame_width,
                                                          height=self.main_frame_heigth, anchor="nw",
                                                          y=self.main_frame_place_y)
    def __create_work_set_label(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="加工设置", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw")
    def __create_mode_and_speed_label(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="模式与速度", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*14, y=self.win.system_interval*3)
    def __create_running_mode_label_and_combox(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="运行模式", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval, y=self.win.system_interval*6)
        self.win.tool.create_combobox_and_layout(self.main_frame, values=("单文件", "多文件"),
                                                 width=self.win.combox_width, anchor="nw",
                                                 x=self.win.system_interval*9, y=self.win.system_interval*6)
    def __create_process_time_label_and_entry(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="加工次数", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*17, y=self.win.system_interval*6)
        self.win.tool.create_entry_and_layout(self.main_frame, width=self.win.entry_width,
                                              anchor="nw",  x=self.win.system_interval*25,
                                              y=self.win.system_interval*6)
    def __create_output_mode_label_and_combox(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="出胶模式", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval, y=self.win.system_interval*9)
        self.win.tool.create_combobox_and_layout(self.main_frame, values=("正常加工", "模拟运行"),
                                                 width=self.win.combox_width, anchor="nw",
                                                 x=self.win.system_interval*9, y=self.win.system_interval*9)
    def __create_speed_rate_label_and_entry(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="速度比例", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*17, y=self.win.system_interval*9)
        self.win.tool.create_entry_and_layout(self.main_frame, width=self.win.entry_width,
                                              anchor="nw",  x=self.win.system_interval*25,
                                              y=self.win.system_interval*9)
    def __create_step_mode_label_and_combox(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="步序模式", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval, y=self.win.system_interval*12)
        self.win.tool.create_combobox_and_layout(self.main_frame, values=("连续运行", "单步运行"),
                                                 width=self.win.combox_width, anchor="nw",
                                                 x=self.win.system_interval*9, y=self.win.system_interval*12)
    def __create_idle_speed_label_and_entry(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="空程速度", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*17, y=self.win.system_interval*12)
        self.win.tool.create_entry_and_layout(self.main_frame, width=self.win.entry_width,
                                              anchor="nw",  x=self.win.system_interval*25,
                                              y=self.win.system_interval*12)
    def __create_function_choice_label_and_combox(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="功能选择", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval, y=self.win.system_interval*15)
        self.win.tool.create_combobox_and_layout(self.main_frame, values=("视觉点胶", "普通点胶"),
                                                 width=self.win.combox_width, anchor="nw",
                                                 x=self.win.system_interval*9, y=self.win.system_interval*15)
    def __create_work_mode_label_and_combox(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="加工模式", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval, y=self.win.system_interval*18)
        self.win.tool.create_combobox_and_layout(self.main_frame, values=("针头加工", "相机跟踪"),
                                                 width=self.win.combox_width, anchor="nw",
                                                 x=self.win.system_interval*9, y=self.win.system_interval*18)
    def __create_file_array_label_and_combox(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="文件阵列", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*17, y=self.win.system_interval*18)
        self.win.tool.create_combobox_and_layout(self.main_frame, values=("关闭", "线性", "圆环"),
                                                 width=self.win.combox_width, anchor="nw",
                                                 x=self.win.system_interval*25, y=self.win.system_interval*18)
    def __create_location_and_offset_label(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="位置与偏移", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*14, y=self.win.system_interval*21)
    def __create_idle_x_y_z_r(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="待机X", width=self.win.label_width,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval, y=self.win.system_interval*24)
        self.win.tool.create_entry_and_layout(self.main_frame, width=int(self.win.entry_width/2),
                                              anchor="nw",  x=self.win.system_interval*5,
                                              y=self.win.system_interval*24)
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="Y", width=self.win.label_width/2,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*9, y=self.win.system_interval*24)
        self.win.tool.create_entry_and_layout(self.main_frame, width=int(self.win.entry_width/2),
                                              anchor="nw",  x=self.win.system_interval*11,
                                              y=self.win.system_interval*24)
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="Z", width=self.win.label_width/2,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*15, y=self.win.system_interval*24)
        self.win.tool.create_entry_and_layout(self.main_frame, width=int(self.win.system_interval/2),
                                              anchor="nw", x=self.win.system_interval*17,
                                              y=self.win.system_interval*24)
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="R", width=self.win.label_width/2,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*21, y=self.win.system_interval*24)
        self.win.tool.create_entry_and_layout(self.main_frame, width=int(self.win.entry_width/2),
                                              anchor="nw",  x=self.win.system_interval*23,
                                              y=self.win.system_interval*24)
    def __create_record_and_locate_button(self):
        self.win.tool.create_button_and_layout(self.main_frame, text="记录", width=self.win.button_width,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*28, y=self.win.system_interval*24)
        self.win.tool.create_button_and_layout(self.main_frame, text="定位", width=self.win.button_width,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*32, y=self.win.system_interval*24)
    def __create_axis_offset_label_and_entry(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="X偏移", width=self.win.label_width,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval, y=self.win.system_interval*27)
        self.win.tool.create_entry_and_layout(self.main_frame, width=int(self.win.entry_width/2),
                                              anchor="nw", x=self.win.system_interval*5,
                                              y=self.win.system_interval*27)
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="Y偏移", width=self.win.label_width,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*10, y=self.win.system_interval*27)
        self.win.tool.create_entry_and_layout(self.main_frame, width=int(self.win.entry_width/2),
                                              anchor="nw", x=self.win.system_interval*14,
                                              y=self.win.system_interval*27)
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="Z偏移", width=self.win.label_width,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*19, y=self.win.system_interval*27)
        self.win.tool.create_entry_and_layout(self.main_frame, width=int(self.win.entry_width/2),
                                              anchor="nw", x=self.win.system_interval*23,
                                              y=self.win.system_interval*27)
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="角度", width=self.win.label_width,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*28, y=self.win.system_interval*27)
        self.win.tool.create_entry_and_layout(self.main_frame, width=int(self.win.entry_width/2),
                                              anchor="nw", x=self.win.system_interval*32,
                                              y=self.win.system_interval*27)
    def __create_search_failed_mark_label(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="Mark搜索失败处理",
                                                    width=self.win.label_width*4, height=self.win.label_heigth,
                                                    anchor="nw", x=self.win.system_interval*11,
                                                    y=self.win.system_interval*30)

    def __create_search_failed_processing_radio_button(self):
        var = StringVar()
        var.set("A")
        self.win.tool.create_radio_button_and_layout(self.main_frame, text="搜索失败跳过", variable=var, value="A",
                                                     anchor="nw", x=self.win.system_interval,
                                                     y=self.win.system_interval*33)
        self.win.tool.create_radio_button_and_layout(self.main_frame, text="搜索失败停止", variable=var, value="B",
                                                     anchor="nw", x=self.win.system_interval*12,
                                                     y=self.win.system_interval*33)
        self.win.tool.create_radio_button_and_layout(self.main_frame, text="搜索失败弹窗处理", variable=var, value="C",
                                                     anchor="nw", x=self.win.system_interval*23,
                                                     y=self.win.system_interval*33)
    def __create_before_working_label(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="加工前处理", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*14, y=self.win.system_interval*36)

    def __create_widgets_using_before_working(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="运行前擦胶", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval, y=self.win.system_interval*39)
        self.win.tool.create_combobox_and_layout(self.main_frame, values=("关闭", "打开"),
                                                 width=self.win.combox_width,
                                                 anchor="nw", x=self.win.system_interval*9,
                                                 y=self.win.system_interval*39)
        self.win.tool.create_button_and_layout(self.main_frame, text="具体参数", width=self.win.button_width_ex,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*22, y=self.win.system_interval*39)
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="预点胶", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval, y=self.win.system_interval*42)
        self.win.tool.create_combobox_and_layout(self.main_frame, values=("关闭", "打开"),
                                                 width=self.win.combox_width,
                                                 anchor="nw", x=self.win.system_interval*9,
                                                 y=self.win.system_interval*42)
        self.win.tool.create_button_and_layout(self.main_frame, text="具体参数", width=self.win.button_width_ex,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*22, y=self.win.system_interval*42)
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="真空点胶", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval, y=self.win.system_interval*45)
        self.win.tool.create_combobox_and_layout(self.main_frame, values=("关闭", "打开"),
                                                 width=self.win.combox_width,
                                                 anchor="nw", x=self.win.system_interval*9,
                                                 y=self.win.system_interval*45)
        self.win.tool.create_button_and_layout(self.main_frame, text="具体参数", width=self.win.button_width_ex,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*22, y=self.win.system_interval*45)