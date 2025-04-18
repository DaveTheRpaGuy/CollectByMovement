from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.winfo_height = height
        self.__root.winfo_width = width
        self.__root.title("Collect By Movement")
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False