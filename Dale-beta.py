from pathlib import Path
import tkinter as tk
#import matplotlib.pyplot as plt
from tkinter import ttk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets"
root = tk.Tk()
WINDOW_WIDTH = root.winfo_screenwidth() // 2
WINDOW_HEIGHT = root.winfo_screenheight() // 2
root.destroy()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#window
class DalePositioning(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("DALE")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        #binds configure event to on_resize
        self.bind("<Configure>", self.on_resize)

        #creates frame, that fills all space
        container = ttk.Frame(self)
        container.pack(expand=True, fill='both')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #dictionary that stores the pages
        #gets page name, creates an instance, stores page, places in grid
        self.frames = {}
        for F in (Home, Acceleration, Speed, Temperature, Straingauges, Log):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        #shows page one
        self.show_frame("Page1")
    
    #retrieves frame from dictionary and brings to front
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    #called when page is configured
    def on_resize(self, event):
        # Dynamic resizing logic can be added here
        for frame in self.frames.values():
            for child in frame.winfo_children():
                if isinstance(child, ttk.Button):
                    child.config(width=event.width//20, height=event.height//50)

#base class for the pages
class BasePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)  # inherits from ttk.Frame
        self.controller = controller
        self.create_header()
        self.create_grid()  # Call create_grid here to set up the grid

    # creates a header that stretches horizontally
    def create_header(self):
        header_frame = ttk.Frame(self)
        header_frame.grid(row=0, column=0, columnspan=10, sticky="nsew", pady=1)  # Use grid instead of pack

        # for each page, creates a button in the header
        for i, page in enumerate(("Home", "Acceleration", "Speed", "Temperature", "Strain Gauges", "Log")):
            button = ttk.Button(header_frame, text=f"Go to {page}",
                                command=lambda p=page: self.controller.show_frame(p))
            button.grid(row=0, column=i, sticky="nsew", padx=3, pady=3)  # Use grid instead of pack

    # creates a 10x10 grid for positioning
    def create_grid(self):
        for i in range(10):
            self.grid_columnconfigure(i, weight=1, minsize=33)
            self.grid_rowconfigure(i, weight=1, minsize=33)

        # Configure the rows and columns to be expandable
        for i in range(10): 
            self.grid_rowconfigure(i+2, weight=1) 
            self.grid_columnconfigure(i, weight=1)

    def get_color(self, row, col): 
        # Generate a color based on row and column 
        r = (row * 25) % 256 # Generate a red value between 0-255 
        g = (col * 25) % 256 # Generate a green value between 0-255 
        b = ((row + col) * 10) % 256 # Generate a blue value between 0-255 
        return f'#{r:02x}{g:02x}{b:02x}'



#extends basepage, page one 
class Home(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        #label and its positioning
        #label = ttk.Label(self, text="This is Page 1")

        for row in range(10): 
            for col in range(10): 
                color = {0,0,0}
                widget = tk.Canvas(self, width=50, height=50, bg="black", highlightthickness=0) 
                widget.grid(row=row+1, column=col, padx=3, pady=3, sticky="nsew") 
                
        # Configure the rows and columns to be expandable 
        #for i in range(10): 
            #self.grid_rowconfigure(i+2, weight=1) 
            #self.grid_columnconfigure(i, weight=1)

        # placeholders in 10x10 grid 
        #for row in range(10): 
            #for col in range(10): 
                #widget = ttk.Label(self, text=f"R{row+1} C{col+1}")
                #widget.grid(row=row+1, column=col, padx=5, pady=5, sticky="nsew")

#page 2
class Acceleration(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # placeholders in 10x10 grid 
        widget = tk.Canvas(self, width=screen_width/3, height=screen_height/3, bg="black", highlightthickness=0) 
        widget.grid(row=5, column=5) 

        widget = tk.Canvas(self, width=5, height=5, bg="black", highlightthickness=0) 
        widget.grid(row=1, column=2, sticky="nsew") 

        widget = tk.Canvas(self, width=5, height=5, bg="black", highlightthickness=0) 
        widget.grid(row=3, column=2, sticky="nsew") 

        widget = tk.Canvas(self, width=5, height=5, bg="black", highlightthickness=0) 
        widget.grid(row=2, column=1, sticky="nsew") 

        widget = tk.Canvas(self, width=5, height=5, bg="black", highlightthickness=0) 
        widget.grid(row=2, column=3, sticky="nsew") 

        widget = tk.Canvas(self, width=11, height=11, bg="red", highlightthickness=0) 
        widget.grid(row=2, column=2) 

        widget = tk.Canvas(self, width=5, height=5, bg="black", highlightthickness=0) 
        widget.grid(row=5, column=2, sticky="nsew") 

        widget = tk.Canvas(self, width=5, height=5, bg="black", highlightthickness=0) 
        widget.grid(row=2, column=5, sticky="nsew") 


#page 3
class Speed(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        # placeholders in 10x10 grid 
        for row in range(10): 
            for col in range(10): 
                widget = ttk.Label(self, text=f"R{row+1} C{col+1}") 
                widget.grid(row=row+1, column=col, padx=5, pady=5, sticky="nsew")

#page 4
class Temperature(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        #label and positioning
        label = ttk.Label(self, text="This is Page 4")
        label.grid(row=0, column=0, columnspan=10, pady=10, sticky="nsew")
        
        # placeholders in 10x10 grid 
        for row in range(10): 
            for col in range(10): 
                widget = ttk.Label(self, text=f"R{row+1} C{col+1}") 
                widget.grid(row=row+1, column=col, padx=5, pady=5, sticky="nsew")

#page 5
class Straingauges(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        #label and positioning
        label = ttk.Label(self, text="This is Page 5")
        label.grid(row=0, column=0, columnspan=10, pady=10, sticky="nsew")
        
        # placeholders in 10x10 grid 
        for row in range(10): 
            for col in range(10): 
                widget = ttk.Label(self, text=f"R{row+1} C{col+1}") 
                widget.grid(row=row+1, column=col, padx=5, pady=5, sticky="nsew")

#page 6
class Log(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        #label and positioning
        label = ttk.Label(self, text="This is Page 6")
        label.grid(row=0, column=0, columnspan=10, pady=10, sticky="nsew")
        
        # placeholders in 10x10 grid 
        for row in range(10): 
            for col in range(10): 
                widget = ttk.Label(self, text=f"R{row+1} C{col+1}") 
                widget.grid(row=row+1, column=col, padx=5, pady=5, sticky="nsew")

#main loop
if __name__ == "__main__":
    app = DalePositioning()
    app.mainloop() 