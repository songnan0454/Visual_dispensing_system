from SystemMain import *


class StatusMonitorPage:
    def __init__(self, win_obj):
        self.win = win_obj
        self.main_frame = None
        self.view_frame = None
        self.main_frame_width = int(self.win.screen_width * 3 / 7)
        self.main_frame_heigth = int(self.win.screen_heigth * 11 / 16)
        self.view_frame_width = int(self.win.screen_width * 5 / 14)
        self.view_frame_heigth = int(self.win.screen_heigth * 19 / 32)
        self.main_frame_place_x = self.win.system_interval * 37
        self.main_frame_place_y = self.win.system_interval * 2
        self.bottom_widgets_place_y = int(47 * self.win.system_interval)

    def status_monitor_page_entry(self):
        self.frame_and_widgets_create()
    def frame_and_widgets_create(self):
        pass