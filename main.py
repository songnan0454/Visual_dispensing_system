from Login import Login


def main_login_func():
    Login_window = Login()
    Login_window.create_ueser_entry()
    Login_window.create_password_entry()
    Login_window.create_exit_button()
    Login_window.create_version_label()
    Login_window.mainloop()

if __name__ == "__main__":
    main_login_func()






