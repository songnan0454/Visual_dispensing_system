import time
import ctypes
from SystemMain import *
from datetime import datetime, date
from ZmcLibUsing import ZmcLibUsing


class StatusInfo:
    def __init__(self, win_obj):
        self.win = win_obj
        self.frame_width = self.win.screen_width
        self.frame_heigth = int(8 * self.win.system_interval)
        self.status_scrollbar = None
        self.zmc_controller = ZmcLibUsing()
        
    def status_info_entry(self):
        self.create_status_info_label()
        self.frame_and_widgets_create()
    def create_status_info_label(self):
        self.win.tool.create_fixed_label_and_layout(self.win, text="状态信息", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth * 2 / 3,
                                                    anchor="nw", y=self.win.system_interval * 54)
    def frame_and_widgets_create(self):
        self.__create_status_info_frame()
        self.__create_status_info_scrollbar()
        self.__create_system_time_label()
        self.__create_show_system_time_label()
        self.__create_system_date_label()
        self.__create_show_system_date_label()
    def __create_status_info_frame(self):
        self.status_monitor_frame = \
            self.win.tool.create_frame_with_bg_and_layout(self.win, bg="lightblue", width=self.frame_width,
                                                          height=self.frame_heigth,
                                                          anchor="sw", y=self.win.system_interval * 64)
    def __create_status_info_scrollbar(self):
        self.status_scrollbar = self.win.tool.create_scrollbar_and_layout(self.status_monitor_frame, wrap=tk.WORD,
                                                                          width=self.frame_width,
                                                                          height=self.frame_heigth / 2, anchor="nw")
        ret_val = self.zmc_controller.zmotion_lib.ZMC_Open(2, "127.0.0.1", ctypes.c_void_p())
        print(f"ret_val:{ret_val}")
        self.status_scrollbar.insert(tk.END, ret_val)
    def __create_system_time_label(self):
        self.win.tool.create_fixed_label_and_layout(self.status_monitor_frame, text="系统时间：",
                                                    width=self.win.label_width_ex,
                                                    height=self.win.label_heigth * 2 / 3, anchor="nw",
                                                    x=self.win.system_interval * 92,
                                                    y=self.win.system_interval * 4.5)
    def __create_show_system_time_label(self):
        def update_time():
            current_time = datetime.now().strftime("%H:%M:%S")
            time_label.config(text=current_time)
            time_label.after(1000, update_time)
        time_label = self.win.tool.create_fixed_label_and_layout(self.status_monitor_frame, text="09:23:45",
                                                                 width=self.win.label_width_ex,
                                                                 height=self.win.label_heigth * 2 / 3, anchor="nw",
                                                                 x=self.win.system_interval * 100,
                                                                 y=self.win.system_interval * 4.5)
        update_time()
    def __create_system_date_label(self):
        self.win.tool.create_fixed_label_and_layout(self.status_monitor_frame, text="系统日期：",
                                                    width=self.win.label_width_ex,
                                                    height=self.win.label_heigth * 2 / 3, anchor="nw",
                                                    x=self.win.system_interval * 110,
                                                    y=self.win.system_interval * 4.5)
    def __create_show_system_date_label(self):
        def update_date():
            current_date = date.today().strftime("%d:%m:%Y")
            date_label.config(text=current_date)
            date_label.after(1000, update_date)
        date_label = self.win.tool.create_fixed_label_and_layout(self.status_monitor_frame, text="21:11:2023",
                                                                 width=self.win.label_width_ex,
                                                                 height=self.win.label_heigth * 2 / 3, anchor="nw",
                                                                 x=self.win.system_interval * 118,
                                                                 y=self.win.system_interval * 4.5)
        update_date()