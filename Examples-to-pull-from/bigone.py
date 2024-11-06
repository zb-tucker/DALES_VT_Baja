import tkinter as tk
from tkinter import ttk

class AdaptiveGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Adaptive GUI")

        self.bind("<Configure>", self.on_resize)

        # Create a container
        container = ttk.Frame(self)
        container.pack(expand=True, fill='both')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Create the different pages
        for F in (Page1, Page2, Page3, Page4, Page5):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # Place all the pages in the same location
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Page1")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def on_resize(self, event):
        # Dynamic resizing logic can be added here
        for frame in self.frames.values():
            for child in frame.winfo_children():
                if isinstance(child, ttk.Button):
                    child.config(width=event.width//10, height=event.height//50)

class Page1(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="This is Page 1")
        label.pack(side="top", fill="x", pady=10)

        # Add 5 widgets
        for i in range(1, 6):
            button = ttk.Button(self, text=f"Button {i}")
            button.pack(side="top", fill="x")

        # Navigation
        button_next = ttk.Button(self, text="Next Page",
                                 command=lambda: controller.show_frame("Page2"))
        button_next.pack()

class Page2(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="This is Page 2")
        label.pack(side="top", fill="x", pady=10)

        # Add 3 widgets
        for i in range(1, 4):
            button = ttk.Button(self, text=f"Button {i}")
            button.pack(side="top", fill="x")

        # Navigation
        button_next = ttk.Button(self, text="Next Page",
                                 command=lambda: controller.show_frame("Page3"))
        button_next.pack()

class Page3(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="This is Page 3")
        label.pack(side="top", fill="x", pady=10)

        # Add 3 widgets
        for i in range(1, 4):
            button = ttk.Button(self, text=f"Button {i}")
            button.pack(side="top", fill="x")

        # Navigation
        button_next = ttk.Button(self, text="Next Page",
                                 command=lambda: controller.show_frame("Page4"))
        button_next.pack()

class Page4(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="This is Page 4")
        label.pack(side="top", fill="x", pady=10)

        # Add 3 widgets
        for i in range(1, 4):
            button = ttk.Button(self, text=f"Button {i}")
            button.pack(side="top", fill="x")

        # Navigation
        button_next = ttk.Button(self, text="Next Page",
                                 command=lambda: controller.show_frame("Page5"))
        button_next.pack()

class Page5(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="This is Page 5")
        label.pack(side="top", fill="x", pady=10)

        # Add 3 widgets
        for i in range(1, 4):
            button = ttk.Button(self, text=f"Button {i}")
            button.pack(side="top", fill="x")

        # Navigation
        button_prev = ttk.Button(self, text="Previous Page",
                                 command=lambda: controller.show_frame("Page1"))
        button_prev.pack()

if __name__ == "__main__":
    app = AdaptiveGUI()
    app.mainloop()
