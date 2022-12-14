import os

import random
import time

import keyboard
from automacao.screen_manager import ScreenManager


def run():
    print("Aguardando....")
    while True:
        total_follows_count = 0

        if ScreenManager.is_app_focused(app_tittle_name="instagram"):
            img = os.getcwd() + os.sep + "automacao" + os.sep + "img" + os.sep + "follow.png"
            coordinates = ScreenManager.search_image_on_screen(image_to_search=img)
            print(coordinates)

            for coordinate in coordinates:
                total_follows_count += 1
                ScreenManager.click_on_screen(coordinate_to_click=coordinate)
                # time.sleep(random.randint(3, 4))

            ScreenManager.scroll_on_screen(value_scroll=-400)
            time.sleep(random.randint(90, 120))
            print(f"Total de follows até o momento {str(total_follows_count)}")

        if keyboard.is_pressed("ESC"):
            print("Saindo do programa InstagramBot")
            break


print("Olá, estou aguardando você abrir o navegador\n"
      "e selecionar o perfil que quer copiar os seguidores!")
time.sleep(5)
print("Vou executar a função!")
run()
