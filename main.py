import threading
import keyboard
from PIL import Image, ImageTk
import pyautogui as pg
from tkinter import Tk, Frame, LabelFrame, Button
from tkinter.ttk import Frame as frame
import yaml


class FrameController(frame):
    def __init__(self, ui_configs, controller=None):
        self.ui_configs = ui_configs
        self.controller = controller
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
        button_start = Button(frame_start, image=start_image, command=self.controller.start)
        button_start.image = start_image
        button_start.pack()

        frame_end = LabelFrame(start_end, text="終わりましょう。")
        frame_end.pack(side="right")
        end_image = Image.open("./end.png")
        end_image = end_image.resize((100, 100))
        end_image = ImageTk.PhotoImage(end_image)
        button_end = Button(frame_end, image=end_image, command=self.controller.end)
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


class WidgetController:
    def __init__(self):
        self.is_end = False
    
    def start(self):
        t = threading.Thread(target=self._start)
        t.start()
    
    def _start(self):
        print("ESC키 입력 시 프로그램이 종료됩니다.")
        print("q키 입력 시 ctrl + alt + shift + s 매크로가 실행됩니다.")
        i = 0
        while not self.is_end:
            if keyboard.is_pressed("q"):
                i += 1
                print(f"{i}번 매크로를 실행했습니다.")
                pg.hotkey("ctrl", "alt", "shift", "s")
        self.is_end = False
    
    def end(self):
        print("End 함수 발동")
        self.is_end = True


if __name__ == "__main__":
    # Get configurations
    with open("configs.yaml") as f:
        configs = yaml.load(f, Loader=yaml.FullLoader)
    
    # Execution
    wc = WidgetController()
    fc = FrameController(configs.get("ui", {}), wc)
    fc.mainloop()
