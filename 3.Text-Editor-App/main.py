import tkinter as tk
from tkinter import filedialog, messagebox

# Main window code
home = tk.Tk()
home.title("Vijay's Notepad")
home.geometry("850x550")
home.configure(bg="#252526")

current_file = None

# Main Logic

#Funtion 1 - to create a new file
def new_file():
    global current_file
    current_file = None
    text.delete(1.0, tk.END)
    home.title("📝 Untitled - Notepad")

#Function 2 - to open a new file
def open_file():
    global current_file

    # Open File
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        current_file = file_path

        #open Selected File
        with open(file_path,'r', encoding="utf-8") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

#Function 3 - Save File
def save_file():
    global current_file

    #open save file dialogue
    if current_file is None:
        current_file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
        
    if current_file:
        with open(current_file, 'w', encoding="utf-8") as file:
            file.write(text.get(1.0, tk.END))

    messagebox.showinfo("Saved", "File saved successfully!")

# Function 4 - Exit
def exit_notepad():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        home.destroy()

# Status Bar Update
def update_status(event=None):
    content = text.get("1.0", "end-1c")

    words = len(content.split())
    chars = len(content)

    status.config(
        text=f" Words: {words}     Characters: {chars}"
    )

# Tool Bar
toolbar = tk.Frame(
    home,
    bg="#252526",
    height=45
)

toolbar.pack(side=tk.TOP, fill=tk.X)
toolbar.pack_propagate(False)

button_style = {
    "bg": "#3c3c3c",
    "fg": "white",
    "activebackground": "#0078D7",
    "activeforeground": "white",
    "relief": "flat",
    "font": ("Segoe UI", 10, "bold"),
    "padx": 10,
    "pady": 3,
    "cursor": "hand2"
}

tk.Button(toolbar,
          text="📄 New",
          command=new_file,**button_style).pack(side=tk.LEFT, padx=8, pady=8)

tk.Button(toolbar,
          text="📂 Open",
          command=open_file,**button_style).pack(side=tk.LEFT, padx=8)

tk.Button(toolbar,
          text="💾 Save",
          command=save_file,**button_style).pack(side=tk.LEFT, padx=8)

# Text Area  and Scrollbar
editor_frame = tk.Frame(home,  bg="#1e1e1e")

editor_frame.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(editor_frame)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create Text Area
text = tk.Text(
    editor_frame,
    wrap=tk.WORD,
    undo=True,
    font=("Consolas", 14),
    bg="#1e1e1e",
    fg="white",
    insertbackground="white",
    selectbackground="#0078D7",
    relief="flat",
    borderwidth=0,
    padx=12,
    pady=12,
    yscrollcommand=scrollbar.set
)


text.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=text.yview)

#Status Bar

status = tk.Label(
    home,
    text="Words: 0     Characters: 0",
    bg="#252526",
    fg="white",
    anchor="w",
    font=("Segoe UI", 10),
    padx=10,
    pady=4
)

status.pack(side=tk.BOTTOM, fill=tk.X)


# Create Menu Bar
menu = tk.Menu(home)
home.config(menu = menu)

file_menu = tk.Menu(menu, tearoff=0)

# add filemenu to menu bar (New, Open , Save, Exit)
menu.add_cascade(label="File", menu = file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit\tCtrl+E",command=exit_notepad)

#Keyboard shortcuts
home.bind("<Control-n>", lambda event: new_file())
home.bind("<Control-o>", lambda event: open_file())
home.bind("<Control-s>", lambda event: save_file())
home.bind("<Control-e>", lambda event: exit_notepad())
# Update status while typing
text.bind("<KeyRelease>", update_status)


#Starts and Keeps the window open
home.mainloop()