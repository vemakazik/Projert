import matplotlib.pyplot as plt  # Importiert das Modul zum Erstellen von Grafiken
import pandas as pd  # Importiert die pandas-Bibliothek für die Datenverarbeitung
from matplotlib.figure import Figure  # Importiert die Klasse für die Erstellung von Diagrammfiguren


def prepare_data(data: pd.DataFrame) -> pd.DataFrame:  # Funktion zur Vorbereitung der Daten
    # Bereitet die Daten für die Woche-Differenz vor
    data["Woche"] = data["Woche"].astype(str)  # Konvertiert die Woche in einen String
    data["Datum_parsed"] = data["Datum"].apply(  # Wandelt das Datum in das Datetime-Format um
        lambda x: pd.to_datetime(
            x.replace(" ", "").split("-")[0].strip(), format="%d.%m.%Y"  # Entfernt Leerzeichen und konvertiert das Datum
        )
    )
    # Berechnet die Differenz in Wochen
    data["Wochen_Differenz"] = (
        data["Datum_parsed"] - data["Datum_parsed"].shift(1)  # Berechnet die Differenz zu der vorherigen Woche
    ).dt.days / 7  # Konvertiert die Differenz in Wochen

    # Berechnet die prozentuale Veränderung im Vergleich zur Vorwoche
    data["Ertrag_Prozent_Änderung"] = round(data["Ertrag (€)"].pct_change() * 100, 2)  
    data["Gewinn_Prozent_Änderung"] = round(data["Gewinn (€)"].pct_change() * 100, 2)  
    data["Gesamtverkäufe_Prozent_Änderung"] = round(data["Gesamtverkäufe (€)"].pct_change() * 100, 2)  
    
    data["Kosten_Prozent_Änderung"] = round(data["Kosten (€)"].pct_change() * 100, 2)  
    data["Anzahl_Verkäufe_Prozent_Änderung"] = round(data["Anzahl der Verkäufe"].pct_change() * 100, 2)  
    
    data["Rückgaben_Prozent_Änderung"] = round(data["Rückgaben (€)"].pct_change() * 100, 2)  
    data["Beschädigte_Ware_Prozent_Änderung"] = round(data["Beschädigte Ware (€)"].pct_change() * 100, 2)  

    return data  # Gibt das bearbeitete DataFrame zurück


def prepare_plots(data: pd.DataFrame) -> list[Figure]:  # Funktion zur Erstellung von Diagrammen
    figures = []  # Liste zur Speicherung der erstellten Figuren

    # Schließt alle bestehenden Figuren, um Speicherprobleme zu vermeiden
    plt.close("all")

    # Verarbeitet jede Woche, außer der ersten
    for i in range(1, len(data)):  # Iteriert über die Zeilen, beginnend mit der zweiten Woche
        current_week = data.iloc[i]  # Aktuelle Woche
        previous_week = data.iloc[i - 1]  # Vorherige Woche

        fig, ax = plt.subplots(figsize=(12, 8))  # Erstellt ein neues Diagramm
        ax.grid(True, linestyle="--", alpha=0.7, axis="y")  # Fügt ein Gitter für die y-Achse hinzu

        # Setzt die Positionen der Balken
        labels = [
            "Gesamtverkäufe (€)",  
            "Kosten (€)",  
            "Ertrag (€)",  
            "Gewinn (€)",  
            "Anzahl der Verkäufe",  
            "Rückgaben (€)",  
            "Beschädigte Ware (€)",  
        ]
        x = range(len(labels))  # Definiert die Positionen auf der x-Achse
        bar_width = 0.35  # Setzt die Breite der Balken

        # Zeichnet Balken für die aktuelle und die vorherige Woche
        for j, label in enumerate(labels):  # Iteriert über die Spalten
            ax.bar(
                j - bar_width / 2,
                previous_week[label],  # Balken für die vorherige Woche
                bar_width,
                label=f"{label} (Vorherige Woche)" if i == 1 else "",  # Label nur in der ersten Iteration
                edgecolor="black",  # Schwarze Ränder für die Balken
                linewidth=1,  # Linienbreite der Balkenränder
            )
            ax.bar(
                j + bar_width / 2,
                current_week[label],  # Balken für die aktuelle Woche
                bar_width,
                label=f"{label} (Aktuelle Woche)" if i == 1 else "",  # Label nur in der ersten Iteration
                edgecolor="black",  # Schwarze Ränder für die Balken
                linewidth=1,  # Linienbreite der Balkenränder
            )

        # Fügt Titel und Achsenbeschriftungen hinzu
        ax.set_title(
            f'Woche {current_week["Woche"]}\n'  # Titel mit der Woche
            # f'Ertrag Änderung: {current_week["Ertrag_Prozent_Änderung"]:.1f}%\n'  # Ertrag-Änderung (auskommentiert)
            # f'Gewinn Änderung: {current_week["Gewinn_Prozent_Änderung"]:.1f}%'  # Gewinn-Änderung (auskommentiert)
        )

        ax.set_ylabel("Betrag (€)")  # Y-Achsen-Beschriftung
        ax.set_xticks(x)  # Setzt die x-Achsen-Ticks
        ax.set_xticklabels(labels, rotation=45, ha="right")  # Setzt die Labels auf der x-Achse und dreht sie

        # Fügt Werte auf den Balken hinzu
        for idx, week in enumerate([previous_week, current_week]):  # Iteriert über die Wochen
            for j, label in enumerate(labels):  # Iteriert über die Labels
                ax.text(
                    j - bar_width / 2 if idx % 2 == 0 else j + bar_width / 2,  # Position des Textes
                    week[label],  # Position des Werts
                    f"{week[label]:,.2f}€",  # Formatierte Darstellung des Werts
                    ha="center",  # Horizontal ausrichten
                    va="bottom",  # Vertikal ausrichten
                )

        # Fügt eine Legende hinzu und entfernt doppelte Labels
        handles, labels = ax.get_legend_handles_labels()  # Holt die Legenden-Handles und Labels
        by_label = dict(zip(labels, handles))  # Entfernt doppelte Labels
        ax.legend(by_label.values(), by_label.keys())  # Fügt die Legende hinzu

        plt.tight_layout()  # Sorgt dafür, dass das Layout der Grafik gut aussieht
        figures.append(fig)  # Fügt die Figur zur Liste hinzu

    return figures  # Gibt die Liste der Figuren zurück
