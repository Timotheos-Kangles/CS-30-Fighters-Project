import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Simple UI in Thonny")
root.geometry("300x200")

# Function to handle button click
def on_button_click():
    messagebox.showinfo("Message", "Hello from Thonny!")

# Create a label
label = tk.Label(root, text="Welcome to Thonny UI!", font=("Arial", 12))
label.pack(pady=10)

# Create a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Run the application
root.mainloop()
