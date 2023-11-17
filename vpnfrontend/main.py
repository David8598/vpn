import front_end
import webbrowser
from tkinter import *
import requests
import subprocess
import os

# фнкции под кнопки


def BUTTON_EVENT():
    front_end.frame_login.pack_forget()
    front_end.frame_basic.pack(pady=10, padx=20, fill="both", expand=TRUE)


def regir_button():
    webbrowser.open_new("https://404.vodka/")


def settingsbtn_func():
    front_end.frame_basic.pack_forget()
    front_end.frame_settings.pack(pady=20, padx=20, fill="both", expand=TRUE)


def back_home():
    front_end.frame_settings.pack_forget()
    front_end.frame_basic.pack(pady=10, padx=20, fill="both", expand=TRUE)


PHOTO_COUNTER = 0


def switch_on_off(button):
    global PHOTO_COUNTER
    if PHOTO_COUNTER == 0:
        PHOTO_COUNTER += 1
    elif PHOTO_COUNTER == 1:
        PHOTO_COUNTER += 1
    elif PHOTO_COUNTER == 2:
        PHOTO_COUNTER -= 1
    front_end.base_btn.config(image=front_end.photo_list[PHOTO_COUNTER])


def switch_event_1():
    webbrowser.open_new("https://404.vodka/")
    # print("switch toggled, current value:", switch_var_1.get())


def switch_event_2():
    webbrowser.open_new("https://404.vodka/")
    # print("switch toggled, current value:", switch_var_2.get())


# def update_repository():
#     try:
#         # Перейти в директорию вашего репозитория
#         subprocess.run(
#             [r"cd", r"C:\Users\dava2\Desktop\vpn\pythonprojects\pnfrontend"],
#             check=True,
#             shell=True,
#         )

#         # Выполнить git pull
#         subprocess.run(["git", "pull", "origin", "front_end"], check=True)

#         print("Обновление успешно выполнено.")
#     except subprocess.CalledProcessError as e:
#         print(f"Ошибка при обновлении: {e}")


# def check_for_updates(owner, repo):
#     url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"

#     headers = {"Accept": "application/vnd.github.v3+json"}

#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()  # Проверка на ошибки HTTP

#         # Парсинг JSON ответа
#         release_info = response.json()

#         # Получение версии релиза и URL для загрузки файлов
#         latest_version = release_info["tag_name"]
#         download_url = release_info["assets"][0]["browser_download_url"]

#         return latest_version, download_url

#     except requests.exceptions.RequestException as e:
#         print(f"Ошибка при выполнении запроса: {e}")
#         return None, None


# owner = "David8598"
# repo = "vpn"
# local_version = 1.1
# latest_version, download_url = check_for_updates(owner, repo)
# latest_version_num = float(latest_version)

# if latest_version_num == local_version:
#     print(f"Последняя версия: {latest_version}")
#     print(f"URL для загрузки: {download_url}")
#     print(type(download_url))
# else:
#     update_repository()


if __name__ == "__front_end__":
    print(1)
else:
    print(2)

    os.chdir(r"C:\Users\dava2\Desktop\pythonprojects\vpn\vpnfrontend")
    print(os.getcwd())
