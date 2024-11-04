from pathlib import Path
import tkinter as tk
from tkinter import ttk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/ryanheiss/Documents/DALES_VT_Baja/assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MultiPageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DALES GUI")
        self.geometry("1000x550")

        self.container = ttk.Frame(self)
        self.container.pack(fill='both', expand=True)

        self.frames = {}
        for F in (HomePage, LogPage, SpeedPage, AccelerationPage, TemperaturePage, StrainGaugePage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Set up a canvas
        canvas = Canvas(
            self,
            bg="#CF4420",
            height=550,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack(fill='both', expand=True)

        # Header
        self.header = PhotoImage(file=relative_to_assets("header.png"))
        canvas.create_image(500.0, 37.0, image=self.header)
        # Navigation buttons
        self.log_button = PhotoImage(file=relative_to_assets("log_Button.png"))
        logButton = Button(
            self,
            image=self.log_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(LogPage),
            relief="flat"
        )
        logButton.place(x=25.0, y=32.0, width=116.0, height=38.0)

        self.speed_button = PhotoImage(file=relative_to_assets("speed_Button.png"))
        speedButton = Button(
            self,
            image=self.speed_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(SpeedPage),
            relief="flat"
        )
        speedButton.place(x=155.0, y=32.0, width=116.0, height=38.0)

        self.acceleration_button = PhotoImage(file=relative_to_assets("acceleration_Button.png"))
        accelerationButton = Button(
            self,
            image=self.acceleration_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(AccelerationPage),
            relief="flat"
        )
        accelerationButton.place(x=296.0, y=32.0, width=175.0, height=38.0)

        self.temperature_button = PhotoImage(file=relative_to_assets("temp_Button.png"))
        temperatureButton = Button(
            self,
            image=self.temperature_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(TemperaturePage),
            relief="flat"
        )
        temperatureButton.place(x=485.0, y=32.0, width=175.0, height=38.0)

        self.strain_button = PhotoImage(file=relative_to_assets("strainGauge_Button.png"))
        strainButton = Button(
            self,
            image=self.strain_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(StrainGaugePage),
            relief="flat"
        )
        strainButton.place(x=674.0, y=32.0, width=175.0, height=38.0)

        self.main_button = PhotoImage(file=relative_to_assets("main_Button.png"))
        mainButton = Button(
            self,
            image=self.main_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(HomePage),
            relief="flat"
        )
        mainButton.place(x=863.0, y=32.0, width=116.0, height=38.0)




        # Add images and text to the canvas
        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        canvas.create_image(117.0, 440.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        canvas.create_image(428.0, 245.0, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        canvas.create_image(428.0, 440.0, image=self.image_image_5)

        #Text labels
        canvas.create_text(228.0, 331.0, anchor="nw", text="Acceleration", fill="#FFFFFF", font=("InriaSans Bold", 16 * -1))
        canvas.create_text(213.0, 134.0, anchor="nw", text="Speed", fill="#FFFFFF", font=("InriaSans Bold", 16 * -1))
        canvas.create_text(654.0, 75.0, anchor="nw", text="Strain Gauges", fill="#FFFFFF", font=("InriaSans Bold", 16 * -1))
        canvas.create_text(32.0, 330.0, anchor="nw", text="Orientation", fill="#FFFFFF", font=("InriaSans Bold", 16 * -1))
        canvas.create_text(27.0, 245.0, anchor="nw", text="Temperature", fill="#FFFFFF", font=("InriaSans Bold", 16 * -1))

        self.image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
        canvas.create_image(814.0, 165.0, image=self.image_image_6)

        self.image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        canvas.create_image(814.0, 313.0, image=self.image_image_7)

        self.image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
        canvas.create_image(814.0, 461.0, image=self.image_image_8)

        self.image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
        canvas.create_image(114.0, 300.0, image=self.image_image_9)

        self.image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
        canvas.create_image(112.0, 202.0, image=self.image_image_10)

        canvas.create_text(39.0, 178.0, anchor="nw", text="00:00:00.0", fill="#FFFFFF", font=("InriaSans Bold", 28 * -1))

        # Create buttons
        self.start_buton = PhotoImage(file=relative_to_assets("start_Button.png"))
        start_buton = Button(
            self,
            image=self.start_buton,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Start Button Clicked"),
            relief="flat"
        )
        start_buton.place(x=27.0, y=89.0, width=175.0, height=50.0)

        self.save_button = PhotoImage(file=relative_to_assets("save_Button.png"))
        save_button = Button(
            self,
            image=self.save_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Save Button clicked"),
            relief="flat"
        )
        save_button.place(x=228.0, y=86.0, width=175.0, height=50.0)

        self.clear_button = PhotoImage(file=relative_to_assets("clear_Button.png"))
        clear_button = Button(
            self,
            image=self.clear_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Clear Button clicked"),
            relief="flat"
        )
        clear_button.place(x=433.0, y=84.0, width=175.0, height=50.0)



        

class LogPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        canvas = Canvas(
            self,
            bg="#CF4420",
            height=550,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack(fill='both', expand=True)

        # Header
        self.header = PhotoImage(file=relative_to_assets("header.png"))
        canvas.create_image(500.0, 37.0, image=self.header)
        # Navigation buttons
        self.log_button = PhotoImage(file=relative_to_assets("log_Button.png"))
        logButton = Button(
            self,
            image=self.log_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(LogPage),
            relief="flat"
        )
        logButton.place(x=25.0, y=32.0, width=116.0, height=38.0)

        self.speed_button = PhotoImage(file=relative_to_assets("speed_Button.png"))
        speedButton = Button(
            self,
            image=self.speed_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(SpeedPage),
            relief="flat"
        )
        speedButton.place(x=166.0, y=32.0, width=116.0, height=38.0)

        self.acceleration_button = PhotoImage(file=relative_to_assets("acceleration_Button.png"))
        accelerationButton = Button(
            self,
            image=self.acceleration_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(AccelerationPage),
            relief="flat"
        )
        accelerationButton.place(x=307.0, y=32.0, width=175.0, height=38.0)

        self.temperature_button = PhotoImage(file=relative_to_assets("temp_Button.png"))
        temperatureButton = Button(
            self,
            image=self.temperature_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(TemperaturePage),
            relief="flat"
        )
        temperatureButton.place(x=507.0, y=32.0, width=175.0, height=38.0)

        self.strain_button = PhotoImage(file=relative_to_assets("strainGauge_Button.png"))
        strainButton = Button(
            self,
            image=self.strain_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(StrainGaugePage),
            relief="flat"
        )
        strainButton.place(x=707.0, y=32.0, width=175.0, height=38.0)


        label = ttk.Label(self, text="This is Page One", font=("Helvetica", 16))
        label.pack(pady=10)

        button = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button.pack()

class SpeedPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        canvas = Canvas(
            self,
            bg="#CF4420",
            height=550,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack(fill='both', expand=True)

        # Header
        self.header = PhotoImage(file=relative_to_assets("header.png"))
        canvas.create_image(500.0, 37.0, image=self.header)
        # Navigation buttons
        self.log_button = PhotoImage(file=relative_to_assets("log_Button.png"))
        logButton = Button(
            self,
            image=self.log_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(LogPage),
            relief="flat"
        )
        logButton.place(x=25.0, y=32.0, width=116.0, height=38.0)

        self.speed_button = PhotoImage(file=relative_to_assets("speed_Button.png"))
        speedButton = Button(
            self,
            image=self.speed_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(SpeedPage),
            relief="flat"
        )
        speedButton.place(x=166.0, y=32.0, width=116.0, height=38.0)

        self.acceleration_button = PhotoImage(file=relative_to_assets("acceleration_Button.png"))
        accelerationButton = Button(
            self,
            image=self.acceleration_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(AccelerationPage),
            relief="flat"
        )
        accelerationButton.place(x=307.0, y=32.0, width=175.0, height=38.0)

        self.temperature_button = PhotoImage(file=relative_to_assets("temp_Button.png"))
        temperatureButton = Button(
            self,
            image=self.temperature_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(TemperaturePage),
            relief="flat"
        )
        temperatureButton.place(x=507.0, y=32.0, width=175.0, height=38.0)

        self.strain_button = PhotoImage(file=relative_to_assets("strainGauge_Button.png"))
        strainButton = Button(
            self,
            image=self.strain_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(StrainGaugePage),
            relief="flat"
        )
        strainButton.place(x=707.0, y=32.0, width=175.0, height=38.0)

        self.main_button = PhotoImage(file=relative_to_assets("main_Button.png"))
        mainButton = Button(
            self,
            image=self.main_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(HomePage),
            relief="flat"
        )
        mainButton.place(x=863.0, y=32.0, width=116.0, height=38.0)


        label = ttk.Label(self, text="This is Page Two", font=("Helvetica", 16))
        label.pack(pady=10)

        button = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button.pack()

class AccelerationPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        canvas = Canvas(
            self,
            bg="#CF4420",
            height=550,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack(fill='both', expand=True)

        # Header
        self.header = PhotoImage(file=relative_to_assets("header.png"))
        canvas.create_image(500.0, 37.0, image=self.header)
        # Navigation buttons
        self.log_button = PhotoImage(file=relative_to_assets("log_Button.png"))
        logButton = Button(
            self,
            image=self.log_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(LogPage),
            relief="flat"
        )
        logButton.place(x=25.0, y=32.0, width=116.0, height=38.0)

        self.speed_button = PhotoImage(file=relative_to_assets("speed_Button.png"))
        speedButton = Button(
            self,
            image=self.speed_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(SpeedPage),
            relief="flat"
        )
        speedButton.place(x=166.0, y=32.0, width=116.0, height=38.0)

        self.acceleration_button = PhotoImage(file=relative_to_assets("acceleration_Button.png"))
        accelerationButton = Button(
            self,
            image=self.acceleration_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(AccelerationPage),
            relief="flat"
        )
        accelerationButton.place(x=307.0, y=32.0, width=175.0, height=38.0)

        self.temperature_button = PhotoImage(file=relative_to_assets("temp_Button.png"))
        temperatureButton = Button(
            self,
            image=self.temperature_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(TemperaturePage),
            relief="flat"
        )
        temperatureButton.place(x=507.0, y=32.0, width=175.0, height=38.0)

        self.strain_button = PhotoImage(file=relative_to_assets("strainGauge_Button.png"))
        strainButton = Button(
            self,
            image=self.strain_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(StrainGaugePage),
            relief="flat"
        )
        strainButton.place(x=707.0, y=32.0, width=175.0, height=38.0)

        self.main_button = PhotoImage(file=relative_to_assets("main_Button.png"))
        mainButton = Button(
            self,
            image=self.main_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(HomePage),
            relief="flat"
        )
        mainButton.place(x=863.0, y=32.0, width=116.0, height=38.0)


        label = ttk.Label(self, text="This is Page Two", font=("Helvetica", 16))
        label.pack(pady=10)

        button = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button.pack()

class TemperaturePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        canvas = Canvas(
            self,
            bg="#CF4420",
            height=550,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack(fill='both', expand=True)

        # Header
        self.header = PhotoImage(file=relative_to_assets("header.png"))
        canvas.create_image(500.0, 37.0, image=self.header)
        # Navigation buttons
        self.log_button = PhotoImage(file=relative_to_assets("log_Button.png"))
        logButton = Button(
            self,
            image=self.log_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(LogPage),
            relief="flat"
        )
        logButton.place(x=25.0, y=32.0, width=116.0, height=38.0)

        self.speed_button = PhotoImage(file=relative_to_assets("speed_Button.png"))
        speedButton = Button(
            self,
            image=self.speed_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(SpeedPage),
            relief="flat"
        )
        speedButton.place(x=166.0, y=32.0, width=116.0, height=38.0)

        self.acceleration_button = PhotoImage(file=relative_to_assets("acceleration_Button.png"))
        accelerationButton = Button(
            self,
            image=self.acceleration_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(AccelerationPage),
            relief="flat"
        )
        accelerationButton.place(x=307.0, y=32.0, width=175.0, height=38.0)

        self.temperature_button = PhotoImage(file=relative_to_assets("temp_Button.png"))
        temperatureButton = Button(
            self,
            image=self.temperature_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(TemperaturePage),
            relief="flat"
        )
        temperatureButton.place(x=507.0, y=32.0, width=175.0, height=38.0)

        self.strain_button = PhotoImage(file=relative_to_assets("strainGauge_Button.png"))
        strainButton = Button(
            self,
            image=self.strain_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(StrainGaugePage),
            relief="flat"
        )
        strainButton.place(x=707.0, y=32.0, width=175.0, height=38.0)

        self.main_button = PhotoImage(file=relative_to_assets("main_Button.png"))
        mainButton = Button(
            self,
            image=self.main_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(HomePage),
            relief="flat"
        )
        mainButton.place(x=863.0, y=32.0, width=116.0, height=38.0)

        label = ttk.Label(self, text="This is Page Two", font=("Helvetica", 16))
        label.pack(pady=10)

        button = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button.pack()

class StrainGaugePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        canvas = Canvas(
            self,
            bg="#CF4420",
            height=550,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack(fill='both', expand=True)

        # Header
        self.header = PhotoImage(file=relative_to_assets("header.png"))
        canvas.create_image(500.0, 37.0, image=self.header)
        # Navigation buttons
        self.log_button = PhotoImage(file=relative_to_assets("log_Button.png"))
        logButton = Button(
            self,
            image=self.log_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(LogPage),
            relief="flat"
        )
        logButton.place(x=25.0, y=32.0, width=116.0, height=38.0)

        self.speed_button = PhotoImage(file=relative_to_assets("speed_Button.png"))
        speedButton = Button(
            self,
            image=self.speed_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(SpeedPage),
            relief="flat"
        )
        speedButton.place(x=166.0, y=32.0, width=116.0, height=38.0)

        self.acceleration_button = PhotoImage(file=relative_to_assets("acceleration_Button.png"))
        accelerationButton = Button(
            self,
            image=self.acceleration_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(AccelerationPage),
            relief="flat"
        )
        accelerationButton.place(x=307.0, y=32.0, width=175.0, height=38.0)

        self.temperature_button = PhotoImage(file=relative_to_assets("temp_Button.png"))
        temperatureButton = Button(
            self,
            image=self.temperature_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(TemperaturePage),
            relief="flat"
        )
        temperatureButton.place(x=507.0, y=32.0, width=175.0, height=38.0)

        self.strain_button = PhotoImage(file=relative_to_assets("strainGauge_Button.png"))
        strainButton = Button(
            self,
            image=self.strain_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(StrainGaugePage),
            relief="flat"
        )
        strainButton.place(x=707.0, y=32.0, width=175.0, height=38.0)

        self.main_button = PhotoImage(file=relative_to_assets("main_Button.png"))
        mainButton = Button(
            self,
            image=self.main_button,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(HomePage),
            relief="flat"
        )
        mainButton.place(x=863.0, y=32.0, width=116.0, height=38.0)

        label = ttk.Label(self, text="This is Page Two", font=("Helvetica", 16))
        label.pack(pady=10)

        button = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button.pack()  



if __name__ == "__main__":
    app = MultiPageApp()
    app.mainloop()
