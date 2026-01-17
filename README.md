# Kontaktbuch

Eine Python-Anwendung zur Verwaltung von Kontakten mit persistenter Datenspeicherung.

## Features

- Kontakte hinzufügen (Name, Telefon, E-Mail)
- Alle Kontakte anzeigen
- Kontakte nach Namen suchen
- Kontakte löschen
- Automatisches Speichern in Textdatei

## Verwendung

```bash
python kontaktbuch.py
```

## Menüoptionen

```
=== Kontaktbuch ===

1. Kontakt hinzufügen
2. Alle Kontakte anzeigen
3. Kontakt suchen
4. Kontakt löschen
5. Beenden
```

## Datenspeicherung

Kontakte werden in `kontaktbuch.txt` gespeichert im Format:

```
Name: Max Mustermann
Telefon: 0123456789
Email: max@beispiel.de
```

## Technologien

- Python 3
- Dateioperationen (lesen/schreiben)
- Listen und Dictionaries

## Lernziele

- CRUD-Operationen (Create, Read, Update, Delete)
- Persistente Datenspeicherung
- Menügesteuerte Benutzerführung
- String-Manipulation und Parsing
