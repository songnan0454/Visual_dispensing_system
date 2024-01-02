import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.constants import *
from tkinter import scrolledtext
from FramesAndWidgets import *
from SystemMenuArea import SystemMenu
from StatusInfoArea import StatusInfo
from ManualOperationArea import ManualOperation
from ViewArea import ViewMain
from WorkArea import WorkMain

class SystemMain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.screen_width = self.winfo_screenwidth()
        self.screen_heigth = self.winfo_screenheight()
        print(f"screen_width:{self.screen_width}, screen_heigth:{self.screen_heigth}")
        self.geometry(f"{self.screen_width}x{self.screen_heigth}")
        self.system_interval = 10
        self.entry_width = self.system_interval
        self.entry_heigth = self.system_interval
        self.button_width = int(3.5 * self.system_interval)
        self.button_width_ex = int(7 * self.system_interval)
        self.button_heigth = int(2.5 * self.system_interval)
        self.label_width = int(3.5 * self.system_interval)
        self.label_heigth = int(2.5 * self.system_interval)
        self.label_width_ex = int(7 * self.system_interval)
        self.combox_width = int(0.5 * self.system_interval)
        self.combox_heigth = self.system_interval
        self.combox_width_ex = self.system_interval
        self.tool = FramesAndWidgets()
        self.system_menu = SystemMenu(self)
        self.StatusInfo = StatusInfo(self)
        self.manual_operation = ManualOperation(self)
        self.view_main = ViewMain.ViewMain(self)
        self.work_main = WorkMain.WorkMain(self)

    def system_main_entry(self):
        self.system_menu.system_menu_entry()
        self.StatusInfo.status_info_entry()
        self.manual_operation.manual_operation_entry()
        self.view_main.view_main_entry()
        self.work_main.work_main_entry()
