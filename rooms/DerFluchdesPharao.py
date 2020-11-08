from EscapeRoom import EscapeRoom
from random import randint
import random

#+++++++++++   FUNKTIONEN/ METHODEN   ++++++++++++++++++++++++++++

#+++++++++++++++++++++++++++++++++++++++++++++
#  1.  globale Funktion Buchstabe in Ascii umwandeln

def umwandeln_in_ascii(buchstabe):

    asci0=ord(buchstabe)

    return asci0 #gibt Zahl zurück

#+++++++++++++++++++++++++++++++++++++++++++++
#  2.  globale Funktion Zahl mit Cäsarverschlüsselung verschlüsseln

def caesar(asci):

    zahl=asci+3 #Zahl +3
    
    return zahl

#+++++++++++++++++++++++++++++++++++++++++++++
#  3.  globale Funktion Ascii Zahl in Buchstabe umwandeln

def umwandeln_in_buchstabe(zahl):

    buchstabe=chr(zahl)

    return buchstabe

##+++++++++++++++++++++++++++++++++++++++++++++
#  4.  globale Funktion Zahl in Binär umwandeln
# code3=zahl_in_binaer(10)

def binary(dezimalzahl):
    binaer=bin(dezimalzahl)

    return binaer

code3=binary(380)

#+++++++++++++++++++++++++++++++++++++++++++++
#  5.  globale Funktion Code mit Cäsar verschlüsseln




#+++++++++++  VARIABLEN  LISTEN  DICTIONARIES  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#+++++++++++++++++++++++++++++++++++++++++++++
#  1. SPIEL01 globale Liste Spiegelrätsel "spiegelraetsel" enthält 4 fast gleiche Bilder, Unterschied ist den zu erkennenden Code

spiegelraetsel=["<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/wp1.png' width='250' height='400'>",
    "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/wp2.png'width='250' height='400' >", 
    "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/wp3.png'width='250' height='400'>",
    "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/wp4.png'width='250' height='400'>"]


#Variable "spiegelbild" als zufällige Auswahl von Bildern aus der Liste "spiegelraetsel" --> Beim Neustart des Rätsels wird jedes Mal ein anderes Bild zufällig ausgewählt

spiegelbild = random.choice(spiegelraetsel)   #Bildauswahl "spiegelraetsel" zufällig


#In Abhängigkeit vom zufällig ausgewählten Bild unterscheidet sich der Code, der zur Lösung führt 

if spiegelbild==spiegelraetsel[0]:   
    spiegelcode = 31
else:
    if spiegelbild==spiegelraetsel[1]:
        spiegelcode = 130     
    else:
        if spiegelbild==spiegelraetsel[2]:
            spiegelcode = 813 
        else:
            if spiegelbild==spiegelraetsel[3]:
                spiegelcode = 308  


#+++++++++++++++++++++++++++++++++++++++++++++
#  2.  SPIEL02  globale Liste KleopatrasHieroglyphen "wortraetsel" beienhaltet 4 fast gleiche Bilder, der Unterschied sind KleopatrasHieroglyphen

wortraestel = ["<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Personen.jpg' width='800' height='500'>"+"<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Schloss3.jpg'  width='100' height='70'>",
    "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Schnuller.jpg' width='800' height='500' >"+"<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Schloss3.jpg'  width='100' height='70'>", 
    "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Meinung.jpg' width='800' height='500'>" + "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Schloss3.jpg'  width='100' height='70'>",
    "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Einstein.jpg' width='800' height='500'>"+"<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Schloss4.jpg'  width='100' height='70'>"]

#Variable "wortraetsel" als zufällige Auswahl von Bildern aus der Liste "wortraetsel" --> Beim Neustart des Rätsels wird jedes Mal ein anderes Bild zufällig ausgewählt

zufallssatz=random.choice(wortraestel)  #Bildauswahl zufällig


#In Abhängigkeit vom zufällig ausgewählten Bild unterscheidet sich der Code, der zur Lösung führt 

if zufallssatz==wortraestel[0]:
    wortcode = 328
else:
    if zufallssatz==wortraestel[1]:
        wortcode = 210     
    else:
        if zufallssatz==wortraestel[2]:
            wortcode = 185  
        else:
            if zufallssatz==wortraestel[3]:
                wortcode = 1411  


#+++++++++++++++++++++++++++++++++++++++++++++
#  3.  globale Variable "startbild"  -> evtl wird das Startbild in verschiedenen Leveln verwendet

startbild = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab.jpg'  width='800' height='600'>"




#+++++++++++++++++++++++++++++++++++++++++++++
#  4.  SPIEL03   - Code ermitteln & mit Cäsar verschlüsseln & in Binär umwandeln 

#buchstabenspiel

buchstabenraetsel = ["D vor B", "A hinter C", "C tauscht mit D", "B vor A"]

# def bspiel(item):

#     for i in item:
#         tipp_bspiel = buchstabenspiel[i]
#         i+=1
    
#     return tipp_bspiel

# buchstabe_position = bspiel(buchstabenspiel)


buchstaben_loesung = ["C", "D", "B", "A"]

buchstabencode= umwandeln_in_ascii(buchstaben_loesung[0])  #erste Stelle muss richtig ermittelt werden

hieroglyphenraetsel = ["<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Raum2.jpg'  width='1000' height='600'>",
"<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Raum3.jpg'  width='1000' height='600'>"
]

buchstabencode = caesar(buchstabencode)


#++++++++++++++++++ CODE GESAMT

code_gesamt = spiegelcode + wortcode + buchstabencode


#++++++++++++++ HAUPTTEIL ++++++++++++++++++++++++

class DerFluchdesPharao(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Alex, Isi, Jessi, Laura", __name__)
        self.add_level(self.create_level1())
        #self.add_level(self.create_level2())

    ### LEVELS ###
    
    def create_level1(self):
    
        task_messages = [
            "Du wachst auf und fühlst dich noch etwas benommen. Du schaust dich um, aber erkennst nichts wieder..",
            "Du merkst, dass du inmitten einer alten Pyramide bist. Aber wie kommst du hier raus?",
            "Um dich herum stehen lauter komische Dinge an den Wänden, sind da vielleicht irgendwelche nützlichen Tipps versteckt?",
            "<br></br>",
            # "<small><i>Es gibt Schlösser, keine Ahnung welches du drehen musst aber scheinbar gibt es hier einen Code zu finden. Das ist nicht so leicht. Ich habe 3 Rätsel gefunden, ich hoffe du kannst sie lösen!</i></small>",
            "<b>RÄTSEL1</b>",
            "<br></br>",
            startbild,
            "<br></br>",
            "<b><i>Die Karten die Karten</i></b>",
            "<br></br>",
            spiegelbild,
            "<br></br>",
            "<b>RÄTSEL2</b>", 
            "<br></br>",
            "<b><i>Wenn Kleopatra mit Worten spinnt, dann sie immer nur von h..... beginnt</i></b>" , 
            "<br></br>",
            "<b><i>Wer hier nicht richtig liest, sich dieses Rätsel bestimmt vermiest </i></b>" , 
            "<br></br>",
            zufallssatz,
            "<br></br>",
            "<b>RÄTSEL3</b>",
            "<br></br>",
            "<i>Wenn Nofretete mit Buchst<b>A</b>ben spielt, <b>S</b>ie mit dem Stift auf Steine zielt.Do<b>C</b>h ist sie noch <b>I</b>mmer ein kleines Schl<b>I</b>tzohr, einfach gemacht, das käme ihr zu langweilig vor. Auch wenn Sie gerne mit Buchstaben spielt, sie doch nur auf einen genau abzielt.  </i>", 
            "<br></br>",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/nofre.jpg'  width='350' height='100'>" + "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Schloss2.jpg'  width='120' height='70'>",
            "<br></br>",
            hieroglyphenraetsel[1] + hieroglyphenraetsel[0],
            "<small><i>Also ich hab ja schon Mal gelesen, dass der Tutanch der da im Sarg liegt, irgendwie eng verwandt mit dem Cäsar ist! Der Typ hatte eh übernatürliche Kräfte und 3 Mal darfst du raten, wieso der so viele Schlösser braucht</i></small>",
            "<br></br>",
            "<b><i>Finde erst eine kurze Zahl um auch das letzte Schloss zu knacken aber denke dran, die Verwandschaft spielt hier ne +3 Rolle</i></b>",
            "<br></br>",
            "<b>RÄTSEL4</b>",
            "<br></br>",
            "<b><i>Tutanchamun war ein großer Mann, der damals schon mit Zahlen kann. Doch hat er eine Rechnung hinterlassen, die schon viele Leute hat verblassen lassen </i></b>",
            "<br></br>",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/4.jpg'  width='500' height='115'>",
            "<br></br>",
            "<b><i>Es gibt nur 10 Arten von Menschen, die das lösen können. Diese oder Jene.</i></b>",
            "<br></br>",           
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/code4.jpg'  width='500' height='115'>",
            "<br></br>",
            "<br></br>",
            # code_gesamt,
            # bin(code_gesamt)
            ]

    
        
        hints = ["Du siehst die Grabkammer, daneben ein komisches Bild mit halbierter Schrift. Findest du eine Gemeinsamkeit? Was hat diese wohl zu bedeuten? Ergibt das etwa einen Sinn?",
                "Als nächstes suchst du versteckte Botschaften. Kann es sein, dass vor dir jemand die alten Zeichen übersetzt hat?",
                "War Kleopatra nicht bekannt für ihre schön gemalten Zeichen? Ich meine irgendwo eine ihrer Spielregeln gelesen zu haben...",
                "Lies rückwärts...",
                "Den zweiten Code findest du in den Worten, schau genau hin!!",
                "Findest du ein Wort, das eine Zahl enthält? Dann solltest du auch den Rest finden",
                "Es gibt 4 Buchstaben und jede Menge fremder Zeichen, wenn du genau schaust entdeckst du vielleicht eine Gemeinsamkeit",
                "Die Reihenfolge ist elementar, die solltest du von anderen Bildern erkennen, suche nach Gemeinsamkeiten",
                "nur der erste Buchstabe ergibt eine Zahl, die du hier brauchst. ",
                "es ist eine zweistellige Zahl, was hat wohl eine Zahl mit nem Buchstaben zu tun?",
                "wofür stehen die drei Viererblöcke",
                "Umrechnen du musst! Es gibt nur 10 Ziffern um sie zu lösen"] 




        # if zufallssatz==wortraestel[0]:
        #     hints = ["Du siehst die Grabkammer, daneben ein komisches Bild mit halbierter Schrift. Findest du eine Gemeinsamkeit? Was hat diese wohl zu bedeuten? Ergibt das etwa einen Sinn?",
        #             "Als nächstes suchst du versteckte Botschaften. Kann es sein, dass vor dir jemand die alten Zeichen übersetzt hat?",
        #             "War Kleopatra nicht bekannt für ihre schön gemalten Zeichen? Ich meine irgendwo eine ihrer Spielregeln gelesen zu haben...",
        #             "Lies rückwärts...",
        #             "Den zweiten Code findest du in den Worten, schau genau hin!!",
        #             "Findest du ein Wort, das DREIstigkeit ist? Dann solltest du auch den Rest finden",
        #             "328, mano man das war zäh!"
        #           ]
        # else:
        #     if zufallssatz==wortraestel[1]:
        #         hints = [ 
        #                     "Du siehst die Grabkammer, daneben ein komisches Bild mit halbierter Schrift. Findest du eine Gemeinsamkeit? Was hat diese wohl zu bedeuten? Ergibt das etwa einen Sinn?",
        #                     "Als nächstes suchst du versteckte Botschaften. Kann es sein, dass vor dir jemand die alten Zeichen übersetzt hat?",
        #                     "War Kleopatra nicht bekannt für ihre schön gemalten Zeichen? Ich meine irgendwo eine ihrer Spielregeln gelesen zu haben...",
        #                     "Lies rückwärts...",
        #                     "Den zweiten Code findest du in den Worten, schau genau hin!!",
        #                     "Findest du ein Wort, das ZWEItrangig ist? Dann solltest du auch den Rest finden",
        #                     "210, mano man das war zäh!"
        #             ]     
        #     else:
        #         if zufallssatz==wortraestel[2]:
        #             hints = [
        #                         "Du siehst die Grabkammer, daneben ein komisches Bild mit halbierter Schrift. Findest du eine Gemeinsamkeit? Was hat diese wohl zu bedeuten? Ergibt das etwa einen Sinn?",
        #                         "Als nächstes suchst du versteckte Botschaften. Kann es sein, dass vor dir jemand die alten Zeichen übersetzt hat?",
        #                         "War Kleopatra nicht bekannt für ihre schön gemalten Zeichen? Ich meine irgendwo eine ihrer Spielregeln gelesen zu haben...",
        #                         "Lies rückwärts...",
        #                         "Den zweiten Code findest du in den Worten, schau genau hin!!",
        #                         "Findest du ein Wort, das überEINStimmst ist? Dann solltest du auch den Rest finden",
        #                         "185, mano man das war zäh!"
        #                     ] 
        #         else:
        #             if zufallssatz==wortraestel[3]:
        #                 hints = [
        #                                 "Du siehst die Grabkammer, daneben ein komisches Bild mit halbierter Schrift. Findest du eine Gemeinsamkeit? Was hat diese wohl zu bedeuten? Ergibt das etwa einen Sinn?",
        #                                 "Als nächstes suchst du versteckte Botschaften. Kann es sein, dass vor dir jemand die alten Zeichen übersetzt hat?",
        #                                 "War Kleopatra nicht bekannt für ihre schön gemalten Zeichen? Ich meine irgendwo eine ihrer Spielregeln gelesen zu haben...",
        #                                 "Lies rückwärts...",
        #                                 "Den zweiten Code findest du in den Worten, schau genau hin!!",
        #                                 "Findest du ein Wort, das EINStein ist? Dann solltest du auch den Rest finden",
        #                                 "1411, mano man das war zäh!"
        #                         ]   
        #             else:
        #                 hints = ["ERROR"]


     
          
        

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": spiegelbild}
    

    

   # Level2


    # def create_level2(self):

        
    #     liste = [" AB, ", "CD"]

    #     task_messages = [
    #         "Shalom, das war gut, leider bist du immer noch im gleichen Raum",
    #         "Aber schau mal da, siehst du den kleine Skarabäuskäfer der rechts von dir auf dem Boden sitzt?",
    #         "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/SkarabaeusTruhe.jpg' width='400' height='250'>"
    #     ]
    #     hints = [
    #         "Was hat es mit der Raute auf sich, siehst du etwas, das dazu passen könnte?"
    #     ]
    #     return {"task_messages": task_messages, "hints": hints, "solution_function": self.remove_vowels, "data": liste}


    ### SOLUTIONS ###

    def sol_lv1(self, pharao):
        
        code = bin(code_gesamt)

        return code

