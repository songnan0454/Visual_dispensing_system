import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

class FramesAndWidgets:
    def __init__(self):
        pass

    def create_frame_and_layout(self, master, width=0, height=0, anchor="sw", x=0, y=0):
        frame = tk.Frame(master, width=width, height=height)
        frame.place(anchor=anchor, x=x, y=y)
        return frame
    def create_frame_with_bg_and_layout(self, master, bg="gray", width=0, height=0, anchor="sw", x=0, y=0):
        frame = tk.Frame(master, bg=bg, width=width, height=height)
        frame.place(anchor=anchor, x=x, y=y)
        return frame
    def create_label_frame_and_layout(self, master, text="", width=0, height=0, anchor="center", x=0, y=0):
        label_frame = tk.LabelFrame(master, text=text, width=width, height=height)
        label_frame.place(anchor=anchor, x=x, y=y)
        return label_frame

    def create_label_and_layout(self, master, text, bg="gray", anchor="center", x=0, y=0):
        label = tk.Label(master, text=text, bg=bg)
        label.place(anchor=anchor, x=x, y=y)
        return label
    def create_fixed_label_and_layout(self, master, text, width=0, height=0, anchor="center", x=0, y=0):
        label = tk.Label(master, text=text)
        label.place(anchor=anchor, x=x, y=y, width=width, height=height)
        return label

    def create_fixed_bg_label_and_layout(self, master, text, bg="gray", width=0, height=0, anchor="center", x=0, y=0):
        label = tk.Label(master, text=text, bg=bg)
        label.place(anchor=anchor, x=x, y=y, width=width, height=height)
        return label
    def create_combobox_and_layout(self, master, values=("", ""), width=0, anchor="center", x=0, y=0):
        box = ttk.Combobox(master, values=values, width=width)
        box.current(0)
        box.place(anchor=anchor, x=x, y=y)
        return box
    def create_entry_and_layout(self, master, width=0, anchor="center", x=0, y=0):
        entry = tk.Entry(master, width=width)
        entry.place(anchor=anchor, x=x, y=y)
        return entry
    def create_button_and_layout(self, master, text="", command="", width=0, height=0, anchor="center", x=0, y=0):
        button = tk.Button(master, text=text, command=command)
        button.place(anchor=anchor, x=x, y=y, width=width, height=height)
        return button
    def create_radio_button_and_layout(self, master, text="", variable=None, value=None, anchor="center", x=0, y=0):
        radio_button = Radiobutton(master, text=text, variable=variable, value=value)
        radio_button.place(anchor=anchor, x=x, y=y)
        return radio_button
    def create_scrollbar_and_layout(self, master, wrap=None, width=0, height=0, anchor="center", x=0, y=0):
        scrollbar = scrolledtext.ScrolledText(master, wrap=wrap)
        scrollbar.place(anchor=anchor, x=x, y=y, width=width, height=height)
        return scrollbar
    def create_menu(self, master):
        menu_bar = Menu(master)
        return Menu(menu_bar, tearoff=0)
