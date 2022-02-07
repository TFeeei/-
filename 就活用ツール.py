from tkinter import *
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

# chromeを起動するためにchromedriverを自動的に入れる
chromedriver_autoinstaller.install()


# gui画面の構築
root = tk.Tk()
root.title("就活用プログラム")

root.geometry('400x200')
root.resizable(width=False, height=False)

gui_title = Label(root, text="会社の名前を入力してください。", font=('游ゴシック', 14), width=30, height=2)
gui_title.pack(side=TOP)

gui_inputBox = tk.Entry(root,show=None)
gui_inputBox.pack()



def gui_confirm():
    company_name = gui_inputBox.get()
    if company_name != "":

        # Chromeを起動する
        driver = webdriver.Chrome()

        # googleで会社名を調べる。
        url_google = "https://www.google.com/"
        driver.get(url_google)

        input_google = driver.find_element(By.NAME, "q")
        input_google.send_keys(company_name)

        time.sleep(0.5)

        search_google = driver.find_element(By.NAME, "btnK")
        search_google.click()


        # マイナビで会社名を調べる。
        new_page2 = "window.open('https://job.mynavi.jp/2023/')"
        driver.execute_script(new_page2)
        # 現在のブラウザのすべてのウィンドウハンドルを取得する。
        handles = driver.window_handles
        # 最新のページに切り替える。
        driver.switch_to.window(handles[-1])

        input_mynavi = driver.find_element(By.ID, "srchWord")
        input_mynavi.send_keys(company_name)

        time.sleep(0.5)

        search_mynavi = driver.find_element(By.ID, "srchButton")
        search_mynavi.click()


        # リクナビで会社名を調べる。
        new_page3 = "window.open('https://job.rikunabi.com/2023/')"
        driver.execute_script(new_page3)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

        input_rikunabi = driver.find_element(By.NAME, "mp_fw")
        input_rikunabi.send_keys(company_name)

        time.sleep(0.5)

        search_rikunabi = driver.find_element(By.CLASS_NAME, "mp_input_submit")
        search_rikunabi.click()


        # openworkで会社名を調べる。
        new_page4= "window.open('https://www.vorkers.com')"
        driver.execute_script(new_page4)
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

        input_openwork = driver.find_element(By.NAME, "src_str")
        input_openwork.send_keys(company_name)

        time.sleep(0.5)

        search_openwork = driver.find_element(By.CLASS_NAME, "keywordSearch_button")
        search_openwork.click()

        root.mainloop()



    else:
        time.sleep(0.5)
        gui_input_error["text"] = "入力し直してください。"


def gui_quit():
    quit()

gui_confirm_btn = Button(root, text="確認", width=10, height=1, command=gui_confirm)
gui_confirm_btn.pack()


gui_quit_btn = Button(root, text="閉じる", width=10, height=1, command=gui_quit)
gui_quit_btn.pack()

gui_input_error = Label(root,text="")
gui_input_error.pack()

root.mainloop()