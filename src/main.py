import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import sys
import os

def f(m: int | float, x: int | float, b: int | float) -> int | float:
    return m * x + b

def g(m: int | float, x: int | float, b: int | float) -> int | float:
    return m * x ** 2 + b

def z(m: int | float, x: int | float, b: int | float) -> int | float:
    return m * x ** 3 + b

def calculate():
    try:
        limit_low = int(entry_low.get())
        limit_high = int(entry_high.get())
        steps = int(entry_steps.get())
        m = int(entry_m.get())
        b = int(entry_b.get())
        func_choice = func_var.get()

        func = f if func_choice == 'f' else g if func_choice == 'g' else z

        for row in table.get_children():
            table.delete(row)
        
        for i in range(limit_low, limit_high + 1, steps):
            table.insert("", "end", values=(i, func(m, i, b)))
    except ValueError:
        status_label.config(text="Fehler: Ungültige Eingabe!", fg="red")

def resource_path(relative_path):
    try:
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    except Exception as e:
        print(f"Fehler beim Bestimmen des Ressourcenpfades: {e}")
        return relative_path

root = tk.Tk()
root.title("Funktionsrechner")
root.config(bg="#f0f0f0")
icon = PhotoImage(file=resource_path("src\\res\\img\\icon.png"))
root.iconphoto(True, icon)

root.state("zoomed")

frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
frame.pack(pady=10, fill="both", expand=True)

frame.grid_rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
frame.grid_columnconfigure([0, 1], weight=1)

tk.Label(frame, text="Untergrenze:", bg="#ffffff", font=("Arial", 14)).grid(row=0, column=0, sticky="w", pady=5)
entry_low = tk.Entry(frame, font=("Arial", 14))
entry_low.grid(row=0, column=1, pady=5, sticky="ew")
entry_low.insert(0, "-100")

tk.Label(frame, text="Obergrenze:", bg="#ffffff", font=("Arial", 14)).grid(row=1, column=0, sticky="w", pady=5)
entry_high = tk.Entry(frame, font=("Arial", 14))
entry_high.grid(row=1, column=1, pady=5, sticky="ew")
entry_high.insert(0, "100")

tk.Label(frame, text="Schrittweite:", bg="#ffffff", font=("Arial", 14)).grid(row=2, column=0, sticky="w", pady=5)
entry_steps = tk.Entry(frame, font=("Arial", 14))
entry_steps.grid(row=2, column=1, pady=5, sticky="ew")
entry_steps.insert(0, "1")

tk.Label(frame, text="m:", bg="#ffffff", font=("Arial", 14)).grid(row=3, column=0, sticky="w", pady=5)
entry_m = tk.Entry(frame, font=("Arial", 14))
entry_m.grid(row=3, column=1, pady=5, sticky="ew")
entry_m.insert(0, "2")

tk.Label(frame, text="b:", bg="#ffffff", font=("Arial", 14)).grid(row=4, column=0, sticky="w", pady=5)
entry_b = tk.Entry(frame, font=("Arial", 14))
entry_b.grid(row=4, column=1, pady=5, sticky="ew")
entry_b.insert(0, "2")

func_var = tk.StringVar(value='f')
tk.Label(frame, text="Funktion:", bg="#ffffff", font=("Arial", 14)).grid(row=5, column=0, sticky="w", pady=5)
f_radio = tk.Radiobutton(frame, text="f(x) = m*x + b", variable=func_var, value='f', bg="#ffffff", font=("Arial", 14))
f_radio.grid(row=5, column=1, sticky="w", pady=5)
g_radio = tk.Radiobutton(frame, text="g(x) = m*x^2 + b", variable=func_var, value='g', bg="#ffffff", font=("Arial", 14))
g_radio.grid(row=6, column=1, sticky="w", pady=5)
z_radio = tk.Radiobutton(frame, text="z(x) = m*x^3 + b", variable=func_var, value='z', bg="#ffffff", font=("Arial", 14))  # Neuer Radiobutton
z_radio.grid(row=7, column=1, sticky="w", pady=5)

calculate_button = tk.Button(root, text="Berechnen", command=calculate, bg="#4CAF50", fg="white", font=("Arial", 16), relief="flat")
calculate_button.pack(pady=10, fill="x", padx=60)

status_label = tk.Label(root, text="", fg="black", font=("Arial", 14))
status_label.pack()

table_frame = tk.Frame(root)
table_frame.pack(expand=True, fill="both", padx=20, pady=0)

scrollbar = tk.Scrollbar(table_frame, orient="vertical")

table = ttk.Treeview(table_frame, columns=("X", "Y"), show="headings", height=20, yscrollcommand=scrollbar.set)  # Höhere Tabelle
table.heading("X", text="X")
table.heading("Y", text="Y")

scrollbar.config(command=table.yview)
scrollbar.pack(side="right", fill="y")

style = ttk.Style()
style.configure("Treeview",
                font=("Arial", 14),
                rowheight=30,
                background="#f9f9f9",
                foreground="#333")
style.configure("Treeview.Heading", font=("Arial", 14, "bold"), background="white", foreground="black")
style.configure("Treeview", foreground="black", background="white")
style.map("Treeview", background=[('selected', '#c2f0c2')])

table.pack(expand=True, fill="both", padx=20, pady=10)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
