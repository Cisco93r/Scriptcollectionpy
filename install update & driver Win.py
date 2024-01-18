import subprocess
import sys
import platform

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione del comando: {e}")
        sys.exit(1)

def check_windows_version():
    version = platform.version()
    if '10.0.19041' in version:
        return 'Windows 10'
    elif '10.0.22000' in version:
        return 'Windows 11'
    else:
        print("Versione di Windows non supportata.")
        sys.exit(1)

def check_for_updates():
    print("Verifica degli aggiornamenti...")
    if platform.system() == "Windows":
        run_command("Start-Process -Wait -FilePath 'ms-settings:windowsupdate-action'")
    else:
        print("Questo script è progettato per Windows.")
        sys.exit(1)

def install_drivers():
    print("Installazione dei driver...")
    # Installazione del driver audio
    run_command("choco install chocolatey-audio-drivers -y")

    # Installazione del driver video
    run_command("choco install chocolatey-video-drivers -y")

    # Installazione del driver LAN
    run_command("choco install chocolatey-lan-drivers -y")

    # Aggiungi qui ulteriori istruzioni per installare altri driver, se necessario

def main():
    windows_version = check_windows_version()
    print(f"Sistema operativo rilevato: {windows_version}")

    check_for_updates()

    user_input = input("Vuoi installare i driver? (s/n): ").lower()
    if user_input == 's':
        install_drivers()
    else:
        print("Installazione dei driver annullata.")

if __name__ == "__main__":
    main()
