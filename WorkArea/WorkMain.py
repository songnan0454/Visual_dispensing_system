from WorkArea.WorkModePage import *
from WorkArea.CADGuidePage import *
from WorkArea.TaskManagePage import *
from WorkArea.ContourExtractionPage import *


class WorkMain(WorkModePage, CADGuidePage, TaskManagePage, ContourExtractionPage):
    def __init__(self, win_obj):
        super().__init__(win_obj)
        self.menu_items = ["加工设置", "任务管理", "轮廓提取", "CAD导图"]

    def work_main_entry(self):
        self.work_mode_page_entry()
        self.create_label_page_for_work()

    def create_label_page_for_work(self):
        notebook = ttk.Notebook(self.win)
        for item in self.menu_items:
            frame = ttk.Frame(notebook)
            notebook.add(frame, text=item)
        notebook.bind("<<NotebookTabChanged>>", lambda event: self.work_label_page_switch_event)
        notebook.place(anchor="nw", y=self.win.system_interval*51)
    def work_label_page_switch_event(self, event):
        tab_index = notebook.index(event.widget)
        self.destroy_work_frame()
        if tab_index == 0:
            self.work_mode_page_entry()
        elif tab_index == 1:
            self.task_manage_page_entry()
        elif tab_index == 2:
            self.contour_extraction_page_entry()
        elif tab_index == 3:
            self.cad_guide_page_entry()
        else:
            raise Exception("暂时不支持！")
    def destroy_work_frame(self):
        self.work_frame.destroy()