print("Quiz Time")
input("Press ENTER to continue")
antwort = 0
krieg = input("Wie lange dauert der 30-Jähriger Krieg?\n")
if krieg == "30" or krieg == "30 Jahre":
    print("Nicht schlecht")
    antwort = antwort + 1
else:
    print("Beim nächsten Mal hast du es!")
input()

monate = input("Einige Monate haben 30, einige 31 Tage. Wie viele haben 28 Tage?\n")
if monate == "12" or monate == "alle" or monate == "12 Monate" or monate == "alle Monate":
    print("hätte ich nicht gedacht")
    antwort = antwort + 1
    if antwort == 2:
        print("2 von 2! WOW!")
else:
    print("Leider Falsch. Denk noch einmal nach")
input()

golf = input("Wie viele Einkerbungen hat ein Golfball?\n")
if golf == "336":
    print("Das hätte ich auch gewusst!")
    antwort = antwort + 1
else:
    print("Wie, das weißt du nicht?")
input()

park = input("Ein Informatiker schiebt einen Kinderwagen durch den Park. Kommt ein älteres Ehepaar: „Junge oder Mädchen?“\n")
if park == "Informatiker: „Richtig!“" or park == "richtig" or park == "true":
    print("RICHTIG!")
    antwort = antwort + 1
else:
    print("Informatiker: „Richtig!“")
input()

lampe = input("Wie viele Programmierer braucht man, um eine Glühbirne zu wechseln?\n")
if lampe == "keinen" or lampe == "0":
    print("Ist ja auch ein Hardware-Problem!")
    antwort = antwort + 1
else:
    print("Keinen einzigen, ist ein Hardware-Problem!")
input()

weihnachten = input("Was ist das beste Weihnachtsgeschenk?\n")
if weihnachten == "kaputte Trommel":
    print("richtig, die ist unschlagbar")
    antwort = antwort + 1
else:
    print("EINE KAPUTTE TROMMEL!")
    input()
    print("unschlagbar!")
input()

print("Quiz Ende")
prozent = antwort / 6 * 100
if antwort > 2:
    print("Glückwunsch! Du hast ", antwort ," Fragen richtig beantwortet")
elif antwort == 0:
    print("Das ist nicht möglich! Du bist leider durchgefallen")
else:
    print("Leider hast du nur ",antwort," Fragen beantwortet")
print("Das entspricht ca ",round(prozent,2)," Prozent")
