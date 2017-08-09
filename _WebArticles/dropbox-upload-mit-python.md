# Dropbox-Upload mit Python

_Captured: 2017-05-06 at 16:30 from [pi-buch.info](https://pi-buch.info/dropbox-upload-mit-python/)_

Dieser Beitrag zeigt, wie Sie mit einem kleinen Python-Script Dateien vom Raspberry Pi in Ihr Dropbox-Konto hochladen. Da der in der ersten Auflage unseres Buchs beschriebene Python-Dropbox-Uploader nicht mehr funktioniert, erklaren wir Ihnen hier die Verwendung der offiziellen Dropbox-API.

**VORSICHT: Dieser Artikel beschreibt eine Vorgehensweise auf Basis der Dropbox API v1. Diese API-Version wird ab 28.6.2017 nicht mehr funktionieren. Alle Dropbox-Programme mussen dann die neue API v2 nutzen. Hier ist [eine aktualisierte Fassung dieses Artikels](https://pi-buch.info/dropbox-upload-mit-python-api-v2/)!**

### Dropbox-App einrichten

Die Grundvoraussetzung besteht naturlich einmal darin, dass Sie uber ein eigenes Dropbox-Konto verfugen. Auf den Dropbox-Developer-Seiten richten Sie in der sogenannten »App Console« eine neue Dropbox-App ein:

<https://www.dropbox.com/developers/apps>

Fur dieses Beispiel haben wir der App den Namen _rapi-uploader_ gegeben. **Sie mussen als App-Namen einen im Dropbox-Universum eindeutigen Namen verwenden! Wenn Ihnen nichts besseres einfallt, versuchen Sie es mit einer Kombination aus Ihrem Namen vorname-nachname-test123.**

Beim Einrichten den App haben Sie die Wahl zwischen zwei Zugriffsvarianten (_access type_):

  * App folder: die App hat nur den Zugriff auf ein Verzeichnis, das gleichlautend wie der App-Name ist
  * Full dropbox: die App hat Zugriff auf alle ihre Dropbox-Daten

In der Einstellungsseite dieser App finden Sie nun den Button _Generate_, um einen App-spezifischen Code (ein _Token_) zu generieren.

![Dropbox-App einrichten](https://pi-buch.info/wp-content/uploads/2015/05/python-dropbox1-500x418.png)

> _Dropbox-App einrichten_

### Dropbox-Funktionen installieren

Fur Python-Funktionen zur Kommunikation mit Dropbox befinden sich in einem Erweiterungspaket, das sich am einfachsten mit `pip` installieren lasst. Der Kommandoname `pip` steht fur _Pip Installs Python_ und ist eine eigenes Paketverwaltungssystem fur Python.
    
    
    sudo apt-get install python3-pip
    sudo pip-3.2 install dropbox
    

### Erste Tests

Mit dem zuvor generierten Token konnen wir nun testen, ob der Verbindungsaufbau  
zu Dropbox gelingt. Das folgende Mini-Script sollte Informationen uber Ihren  
Dropbox-Account liefern:
    
    
    #!/usr/bin/python3
    import dropbox
    dbc = dropbox.client.DropboxClient('xxx-token-code-xxx')
    print('linked account: ', dbc.account_info())
    

Klappt soweit alles, ist es Zeit fur den ersten Upload. Die folgenden Zeilen laden die Datei `test.jpg` aus dem lokalen Verzeichnis in das Root-Verzeichnis Ihres Dropbox-Kontos hoch:
    
    
    #!/usr/bin/python3
    # Datei dropbox-upload.py
    import dropbox
    dbc = dropbox.client.DropboxClient('xxx-token-code-xxx')
    fname = 'test.jpg'
    f = open(fname, 'rb')              # Datei öffnen,
    response = dbc.put_file(fname, f)  # ... hochladen
    print('uploaded:', response)
    f.close()                          # ... und schließen
    

### Foto mit Datum- und Zeitinfos hochladen

Ein wenig praxisnaher ist das zweite Beispiel: Es erstellt zuerst ein Foto und ladt dieses dann in das Dropbox-Verzeichnis hoch. Der Dateiname des Fotos unter Dropbox setzt sich aus `Rapi-` und dem Datum zusammen, z.B. `Rapi-2015-06-30.jpg`.
    
    
    #!/usr/bin/python3
    # Datei dropbox-foto.py
    import datetime, dropbox, picamera
    dbc = dropbox.client.DropboxClient('xxx-token-code-xxx')
    
    # Foto erstellen und lokal speichern
    localname = 'tmp.jpg'
    camera = picamera.PiCamera()
    camera.resolution=(1280, 960)
    camera.capture(localname)
    camera.close()
    
    # Foto hochladen
    f = open(localname, 'rb')
    today = datetime.date.today()
    upname = today.strftime('Rapi-%Y-%m-%d.jpg')
    dbc.put_file(upname, f)
    f.close()
    

### Allgemeingultige Dropbox-Authentifizierung

Wir sind hier davon ausgegangen, dass Ihr Script nur mit Ihrem eigenen Dropbox-Konto kommunizieren mochte. Ganz anders ist die Ausgangslage, wenn Sie ein Script zur Weitergabe an andere Benutzer entwickeln, die jeweils ihre eigenen Dropbox-Konten verwenden mochten.

In diesem Fall mussen Sie im Script Code vorsehen, der dem Benutzer die Moglichkeit gibt, den jeweiligen Dropbox-Zugriff zu authentifizieren. Der Benutzer wird dabei auf eine Seite von Dropbox geleitet, muss dort sein Dropbox-Passwort angeben und erhalt dann einen speziellen Code fur das Script. Ihr Script bittet um die Eingabe dieses Codes und speichert ihn so, dass es spater wieder darauf zugreifen kann. Mehr Details konnen Sie hier nachlesen:

<https://stackoverflow.com/questions/23894221>  
<https://www.dropbox.com/developers/core/docs/python>
