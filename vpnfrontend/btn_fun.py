import main
import webbrowser
from tkinter import *


# фнкции под кнопки


def BUTTON_EVENT():
    main.frame_login.pack_forget()
    main.frame_basic.pack(pady=10, padx=20, fill="both", expand=TRUE)


def regir_button():
    webbrowser.open_new("https://404.vodka/")


def settingsbtn_func():
    main.frame_basic.pack_forget()
    main.frame_settings.pack(pady=20, padx=20, fill="both", expand=TRUE)


def back_home():
    main.frame_settings.pack_forget()
    main.frame_basic.pack(pady=10, padx=20, fill="both", expand=TRUE)


PHOTO_COUNTER = 0


def switch_on_off(button):
    global PHOTO_COUNTER
    if PHOTO_COUNTER == 0:
        PHOTO_COUNTER += 1
    elif PHOTO_COUNTER == 1:
        PHOTO_COUNTER += 1
    elif PHOTO_COUNTER == 2:
        PHOTO_COUNTER -= 1
    main.base_btn.config(image=main.photo_list[PHOTO_COUNTER])


def switch_event_1():
    webbrowser.open_new("https://404.vodka/")
    # print("switch toggled, current value:", switch_var_1.get())


def switch_event_2():
    webbrowser.open_new("https://404.vodka/")
    # print("switch toggled, current value:", switch_var_2.get())


if __name__ == "__main__":
    print(__name__)
else:
    print(__name__)
