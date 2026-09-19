import tkinter as tk

# main application window
root = tk.Tk()
root.title("Hello World App")
root.geometry("300x150")  # Sets (Width x Height)

# CreateLabel to display text
label = tk.Label(root, text="Hello, World!", font=("Arial", 16))

# Pack the label into the window (makes it visible)
label.pack(pady=40)  # pady adds vertical spacing

# Start application event loop
root.mainloop()