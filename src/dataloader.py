from typing import Optional  # Ermöglicht die Verwendung von optionalen Typen in Funktionen

import pandas as pd  # Importiert die pandas-Bibliothek für die Datenverarbeitung
from loguru import logger  # Importiert das Log-Modul für das Protokollieren von Nachrichten

def load_data(
    data_path: Optional[str] = "./testdaten/testdaten-excel.xlsx",  # Pfad zur Excel-Datei (Standardpfad)
) -> pd.DataFrame | None:  # Funktion gibt ein DataFrame zurück oder None, wenn ein Fehler auftritt
    # Definiert die benötigten Spalten für die Berichtserstellung
    df_entries = [
        "Woche",  
        "Datum",  
        "Gesamtverkäufe (€)",  
        "Kosten (€)",  
        "Anzahl der Verkäufe",  
        "Rückgaben (€)",  
        "Beschädigte Ware (€)",  
        "Ertrag (€)",  
        "Gewinn (€)"  
    ]

    # Liest die Excel-Datei und gibt sie als DataFrame zurück
    df = pd.read_excel(data_path)  # Lädt die Excel-Datei in ein DataFrame

    if len(df) == 0:  # Überprüft, ob das DataFrame leer ist
        logger.critical("No data found or empty excel file")  # Protokolliert einen kritischen Fehler
        return None  # Gibt None zurück, wenn keine Daten gefunden werden

    # Überprüft, ob alle erforderlichen Spalten vorhanden sind
    missing_columns = [col for col in df_entries if col not in df.columns]  # Listet fehlende Spalten auf
    if missing_columns:  # Wenn Spalten fehlen
        raise ValueError(f"Missing required columns: {missing_columns}")  # Wirft einen Fehler

    # Wählt nur die benötigten Spalten aus, andere werden ignoriert
    df = df[df_entries]  # Reduziert das DataFrame auf die erforderlichen Spalten

    # Sucht nach Zeilen mit fehlenden Werten
    rows_with_na = df[df.isna().any(axis=1)]  # Findet Zeilen mit NaN-Werten
    if not rows_with_na.empty:  # Wenn Zeilen mit fehlenden Werten gefunden werden
        logger.warning(
            f"Found rows with missing values for dates: {rows_with_na['Datum'].tolist()}"  # Protokolliert eine Warnung
        )

    return df  # Gibt das DataFrame zurück
