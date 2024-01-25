import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup

def parse_battery_report(file_path):
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        informazioni_batteria = {}
        informazioni_batteria['Capacità di progettazione'] = soup.find(text='Capacità di progettazione').find_next('td').text.strip()
        informazioni_batteria['Capacità di carica completa'] = soup.find(text='Capacità di carica completa').find_next('td').text.strip()
        # Aggiungi altri campi se necessario
        
        return informazioni_batteria

def sfoglia_file():
    percorso_file = filedialog.askopenfilename(filetypes=[("File HTML", "*.html")])
    if percorso_file:
        informazioni_batteria = parse_battery_report(percorso_file)
        risultato_text.delete(1.0, tk.END)
        for chiave, valore in informazioni_batteria.items():
            risultato_text.insert(tk.END, f"{chiave}: {valore}\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Analizzatore di Report della Batteria")

    sfoglia_button = tk.Button(root, text="Sfoglia", command=sfoglia_file)
    sfoglia_button.pack(pady=10)

    risultato_text = tk.Text(root, height=10, width=50)
    risultato_text.pack(padx=10, pady=10)

    root.mainloop()

