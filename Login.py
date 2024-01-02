import tkinter as tk
from tkinter import messagebox
from SystemMain import *

__version__ = "0.0.2"
class Login(tk.Tk):
    def __init__(self, width=500, heigth=200, padx=400, pady=100):
        super().__init__()
        self.title("登录界面")
        self.geometry(f"{width}x{heigth}+{padx}+{pady}")
        self.resizable(False, False)
        self.username_entry = None
        self.password_entry = None
        self.login_time = 0

    def create_ueser_entry(self, padx=80, pady=20):
        tk.Label(self, text="用户名:").grid(row=0, column=0, padx=padx, pady=pady)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1)

    def create_password_entry(self, padx=80, pady=20):
        tk.Label(self, text="密   码:").grid(row=1, column=0, padx=padx, pady=pady)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1)

    def create_exit_button(self, padx=20):
        # 创建登录按钮，并将登录函数绑定到其点击事件上
        tk.Button(self, text="登录", command=self.login_func).grid(row=2, column=1, padx=padx)

    def create_version_label(self, padx=20):
        tk.Label(self, text=f"Version: {__version__}").grid(row=2, column=3, padx=padx)

    def login_func(self):
        self.login_time += 1
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "123456":
            messagebox.showinfo("登录成功", "欢迎，管理员！")
            self.destroy()
            system_main_window()
        else:
            if self.login_time > 3:
                messagebox.showerror("登录失败", "登录失败次数大于3次,退出登录！")
                self.destroy()
            else:
                messagebox.showerror("登录失败", "用户名或密码错误，请重试。")

def system_main_window():
    system_window = SystemMain()
    system_window.system_main_entry()
    system_window.mainloop()
