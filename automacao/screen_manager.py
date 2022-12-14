import time
import logging
import win32gui

import pyautogui as auto

import cv2


class ScreenManager:

    @staticmethod
    def is_app_focused(app_tittle_name: str):
        active_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower()
        return app_tittle_name in active_window_title

    @staticmethod
    def click_on_screen(coordinate_to_click: int):
        auto.click(coordinate_to_click)

    @staticmethod
    def scroll_on_screen(value_scroll: int):
        auto.scroll(value_scroll)

    @staticmethod
    def search_image_on_screen(image_to_search: str):
        try:
            print("Start Locate All On Screen")
            coordinate = auto.locateAllOnScreen(image=image_to_search, grayscale=True, confidence=0.9)
            if coordinate is not None:
                print(coordinate)
            if coordinate is not None:
                return coordinate
        except Exception as ex:
            logging.info(f"Image not found. Error: {ex}")
