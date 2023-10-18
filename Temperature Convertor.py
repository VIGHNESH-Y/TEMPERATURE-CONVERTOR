import tkinter as tk
from tkinter import ttk, messagebox

def c_to_f():
    try:
        c = float(c_entry.get())
        f = c * 9 / 5 + 32
        f_entry.delete(0, tk.END)
        f_entry.insert(0, str(round(f, 2)))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for Celsius.")

def f_to_c():
    try:
        f = float(f_entry.get())
        c = (f - 32) * 5 / 9
        c_entry.delete(0, tk.END)
        c_entry.insert(0, str(round(c, 2)))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for Fahrenheit.")

def on_resize(event):
    pass

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("500x300")
root.resizable(False, False)
root.bind("<Configure>", on_resize)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=('Arial', 12), foreground='white', background='#4285F4', relief='flat')
style.map('TButton', foreground=[('active', 'white')], background=[('active', '#3367D6')])
style.configure('TLabel', font=('Arial', 12), foreground='#202124')
style.configure('TEntry', font=('Arial', 12), fieldbackground='#f1f3f4')

main_frame = ttk.Frame(root, padding=(30, 15))
main_frame.grid(row=0, column=0, sticky="nsew")

mode_label = ttk.Label(main_frame, text="Conversion Mode:")
mode_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

mode_var = tk.StringVar()
mode_var.set("Celsius to Fahrenheit")  # default value

mode_choices = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
mode_menu = ttk.Combobox(main_frame, textvariable=mode_var, values=mode_choices, state="readonly", style="TCombobox")
mode_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")

c_label = ttk.Label(main_frame, text="Celsius:")
c_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
c_entry = ttk.Entry(main_frame, style="TEntry")
c_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

f_label = ttk.Label(main_frame, text="Fahrenheit:")
f_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
f_entry = ttk.Entry(main_frame, style="TEntry")
f_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

convert_button = ttk.Button(main_frame, text="Convert", command=lambda: convert(mode_var.get()))
convert_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

def convert(mode):
    if mode == "Celsius to Fahrenheit":
        c_to_f()
    elif mode == "Fahrenheit to Celsius":
        f_to_c()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(3, weight=1)

root.mainloop()
