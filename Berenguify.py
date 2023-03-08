
import re
opcio=1
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

            print("                         ♬ :;;;:♬  Canco 2 ♬ :;;;:♬"                                )
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
            nomcomplet=input("⇉ Escriu el teu nom i llinatge: ")
            #LLuís: encarregat de fer la data de naixement   
            datanaixement=input("⇉ Escriu la teva data de naixement: ")
            expresiodata = "^[0-9]{2}/[0-9]{2}/[0-9]{4}$"
            comprobacio = re.search(expresiodata, datanaixement)
            if comprobacio:
                print("es correcte")
            else:
                print("es incorrecte")
                datanaixement=input("⇉ Escriu la teva data de naixement: ")
                comprobacio = re.search(expresiodata, datanaixement)
                if comprobacio:
                    print("Es correcte")
                else:
                    print("Ja has fet els 2 intents")
                    sys.exit()
            
            correu=input("⇉ Escriu el teu correu: ")
            expresiocorreu = ".+@.+..+"
            comprobacio = re.search(expresiocorreu, correu)
            if comprobacio:
                print("es correcte")
            else:
                print("es incorrecte")
                correu=input("⇉ Escriu el teu correu: ")
                comprobacio = re.search(expresiocorreu, correu)
                if comprobacio:
                    print("Es correcte")
                else:
                    print("Ja has fet els 2 intents")
                    sys.exit()
                
                
            poblacio=input("⇉ Escriu la teva població: ")
            print("                                ✦ Usuari 2✦")
            nomcomplet1=input("⇉ Escriu el teu nom i llinatge: ")
            datanaixement1=input("⇉ Escriu la data de naixement: ") 
            comprobacio = re.search(expresiodata, datanaixement1)
            if comprobacio:
                print("es correcte")
            else:
                print("es incorrecte")
                datanaixement1=input("⇉ Escriu la teva data de naixement: ")
                comprobacio = re.search(expresiodata, datanaixement1)
                if comprobacio:
                    print("Es correcte")
                else:
                    print("Ja has fet els 2 intents")
                    sys.exit()
                
            
            
            correu1=input("⇉ Escriu el teu correu: ")
            comprobacio = re.search(expresiocorreu, correu1)
            if comprobacio:
                print("es correcte")
            else:
                print("es incorrecte")
                correu1=input("⇉ Escriu el teu correu: ")
                comprobacio = re.search(expresiocorreu, correu1)
                if comprobacio:
                    print("Es correcte")
                else:
                    print("Ja has fet els 2 intents")
                    sys.exit()
            poblacio1=input("⇉ Escriu la teva població: ")
        
        
        elif opcio==3:
            
            canco_1="La Ramona"
            autorcanco1="Fernando Esteso"
            anyllancamentcanco1="1976"
            estilcanco1="humor"
            enllaccanco1= "https://youtu.be/UpzDkJ6Ldk4"
            print(" Per veure la ♬ :;;;:♬  Canco 1 ♬ :;;;:♬: ")
            print()
            print("★ *――――*★ Nom de la cançó★ *――――*★ :" + canco_1)
            print("★ *――――*★ Nom de l'autor★ *――――*★ : " + autorcanco1)
            print("★ *――――*★ L'any de llancament★ *――――*★ :" + anyllancamentcanco1)
            print("★ *――――*★ L'estil de la cançó es★ *――――*★ :" + estilcanco1)
            print("★ *――――*★ L'enllac de la cançó es★ *――――*★ :"+ enllaccanco1)
            print()
            
            canco_2="asereje"
            autorcanco2="Las Ketchup"
            anyllancamentcanco2="2002"
            estilcanco2="Pop latino, surf pop"
            enllaccanco2="https://youtu.be/arZZw8NyPq8"
            print(" Per veure la ♬ :;;;:♬  Canco 2 ♬ :;;;:♬: ")
            print()
            print("★ *――――*★ Nom de la cançó ★ *――――*★ :" + canco_2)
            print("★ *――――*★ Nom de l'autor ★ *――――*★ :" + autorcanco2)
            print("★ *――――*★ L'any de llancament ★ *――――*★ :" + anyllancamentcanco2)
            print("★ *――――*★ L'estil de la cançó ★ *――――*★ :" + estilcanco2)
            print("★ *――――*★ L'enllac de la cançó ★ *――――*★ :" + enllaccanco2)
        
        elif opcio==4:
        
            usuari="Lluís Felip Seguí Frei"
            datanaixementusuari="17/12/2005"
            correuusuari="a17030@iesberenguer.net"
            poblaciousuari="Inca"
            print(" Totes les dades de ✦ l'usuari 1 ✦ ")
            print()
            print("★ *――――*★ Nom de l'usuari★ *――――*★ :" + usuari)
            print("★ *――――*★ Data de naixement★ *――――*★ :" + datanaixementusuari)
            print("★ *――――*★ Correu de l'usuari 1★ *――――*★ :" + correuusuari)
            print("★ *――――*★ La poblacio de l'usuari es★ *――――*★ :" + poblaciousuari)
            print()
            
            
            usuari2=("Marc Daniel Seguí Frei")
            data2=("17/12/2005")
            correuusuari2=("a17507@iesberenguer.net")
            poblaciousuari2=("Inca")
            print(" Totes les dades de ✦ l'usuari 2 ✦ ")
            print()
            print("★ *――――*★ Nom de l'usuari★ *――――*★ :" + usuari2)
            print("★ *――――*★ Data de naixement★ *――――*★ :" + data2)
            print("★ *――――*★ Correu de l'usuari★ *――――*★ :" + correuusuari2)
            print("★ *――――*★ La poblacio de l'usuari ★ *――――*★ :" + poblaciousuari2)
        
        
        elif opcio==5:
            print("Gràcies per emprar l'aplicació, adeu!!")
    except:
        print("ERROR")