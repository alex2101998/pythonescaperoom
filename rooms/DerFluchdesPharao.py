from EscapeRoom import EscapeRoom
from random import randint
from os import *
import random


class DerFluchdesPharao(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Alex, Isi, Jessi, Laura", __name__)
        self.add_level(self.create_level4())
        self.add_level(self.create_level3())
        self.add_level(self.create_level7())
        self.add_level(self.create_level8())

    ### LEVELS ###
    #Level 3 Jessi#
    def create_level3(self):

        mythos = ["Kleopatra liess ihren Mann ermorden,kurz bevor ihre Ehe annulliert werden sollte, um gemeinsam mit Ihrem Sohn an die Macht zu kommen!.", 
        "Man sagt, dass Hieroglyphen soviel wie in Stein gemeißelt heisst. Die Zeichen wurden sogar vielfach farbig geschrieben und sind immer eine Bildreihe!", 
        "Nicht nur Pharaonen hatten damals so viel Macht, auch Lokalkönige waren sehr mächtig. So waren sie zuständig für all die Kleinstaaten! Beide Arten von Regenten waren allerdings sehr streng beim Aussieben von Sand!",
        "Die goettliche Legitimation beginnt mit der rituellen Aktivierung der Göttlichkeit. Das ist etwa vergleichbar mit einer Routineuntersuchung!" ,
        "Vorgänger der fünfkantigen Pyramide ist ein Mstabas, ein einstufiger und flacher Bau. Auch sie hatten bereits Kammern, die tief ins Erdreich verlagert wurden." ,
        "Pyramiden dienen als Begräbnisstätten, deren Steine sind aus Kalkstein. Die Bauwerke haben unter anderem Stollen die von Schächten abzweigen. Es gibt eine Pyramide, die während der Bauzeit fünfmal erweitert wurde! Die meisten Pyramiden sind viereckig ",
        "Cheops, der boese Pharao, zwang alle Untertanen seines Reviers beim Pyramidenbau zu helfen."  ]

        myth = random.choice(mythos)

        if myth == mythos[0]:
            zahl = 3
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"
        elif myth == mythos[1]:
            zahl = 2
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"
        elif myth == mythos[2]:
            zahl = 3
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"
        elif myth == mythos[3]:
            zahl = 2
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"
        elif myth == mythos[4]:
            zahl = 3
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"
        elif myth == mythos[5]:
            zahl = 3
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"
        else: 
            zahl = 2
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"

        

        zahl_in_worten = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf"]
        code = [0,1,2,3,4,5,6,7,8,9,10,11]
                
        task_messages = [ "Juhuu, du hast den Schlüssel für die nächste Tür gefunden! Los, öffne sie und schau, was dich dahinter erwaret!",
            "<br></br>",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Toroffe.jpg' width='280' height='210'>",
            "<br></br>",
            "Du betrittst einen großen Raum, mitten drin steht ein Sarkopharg! OMG!!!",
            "Du schaust dich im Raum um und entdeckst ein Gekritzel an der Wand rechts",
            "<h2><i> Kleopatra´s Mythenspiel</i></h2>",
            "<b>"+myth+"</b>",
            "<br></br>",
            "<i>Wenn Kleopatra Mythen erzählt, sie es immer <b>wörtlich</b> meint! Aber nimm dich in Acht, von klein nach groß, von unten nach oben, hast du das bedacht? </i>",
            "<br></br>",
            "Was hat denn das nun wieder zu bedeuten?",
            "<br></br>",
            schriftrolle_zu,
            "Du drehst dich im Raum und siehst dich um, am Sarkophag findest eine Schriftrolle und ein Schloss mit " + str(zahl) + " Drehscheiben!",
            schriftrolle_offen
            ]
        hints = [
            "1. Wenn du einen Mythos gefunden hast, dann lies ihn genau durch. Ganz genau.",
            "2. Nimm´s wörtlich.",
            "3. In jedem Mythos steckt mindestens eine Zahl. Vielleicht auch mehr",
            "4. Öffne die Schriftrolle! Darin ist ein Hinweis für zwei Listen enthalten",
            "5. Eine Liste besteht aus Strings, die andere aus Int",
            "6. Verwende liste1 = ['null',.....,'elf'], liste2 = [0,...,11]",
            "7. Schreibe ein Programm das anhand der Listen die du ermittelt hast, übereinstimmende Zahlen aus dem Mythos ausgibt"
            
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.mythos, "data": myth}
    

    def create_level4(self):
        task_messages = ["Auswerten einer CSV Datei"]

        hints = []

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv4, "data": data} 

    #Level 7 Jess #
    def create_level7(self):

        bauplan = [
        "                /\ ",
        "               /][\ ",
        "              /[][[\ ",
        "             /[][]T[\ ",
        "            /[][][]U[\ ",
        "           /[][][]T[][\ ", 
        "          /[][][]A[][][\ ", 
        "         /[][][]N[][][][\ ", 
        "        /[][][][]C[][][][\ ",
        "       /[][]H[][][][][][][\ ", 
        "      /[]A[][][][][][][][][\ ", 
        "     /[][][]M[][][][][][][][\ ", 
        "    /[]U[][][][][][][][][][][\ ", 
        "   /[][][][][][][][]N[][][][][\ "]

        rohbau =[]
        for i in range(len(bauplan)):
            reihe = random.choice(bauplan)
            rohbau.append(reihe)
            bauplan.remove(reihe)
                
        task_messages = [ "<h2>Willkommen in der Kammer des <i>Greywolf!</h2></i>",
            "Während du dich im Raum umschaust entdeckst du zwei Zeichnungen an einer Säule und an der Wand",
            "<br></br>",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Bauplan.jpg' width='1500' height='1000'>",
            "<br></br>",
            "Auf dem Boden liegt ein zerknüllter Zettel","<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/pyramide.txt'target ='_blank'><b><i>Bitte heb mich auf</i></b> </a>",
            "<br></br>",
            "Du entknüllst den Zettel und siehst eine seltsame Zeichnung, sind da etwa Buchstaben eingraviert?!",
            "Auf der Rückseite siehst du folgednes Gekritzel : <a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/erklaerung.txt'target ='_blank'><b>Rückseite!</b> </a>",
            "<br></br>",
            "Du siehst zwei Türen, eine ist mit 3 Schlössern gesichert, <i> na toll </i> die zweite ist Spalt geöffnet, vorsichtig schaust du, was sich hinter der Tür verbirgt ",
            "Es scheint eine Art Schatzkammer zu sein, sind hier drin vielleicht die Schlüssel für die andere Tür versteckt?",
            "<br></br>",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Schatzkammer.jpg' width='1500' height='1000'>",
            "<br></br>",
            "Es scheint, als müsstest du gleich 3 Rätsel lösen um diesem Raum zu entkommen!",
            "<br></br>",
            "Du gehst wieder in den großen Raum und fängst an dich nach Hinweisen umzusehen!",
            "<br></br>",
            "An einer Wand steht:" + "<i>Schau dich um! Du darfst alles verwenden was du hier findest!",
            "<br></br>",
            "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/DasBildvomSarg.txt'target ='_blank'><b>Ich könnte nützlich sein!</b> </a>",
            "<br></br>",
            "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Tal%20der%20Koenige.jpg'target ='_blank'><b>Ich könnte auch nützlich sein!</b> </a>"
            
            ]
        hints = [
            "Auf dem zerknüllten Papier ist ein Bauplan zu sehen, leider ist etwas durcheinander geraten.",
            "Der Bauplan ist für eine Pyramide! Versuche ihn zu sortieren!",
            "Jede Reihe hat eine aufsteigende Anzahl von [], das sollte hilfreich sein!",
            "Wenn du erfolgreich sortiert hast, solltest du ein Wort erkennen können!",
            "Leider ist mit dem Wort noch nicht Schluss, beachte die zweite Zeichnung an der Wand!",
            "Du solltest ein Lösungswort mit 11 Stellen erhalten haben",
            "Lies von oben nach unten, es ist ein bekannter Pharao! Dessen Sarg haben wir heute schon Mal gesehen!",
            "Die erste Lösung ist TUTANCHAMUN!",
            "Die zweite ergibt nur 3 Stellen. Siehst du die Rechenoperatoren an der Wand?",
            "Du sollst alle Buchstaben umwandeln in deren ASCII Code, danach alle zusammen rechnen. Voilá eine 3 stellige Zahl!",
            "Jetzt reicht es aber mit Hinweisen! 840 Herrje! Was für eine schwache Rätselleistung Meister!",
            "Die dritte Lösung musst du suchen, nimm die Handnotiz als Hilfe!",
            "Rechne jeden einzelnen Buchstaben um und rechne alle Ergebnisse zusammen!",
            "Jetzt reicht es aber mit Hinweisen! 840 Herrje! Was für eine schwache Rätselleistung Meister!",
            "Hast du das Geheimnis schon gefunden? Es hieß doch, du darfst alles verwenden! Hast du dir auch alles angeschaut? Die Datei, die nützlich erschien, ist es definitiv! Du musst nur hinschauen!",
            "Hast du weit genug nach oben geschaut? Also ganz nach oben.",
            "Das Geheimnis ist, wo die Grabstätte gefunden wurde. Suche nach dem Ort!",
            "Manchmal muss man über den Tellerrand schauen!",
            "Wie wäre es, wenn du einfach den Dateinamen nimmst, der dir angezeigt wird? Jetzt gilt es nur noch, diese richtig auszulesen, ohne störende Zeichen, ohne %20, ohne Endung..."
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.bauplan, "data": rohbau}

    def create_level8(self):

        task_messages = [
            "Du hast bisher alle Hindernisse und Rätsel erfolgreich überwunden. Eine letzte Aufgabe steht dir noch ",
            "im Weg, bevor du wieder in die Freiheit entlassen wirst.",

        ]

        hints = []

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv8, "data": "myth"} 

    ### SOLUTIONS ###
    #Level3
    def mythos(self, myth):
        zahl_in_worten = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf"]
        zahlen = [0,1,2,3,4,5,6,7,8,9,10,11]
        code = []
        for word in zahl_in_worten:
                if (word in myth):
                    code.append(zahlen[zahl_in_worten.index(word)])
                    print(zahlen[zahl_in_worten.index(word)])
                print(code)
        return code 


    # Level 4
    def sol_lv4(self, data):
        count = 0
        with open(data, 'r') as file:
            for line in file:
                    dates = str(line).split(",")[1].split("-")
                    duratrion = int(dates[0])-int(dates[1])
                    if(duratrion >= 30):
                        count += 1
        return count

    def bauplan(self,rohbau):

        #Liste reinkopieren aus txt file      
        lines = ['                /\\ ', '     /[][][]M[][][][][][][][\\ ', '       /[][]H[][][][][][][\\ ', '              /[][[\\ ', '   /[][][][][][][][]N[][][][][\\ ', '        /[][][][]C[][][][\\ ', '               /][\\ ', '      /[]A[][][][][][][][][\\ ', '         /[][][]N[][][][\\ ', '    /[]U[][][][][][][][][][][\\ ', '           /[][][]T[][\\ ', '            /[][][]U[\\ ', '          /[][][]A[][][\\ ', '             /[][]T[\\ ']

        #zählen der Steine [] & sortieren um es als richtige Pyramide auszugeben
        for i in range(len(lines)):

            lines.count("[]") 
            lines.sort()

        print("\n ")

        for i in range(len(lines)):
            print(lines[i])

        #Zeilen zu einem Eintrag zusammenführen und alles außer Buchstaben entfernen    
        letterneu = []
        for l in range(len(lines)):
            #Wortliste zusammenführen zu einem String und alles außer Buchstaben löschen
            letter = "".join(lines[l])
            letter = letter.replace("[", "")
            letter = letter.replace("]", "")
            letter = letter.replace(" ", "")
            letter = letter.replace("/", "")
            letter = letter.replace("\n", "")
            letter = letter.replace("\\", "")
            letterneu +=letter
            
        letterneu = "".join(letterneu)

        print("\nLösungswort: " + letterneu + "\n ") #Ausgabe 

        code = 0
        #Berechnen des ACSII Code für die einzelnen Buchstaben & alle zusammenrechnen = Code 840
        for i in range(len(letterneu)):   
            
            zahl = ord(letterneu[i])
            code +=zahl
        print("Lösungscode: " + str(code))

        loesungswort = "TUTANCHAMUN"

        #geheimnis = "Tal der Koenige" 

        dir = "https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Tal%20der%20Koenige.jpg"

        geheimnis = dir.split('\\').pop().split('/').pop().rsplit('.', 1)[0] 
        geheimnis = geheimnis.replace('%20', " ")
        print("Das Grab von " + loesungswort + " liegt im " + geheimnis)
        print("Der Code " + code + " knackt das Schloss und du konntest die Tür öffnen!")

        return code, loesungswort, geheimnis

    # Level 8
    def sol_lv8(self, data):
        return 0



    

