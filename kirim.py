# Otomisasi Pengirim WhatsApp
# MOCHAMMAD RAFI
# https://twitter.com/MochammadRafi18

import os
import time
from os import system, name 
import inquirer
import pyperclip
import pyautogui

def clear_console(): 
    clear = system('clear' if os.name =='posix' else 'cls') 

def win_r():
    pyautogui.hotkey("win", "r")

def buka_whatsapp(browser):
    if browser == "Edge":
        win_r()
        pyautogui.typewrite("microsoft-edge:")
        pyautogui.press("enter")
    elif browser == "Google Chrome":
        win_r()
        pyautogui.typewrite("chrome")
        pyautogui.press("enter")
    elif browser == "Mozilla Firefox":
        win_r()
        pyautogui.typewrite("firefox.exe")
        pyautogui.press("enter")

def kirim_pesan():
    nomor = open("nomor.txt", 'r')
    pesan = open("pesan.txt", 'r').read()
    for i in nomor:
        pyperclip.copy("https://web.whatsapp.com/send?phone="+i)
        time.sleep(0.1)
        pyautogui.hotkey("ctrl", "t")
        time.sleep(0.1)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.1)
        pyautogui.press("enter")
        pyperclip.copy(pesan)
        time.sleep(12)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        time.sleep(12)
        pyautogui.hotkey("ctrl", "w")

def pilih_browser():
    pertanyaan = [
        inquirer.List(
            "browser",
            message = "Browser yang di gunakan",
            choices = ["Edge", "Google Chrome", "Mozilla Firefox"]
        )
    ]
    jawaban = inquirer.prompt(pertanyaan)
    buka_whatsapp(jawaban["browser"])

clear_console()
pilih_browser()
kirim_pesan()