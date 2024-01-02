from ViewArea.ViewGuiPage import *
from ViewArea.TrackDrawingPage import *
from ViewArea.StatusMonitorPage import *

class ViewMain(ViewGuiPage, TrackDrawingPage, StatusMonitorPage):
    def __init__(self, win_obj):
        super().__init__(win_obj)
        self.menu_items = ["视觉图像", "轨迹绘制", "状态监控"]
    def view_main_entry(self):
        self.view_gui_page_entry()
        self.create_label_page_for_view()
    def create_label_page_for_view(self):
        notebook = ttk.Notebook(self.win)
        for item in self.menu_items:
            frame = ttk.Frame(notebook)
            notebook.add(frame, text=item)
        notebook.bind("<<NotebookTabChanged>>", lambda event: self.view_label_page_switch_event)
        notebook.place(anchor="nw", x=self.win.system_interval*37, y=self.win.system_interval*51)
    def view_label_page_switch_event(self, event):
        tab_index = notebook.index(event.widget)
        self.destroy_view_frame()
        if tab_index == 0:
            self.view_gui_page_entry()
        elif tab_index == 1:
            self.track_drawing_page_entry()
        elif tab_index == 2:
            self.status_monitor_page_entry()
        else:
            raise Exception("暂时不支持！")
    def destroy_view_frame(self):
        self.view_frame.destroy()