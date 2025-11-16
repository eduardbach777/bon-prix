# Produktfilter für E-Commerce

Ein Produktfilter-System, das ich als Übungsprojekt entwickelt habe. Die Idee war, grundlegende E-Commerce-Funktionen nachzubauen.

## Was macht das Projekt?

Das Programm kann Produkte filtern und durchsuchen:
- Suche nach Produktname oder Kategorie
- Filter nach Größe, Farbe und Preisbereich
- Sortierung nach Preis oder Beliebtheit
- Funktioniert als Command-Line Tool oder als Webseite

## Wie starte ich es?

**Terminal-Version:**
```bash
python bonprix_product_filter.py
```

**Web-Version:**
```bash
pip install flask
python app.py
```
Dann im Browser: http://localhost:8080

## Technisches

- Python 3
- Flask (für die Web-Version)
- HTML/CSS für die Oberfläche
- Verwendet Mock-Daten statt Datenbank

## Ordnerstruktur
```
├── bonprix_product_filter.py    # Terminal-Version
├── app.py                        # Flask Web-App
├── templates/
│   └── index.html               
├── requirements.txt
└── README.md
```

## Was ich dabei gelernt habe

- List Comprehensions zum Filtern von Listen
- Flask Basics (Routing, Templates, Forms)
- HTML-Formulare und GET-Parameter
- Unterschied zwischen Mock-Daten und Datenbanken

Das Projekt benutzt absichtlich keine Datenbank, damit die Logik im Vordergrund steht. Später könnte man SQL integrieren.

## Mögliche Verbesserungen

- Datenbank statt Mock-Daten
- Mehr Produkte hinzufügen
- Warenkorb-Funktion
- Pagination für viele Ergebnisse
- Unit Tests schreiben

## Notizen

Die Produktdaten sind aktuell hardcoded im Code. In einer echten Anwendung würde das natürlich aus einer Datenbank kommen. Das Projekt ist hauptsächlich zum Lernen gedacht.Ich habe noch keine praktischen Erfahrungen gemacht mit SQL in diesem Sinne, würde mich aber natürlich freuen dieses später in meinen Techstack aufzunehem und zu lernen.

Größten hilfen beim Projekt waren YouTube Tutorials und natürlich StackOverflow.

grüßis