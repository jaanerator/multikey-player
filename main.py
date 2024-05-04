import keyboard
from PIL import Image, ImageTk
import pyautogui as pg
from tkinter import Tk, Frame, LabelFrame, Button
from tkinter.ttk import Frame as frame


class FrameController(frame):
    def __init__(self, ui_configs):
        self.ui_configs = ui_configs
        self._set_widget()
        self._init_interface()
    
    def mainloop(self):
        self.window.mainloop()
    
    def _set_widget(self):
        self.window = Tk()
        self.window.iconbitmap("./dist/main_icon_ouk_icon.ico")

        start_end = Frame(self.window)
        start_end.pack(side="bottom", pady=20)

        frame_start = LabelFrame(start_end, text="始めましょう。")
        frame_start.pack(side="left")
        start_image = Image.open("./start.png")
        start_image = start_image.resize((100, 100))
        start_image = ImageTk.PhotoImage(start_image)
        button_start = Button(frame_start, image=start_image)
        button_start.image = start_image
        button_start.pack()

        frame_end = LabelFrame(start_end, text="終わりましょう。")
        frame_end.pack(side="right")
        end_image = Image.open("./end.png")
        end_image = end_image.resize((100, 100))
        end_image = ImageTk.PhotoImage(end_image)
        button_end = Button(frame_end, image=end_image)
        button_end.image = end_image
        button_end.pack()

    def _init_interface(self):
        super().__init__()
        master_title = self.ui_configs.get("master_title", "None Name")
        self.master.title(master_title)

        # Set window size
        w, h = self.ui_configs.get("window_size", (850, 600))
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
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


if __name__ == "__main__":
    # Execution
    fc = FrameController({})
    fc.mainloop()
