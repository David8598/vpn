import pystray, PIL.Image
from pystray import MenuItem as item
import customtkinter
from PIL import ImageTk
from tkinter import *
import tkinter as tk
import webbrowser
# from pynput import mouse
app = customtkinter.CTk()  # create CTk window like you do with the Tk window

image = PIL.Image.open("logo.png")  
#   icon = pystray.Icon("Vodka vpn", image, menu = pystray.Menu(pystray.MenuItem("Вызвать меню", on_click, default=True)))
# отслеживаем нажатие клавиш за пределами окна
# def onMouseClick(*args):

#     print()
#     print(args)
# listener = mouse.Listener(on_click=onMouseClick)
# listener.start()

# фнкции под кнопки
def button_event():
    frame_login.pack_forget()
    frame_basic.pack(pady = 10, padx = 20, fill = "both", expand = TRUE)

def regir_button():
    webbrowser.open_new('https://404.vodka/')

def settingsbtn_func():
    frame_basic.pack_forget()
    frame_settings.pack(pady = 20, padx = 20, fill = "both", expand = TRUE)
def back_home():
    frame_settings.pack_forget()
    frame_basic.pack(pady = 10, padx = 20, fill = "both", expand = TRUE)
PHOTO_COUNTER = 0
def switch_on_off(button):
    global PHOTO_COUNTER
    if(PHOTO_COUNTER == 0):
        PHOTO_COUNTER += 1
    elif(PHOTO_COUNTER == 1):
        PHOTO_COUNTER += 1
    elif(PHOTO_COUNTER == 2):
        PHOTO_COUNTER -= 1
    base_btn.config(image=photo_list[PHOTO_COUNTER])
def switch_event_1():
    print("switch toggled, current value:", switch_var_1.get())
def switch_event_2():
    print("switch toggled, current value:", switch_var_2.get())

photo_list = [
    tk.PhotoImage(file="offon200.png"),
    tk.PhotoImage(file="on200.png"),
    tk.PhotoImage(file="off200.png"),
]
# начало fronend
# меню логина
frame_login = customtkinter.CTkFrame(master=app)
frame_login.pack(pady = 20, padx = 20, fill = "both", expand = TRUE)
label = customtkinter.CTkLabel(master=frame_login ,
                               text="Vodka VPN",
                               width=120,
                               height=25,
                               corner_radius=8,
                               font=("Roboto", 25)
                              )
label.place(relx=0.5, rely=0.1, anchor=CENTER)

label = customtkinter.CTkLabel(master=frame_login,
                               text="login",
                               width=120,
                               height=25,
                               corner_radius=8,
                               font=("Roboto", 20)
                              )
label.place(relx=0.35, rely=0.35, anchor=CENTER)


entry = customtkinter.CTkEntry(master=frame_login,
                               width=150,
                               height=25,
                               corner_radius=10)
entry.place(relx=0.5, rely=0.4, anchor=CENTER)

text = entry.get()
button = customtkinter.CTkButton(master=frame_login,
                                 text="Войти",
                                 command=button_event,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8)
button.place(relx=0.5, rely=0.5, anchor=CENTER)
register_text = customtkinter.CTkButton(master=frame_login,
                               text="зарегестрироватся",
                               width=120,
                               height=25,
                               corner_radius=8,
                                command=regir_button,
                               font=("Roboto", 10)
                              )
register_text.place(relx=0.5, rely=0.96, anchor=CENTER)

# основоне меню
frame_basic = customtkinter.CTkFrame(master=app)
label = customtkinter.CTkLabel(master=frame_basic ,
                               text="Vodka VPN",
                               width=120,
                               height=25,
                               corner_radius=8,
                               font=("Roboto", 40)
                              )
label.place(relx=0.5, rely=0.1, anchor=CENTER)
base_btn = tk.Button(master=frame_basic, 
                  border=0,
                width=200,
                height=200,
               image=photo_list[PHOTO_COUNTER],
                bg='#2b2b2b',
                fg='#2b2b2b',
                command=switch_on_off)
base_btn.config(command=lambda: switch_on_off(base_btn))

base_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

settingsbtn_img = ImageTk.PhotoImage(file="settings50.png")
settingsbtn = tk.Button(master=frame_basic, 
                border=0,
                width=50,
                height=50,
                image=settingsbtn_img,
                bg='#2b2b2b',
                command=settingsbtn_func)
settingsbtn.place(relx=0.9, rely=0.93, anchor=CENTER)
# настройки 
frame_settings = customtkinter.CTkFrame(master=app)
switch_var_1 = customtkinter.StringVar(value="on")


switch_1 = customtkinter.CTkSwitch(master=frame_settings, 
                                   text="CTkSwitch", 
                                   command=switch_event_1,
                                   variable=switch_var_1, 
                                   onvalue="on", 
                                   offvalue="off")
switch_1.place(relx=0.75, rely=0.35, anchor=CENTER)
switch_var_2 = customtkinter.StringVar(value="on")


switch_2 = customtkinter.CTkSwitch(master=frame_settings, 
                                   text="CTkSwitch", 
                                   command=switch_event_2,
                                   variable=switch_var_2, 
                                   onvalue="on", 
                                   offvalue="off")
switch_2.place(relx=0.75, rely=0.45, anchor=CENTER)
label_settings = customtkinter.CTkLabel(master=frame_settings ,
                               text="settings",
                               width=120,
                               height=25,
                               corner_radius=8,
                               font=("Roboto", 40)
                              )
label_settings.place(relx=0.5, rely=0.1, anchor=CENTER)
label_update = customtkinter.CTkLabel(master=frame_settings ,
                               text="вам не нужно обновлять",
                               width=120,
                               height=25,
                               corner_radius=8,
                               font=("Roboto", 13)
                              )
label_update.place(relx=0.25, rely=0.25, anchor=CENTER)
update_btn = customtkinter.CTkButton(master=frame_settings,
                                     text="Обновить",
                                    command=button_event,
                                    width=120,
                                    height=32,
                                    border_width=0,
                                    corner_radius=3)
update_btn.place(relx=0.75, rely=0.25, anchor=CENTER)
label_settings_2 = customtkinter.CTkLabel(master=frame_settings ,
                               text="краткое описание 2",
                               width=120,
                               height=25,
                               corner_radius=8,
                               font=("Roboto", 13)
                              )
label_settings_2.place(relx=0.25, rely=0.35, anchor=CENTER)
# settings_1_btn = customtkinter.CTkButton(master=frame_settings,
#                                      text="кнопка 2",
#                                     command=button_event,
#                                     width=120,
#                                     height=32,
#                                     border_width=0,
#                                     corner_radius=3)
# settings_1_btn.place(relx=0.75, rely=0.35, anchor=CENTER)
# settings_2_btn = customtkinter.CTkButton(master=frame_settings,
#                                      text="кнопка 3",
#                                     command=button_event,
#                                     width=120,
#                                     height=32,
#                                     border_width=0,
#                                     corner_radius=3)
# settings_2_btn.place(relx=0.75, rely=0.45, anchor=CENTER)
label_settings_3 = customtkinter.CTkLabel(master=frame_settings ,
                               text="краткое описание 3",
                               width=120,
                               height=25,
                               corner_radius=8,
                               font=("Roboto", 13)
                              )
label_settings_3.place(relx=0.25, rely=0.45, anchor=CENTER)

settings_to_home_img = ImageTk.PhotoImage(file="home50.png")
settings_to_home_btn = tk.Button(master=frame_settings, 
                border=0,
                width=50,
                height=50,
                image=settings_to_home_img,
                bg='#2b2b2b',
                command=back_home)
settings_to_home_btn.place(relx=0.9, rely=0.93, anchor=CENTER)

# конец frontend
# запуск и закрытие 
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app.geometry("350x500")
app.title("Vodka vpn")
app.resizable(width=False, height=False)
app.iconbitmap('favicon.ico')

def quit_window(icon, item):
    icon.stop()
    app.destroy()

def show_window(icon, item):
    icon.stop()
    app.after(0,app.deiconify)

def withdraw_window():  
    app.withdraw()
    menu = (item('Quit', quit_window), item('Show', show_window, default=True))
    icon = pystray.Icon("name", image, "title", menu)
    icon.run()

app.protocol('WM_DELETE_WINDOW', withdraw_window)
app.mainloop()




