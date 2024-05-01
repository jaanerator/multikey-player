import keyboard
import pyautogui as pg


if __name__ == "__main__":
    print("ESC키 입력 시 프로그램이 종료됩니다.")
    print("q키 입력 시 ctrl + alt + shift + s 매크로가 실행됩니다.")
    i = 0
    while True:
        if keyboard.is_pressed("esc"):
            print("프로그램을 종료합니다.")
            break
        elif keyboard.is_pressed("q"):
            i += 1
            print(f"{i}번 매크로를 실행했습니다.")
            pg.hotkey("ctrl", "alt", "shift", "s")
        else:
            pass
