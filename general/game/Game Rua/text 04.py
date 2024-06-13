import tkinter as tk


class Widgets(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init___(self, parent)
        self.parent = parent

        self.initUI()

    def initUI():

        # Lots of other different tkinter widgets go here

        self.button = tk.Button(command=App(get_details))
        self.button.pack()


class PopUp(tk.TopLevel): 

class App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()

    def get_details(self):

        # Complete a function

    def initUI(self):

        self.parent.title("My Application")
        self.style = Style()
        self.style.theme_use("default")

        self.pack()

        self.widgets = Widgets(self)
        self.widgets.pack(side="top", anchor="center", fill="both", expand=True)

if __name__ == "__main__":

    root = tk.Tk()
    App(root).pack(side="top", fill="both", expand=True)
    root.resizable(0,0)
    root.mainloop()