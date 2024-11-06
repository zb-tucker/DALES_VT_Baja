import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Adaptive Tkinter GUI")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size as a fraction of the screen size (e.g., 70% of screen width and height)
window_width = int(screen_width * 0.7)
window_height = int(screen_height * 0.7)

# Set the window geometry
root.geometry(f"{window_width}x{window_height}")

# Create a frame within the window
frame = tk.Frame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Add widgets to the frame
label = tk.Label(frame, text="This window adapts to screen size!")
label.pack(pady=10)

entry = tk.Entry(frame)
entry.pack(pady=10)

def on_button_click():
    print("Button clicked!")

button = tk.Button(frame, text="Click me!", command=on_button_click)
button.pack(pady=10)

# Start the main loop
root.mainloop()
