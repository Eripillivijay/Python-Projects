import time
import tkinter as tk

home = tk.Tk()
home.title("Digital Clock")


def currentTime():
    string = time.strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,currentTime)


dark_mode = True

def toggle_theme():
    global dark_mode

    if dark_mode:
        home.config(bg="#FFFFFF")
        label.config(background="#FFFFFF", foreground="#000000")
        button.config(text="🌙 Dark Mode", bg="#DDDDDD", fg="black")
    
    else:
        home.config(bg="#000000")
        label.config(background="#000000", foreground="#00E5FF")
        button.config(text="☀ Light Mode", bg="#333333", fg="white")

    dark_mode = not dark_mode

label = tk.Label(
    home,
    font=('Orbitron', 100, 'bold'),
    background='#000000',
    foreground='#00E5FF'
)
label.pack(anchor='center')

home.config(bg="#000000")

button = tk.Button(
    home,
    text="☀ Light Mode",
    command=toggle_theme,
    font=("Arial", 12, "bold"),
    bg="#333333",
    fg="white",
    relief="flat",
    padx=10,
    pady=5
)

button.pack(pady=10)

currentTime()
home.mainloop()