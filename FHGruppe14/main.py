import backend # Artem
import tkinter as tk
from tkinter import filedialog

# Farben und Stile
hintergrundFarbe = "#2f4d62"
HintergrundFarbeTitel = "#ffffe1"
schriftFarbe = "#2f4d62"
buttonHover = "#f5ebc7"
buttonFarbe = "#ffffe1"

# Hauptfenster erstellen
root = tk.Tk()
root.title("Konvertierung")

# Ermittlung der Bildschirmmaße des Benutzers
bildschirmBreite = root.winfo_screenwidth()
bildschirmHöhe = root.winfo_screenheight()

# An Benutzer Angepasstes Fenster
root.geometry(f"{int(bildschirmBreite * 0.8)}x{int(bildschirmHöhe * 0.7)}")
root.configure(background=hintergrundFarbe)

#Auswahl der Excel Datei
def open_it():
    file = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file:
        print(f"Ausgewählte Datei: {file}")
        backend.prepare_report(file) # Artem

#Hover effekt
def on_enter(e):
    e.widget.config(background = schriftFarbe, foreground = HintergrundFarbeTitel)

def on_leave(e):
    e.widget.config(background = buttonFarbe, foreground = schriftFarbe)

label = tk.Label(root, text="PDF - Generator", font= ("Arial", 18), background = hintergrundFarbe, foreground = buttonFarbe) #Titel
label.pack(padx=20, pady=20) #Verschiebung der Überschrift

#Button zur Dateieingabe 
button = tk.Button(root, text = "Wählen Sie bitte eine Excel-Datei aus!", font = ('Arial', 12), bg = buttonFarbe, fg = schriftFarbe, command = open_it)
button.pack(pady = 230)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

# Starten des Tkinter Hauptloops
root.mainloop()
