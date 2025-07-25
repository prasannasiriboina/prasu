import tkinter as tk
from tkinter import colorchooser

def choose_color():
    # Open the color chooser dialog
    color = colorchooser.askcolor(title="Select a Color")
    
    if color[1]:  # color[1] is the hex code
        color_display.config(bg=color[1])
        color_label.config(text=f"Selected Color: {color[1]}")

# Main window
root = tk.Tk()
root.title("Color Picker Tool")
root.geometry("300x200")

# Button to choose color
btn = tk.Button(root, text="Choose Color", command=choose_color)
btn.pack(pady=20)

# Label to show color hex code
color_label = tk.Label(root, text="Selected Color: None")
color_label.pack(pady=10)

# Frame to display selected color visually
color_display = tk.Label(root, width=20, height=5, bg="white", relief="ridge", borderwidth=2)
color_display.pack(pady=10)

root.mainloop()
