import random
import time

import keyboard
from automacao.screen_manager import ScreenManager


def run():
    while True:
        total_follows_count = 0
        
        if ScreenManager.is_app_focused(app_tittle_name="instagram"):
            coordinates = ScreenManager.search_image_on_screen(image_to_search="C:\\Users\\rafam\\Projects\\automatizacao-processos\\automacao\\img\\follow.png")
            print(coordinates)
            for coordinate in coordinates:
                total_follows_count += 1
                ScreenManager.click_on_screen(coordinate_to_click=coordinate)
                time.sleep(random.randint(3, 4))

            ScreenManager.scroll_on_screen(value_scroll=-400)
            time.sleep(random.randint(3, 4))
            print(f"Total de follows até o momento {str(total_follows_count)}")

        if keyboard.is_pressed("ESC"):
            print("Saindo do programa InstagramBot")
            break

run()
