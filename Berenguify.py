
import re

opcio=1
while opcio >=1 and opcio <5:
    print("                    ⸻    ♫ Benvinguts a BERENGUIFY!!!♫ ⸻")
    print()
    print("                        ☻ _MENÚ_☻")
    print()
    print("Opció 1: Afegir una cançó:")
    print("Opció 2: Registrar un usuari:")
    print("Opció 3: Veure cançons disponibles:")
    print("Opció 4: Veure usuaris del sistema:")
    print("Opció 5: Sortir del programa:")
    try:
        opcio=int(input("introdueix una opció de l'1 al 5: "))
        print()
    
        if opcio==1:
            #Marc: Responsable de la validació d'alta de cançons
            print("                         ♬ :;;;:♬  Cançó 1 ♬ :;;;:♬")
            canco=input("*★ *――――*★ *Introdueix el nombre de la cançó*★ *――――*★ *: ")
            autor=input("*★ *――――*★ *Introdueix l'autor de la cançó*★ *――――*★ *: ")
            anyllancament=input("*★ *――――*★ *Introduiex l'any de llancament de la cançó*★ *――――*★ *: ")
            expresion = "^[0-9]{4}$"
            comprobacio = re.search(expresion, anyllancament)
            if comprobacio:
                print("es correcte")
            else:
                print("es incorrecte")
                anyllancament=input("*★ *――――*★ *Introduiex l'any de llancament de la cançó*★ *――――*★ *: ")
                comprobacio = re.search(expresion, anyllancament)
                if comprobacio:
                    print("Es correcte")
                else:
                    print("Ja has fet els 2 intents")
                    sys.exit()
            estil=input("*★ *――――*★ *Introdueix l'estil de la cançó*★ *――――*★ *: ")

            url = input("Introdueix l'enllac1: ")
            expresion = "^https://"
            comprobacio = re.search(expresion, url)
            if comprobacio:
                print("es correcte")
            else:
                print("es incorrecte")
                url1 = input("Introdueix l'enllac2: ")
                comprobacio = re.search(expresion, url1)
                if comprobacio:
                    print("Es correcte")
                else:
                    print("Ja has fet els 2 intents")
                    sys.exit()
                
                

            print("                         ♬ :;;;:♬  Cançó 2 ♬ :;;;:♬"                                )
            canco1=input("*★ *――――*★ *Introdueix el nombre de la cançó*★ *――――*★ *: ")
            autor1=input("*★ *――――*★ *Introdueix l'autor de la cançó*★ *――――*★ *: ")
            anyllancament1=input("*★ *――――*★ *Introduiex l'any de llancament de la cançó*★ *――――*★ *: ")
            expresion = "^[0-9]{4}$"
            comprobacio = re.search(expresion, anyllancament1)
            if comprobacio:
                print("es correcte")
            else:
                print("es incorrecte")
                anyllancament1=input("*★ *――――*★ *Introduiex l'any de llancament de la cançó*★ *――――*★ *: ")
                comprobacio = re.search(expresion, anyllancament1)
                if comprobacio:
                    print("Es correcte")
                else:
                    print("Ja has fet els 2 intents")
                    sys.exit()

            estil1=input("*★ *――――*★ *Introdueix l'estil de la cançó*★ *――――*★ *: ")

            url3 = input("Introdueix l'enllac1: ")
            expresion = "^https://"
            comprobacio = re.search(expresion, url3)
            if comprobacio:
                print("es correcte")
            else:
                print("es incorrecte")
                url4 = input("Introdueix l'enllac2: ")
                comprobacio = re.search(expresion, url4)
                if comprobacio:
                    print("Es correcte")
                else:
                    print("Ja has fet els 2 intents")
                    sys.exit()
                
            
            
    
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