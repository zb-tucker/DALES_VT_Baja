import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Frame example gui")
        self.geometry("400x300")
        
        self.frame1 = Frame1(self)
        self.frame2 = Frame2(self)
        
        self.frame1.pack(fill="both", expand=True)
    
    def show_frame1(self):
        self.frame2.pack_forget()
        self.frame1.pack(fill="both", expand=True)

    def show_frame2(self):
        self.frame1.pack_forget()
        self.frame2.pack(fill="both", expand=True)

class Frame1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label(self, text="This is Frame 1")
        label.pack(pady=10)
        
        button = tk.Button(self, text="Go to Frame 2", command=master.show_frame2)
        button.pack(pady=10)

class Frame2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label(self, text="This is Frame 2")
        label.pack(pady=10)
        
        button = tk.Button(self, text="Back to Frame 1", command=master.show_frame1)
        button.pack(pady=10)

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
