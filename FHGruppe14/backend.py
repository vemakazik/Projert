
#Artem
import os
from matplotlib.figure import Figure
from typing import Optional

from src.data_export import insert_content, create_report_template
from src.data_preperation import prepare_data, prepare_plots
from src.dataloader import load_data


def prepare_report(data_path: Optional[str]):
    #TODO: data_export()
    create_report_template()
    unproccessed_data = load_data(data_path)
    proccessed_data = prepare_data(unproccessed_data)
    figures: list[Figure] = prepare_plots(proccessed_data) 

    # Extract the first week (start date of the first week)
    first_week = proccessed_data["Datum"].iloc[0].split("-")[0].strip()
    first_week_ending = proccessed_data["Datum"].iloc[0].split("-")[1].strip()

    # Extract the second week (end date of the second week)
    second_week = proccessed_data["Datum"].iloc[1].strip()  # Get the end date of the second week

    # Extract the datafor the first_analysis
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

    # Extract the data for the second_analysis
    Gesamtverkäufe_Prozent_Änderung = proccessed_data["Gesamtverkäufe_Prozent_Änderung"].iloc[1]
    zeichen_GPÄ = get_sign_dependency(Gesamtverkäufe_Prozent_Änderung)

    Kosten_Prozent_Änderung = proccessed_data["Kosten_Prozent_Änderung"].iloc[1]
    zeichen_KPÄ = get_sign_dependency(Kosten_Prozent_Änderung)

    Anzahl_Verkäufe_Prozent_Änderung = proccessed_data["Anzahl_Verkäufe_Prozent_Änderung"].iloc[1]
    zeichen_AVPÄ = get_sign_dependency( Anzahl_Verkäufe_Prozent_Änderung)
    
    Rückgaben_Prozent_Änderung = proccessed_data["Rückgaben_Prozent_Änderung"].iloc[1]
    zeichen_RPÄ = get_sign_dependency(Rückgaben_Prozent_Änderung)

    Beschädigte_Ware_Prozent_Änderung = proccessed_data["Beschädigte_Ware_Prozent_Änderung"].iloc[1]
    zeichen_BWPÄ = get_sign_dependency(Beschädigte_Ware_Prozent_Änderung)

    second_analysis = f"Im Vergleich zur Woche vom {first_week}-{first_week_ending} ist der Umsatz um {Gesamtverkäufe_Prozent_Änderung}% {zeichen_GPÄ:}.\
Die Kosten sind um ca. {Kosten_Prozent_Änderung}% {zeichen_KPÄ}, jedoch im Verhältnis zum Umsatz moderater.\
Die Anzahl der Verkäufe hat sich um {Anzahl_Verkäufe_Prozent_Änderung}% {zeichen_AVPÄ}, während die Rückgaben um ca. {Rückgaben_Prozent_Änderung}% {zeichen_RPÄ} sind.\
Gleichzeitig ist der Anteil der beschädigten Ware um {Beschädigte_Ware_Prozent_Änderung}% {zeichen_BWPÄ}."
    

    test_dict = {
        "week": f"{second_week}",
        "Wochenbericht": f"{first_analysis}",
        "Vergleich zur vorherigen Woche": f"{second_analysis}",
    }

    insert_content(content_dict=test_dict, image=figures[0])