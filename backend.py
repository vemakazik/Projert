# Artem
import os  # Importiert das Modul für den Umgang mit Dateisystemen
from matplotlib.figure import Figure  # Importiert das Modul für das Erstellen von Diagrammen
from typing import Optional  # Ermöglicht die Angabe optionaler Typen in Funktionen

from src.data_export import insert_content, create_report_template  # Importiert Funktionen für den Export und die Berichtserstellung
from src.data_preperation import prepare_data, prepare_plots  # Importiert Funktionen für die Datenvorbereitung und Diagrammerstellung
from src.dataloader import load_data  # Importiert die Funktion zum Laden der Daten


def prepare_report(data_path: Optional[str]):  # Funktion zur Vorbereitung des Berichts
    create_report_template()  # Erstellt eine Vorlage für den Bericht
    unproccessed_data = load_data(data_path)  # Lädt die unprozessierten Daten aus der angegebenen Datei
    proccessed_data = prepare_data(unproccessed_data)  # Verarbeitet die unprozessierten Daten für die Analyse
    figures: list[Figure] = prepare_plots(proccessed_data)  # Bereitet Diagramme basierend auf den verarbeiteten Daten vor

 
    first_week = proccessed_data["Datum"].iloc[0].split("-")[0].strip()  # Extrahiert den Beginn der ersten Woche
    first_week_ending = proccessed_data["Datum"].iloc[0].split("-")[1].strip()  # Extrahiert das Ende der ersten Woche

    
    second_week = proccessed_data["Datum"].iloc[1].strip()  # Extrahiert das Ende der zweiten Woche

    # Extrahiert die Daten für die erste Analyse
    verkaufen = proccessed_data["Anzahl der Verkäufe"].iloc[1]  
    gesamtverkaufe = proccessed_data["Gesamtverkäufe (€)"].iloc[1]  
    kosten = proccessed_data["Kosten (€)"].iloc[1]  
    ertag = proccessed_data["Ertrag (€)"].iloc[1]  
    ruckgaben = proccessed_data["Rückgaben (€)"].iloc[1]  
    beschadigte = proccessed_data["Beschädigte Ware (€)"].iloc[1]  
    gewinn = proccessed_data["Gewinn (€)"].iloc[1]  

  
    first_analysis = f"In dieser Woche konnten wir mit {verkaufen:,} Verkäufen einen Gesamtgewinn von {gesamtverkaufe:,} Euro erzielen.\
 Nach Abzug der Kosten in Höhe von {kosten:,} Euro ergibt sich ein Nettoertrag von {ertag:,} Euro. Berücksichtigt\
 man Rückgaben im Wert von {ruckgaben:,} Euro sowie beschädigte Ware im Wert von {beschadigte:,} Euro, beläuft sich\
 der endgültige Gewinn auf {gewinn:,} Euro."

    
    def get_sign_dependency(value: float) -> str:
        if value > 0:
            return "gestiegen"  
        elif value < 0:
            return "gesunken"  
        else:
            return "unverändert"  

    # Extrahiert die Daten für die zweite Analyse
    Gesamtverkäufe_Prozent_Änderung = proccessed_data["Gesamtverkäufe_Prozent_Änderung"].iloc[1]  
    zeichen_GPÄ = get_sign_dependency(Gesamtverkäufe_Prozent_Änderung)  

    Kosten_Prozent_Änderung = proccessed_data["Kosten_Prozent_Änderung"].iloc[1]  
    zeichen_KPÄ = get_sign_dependency(Kosten_Prozent_Änderung)  # Bestimmt die Veränderungsrichtung der Kosten

    Anzahl_Verkäufe_Prozent_Änderung = proccessed_data["Anzahl_Verkäufe_Prozent_Änderung"].iloc[1]  
    zeichen_AVPÄ = get_sign_dependency(Anzahl_Verkäufe_Prozent_Änderung)  # Bestimmt die Veränderungsrichtung der Verkäufe
    
    Rückgaben_Prozent_Änderung = proccessed_data["Rückgaben_Prozent_Änderung"].iloc[1]  
    zeichen_RPÄ = get_sign_dependency(Rückgaben_Prozent_Änderung)  # Bestimmt die Veränderungsrichtung der Rückgaben

    Beschädigte_Ware_Prozent_Änderung = proccessed_data["Beschädigte_Ware_Prozent_Änderung"].iloc[1]  
    zeichen_BWPÄ = get_sign_dependency(Beschädigte_Ware_Prozent_Änderung)  # Bestimmt die Veränderungsrichtung der beschädigten Waren

   
    second_analysis = f"Im Vergleich zur Woche vom {first_week}-{first_week_ending} ist der Umsatz um {Gesamtverkäufe_Prozent_Änderung}% {zeichen_GPÄ:}.\
 Die Kosten sind um ca. {Kosten_Prozent_Änderung}% {zeichen_KPÄ}, jedoch im Verhältnis zum Umsatz moderater.\
 Die Anzahl der Verkäufe ist um {Anzahl_Verkäufe_Prozent_Änderung}% {zeichen_AVPÄ}, während die Rückgaben um ca. {Rückgaben_Prozent_Änderung}% {zeichen_RPÄ} sind.\
 Gleichzeitig ist der Anteil der beschädigten Ware um {Beschädigte_Ware_Prozent_Änderung}% {zeichen_BWPÄ}."

    # Erstellt ein Dictionary mit den Ergebnissen zur Verwendung im Bericht
    test_dict = {
        "week": f"{second_week}",
        "Wochenbericht": f"{first_analysis}",
        "Vergleich zur vorherigen Woche": f"{second_analysis}",
    }

    insert_content(content_dict=test_dict, image=figures[0])  # Fügt die Inhalte in den Bericht ein, einschließlich des Diagramms
