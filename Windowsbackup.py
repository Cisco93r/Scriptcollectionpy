import os
import tkinter as tk
from tkinter import filedialog
import subprocess
import zipfile

def select_source_folder():
    source_folder = filedialog.askdirectory()
    source_folder_entry.delete(0, tk.END)
    source_folder_entry.insert(0, source_folder)

def select_destination_folder():
    destination_folder = filedialog.askdirectory()
    destination_folder_entry.delete(0, tk.END)
    destination_folder_entry.insert(0, destination_folder)

def execute_backup():
    source_folder = source_folder_entry.get()
    destination_folder = destination_folder_entry.get()

    # Esegui il backup utilizzando robocopy
    robocopy_command = f'robocopy "{source_folder}" "{destination_folder}" /E /ZB /DCOPY:T /COPYALL /R:3 /W:5 /V /LOG:backup_log.txt'
    subprocess.run(robocopy_command, shell=True)

    # Crea una cartella zip del backup
    zip_filename = os.path.join(destination_folder, 'backup.zip')
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_folder)
                zipf.write(file_path, arcname)

    result_label.config(text="Backup completato e cartella zip creata!")

# Creazione dell'interfaccia grafica
root = tk.Tk()
root.title("Backup di cartelle, app, impostazioni e credenziali su Windows")

source_label = tk.Label(root, text="Seleziona cartella di origine:")
source_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

source_folder_entry = tk.Entry(root, width=50)
source_folder_entry.grid(row=0, column=1, padx=5, pady=5)

source_button = tk.Button(root, text="Scegli", command=select_source_folder)
source_button.grid(row=0, column=2, padx=5, pady=5)

destination_label = tk.Label(root, text="Seleziona cartella di destinazione:")
destination_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

destination_folder_entry = tk.Entry(root, width=50)
destination_folder_entry.grid(row=1, column=1, padx=5, pady=5)

destination_button = tk.Button(root, text="Scegli", command=select_destination_folder)
destination_button.grid(row=1, column=2, padx=5, pady=5)

backup_button = tk.Button(root, text="Esegui Backup", command=execute_backup)
backup_button.grid(row=2, column=0, columnspan=3, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
