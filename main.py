import tkinter as tk
import statusbar
from tkinter import filedialog as fd
import json
from pathlib import PureWindowsPath, PurePosixPath

CFG = dict()

def load_cfg():
    global CFG
    try:
        with open("settings.json", "r") as infile:
            CFG = json.load(infile)
        sb.setText("Settings loaded.")
    except:
        pass

def save_cfg():
    try:
        obj = json.dumps(CFG, indent=4)
        with open("settings.json", "w") as outfile:
            outfile.write(obj)
        sb.setText("Settings saved.")
    except:
        pass

def add_menu(parent):
    menubar = tk.Menu(parent)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Settings", command=lambda: settings(parent))
    menubar.add_cascade(label="Edit", menu=editmenu)

    parent.config(menu=menubar)

def select_directory(entry):
    dir = fd.askdirectory(
        title='Choose directory',
        initialdir='/')

    if dir:
        dir = str(PureWindowsPath(PurePosixPath(dir)))
        CFG["main_dir"] = dir
        entry.delete(0, tk.END)
        entry.insert(0, dir)
        save_cfg()

def save_settings(frame):
    save_cfg()
    frame.destroy()

def settings(parent):
    frame = tk.Frame(master=parent)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    
    fc_frame = tk.Frame(master=frame)
    fc_frame.grid_columnconfigure(0, weight=1)
    fc_frame.grid_columnconfigure(1, weight=1)
    fc_frame.grid_columnconfigure(2, weight=1)
    
    main_dir_label = tk.Label(master=fc_frame, text="Main Directory:")
    main_dir_entry = tk.Entry(master=fc_frame, width=50)
    main_dir_entry.insert(0, CFG.get("main_dir"))
    main_dir_fd_button = tk.Button(master=fc_frame, text="+", command=lambda: select_directory(main_dir_entry))
    main_dir_label.grid(row=0, column=0, sticky=tk.E)
    main_dir_entry.grid(row=0, column=1, sticky=tk.W)
    main_dir_fd_button.grid(row=0, column=2, sticky=tk.W)
    fc_frame.grid(row=0, column=0, padx=20, pady=20)

    bt_frame = tk.Frame(master=frame)
    bt_frame.grid_columnconfigure(0, weight=1)
    bt_frame.grid_columnconfigure(1, weight=1)
    
    ok_button = tk.Button(master=bt_frame, text="OK", command=lambda: save_settings(frame))
    cancel_button = tk.Button(master=bt_frame, text="Cancel", command=lambda: frame.destroy())
    ok_button.grid(row=0, column=0, padx=5)
    cancel_button.grid(row=0, column=1, padx=5)
    bt_frame.grid(row=1, column=0, padx=20, pady=20)

    frame.grid(row=0, column=0, sticky=tk.NSEW)

window = tk.Tk()
window.title("Retro Curator")
window.resizable(width=True, height=True)
window.geometry("640x480")
window.minsize(640, 480)

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

add_menu(window)

sb = statusbar.StatusBar(window)



load_cfg()

window.mainloop()