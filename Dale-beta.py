from pathlib import Path
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkinter import ttk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets"
SAMPLE_RATE = 1 #in MS





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

    def record_action(self):
        print("Record button clicked")

    def stop_action(self):
        print("Stop button clicked")

    def clear_action(self):
        print("Clear button clicked")


#base class for the pages
class Header(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)  # inherits from ttk.Frame
        self.controller = controller

        self.home_button = PhotoImage(file=relative_to_assets("home_Button.png"))
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
            text="Record",
            borderwidth=1,
            highlightthickness=1,
            command=lambda: controller.record_action(),
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

        clearButton = Button(
            self,
            text="Clear",
            borderwidth=1,
            highlightthickness=1,
            command=lambda: controller.clear_action(),
            relief="flat"
        )
        clearButton.place(x=250, y=40, width=120, height=35)
        
        # button1 = tk.Button(self.button_frame, text="Start", command=controller.start_action)
        # button1.place(relx=0, y=35, relwidth=0.1, relheight=0.1)

#page 2
class Log(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        
        
        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)


        # Create a Figure and Axes for Matplotlib
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)


        # Embed Matplotlib Figure into Tkinter
        self.graph_canvas = FigureCanvasTkAgg(self.fig, self)
        self.graph_canvas.get_tk_widget().place(x=0, y=35, relwidth=1, relheight=0.95)

        # Start animation
        self.ani = FuncAnimation(self.fig, self.animate, interval=500, cache_frame_data=False)

    def animate(self, i):
        """Update the graph dynamically."""
        try:
            data = pd.read_csv('data_out.csv')

            self.ax.clear()  # Clear only the Axes, not the entire figure
            self.ax.plot(data['time'], data['Speed'], label='Speed')

            self.ax.legend(loc='upper left')
            self.ax.set_title("Real-time Speed Data")

            self.graph_canvas.draw()  # Update the Tkinter canvas

        except Exception as e:
            print(f"Error reading file: {e}")                

#page 3
class Speed(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        
        
        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)


        # Create a Figure and Axes for Matplotlib
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)


        # Embed Matplotlib Figure into Tkinter
        self.graph_canvas = FigureCanvasTkAgg(self.fig, self)
        self.graph_canvas.get_tk_widget().place(x=0, y=35, relwidth=1, relheight=0.95)

        # Start animation
        self.ani = FuncAnimation(self.fig, self.animate, interval=500, cache_frame_data=False)

    def animate(self, i):
        """Update the graph dynamically."""
        try:
            data = pd.read_csv('data_out.csv')

            self.ax.clear()  # Clear only the Axes, not the entire figure
            self.ax.plot(data['time'], data['Speed'], label='Speed')

            self.ax.legend(loc='upper left')
            self.ax.set_title("Real-time Speed Data")

            self.graph_canvas.draw()  # Update the Tkinter canvas

        except Exception as e:
            print(f"Error reading file: {e}")

#page 4
class Acceleration(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        
        
        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)


        # Create a Figure and Axes for Matplotlib
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)


        # Embed Matplotlib Figure into Tkinter
        self.graph_canvas = FigureCanvasTkAgg(self.fig, self)
        self.graph_canvas.get_tk_widget().place(x=0, y=35, relwidth=1, relheight=0.95)

        # Start animation
        self.ani = FuncAnimation(self.fig, self.animate, interval=500, cache_frame_data=False)

    def animate(self, i):
        """Update the graph dynamically."""
        try:
            data = pd.read_csv('data_out.csv')

            self.ax.clear()  # Clear only the Axes, not the entire figure
            self.ax.plot(data['time'], data['Acceleration'], label='Acceleration')

            self.ax.legend(loc='upper left')
            self.ax.set_title("Real-time Acceleration Data")

            self.graph_canvas.draw()  # Update the Tkinter canvas

        except Exception as e:
            print(f"Error reading file: {e}")

#page 5
class Temperature(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        
        
        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)


        # Create a Figure and Axes for Matplotlib
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)


        # Embed Matplotlib Figure into Tkinter
        self.graph_canvas = FigureCanvasTkAgg(self.fig, self)
        self.graph_canvas.get_tk_widget().place(x=0, y=35, relwidth=1, relheight=0.95)

        # Start animation
        self.ani = FuncAnimation(self.fig, self.animate, interval=500, cache_frame_data=False)

    def animate(self, i):
        """Update the graph dynamically."""
        try:
            data = pd.read_csv('data_out.csv')

            self.ax.clear()  # Clear only the Axes, not the entire figure
            self.ax.plot(data['time'], data['Temp'], label='Temperature')

            self.ax.legend(loc='upper left')
            self.ax.set_title("Real-time Temperature Data")

            self.graph_canvas.draw()  # Update the Tkinter canvas

        except Exception as e:
            print(f"Error reading file: {e}")

#page 6
class Straingauges(Header):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        
        
        self.canvas = Canvas(self, bg="#CF4420")
        self.canvas.place(relx=0, y=35, relwidth=1, relheight=1)


        # Create a Figure and Axes for Matplotlib
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)


        # Embed Matplotlib Figure into Tkinter
        self.graph_canvas = FigureCanvasTkAgg(self.fig, self)
        self.graph_canvas.get_tk_widget().place(x=0, y=35, relwidth=1, relheight=0.95)

        # Start animation
        self.ani = FuncAnimation(self.fig, self.animate, interval=500, cache_frame_data=False)

    def animate(self, i):
        """Update the graph dynamically."""
        try:
            data = pd.read_csv('data_out.csv')

            self.ax.clear()  # Clear only the Axes, not the entire figure
            self.ax.plot(data['time'], data['Bridge1'], label='Bridge 1')
            self.ax.plot(data['time'], data['Bridge2'], label='Bridge 2')
            self.ax.plot(data['time'], data['Bridge3'], label='Bridge 3')
            self.ax.plot(data['time'], data['Bridge4'], label='Bridge 4')

            self.ax.legend(loc='upper left')
            self.ax.set_title("Real-time Strain Gauge Data")

            self.graph_canvas.draw()  # Update the Tkinter canvas

        except Exception as e:
            print(f"Error reading file: {e}")


#main loop
if __name__ == "__main__":
    app = DalePositioning()
    app.mainloop() 