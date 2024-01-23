import shutil
import os
from tkinter import Tk, Label, Button, filedialog, ttk

class GestoreFileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestore File")

        self.frame_origine = ttk.Frame(root, padding="10")
        self.frame_origine.grid(column=0, row=0, sticky="ew")

        self.label_origine = ttk.Label(self.frame_origine, text="Origine:")
        self.label_origine.grid(column=0, row=0, sticky="w")

        self.button_origine = ttk.Button(self.frame_origine, text="Seleziona Origine", command=self.scegli_origine)
        self.button_origine.grid(column=1, row=0, padx=5)

        self.frame_destinazione = ttk.Frame(root, padding="10")
        self.frame_destinazione.grid(column=0, row=1, sticky="ew")

        self.label_destinazione = ttk.Label(self.frame_destinazione, text="Destinazione:")
        self.label_destinazione.grid(column=0, row=0, sticky="w")

        self.button_destinazione = ttk.Button(self.frame_destinazione, text="Seleziona Destinazione", command=self.scegli_destinazione)
        self.button_destinazione.grid(column=1, row=0, padx=5)

        self.frame_buttons = ttk.Frame(root, padding="10")
        self.frame_buttons.grid(column=0, row=2, sticky="ew")

        self.button_copia = ttk.Button(self.frame_buttons, text="Copia File", command=self.copia_file)
        self.button_copia.grid(column=0, row=0, padx=5)

        self.button_sposta = ttk.Button(self.frame_buttons, text="Sposta File", command=self.sposta_file)
        self.button_sposta.grid(column=1, row=0, padx=5)

        self.origine = ""
        self.destinazione = ""

    def scegli_origine(self):
        self.origine = filedialog.askopenfilename(title="Seleziona il file di origine")

    def scegli_destinazione(self):
        self.destinazione = filedialog.askdirectory(title="Seleziona la cartella di destinazione")

    def copia_file(self):
        if self.origine and self.destinazione:
            shutil.copy(self.origine, os.path.join(self.destinazione, os.path.basename(self.origine)))
            print(f"File copiato da {self.origine} a {self.destinazione}")
        else:
            print("Seleziona origine e destinazione prima di copiare il file.")

    def sposta_file(self):
        if self.origine and self.destinazione:
            shutil.move(self.origine, os.path.join(self.destinazione, os.path.basename(self.origine)))
            print(f"File spostato da {self.origine} a {self.destinazione}")
        else:
            print("Seleziona origine e destinazione prima di spostare il file.")

if __name__ == "__main__":
    root = Tk()
    app = GestoreFileApp(root)
    root.mainloop()
