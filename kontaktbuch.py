file = open("kontaktbuch.txt")



kontakte = []
for line in file:
    line = line.rstrip()
    if line.startswith("Name"):
        name = line.split(":")[1]
        #print(name)
    elif line.startswith("Telefon"):
        telefon = line.split(":")[1]
        #print(telefon)
    elif line.startswith("Email"):
        email=line.split(":")[1]
        #print(email)
        kontakt = {"name": name, "telefon": telefon, "email": email}
        kontakte.append(kontakt)

print(kontakte)    

eingabe = None

while eingabe !=5:

    print("=== Kontaktbuch ===")
    print("")
    print("1. Kontakt hinzufügen")
    print("2. Alle Kontakte anzeigen")
    print ("3. Kontakt suchen")
    print("4. Kontakt löschen")
    print ("5. Beenden")
    eingabe = input("Bitte Action auswählen und mit Eingabe bestätigen: ")
    eingabe = int(eingabe)

    if eingabe == 1:
        name = input("Bitte Vor - und NAchname eingeben: ")
        telefon = input("Bitte Telefonnummer eingeben: ")
        email = input("Bitte E-Mail eingeben: ")
        newcontact = {"name": name, "telefon": telefon, "email": email}
        kontakte.append(newcontact)
    elif eingabe == 2:
        for kontakt in kontakte:
            print(kontakt["name"])
            print(kontakt["telefon"])
            print(kontakt["email"])
            print("")
    elif eingabe == 3:
        suche = input("Bitte Suchbegriff eingeben: ")
        gefunden = False
        for kontakt in kontakte:
            if suche in kontakt["name"]:
                print (kontakt["name"])
                gefunden = True
        if not gefunden:
                print("Kontakt nicht gefunden")
    elif eingabe == 4:
        löschen = input("Welchen Kontakt möchten sie Löschen: ")
        gefunden = False
        for kontakt in kontakte:
            if löschen in kontakt["name"]:
                print (kontakt["name"])
               
                bestätigung = input("Diesen Kontakt löschen ? 1 für ja 2 für nein")
                bestätigung = int(bestätigung)
                gefunden = True
                if bestätigung == 1:
                    kontakte.remove(kontakt)
                    continue
                elif bestätigung == 2:
                    break
                else:
                    print ("ungültige eingabe")
                    continue
        if not gefunden:
                print("Kontankt nicht gefunden")
    elif eingabe == 5:
        with open ("kontaktbuch.txt", "w") as datei:
            for kontakt in kontakte:
                datei.write("Name: " + kontakt["name"] + "\n")
                datei.write("Telefon: " + kontakt["telefon"] + "\n")
                datei.write("Email: " + kontakt["email"] + "\n")
                datei.write("\n")
print("Kontakte gespeichert. Auf Wiedersehen!")

       
