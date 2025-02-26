from pathlib import Path
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkinter import ttk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets"
root = tk.Tk()
root.destroy()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#window
class DalePositioning(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("DALE")  # Window Title
        self.geometry(f"878x600")  # Startup Dimensions
        self.minsize(878, 600)  # Minimum Dimensions

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

    def start_action(self):
        print("Start button clicked")

    def stop_action(self):
        print("Stop button clicked")


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

        startButton = Button(
            self,
            text="Start",
            borderwidth=1,
            highlightthickness=1,
            command=lambda: controller.start_action(),
            relief="flat"
        )
        startButton.place(x=0, y=40, width=120, height=35)

        stopButton = Button(
            self,
            text="Stop",
            borderwidth=1,
            highlightthickness=1,
            command=lambda: controller.stop_action(),
            relief="flat"
        )
        stopButton.place(x=125, y=40, width=120, height=35)
        
        # button1 = tk.Button(self.button_frame, text="Start", command=controller.start_action)
        # button1.place(relx=0, y=35, relwidth=0.1, relheight=0.1)

                 

#page 2
class Acceleration(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)


        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Sample Data for the Graph
        x = [1, 2, 3, 4, 5]
        y = [10, 15, 7, 8, 12]
        ax.plot(x, y, marker='o', linestyle='-')

        ax.set_title("Acceleration Over Time")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Acceleration (m/s^2)")

        # Embed Matplotlib Figure into Tkinter Canvas
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().place(x=0, y=35, relwidth=1, relheight=0.95)
        canvas.draw()


#page 3
class Speed(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Sample Data for the Graph
        x = [1, 2, 3, 4, 5]
        y = [10, 15, 7, 8, 12]
        ax.plot(x, y, marker='o', linestyle='-')

        ax.set_title("Speed Over Time")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Speed (m/s)")

        # Embed Matplotlib Figure into Tkinter Canvas
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().place(x=0, y=35, relwidth=1, relheight=0.95)
        canvas.draw()

#page 4
class Temperature(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Sample Data for the Graph
        x = [1, 2, 3, 4, 5]
        y = [10, 15, 7, 8, 12]
        ax.plot(x, y, marker='o', linestyle='-')

        ax.set_title("Tempurature Over Time")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Temp. (C)")

        # Embed Matplotlib Figure into Tkinter Canvas
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().place(x=0, y=35, relwidth=1, relheight=0.95)
        canvas.draw()

#page 5
class Straingauges(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)


        fig = Figure(figsize=(8, 4), dpi=100)  # Create the figure

        # Create 4 subplots in a 4-row, 1-column layout
        axes = [fig.add_subplot(4, 1, i + 1) for i in range(4)]

        # Dummy data for each graph
        data_x = [0, 1, 2, 3, 4, 5]
        data_y = [
            [10, 15, 20, 25, 30, 35],  # Graph 1
            [5, 10, 15, 10, 5, 0],     # Graph 2
            [3, 7, 2, 8, 6, 4],        # Graph 3
            [12, 9, 15, 10, 5, 20]     # Graph 4
        ]
        titles = ["Bridge 1", "Bridge 2", "Bridge 3", "Bridge 4"]

        # Plot each graph
        for ax, y_values, title in zip(axes, data_y, titles):
            ax.plot(data_x, y_values, marker="o", linestyle="-")
            ax.set_title(title)
            ax.grid(True)

        # Adjust spacing between subplots
        fig.tight_layout()

        # Embed the figure into Tkinter Canvas
        figure_canvas = FigureCanvasTkAgg(fig, master=self.canvas)
        figure_canvas.draw()
        figure_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


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