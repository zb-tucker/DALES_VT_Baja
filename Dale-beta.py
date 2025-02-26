from pathlib import Path
import tkinter as tk
#import matplotlib.pyplot as plt
from tkinter import ttk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets"
root = tk.Tk()
WINDOW_WIDTH = root.winfo_screenwidth() // 2
WINDOW_HEIGHT = root.winfo_screenheight() // 2
BASIC_WIDGET_REL_WIDTH = 0.4
BASIC_WIDGET_REL_HEIGHT = 0.4
root.destroy()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#window
class DalePositioning(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("DALE")  # Window Title
        self.geometry(f"878x{self.winfo_screenheight() // 2}")  # Startup Dimensions
        self.minsize(878, 400)  # Minimum Dimensions

        # Creates a frame that fills all space
        self.container = ttk.Frame(self)
        self.container.place(relx=0, rely=0, relwidth=1, relheight=1)  # Use place() for full scaling

        # Dictionary that stores the pages
        self.frames = {}
        for F in (Home, Acceleration, Speed, Temperature, Straingauges, Log):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)  # Full window scaling

        self.show_frame("Home")  # Show the first frame

    # Retrieves frame from dictionary and brings to front
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



#base class for the pages
class Header(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)  # inherits from ttk.Frame
        self.controller = controller

        self.home_button = PhotoImage(file=relative_to_assets("log_Button.png"))
        logButton = Button(
            self,
            image=self.home_button,
            borderwidth=1,
            highlightthickness=1,
            command=lambda: controller.show_frame("Home"),
            relief="flat"
        )
        logButton.place(x=0, y=0, width=116, height=35)

        self.log_button = PhotoImage(file=relative_to_assets("log_Button.png"))
        logButton = Button(
            self,
            image=self.log_button,
            borderwidth=1,
            highlightthickness=1,
            command=lambda: controller.show_frame("Log"),
            relief="flat"
        )
        logButton.place(x=117, y=0, width=116, height=35)

        self.speed_button = PhotoImage(file=relative_to_assets("speed_Button.png"))
        speedButton = Button(
            self,
            image=self.speed_button,
            borderwidth=1,
            highlightthickness=1,
            command=lambda: controller.show_frame("Speed"),
            relief="flat"
        )
        speedButton.place(x=234, y=0, width=116, height=35)

        self.acceleration_button = PhotoImage(file=relative_to_assets("acceleration_Button.png"))
        accelerationButton = Button(
            self,
            image=self.acceleration_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Acceleration"),
            relief="flat"
        )
        accelerationButton.place(x=351, y=0, width=175, height=35)

        self.temperature_button = PhotoImage(file=relative_to_assets("temp_Button.png"))
        temperatureButton = Button(
            self,
            image=self.temperature_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Temperature"),
            relief="flat"
        )
        temperatureButton.place(x=527.0, y=0.0, width=175, height=35)

        self.strain_button = PhotoImage(file=relative_to_assets("strainGauge_Button.png"))
        strainButton = Button(
            self,
            image=self.strain_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("Straingauges"),
            relief="flat"
        )
        strainButton.place(x=703.0, y=0, width=175, height=35)



#extends basepage, page one 
class Home(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)

        start_buton = Button(
            self,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Start Button Clicked"),
            relief="flat"
        )
        start_buton.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.2)

                 

#page 2
class Acceleration(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)

        # Draw a rectangle (x1, y1, x2, y2)
        self.rectangle = self.canvas.create_rectangle(50, 50, 200, 200, fill="blue")


#page 3
class Speed(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)

        # Draw a rectangle (x1, y1, x2, y2)
        self.rectangle = self.canvas.create_rectangle(50, 50, 200, 200, fill="blue")

#page 4
class Temperature(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)

        # Draw a rectangle (x1, y1, x2, y2)
        self.rectangle = self.canvas.create_rectangle(50, 50, 200, 200, fill="blue")

#page 5
class Straingauges(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)

        # Draw a rectangle (x1, y1, x2, y2)
        self.rectangle = self.canvas.create_rectangle(50, 50, 200, 200, fill="blue")
#page 6
class Log(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)

        # Draw a rectangle (x1, y1, x2, y2)
        self.rectangle = self.canvas.create_rectangle(50, 50, 200, 200, fill="blue")

#main loop
if __name__ == "__main__":
    app = DalePositioning()
    app.mainloop() 