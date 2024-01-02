from SystemMain import *


class ViewGuiPage:
    def __init__(self, win_obj):
        self.win = win_obj
        self.main_frame = None
        self.view_frame = None
        self.status_label = None
        self.main_frame_width = int(self.win.screen_width * 3 / 7)
        self.main_frame_heigth = int(self.win.screen_heigth * 11 / 16)
        self.view_frame_width = int(self.win.screen_width * 5 / 14)
        self.view_frame_heigth = int(self.win.screen_heigth * 19 / 32)
        self.main_frame_place_x = self.win.system_interval * 37
        self.main_frame_place_y = self.win.system_interval * 2
        self.bottom_widgets_place_y = int(47 * self.win.system_interval)
        self.continue_capture_button_status = False
        self.capture_button_status = False
        self.str_var_1 = StringVar()


    def view_gui_page_entry(self):
        self.frame_and_widgets_create()
    def frame_and_widgets_create(self):
        self.__create_main_frame()
        self.__create_visual_image_label()
        self.__create_show_status_label()
        self.__create_continue_capture_button()
        self.__create_capture_button()
        self.__create_image_width_heigth_label_and_entry()
        self.create_external_widgets()
        self.__create_view_frame()
        self.__create_camera_scanning_button()
        self.__create_exposure_time_label_and_entry()
        self.__create_capture_height_label_and_entry()
        self.__create_record_button()
        self.__create_locate_button()
    def __create_main_frame(self):
        self.main_frame = \
            self.win.tool.create_frame_with_bg_and_layout(self.win, bg="lightgray", width=self.main_frame_width,
                                                          height=self.main_frame_heigth, anchor="nw",
                                                          x=self.main_frame_place_x,
                                                          y=self.main_frame_place_y)
    def __create_visual_image_label(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="视觉图像", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw")
    def __create_show_status_label(self):
        self.status_label = self.win.tool.create_fixed_label_and_layout(self.main_frame, text="连续采集中",
                                                                        width=self.win.label_width_ex,
                                                                        height=self.win.label_heigth, anchor="nw",
                                                                        x=self.win.system_interval*8)
    def __create_continue_capture_button(self):
        self.win.tool.create_button_and_layout(self.main_frame, text="连续采集",
                                               command=self.__process_continue_capture_button,
                                               width=self.win.button_width_ex,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*16)
    def __process_continue_capture_button(self):
        self.continue_capture_button_status = not self.continue_capture_button_status
        if self.continue_capture_button_status:
            self.status_label.config(text="连续采集中")
    def __create_capture_button(self):
        self.win.tool.create_button_and_layout(self.main_frame, text="采集",
                                               command=self.__process_capture_button,
                                               width=self.win.button_width,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*24)
    def __process_capture_button(self):
        self.capture_button_status = not self.capture_button_status
        if self.capture_button_status:
            self.status_label.config(text="单帧图像")
    def __create_image_width_heigth_label_and_entry(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="图像宽高:", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*28)
        self.win.tool.create_entry_and_layout(self.main_frame, width=self.win.entry_width, anchor="nw",
                                              x=self.win.system_interval*36)
        self.win.tool.create_entry_and_layout(self.main_frame, width=self.win.entry_width, anchor="nw",
                                              x=self.win.system_interval*44)
    def create_external_widgets(self):
        self.win.tool.create_fixed_label_and_layout(self.win, text="输出名称", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval*100,
                                                    y=self.main_frame_place_y)
        self.win.tool.create_entry_and_layout(self.win, width=self.win.entry_width, anchor="nw",
                                              x=self.win.system_interval * 108,
                                              y=self.main_frame_place_y)
        self.win.tool.create_button_and_layout(self.win, text="导出", width=self.win.button_width,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*122, y=self.main_frame_place_y)
    def __create_view_frame(self):
        self.view_frame = \
            self.win.tool.create_frame_with_bg_and_layout(self.main_frame, bg="black", width=self.view_frame_width,
                                                          height=self.view_frame_heigth, anchor="nw",
                                                          x=self.win.system_interval*5, y=self.win.system_interval*3)
    def __create_camera_scanning_button(self):
        self.win.tool.create_button_and_layout(self.main_frame, text="相机扫描", width=self.win.button_width_ex,
                                               height=self.win.button_heigth, anchor="nw",
                                               y=self.bottom_widgets_place_y)
    def __create_exposure_time_label_and_entry(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="曝光时间", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval * 10,
                                                    y=self.bottom_widgets_place_y)
        self.win.tool.create_entry_and_layout(self.main_frame, width=self.win.entry_width, anchor="nw",
                                              x=self.win.system_interval * 18,
                                              y=self.bottom_widgets_place_y)
    def __create_capture_height_label_and_entry(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="取像高度", width=self.win.label_width_ex,
                                                    height=self.win.label_heigth, anchor="nw",
                                                    x=self.win.system_interval * 26,
                                                    y=self.bottom_widgets_place_y)
        self.win.tool.create_entry_and_layout(self.main_frame, width=self.win.system_interval, anchor="nw",
                                              x=self.win.system_interval * 34,
                                              y=self.bottom_widgets_place_y)
    def __create_record_button(self):
        self.win.tool.create_button_and_layout(self.main_frame, text="记录", width=self.win.button_width,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*44, y=self.bottom_widgets_place_y)
    def __create_locate_button(self):
        self.win.tool.create_button_and_layout(self.main_frame, text="定位", width=self.win.button_width,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*50, y=self.bottom_widgets_place_y)

