#Levelbeschreibung

'''Gratuliere, du hast Level 1 erfolgreich gelöst.
Das nächste Level wird anspruchsvoller und du musst folgende Aufgabe lösen.
Generiere eine Zufallszahl zwischen 2 und 100.
Programmiere mittels While-Schleifen die Primzahlen von 2 bis dem Wert deiner Zufallszahl.'''


#Lösung

from random import *

r = randint(1, 100)    # Pick a random number between 1 and 100.
i =2


while (i<r):
	p=2
	while (p<= (i/p)):
		if not (i%p): break
		p=p+1
	if (p> (i/p)): print (i)
	i=i+1

	

