
import re
cancons = []
usuaris = []
canco_nova = ['', '', '', '', '']
usuari_nou = ['', '', '', '']
while True:
    print("                    ⸻    ♫ Benvinguts a BERENGUIFY!!!♫ ⸻")
    print()
    print("                        ☻ _MENU_☻")
    print()
    print("Opcio 1: Afegir una canco:")
    print("Opcio 2: Registrar un usuari:")
    print("Opcio 3: Veure cançons disponibles:")
    print("Opcio 4: Veure usuaris del sistema:")
    print("Opcio 5: Sortir del programa:")
    try:
        opcio=int(input("introdueix una opcio de l'1 al 5: "))
        print() 

        if opcio==1:
            #Marc: Responsable de la validació d'alta cançons
            print("                         ♬ :;;;:♬  Canco 1 ♬ :;;;:♬")
            canco_nova[0]=input("*★ *――――*★ *Introdueix el nombre de la canco*★ *――――*★ *: ")
            canco_nova[1]=input("*★ *――――*★ *Introdueix l'autor de la canco*★ *――――*★ *: ")
            canco_nova[2]=input("*★ *――――*★ *Introduiex l'any de llancament de la canco*★ *――――*★ *: ")
            expresio = "^[0-9]{4}$"
            comprovacio = re.search(expresio, canco_nova[2])
            while not comprovacio:
                print("es incorrecte")
                canco_nova[2]=input("*★ *――――*★ *Introduiex l'any de llancament de la canco*★ *――――*★ *: ")
                comprovacio = re.search(expresio, canco_nova[2])
            print("es correcte")
            canco_nova[3]=input("*★ *――――*★ *Introdueix l'estil de la canco*★ *――――*★ *: ")
            canco_nova[4] = input("Introdueix l'enllac1: ")
            expresio = "^https://"
            comprovacio = re.search(expresio, canco_nova[4])
            while not comprovacio:
                print("es incorrecte")
                canco_nova[4] = input("Introdueix l'enllac2: ")
                comprovacio = re.search(expresio, canco_nova[4])
            print("es correcte")
            cancons.append(list(canco_nova))              
    
        elif opcio==2:
            print("                                ✦ Usuari 1✦")
            usuari_nou[0]=input("⇉ Escriu el teu nom i llinatge: ")   
            usuari_nou[1]=input("⇉ Escriu la teva data de naixement: ")
            expresiodata = "^[0-9]{2}/[0-9]{2}/[0-9]{4}$"
            comprovacio = re.search(expresiodata, usuari_nou[1])
            while not comprovacio:
                print("es incorrecte")
                usuari_nou[1]=input("⇉ Escriu la teva data de naixement: ")
                comprovacio = re.search(expresiodata, usuari_nou[1])
            print("es correcte")
            usuari_nou[2]=input("⇉ Escriu el teu correu: ")
            expresiocorreu = ".+@.+..+"
            comprovacio = re.search(expresiocorreu, usuari_nou[2])
            while not comprovacio:
                print("es incorrecte")
                usuari_nou[2]=input("⇉ Escriu el teu correu: ")
                comprovacio = re.search(expresiocorreu, usuari_nou[2])
            print("es correcte")
            usuari_nou[3]=input("⇉ Escriu la teva poblacio: ")
            usuaris.append(list(usuari_nou))
            
        elif opcio==3:
            #len torna la quantitat d'elements que hi ha de dins d'una llista
            print("En el sistema hi ha " + str(len(cancons)) + " cancons.")
            i = 1
            for c in cancons:
                print(" Per veure la ♬ :;;;:♬  Canco " + str(i) + " ♬ :;;;:♬: ")
                print()
                print("★ *――――*★ Nom de la canco★ *――――*★ :" + c[0])
                print("★ *――――*★ Nom de l'autor★ *――――*★ : " + c[1])
                print("★ *――――*★ L'any de llancament★ *――――*★ :" + c[2])
                print("★ *――――*★ L'estil de la canco es★ *――――*★ :" + c[3])
                print("★ *――――*★ L'enllac de la canco es★ *――――*★ :"+ c[4])
                print()
                i+=1
                
        
        elif opcio==4:
        
            print("En el sistema hi ha " + str(len(usuaris)) + " usuaris.")
            i = 1
            for u in usuaris:
                print(" Totes les dades de ✦ l'usuari " + str(i) + " ✦ ")
                print()
                print("★ *――――*★ Nom de l'usuari★ *――――*★ :" + u[0])
                print("★ *――――*★ Data de naixement★ *――――*★ :" + u[1])
                print("★ *――――*★ Correu de l'usuari 1★ *――――*★ :" + u[2])
                print("★ *――――*★ La poblacio de l'usuari es★ *――――*★ :" + u[3])
                print()
                i+=1        
        
 elif opcio==5:
            print("Gracies per emprar l'aplicacio, adeu!!")
            break
    except: