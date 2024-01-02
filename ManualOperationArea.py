from SystemMain import *


class ManualOperation:
    def __init__(self, win_obj):
        self.win = win_obj
        self.main_frame = None
        self.locate_label_frame = None
        self.move_label_frame = None
        self.main_frame_width = int(self.win.screen_width * 4 / 15)
        self.main_frame_heigth = int(self.win.screen_heigth * 45 / 64)
        self.main_frame_place_x = self.win.system_interval * 92
        self.main_frame_place_y = self.win.system_interval * 5
        self.locate_frame_width = int(self.win.screen_width * 7 / 30)
        self.locate_frame_heigth = int(self.win.screen_heigth * 2 / 7)
        self.move_frame_width = int(self.win.screen_width * 7 / 30)
        self.move_frame_heigth = int(self.win.screen_heigth * 19 / 70)
        
    def manual_operation_entry(self):
        self.create_frame_and_widgets()

    def create_frame_and_widgets(self):
        self.__create_main_frame()
        self.__create_main_label()
        self.__create_locate_label_frame()
        self.__create_widgets_for_x_axis()
        self.__create_widgets_for_y1_axis()
        self.__create_widgets_for_y2_axis()
        self.__create_widgets_for_z_axis()
        self.__create_widgets_for_r_z()
        self.__create_widgets_for_image_heigth()
        self.__creat_speed_label_and_combox()
        self.__create_move_label_frame()
        self.__create_mode_label_and_combox()
        self.__create_widgets_for_manual_area()
        self.__creat_image_track_label_and_combox()
        self.__create_reset_button()
    def __create_main_frame(self):
        self.main_frame = \
            self.win.tool.create_frame_with_bg_and_layout(self.win, bg="lightblue", width=self.main_frame_width,
                                                          height=self.main_frame_heigth, anchor="nw",
                                                          x=self.main_frame_place_x, y=self.main_frame_place_y)
    def __create_main_label(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="点动面板", 
                                                    width=self.win.label_width_ex, height=self.win.label_heigth * 0.8,
                                                    anchor="nw")
    def __create_locate_label_frame(self):
        self.locate_label_frame = self.win.tool.create_label_frame_and_layout(self.main_frame, text="定位",
                                                                              width=self.locate_frame_width,
                                                                              height=self.locate_frame_heigth,
                                                                              anchor="nw",x=self.win.system_interval*2,
                                                                              y=self.win.system_interval*4)
    def __create_widgets_for_x_axis(self):
        self.win.tool.create_fixed_label_and_layout(self.locate_label_frame, text="  X:",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth,
                                                    anchor="nw")

        self.win.tool.create_fixed_label_and_layout(self.locate_label_frame, text="0.000",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth,
                                                    anchor="nw", x=self.win.system_interval*4)

        self.win.tool.create_entry_and_layout(self.locate_label_frame, width=self.win.system_interval,
                                              anchor="nw", x=self.win.system_interval*10)

        self.win.tool.create_button_and_layout(self.locate_label_frame, text="定位", width=self.win.button_width,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*18)
    def __create_widgets_for_y1_axis(self):
        self.win.tool.create_fixed_label_and_layout(self.locate_label_frame, text="Y1:",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth,
                                                    anchor="nw", y=self.win.system_interval*3)
        self.win.tool.create_fixed_label_and_layout(self.locate_label_frame, text="0.000",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth,
                                                    anchor="nw", x=self.win.system_interval*4,
                                                    y=self.win.system_interval*3)
        self.win.tool.create_entry_and_layout(self.locate_label_frame, width=self.win.system_interval,
                                              anchor="nw", x=self.win.system_interval*10,
                                              y=self.win.system_interval*3)
        self.win.tool.create_button_and_layout(self.locate_label_frame, text="定位", width=self.win.button_width,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*18, y=self.win.system_interval*3)

    def __create_widgets_for_y2_axis(self):
        self.win.tool.create_fixed_label_and_layout(self.locate_label_frame, text="Y2:",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth,
                                                    anchor="nw",y=self.win.system_interval*6)
        self.win.tool.create_fixed_label_and_layout(self.locate_label_frame, text="0.000",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth,
                                                    anchor="nw", x=self.win.system_interval*4,
                                                    y=self.win.system_interval*6)
        self.win.tool.create_entry_and_layout(self.locate_label_frame, width=int(self.win.system_interval),
                                              anchor="nw", x=self.win.system_interval*10,
                                              y=self.win.system_interval*6)
        self.win.tool.create_button_and_layout(self.locate_label_frame, text="定位", width=self.win.button_width,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*18, y=self.win.system_interval*6)
    def __create_widgets_for_z_axis(self):
        self.win.tool.create_fixed_label_and_layout(self.locate_label_frame, text="  Z:",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth,
                                                    anchor="nw", y=self.win.system_interval*9)
        self.win.tool.create_fixed_label_and_layout(self.locate_label_frame, text="0.000",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth,
                                                    anchor="nw", x=self.win.system_interval*4,
                                                    y=self.win.system_interval*9)
        self.win.tool.create_entry_and_layout(self.locate_label_frame, width=int(self.win.system_interval),
                                              anchor="nw", x=self.win.system_interval*10,
                                              y=self.win.system_interval*9)
        self.win.tool.create_button_and_layout(self.locate_label_frame, text="定位", width=self.win.button_width,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*18, y=self.win.system_interval*9)
    def __create_widgets_for_r_z(self):
        self.win.tool.create_fixed_label_and_layout(self.locate_label_frame, text="RZ:",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth,
                                                    anchor="nw", y=self.win.system_interval*12)
        self.win.tool.create_fixed_label_and_layout(self.locate_label_frame, text="5.100",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth,
                                                    anchor="nw", x=self.win.system_interval*4,
                                                    y=self.win.system_interval*12)
        self.win.tool.create_entry_and_layout(self.locate_label_frame, width=int(self.win.system_interval),
                                              anchor="nw", x=self.win.system_interval*10,
                                              y=self.win.system_interval*12)
        self.win.tool.create_button_and_layout(self.locate_label_frame, text="定位", width=self.win.button_width,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*18, y=self.win.system_interval*12)
    def __create_widgets_for_image_heigth(self):
        self.win.tool.create_fixed_label_and_layout(self.locate_label_frame, text="取像高度",
                                                    width=self.win.label_width_ex,
                                                    height=self.win.label_heigth,
                                                    anchor="nw", x=self.win.system_interval*3,
                                                    y=self.win.system_interval*15)
        self.win.tool.create_entry_and_layout(self.locate_label_frame, width=int(self.win.system_interval),
                                              anchor="nw", x=self.win.system_interval*10,
                                              y=self.win.system_interval*15)
        self.win.tool.create_button_and_layout(self.locate_label_frame, text="定位", width=self.win.button_width,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*18, y=self.win.system_interval*15)
    def __creat_speed_label_and_combox(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="速度",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth,
                                                    anchor="nw", x=self.win.system_interval*3,
                                                    y=self.win.system_interval*25)
        self.win.tool.create_combobox_and_layout(self.main_frame, values=("20.0", "30.0", "40,0"),
                                                 width=int(self.win.system_interval*0.4),
                                                 anchor="nw",  x=self.win.system_interval*8,
                                                 y=self.win.system_interval*25)
        self.win.tool.create_combobox_and_layout(self.main_frame, values=("全速", "中速", "低速"),
                                                 width=int(self.win.system_interval*0.4),
                                                 anchor="nw", x=self.win.system_interval*15,
                                                 y=self.win.system_interval*25)
        self.win.tool.create_combobox_and_layout(self.main_frame, values=("RZ独立", "其他"),
                                                 width=int(self.win.system_interval*0.6),
                                                 anchor="nw", x=self.win.system_interval*22,
                                                 y=self.win.system_interval*25)
    def __create_move_label_frame(self):
        self.move_label_frame = self.win.tool.create_label_frame_and_layout(self.main_frame, text="点动",
                                                                            width=self.move_frame_width,
                                                                            height=self.move_frame_heigth,
                                                                            anchor="nw", x=self.win.system_interval * 2,
                                                                            y=self.win.system_interval * 28)
    def __create_mode_label_and_combox(self):
        self.win.tool.create_fixed_label_and_layout(self.move_label_frame, text="模式",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth,
                                                    anchor="nw")
        self.win.tool.create_combobox_and_layout(self.move_label_frame, values=("连续", "单击"),
                                                 width=int(self.win.system_interval * 0.4),
                                                 anchor="nw", x=self.win.system_interval*4,
                                                 y=self.win.system_interval*0.5)
    def __create_widgets_for_manual_area(self):
        self.win.tool.create_button_and_layout(self.move_label_frame, text="︽", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*6, y=self.win.system_interval*3)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="︽", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*10, y=self.win.system_interval*3)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="︿", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*6, y=self.win.system_interval*6)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="︿", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*10, y=self.win.system_interval*6)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="《", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               y=self.win.system_interval*9)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="<", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*4, y=self.win.system_interval*9)
        self.win.tool.create_fixed_label_and_layout(self.move_label_frame, text="<XY>",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth * 2 / 3,
                                                    anchor="nw", x=self.win.system_interval*8,
                                                    y=self.win.system_interval*9)
        self.win.tool.create_button_and_layout(self.move_label_frame, text=">", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*12, y=self.win.system_interval*9)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="》", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*16, y=self.win.system_interval*9)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="﹀", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*6, y=self.win.system_interval*12)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="﹀", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*10, y=self.win.system_interval*12)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="︾", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*6, y=self.win.system_interval*15)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="︾", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*10, y=self.win.system_interval*15)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="︽", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*20, y=self.win.system_interval*3)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="++", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*24, y=self.win.system_interval*3)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="︿", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*20, y=self.win.system_interval*6)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="+", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*24, y=self.win.system_interval*6)
        self.win.tool.create_fixed_label_and_layout(self.move_label_frame, text="<Z>",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth * 2 / 3,
                                                    anchor="nw", x=self.win.system_interval*20,
                                                    y=self.win.system_interval*9)
        self.win.tool.create_fixed_label_and_layout(self.move_label_frame, text="<RZ>",
                                                    width=self.win.label_width,
                                                    height=self.win.label_heigth * 2 / 3,
                                                    anchor="nw", x=self.win.system_interval*24,
                                                    y=self.win.system_interval*9)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="﹀", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*20, y=self.win.system_interval*12)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="-", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*24, y=self.win.system_interval*12)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="︾", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*20, y=self.win.system_interval*15)
        self.win.tool.create_button_and_layout(self.move_label_frame, text="--", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval*24, y=self.win.system_interval*15)
    def __creat_image_track_label_and_combox(self):
        self.win.tool.create_fixed_label_and_layout(self.main_frame, text="图像跟随",
                                                    width=self.win.label_width_ex,
                                                    height=self.win.label_heigth,
                                                    anchor="nw", x=self.win.system_interval * 2,
                                                    y=self.win.system_interval * 48)
        self.win.tool.create_combobox_and_layout(self.main_frame, values=("关闭", "打开"),
                                                 width=int(self.win.system_interval * 0.4),
                                                 anchor="nw", x=self.win.system_interval * 10,
                                                 y=self.win.system_interval * 48)
    def __create_reset_button(self):
        self.win.tool.create_button_and_layout(self.main_frame, text="复位", width=30,
                                               height=self.win.button_heigth, anchor="nw",
                                               x=self.win.system_interval * 29, y=self.win.system_interval * 48)