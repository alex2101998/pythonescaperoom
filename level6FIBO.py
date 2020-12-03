#Levelbeschreibung

"""Mehr als die Hälfte hast du bereits geschafft.
Nun... konzentriere dich jetzt besonders auf deine nächste Aufgabe.
Im Jahre ..... v. Chr. kam Pharao Necho II. nach dem Tod seines Vaters an die Macht.
Wir wollen wissen welches Jahr v. Chr. ist gesucht???
Stelle die FIBONACCI-Folge dar, wiederhole diese aber nur 16 Mal.

Zusatzaufgabe: Lasse den Spieler auswählen, wie er die Fibonacci-Folge darstellen will,
das heißt nebeneinander oder untereinander.

Am Ende werden wir sehen, ob du die korrekte Jahreszahl ermittelt hast."""

#Lösung

anzahl_wiederholungen = 16
ansicht = int(input("Wähle deine Ansicht der Darstellung:\n\n1: untereinander\n2: nebeneinander\n\nDeine Wahl: "))
 
 
i = 0
folge = [0,1]
 
#Berechnung der FIBONACCI-Folge
while (i < anzahl_wiederholungen):
    fibo = folge[i]+folge[i+1]
    folge.append(fibo)
    i += 1
 
#Darstellung der Ausgabe untereinander
if(ansicht == 1):
    j = 0
    while (j < anzahl_wiederholungen):
        print(folge[j]) 
        j += 1

#Darstellung der Ausgabe hintereinander
elif(ansicht == 2):
    print(folge [1:16])

#Jahreszahl überprüfen
letzterWert = int(input("Gibt den Wert der letzten Zahl in der Liste ein:"))
if (letzterWert == 610):
    print ("WELL DONE - Level geschafft")
else:print ("Try again")
