import os
import sys
import platform
import subprocess
import tkinter as tk
from tkinter import filedialog

def set_video_wallpaper(video_path):
    system_platform = platform.system()

    if system_platform == 'Windows':
        import win32gui
        import win32con

        # Setta il video come sfondo del desktop su Windows
        SPI_SETDESKWALLPAPER = 20
        win32gui.SystemParametersInfo(SPI_SETDESKWALLPAPER, video_path, 1+2)

    elif system_platform == 'Darwin':  # macOS
        from appscript import app, mactypes

        # Setta il video come sfondo del desktop su macOS
        app('Finder').desktop_picture.set(mactypes.File(video_path))

    elif system_platform == 'Linux':
        # Setta il video come sfondo del desktop su Linux
        try:
            subprocess.Popen(["xwinwrap", "-fs", "-ov", "-ni", "-s", "-st", "-sp", "-b", "-nf", "-argb", "-a", "-b", "--", "mplayer", "-wid", "WID", "-nosound", "-loop", "0", video_path])
        except FileNotFoundError:
            print("xwinwrap non trovato. Assicurati che sia installato.")

    else:
        print("Sistema operativo non supportato.")
        sys.exit(1)

def browse_video_file():
    filename = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.mkv")])
    if filename:
        entry_video_path.delete(0, tk.END)
        entry_video_path.insert(0, filename)

def apply_video_wallpaper():
    video_path = entry_video_path.get()
    if os.path.exists(video_path):
        set_video_wallpaper(video_path)
    else:
        print("Il percorso del video non è valido.")

# Creazione della GUI
root = tk.Tk()
root.title("Video Wallpaper")
root.geometry("400x150")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_video_path = tk.Label(frame, text="Percorso del video:")
label_video_path.grid(row=0, column=0, padx=5, pady=5)

entry_video_path = tk.Entry(frame, width=30)
entry_video_path.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(frame, text="Browse", command=browse_video_file)
button_browse.grid(row=0, column=2, padx=5, pady=5)

button_apply = tk.Button(root, text="Apply", command=apply_video_wallpaper)
button_apply.pack(pady=10)

root.mainloop()
