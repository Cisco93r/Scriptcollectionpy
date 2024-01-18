import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione del comando: {e}")
        sys.exit(1)

# Installazione di Chocolatey
print("Installing Chocolatey...")
chocolatey_install_command = "powershell -Command \"iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))\""
run_command(chocolatey_install_command)

# Attendere che Chocolatey sia installato completamente prima di procedere
input("Chocolatey è stato installato. Premi Enter per continuare...")

# Installazione dei programmi specificati con Chocolatey
programs_to_install = [
    "googlechrome",
    "adobereader",
    "klitecodecpackfull",
    "youtubemusic",
    "firefox",
    "7zip",
    "hwinfo",
    "crystaldiskinfo",
    "vlc",
    "winrar",
    "visualstudiocode",
    "libreoffice-still"
]

for program in programs_to_install:
    print(f"Installing {program}...")
    install_command = f"choco install {program} -y"
    run_command(install_command)

print("Installazione completata.")
