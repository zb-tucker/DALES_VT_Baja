import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x300")
root.title("Button Position Example")

# Create a frame within the window
frame = tk.Frame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Add widgets to the frame
label = tk.Label(frame, text="This window adapts to screen size!")
label.grid(row=0, column=0, columnspan=2, pady=10)

entry = tk.Entry(frame)
entry.grid(row=1, column=0, columnspan=2, pady=10)

def on_button_click():
    print("Button clicked!")

button1 = tk.Button(frame, text="Button 1", command=on_button_click)
button1.grid(row=2, column=0, padx=10, pady=10)

button2 = tk.Button(frame, text="Button 2", command=on_button_click)
button2.grid(row=2, column=1, padx=10, pady=10)

# Start the main loop
root.mainloop()
