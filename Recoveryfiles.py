import os
import tkinter as tk
from tkinter import filedialog

def search_files(directory, extension):
    found_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                found_files.append(os.path.join(root, file))
    return found_files

def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

def search():
    directory = directory_entry.get()
    extension = extension_entry.get()
    found_files = search_files(directory, extension)
    
    if found_files:
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        for file in found_files:
            result_text.insert(tk.END, file + '\n')
        result_text.config(state=tk.DISABLED)
    else:
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "Nessun file trovato con l'estensione specificata.")
        result_text.config(state=tk.DISABLED)

# Creazione dell'interfaccia grafica
root = tk.Tk()
root.title("Recupero di programmi e file su PC Windows")

directory_label = tk.Label(root, text="Percorso del direttoio:")
directory_label.grid(row=0, column=0, sticky=tk.W)

directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(root, text="Sfoglia", command=browse_directory)
browse_button.grid(row=0, column=2, padx=5, pady=5)

extension_label = tk.Label(root, text="Estensione dei file:")
extension_label.grid(row=1, column=0, sticky=tk.W)

extension_entry = tk.Entry(root, width=10)
extension_entry.grid(row=1, column=1, padx=5, pady=5)

search_button = tk.Button(root, text="Cerca", command=search)
search_button.grid(row=1, column=2, padx=5, pady=5)

result_text = tk.Text(root, height=15, width=70)
result_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
result_text.config(state=tk.DISABLED)

root.mainloop()
