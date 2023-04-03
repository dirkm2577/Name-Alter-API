## Name-Alter-API - eine kurze Anwendung zur Eingabe und Darstellung von Nutzerdaten

### Aufgabe

Die Aufgabenstellung war folgende:

*Du entwickelst eine einfache Webanwendung, mit Frontend (Vue3.js) und Backend (Python), die über eine Schnittstelle (REST-API) miteinander kommunizieren. Das Frontend soll eine Form mit zwei Textfeldern (Name und Geburtsdatum) enthalten und einen Bestätigungsbutton, über das man die Eingaben bestätigt. Nach der Bestätigung werden die eingegebenen Daten an das Backend gesendet und dort wird aus dem Geburtsdatum das Alter berechnet und an das Frontend zurückgegeben. Das Frontend fügt den Namen und das Alter in eine neue Zeile in einer Tabelle ein.*

*Das Frontend sollte benutzerfreundlich gestaltet werden.*

*Verwende für die API-Spezifikation bitte das Tool Swagger, das für dich die Controller und Models für Backend (Flask/Python) und Frontend (Typescript oder Javascript) generiert. Hier findest du eine Dokumentation darüber: https://swagger.io/docs/specification/about/*

*Bitte so umsetzen, wie du es in einem professionellen Umfeld machen würdest, also mit Kommentaren und Berücksichtigung von Naming Conventions und benutzerfreundlicher UI etc.*

### Starten der Anwendung

Da ich die Anwendung in einem Python Virtual Environment entwickelt habe und keine Produktionsversion, sind folgende Schritte notwendig, um die Anwendung zu starten:

1. Im CLI in den Ordner 'Name-Alter-API' wechseln.
2. Mit dem Befehl `source myenv/bin/activate` die virtuelle Umgebung starten
3. Mit dem Befehl `python app.py` den Flask-Server starten (localhost:5000)
4. Ein neues Terminal-Fenster öffnen.
5. Dort auch die virtuelle Umgebung starten mit `source myenv/bin/activate`.
6. In den Unterordner 'user-frontend' wechseln.
7. Dann mit dem Befehl `npm run serve` den Web Server starten. (localhost:8080)
8. Nun in Chrome den localhost:8080 aufrufen, um die Anwendung anzuzeigen.
9. Um die virtuelle Umgebung zu verlassen, bitte den Befehl `deactivate`eingeben.
