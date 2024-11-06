import tkinter as tk
from tkinter import ttk

class AdaptiveGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Adaptive GUI")

        # Start as half of the user's screen size
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width//2}x{screen_height//2}")

        self.bind("<Configure>", self.on_resize)

        container = ttk.Frame(self)
        container.pack(expand=True, fill='both')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Page1, Page2, Page3, Page4, Page5, Page6):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
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
                    child.config(width=event.width//20, height=event.height//50)

class BasePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_header()

    def create_header(self):
        header_frame = ttk.Frame(self)
        header_frame.pack(side="top", fill="x")

        for i, page in enumerate(("Page1", "Page2", "Page3", "Page4", "Page5", "Page6")):
            button = ttk.Button(header_frame, text=f"Go to {page}",
                                command=lambda p=page: self.controller.show_frame(p))
            button.pack(side="left")

class Page1(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        label = ttk.Label(self, text="This is Page 1")
        label.pack(side="top", fill="x", pady=10)
        
        for i in range(1, 6):
            widget = ttk.Label(self, text=f"Placeholder {i}")
            widget.pack(side="top", fill="x", pady=5)

class Page2(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        label = ttk.Label(self, text="This is Page 2")
        label.pack(side="top", fill="x", pady=10)
        
        for i in range(1, 3):
            widget = ttk.Label(self, text=f"Placeholder {i}")
            widget.pack(side="top", fill="x", pady=5)

class Page3(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        label = ttk.Label(self, text="This is Page 3")
        label.pack(side="top", fill="x", pady=10)
        
        widget = ttk.Label(self, text="Placeholder 1")
        widget.pack(side="top", fill="x", pady=5)

class Page4(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        label = ttk.Label(self, text="This is Page 4")
        label.pack(side="top", fill="x", pady=10)
        
        widget = ttk.Label(self, text="Placeholder 1")
        widget.pack(side="top", fill="x", pady=5)

class Page5(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        label = ttk.Label(self, text="This is Page 5")
        label.pack(side="top", fill="x", pady=10)
        
        widget = ttk.Label(self, text="Placeholder 1")
        widget.pack(side="top", fill="x", pady=5)

class Page6(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        label = ttk.Label(self, text="This is Page 6")
        label.pack(side="top", fill="x", pady=10)
        
        widget = ttk.Label(self, text="Placeholder 1")
        widget.pack(side="top", fill="x", pady=5)

if __name__ == "__main__":
    app = AdaptiveGUI()
    app.mainloop()
