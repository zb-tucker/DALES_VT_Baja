import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("500x400")
root.title("Button Position Example with Widgets")

# Create a frame within the window
frame = tk.Frame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Add widgets to the frame
label = tk.Label(frame, text="This window adapts to screen size!")
label.grid(row=0, column=0, columnspan=3, pady=10)

entry = tk.Entry(frame)
entry.grid(row=1, column=0, columnspan=3, pady=10)

# Add more widgets
button1 = tk.Button(frame, text="Button 1", command=lambda: print("Button 1 clicked"))
button1.grid(row=2, column=0, padx=10, pady=10)

button2 = tk.Button(frame, text="Button 2", command=lambda: print("Button 2 clicked"))
button2.grid(row=2, column=1, padx=10, pady=10)

button3 = tk.Button(frame, text="Button 3", command=lambda: print("Button 3 clicked"))
button3.grid(row=2, column=2, padx=10, pady=10)

label2 = tk.Label(frame, text="Additional Text")
label2.grid(row=3, column=0, columnspan=3, pady=10)

entry2 = tk.Entry(frame)
entry2.grid(row=4, column=0, columnspan=3, pady=10)

# Add a quit button to close the window
quit_button = tk.Button(frame, text="Quit", command=root.destroy)
quit_button.grid(row=5, column=1, pady=20)

# Start the main loop
root.mainloop()
