# Coding Basics

Dieses Tutorial vermittelt den Einstieg in Grundstrukturen von Programmierung. Es startet mit der grafischen Programmiersprache Scratch und schafft den Übergang zu Python - der Sprache, die an US-Schulen am häufigsten für Einsteiger:innen gelehrt wird. Ein weiterer Vorteil an Python ist, dass es eine große Community gibt, die Python für Data Science (Aufbereitung und Analyse und Visualisierung von Daten) nutzt. Entsprechend nützlich ist Python für Datenjournalist:innen.

## Vorab: Einstieg mit Scratch

Als Vorbereitung auf die Programmiertage spielt euch bitte durch "Programmieren mit der Maus": Von "00 Hallo Welt" bis "06 Listen und Variablen".
https://programmieren.wdrmaus.de/

Falls ihr irgendwo stecken bleibt oder Fragen habt, könnt ihr euch gegenseitig helfen. Das ist für den Programmierteil wirklich wichtig. Ich frag das ab :). Wie schnell das geht, ist sehr individuell ihr solltet zwischen einer und vier Stunden dafür einplanen.

## Installationsparty

Das ist der Teil für den Einsteiger:innen meistens Hilfe brauchen. Deshalb ist es am besten, wenn man das mit jemandem zusammen macht, der schon ein wenig Erfahrung hat.

### Grundlagen vorbereiten (Python, Code Editor, Git/Github)

Wir folgen einigen Schritten (aber nicht allen) aus dem Django Girls Tutorial:
https://tutorial.djangogirls.org/en/installation/
Diese Schritte in der Anleitung installieren grundlegende Dinge auf eurem Rechner, die ihr fürs Programmieren mit Python braucht:

- Open command line (Wie öffne ich die Kommandozeile?)
- Install Python (Installiert Python)
- Install VS Code (Installiert einen Programm, mit dem ihr Python-Dateien bearbeiten werdet)
- Install GIT (Installiert ein Programm, um den aktuellen Stand eurer Programmie abzuspeichern, um zurück gehen zu können, falls mal etwas schief läuft.)
- Create a Github account (Legt einen kostenlosen Account bei Github an, das ist eine Plattform, um Code zu veröffentlichen und gemeinsam mit anderen an einem Programm zu arbeiten.)

### Datenjournalismus-Tools vorbereiten

Für den Teil 'Datenjournalismus - bearbeiten von Daten mit Python und Pandas" führt ihr bitte noch diese Schritte aus:

#### 1. Repo clonen (Einen Ordner aus dem Internet auf deinen Computer herunterladen)

Du öffnest auf deinem Computer ein Terminal. Stelle sicher, dass du an einer Stelle bist, an der du einen Ordner anlegen willst, zum Beispiel auf dem Desktop.
Gib das hier in dein Terminal ein:

`$ git clone https://github.com/P3nny/pfv.git`

Dieser Befehl lädt die Dateien, die wir für den Daten-Tag brauchen, von Github in ein neues Verzeichnis herunter.

### 2. In das Verzeichnis wechseln

Wechsele in deinem Terminal in das neue Verzeichnis:

`$ cd pfv`

### 3. Virtuelles Environment aufsetzen

In deinem neuem Verzeichnis legst du bitte ein neues virtuelles Environment an, das nennst du `myvenv`:

- MacOS/Linux: `$ python3 -m venv myvenv`
- Windows: `> python -m venv myvenv`

### 4. Virtuelles Environment aktivieren

Dann aktivierst du das virtual Environment:

- MacOS/Linux: `$ source myvenv/bin/activate`
- Windows (git bash): `$ ./myvenv/Scripts/activate`
- Windows (Powershell): `> myvenv\Scripts\Activate.ps1`
- Windows (CMD/Eingabeaufforderung): `> myvenv\Scripts\activate.bat`

### 5. Benötigte Pakete installieren

Mit diesen Befehlen installierst du benötigte Python-Pakete auf deinem Rechner:

`$ pip install jupyterlab`
`$ pip install pandas`
`$ pip install matplotlib`
`$ pip install openpyxl`
`$ pip install xlrd`
`$ pip install plotnine`

### 6. Jupyter lab starten

Wenn das Installieren geklappt hat, kannst du jetzt `jupyter lab` starten:

`$ jupyter lab`

### 7. Das erste Notebook öffnen

Es öffnet sich ein Browserfenster, Du siehst links eine Dateistruktur. Da klickst du bitte auf:

**01_jupyter_lab.ipynb**

Dann geht es in deinem Browser weiter. Das Terminal bitte offen lassen, denn dort läuft dein lokaler Server für das `Jupyter Lab`.
