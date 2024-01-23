import shutil
import os
from tkinter import Tk, Label, Button, filedialog

class GestoreFileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestore File")

        self.label_origine = Label(root, text="Origine:")
        self.label_origine.pack()

        self.button_origine = Button(root, text="Seleziona Origine", command=self.scegli_origine)
        self.button_origine.pack()

        self.label_destinazione = Label(root, text="Destinazione:")
        self.label_destinazione.pack()

        self.button_destinazione = Button(root, text="Seleziona Destinazione", command=self.scegli_destinazione)
        self.button_destinazione.pack()

        self.button_copia = Button(root, text="Copia File", command=self.copia_file)
        self.button_copia.pack()

        self.button_sposta = Button(root, text="Sposta File", command=self.sposta_file)
        self.button_sposta.pack()

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

