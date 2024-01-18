import subprocess

def esegui_pulizia_disco():
    try:
        # Avvia l'utility Pulizia disco su Windows
        subprocess.run(['cleanmgr', '/sagerun:1'], check=True)
        print("Pulizia disco completata con successo.")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante la pulizia disco: {e}")

if __name__ == "__main__":
    esegui_pulizia_disco()
