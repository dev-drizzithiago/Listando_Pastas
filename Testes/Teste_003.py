import tkinter as tk


class Test:
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="Text")

        self.button = tk.Button(
            self.root, text="Click to change text below", command=self.changeText)
        self.button.pack()
        self.label.pack()
        self.root.mainloop()

    def changeText(self):
        self.label["text"] = "Text updated"


app = Test()