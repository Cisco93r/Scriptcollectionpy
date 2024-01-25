import os
import subprocess

def generate_battery_report(output_file):
    # Esegui il comando per ottenere il report sull'alimentazione e scrivi l'output su un file HTML
    with open(output_file, "w") as file:
        subprocess.call(["powercfg", "/batteryreport"], stdout=file)

def main():
    # Scegli la directory di destinazione per il report
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file = os.path.join(desktop_path, "Battery-Report.html")

    # Genera il report sull'alimentazione
    generate_battery_report(output_file)

    print(f"Report sull'alimentazione creato: {output_file}")

if __name__ == "__main__":
    main()
