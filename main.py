# Frontend:
# Importiert das Backend-Modul, das die Datenverarbeitung übernimmt
import backend  # Artem

# Importiert die tkinter-Bibliothek für die Benutzeroberfläche
import tkinter as tk                                           
from tkinter import filedialog  # Für Dateiauswahl-Dialog

# Farben und Stile für das Fenster und die Elemente
hintergrundFarbe = "#2f4d62"  # Hintergrundfarbe des Fensters
HintergrundFarbeTitel = "#ffffe1"  # Hintergrundfarbe für Titel
schriftFarbe = "#2f4d62"  # Schriftfarbe für Text
buttonHover = "#f5ebc7"  # Farbe, wenn der Mauszeiger über dem Button ist
buttonFarbe = "#ffffe1"  # Standardfarbe des Buttons

# Hauptfenster für die Benutzeroberfläche erstellen
root = tk.Tk()
root.title("Konvertierung")  # Titel des Fensters             

# Bildschirmgröße des Benutzers ermitteln
bildschirmBreite = root.winfo_screenwidth()  # Breite des Bildschirms
bildschirmHöhe = root.winfo_screenheight()  # Höhe des Bildschirms

# Größe des Fensters anpassen (80% der Breite, 70% der Höhe des Bildschirms)
root.geometry(f"{int(bildschirmBreite * 0.8)}x{int(bildschirmHöhe * 0.7)}")
root.configure(background=hintergrundFarbe)  # Hintergrundfarbe des Fensters

# Funktion zur Auswahl einer Excel-Datei
def open_it():
    # Öffnet einen Dialog, in dem der Benutzer eine Excel-Datei auswählen kann
    file = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file:  # Wenn eine Datei ausgewählt wurde
        print(f"Ausgewählte Datei: {file}")  # Zeigt den Dateipfad in der Konsole an
        backend.prepare_report(file)  # Übergibt die Datei an das Backend zur Verarbeitung 

# Funktionen für den "Hover"-Effekt auf dem Button (wenn die Maus drüber ist)
def on_enter(e):  # Wenn die Maus auf den Button geht
    e.widget.config(background=schriftFarbe, foreground=HintergrundFarbeTitel)  # Ändert Farben

def on_leave(e):  # Wenn die Maus den Button verlässt
    e.widget.config(background=buttonFarbe, foreground=schriftFarbe)  # Stellt ursprüngliche Farben wieder her

# Erstellt ein Label (Überschrift) für die Benutzeroberfläche
label = tk.Label(
    root,  # Im Hauptfenster anzeigen
    text="PDF - Generator",  # Text des Labels
    font=("Arial", 18),  # Schriftart und -größe
    background=hintergrundFarbe,  # Hintergrundfarbe
    foreground=buttonFarbe  # Schriftfarbe
)
label.pack(padx=20, pady=20)  # Abstand oben und unten hinzufügen

# Erstellt einen Button, mit dem der Benutzer eine Excel-Datei auswählen kann
button = tk.Button(
    root,  # Im Hauptfenster anzeigen
    text="Wählen Sie bitte eine Excel-Datei aus!",  # Text des Buttons
    font=('Arial', 12),  # Schriftart und -größe
    bg=buttonFarbe,  # Hintergrundfarbe des Buttons
    fg=schriftFarbe,  # Schriftfarbe des Buttons
    command=open_it  # Die Hauptfunktion des Buttons wird ausgeführt, also der Dialog mit dem Datei-Explorer
)
button.pack(pady=230)  # Abstand einstellen, damit der Button an der richtigen Stelle ist

# Bindet die "Hover"-Effekte an den Button
button.bind("<Enter>", on_enter)  # Wenn die Maus auf den Button geht
button.bind("<Leave>", on_leave)  # Wenn die Maus den Button verlässt

# Starten der Benutzeroberfläche
# Dies zeigt das Fenster an und hält es geöffnet, bis der Benutzer es schließt
root.mainloop()
