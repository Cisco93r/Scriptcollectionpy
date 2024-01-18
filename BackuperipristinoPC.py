import shutil
import os

# Primo script
print("Cisco93r")
print("RICORDATI DI SEGUIRMI SU TIKTOK @Cisco93r")
print("---------------------------------")
input("RIPRISTINO TUTTI I FILE DEL TUO PC!\nPremi Invio per continuare...")

# Copia i file dall'unità USB per il primo script
source_folder_1 = fr"C:\Users\{os.getlogin()}"
destination_folder_1 = r"W:\backup PC"
shutil.copytree(source_folder_1, destination_folder_1, dirs_exist_ok=True)

# Stampa il messaggio di completamento per il primo script
print("Ho finito il primo script")

# Secondo script
input("BACKUPPA TUTTI I FILE DEL TUO PC!\nPremi Invio per continuare...")

# Copia i file sull'unità USB per il secondo script
source_folder_2 = fr"C:\Users\{os.getlogin()}\*"
destination_folder_2 = r"W:\backup PC"
shutil.copytree(source_folder_2, destination_folder_2, dirs_exist_ok=True)

# Stampa il messaggio di completamento per il secondo script
print("Ho finito il secondo script")

# Attesa finale
input("Premi Invio per chiudere...")
