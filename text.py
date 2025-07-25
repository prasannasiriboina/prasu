import tkinter as tk
from tkinter import messagebox

def new_file():
    text_area.delete('1.0', tk.END)

def open_file():
    try:
        with open('sample.txt', 'r') as file:
            content = file.read()
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, content)
    except FileNotFoundError:
        messagebox.showinfo("Info", "No file named 'sample.txt' found.")

def save_file():
    content = text_area.get('1.0', tk.END)
    with open('sample.txt', 'w') as file:
        file.write(content)
    messagebox.showinfo("Info", "File saved as 'sample.txt'.")

root = tk.Tk()
root.title("Simple Text Editor")

# Text widget with light yellow background
text_area = tk.Text(root, wrap='word', font=('Arial', 12), bg='lightyellow')
text_area.pack(expand=True, fill='both')

# Menu bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.geometry("600x400")
root.mainloop()
