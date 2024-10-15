# import de las librerias que utilizo para los juegos
import random
import time
import threading

# Colores que utilizo para decorar todo el texto
morado = "\033[1;35m"
magenta = "\033[35m"
negrita = "\033[1m"
rosa =  "\033[38;5;125m"
cian = "\033[36m"
verde = "\033[32m"
naranja = "\033[38;5;214m"
rojo = "\033[31m"
verde_lima = "\033[38;5;118m"
verde_pastel = "\033[38;5;120m"
verde_marino = "\033[38;5;23m"
granate = "\033[38;5;88m"
dorado = "\033[33;1m"
reset = "\033[0m"

# Portada del videojuego con mi nombre

print(magenta + negrita + "\n\n"
    "__| |_________________________________________________________| |__\n"
    "__   _________________________________________________________   __\n"
    "  | |                                                         | |  \n"
    "  | |   "f"{rosa}_   _   __  __  __ _____ ____    ___{morado + negrita}                  | |  \n"
    "  | |  "f"{rosa}| \\ | |_/_/_|  \\/  | ____|  _ \\  / _ \\ {morado + negrita}                | |  \n"
    "  | |  "f"{rosa}|  \\| | | | | |\\/| |  _| | |_) || | | |{morado + negrita}                | |  \n"
    "  | |  "f"{rosa}| |\\  | |_| | |  | | |___|  _ < | |_| |{morado + negrita}                | |  \n"
    "  | |  "f"{rosa}|_| \\_|\\___/|_|  |_|_____|_| \\_\\ \\___/{morado + negrita}                 | |  \n"
    "  | |      "f"{rosa}_    _     _____    _  _____ ___  ____  ___ ___{morado + negrita}    | |  \n"
    "  | |     "f"{rosa}/ \\  | |   | ____|  / \\|_   _/ _ \\|  _ \\|_ _/ _ \\ {morado + negrita}  | |  \n"
    "  | |    "f"{rosa}/ _ \\ | |   |  _|   / _ \\ | || | | | |_) || | | | |{morado + negrita}  | |  \n"
    "  | |   "f"{rosa}/ ___ \\| |___| |___ / ___ \\| || |_| |  _ < | | |_| |{morado + negrita}  | |  \n"
    "  | |  "f"{rosa}/_/   \\_\\_____|_____/_/   \\_\\_| \\___/|_| \\_\\___\\___/{morado + negrita}   | |  \n"
    "  | |                                                         | |  \n"
    "  | |                               by Marco Fernández Areste | |  \n"
    "__| |_________________________________________________________| |__\n"
    "__   _________________________________________________________   __\n"
    "  | |                                                         | |  \n\n"
)

# Variables globales que utilizo para almacenar datos y para saber si el jugador quiere salir del juego o retroceder en el menú

salir = False
atras = False
puntos = 0

time.sleep(3)

# Pregunto el nombre al jugador

print(morado + negrita + "Primero de todo, me gustaría saber tu nombre...\n" + reset)

time.sleep(0.5)

# El jugador dice su nombre

nombre = input(f"{morado + negrita}Mi nombre es: {reset}")

time.sleep(1)

# Le doy la bienvenida

print(morado + negrita + "\nBienvenido " + reset + rojo + nombre + morado + negrita +", diviértete.\n" + reset)

time.sleep(2)

# Menú principal del juego, mientras el usuario no entre en la opción de salir el menú se mostrará

while not salir:
    print(morado + negrita + "\n\n"
        "__| |______________________________________________| |__\n"
        "__   ______________________________________________   __\n"
        "  | |                                              | |  \n"
        "  | |   "f"{rosa}__  __ _____ _   _   __{morado + negrita}                    | |  \n"
        "  | |  "f"{rosa}|  \\/  | ____| \\ | |_/_/_{morado + negrita}                   | |  \n"
        "  | |  "f"{rosa}| |\\/| |  _| |  \\| | | | |{morado + negrita}                  | |  \n"
        "  | |  "f"{rosa}| |  | | |___| |\\  | |_| |{morado + negrita}                  | |  \n"
        "  | |  "f"{rosa}|_|  |_|_____|_| \\_|\\___/{morado + negrita}                   | |  \n"
        "  | |   "f"{verde}_         _{morado + negrita}                                | |  \n"
        "  | |  "f"{verde}/ |       | |_   _  __ _  __ _ _ __{morado + negrita}         | |  \n"
        "  | |  "f"{verde}| |    _  | | | | |/ _` |/ _` | '__|{morado + negrita}        | |  \n"
        "  | |  "f"{verde}| |_  | |_| | |_| | (_| | (_| | |{morado + negrita}           | |  \n"
        "  | |  "f"{verde}|_(_)  \\___/ \\__,_|\\__, |\\__,_|_|{morado + negrita}           | |  \n"
        "  | |   "f"{naranja}____      ____{morado + negrita}    {verde}|___/{morado + negrita}     {naranja}_{morado + negrita}              | |  \n"
        "  | |  "f"{naranja}|___ \\    |  _ \\ _   _ _ __ | |_ ___  ___{morado + negrita}   | |  \n"
        "  | |    "f"{naranja}__) |   | |_) | | | | '_ \\| __/ _ \\/ __|{morado + negrita}  | |  \n"
        "  | |   "f"{naranja}/ __/ _  |  __/| |_| | | | | || (_) \\__ \\ {morado + negrita} | |  \n"
        "  | |  "f"{naranja}|_____(_) |_|    \\__,_|_| |_|\\__\\___/|___/{morado + negrita}  | |  \n"
        "  | |   "f"{rojo}_____    ____        _ _{morado + negrita}                   | |  \n"
        "  | |  "f"{rojo}|___ /   / ___|  __ _| (_)_ __{morado + negrita}              | |  \n"
        "  | |    "f"{rojo}|_ \\   \\___ \\ / _` | | | '__|{morado + negrita}             | |  \n"
        "  | |   "f"{rojo}___) |   ___) | (_| | | | |{morado + negrita}                | |  \n"
        "  | |  "f"{rojo}|____(_) |____/ \\__,_|_|_|_|{morado + negrita}                | |  \n"
        "__| |______________________________________________| |__\n"
        "__   ______________________________________________   __\n"
        "  | |                                              | |\n"
    )

    atras = False # Variable para retroceder si entra en el segundo menú
    respuestamenu = input(reset + f"{morado + negrita}\nIntroduce la opción deseada: {reset}")

    # Primera opción para entrar en el menú de juegos
    if respuestamenu == "1" or respuestamenu.lower() == "jugar":
        while not atras:
            # Muestro el menú de juegos al usuario
            print(morado + negrita + "\n\n"
                "__| |____________________________________________________________________________________________| |__\n"
                "__   ____________________________________________________________________________________________   __\n"
                "  | |                                                                                            | |  \n"
                "  | |  "f"{rosa}__  __ _____ _   _   __    ____  _____       {verde}_ _   _ _____ ____  ___  ____{morado + negrita}                | |  \n"
                "  | | "f"{rosa}|  \\/  | ____| \\ | |_/_/_  |  _ \\| ____|     {verde}| | | | | ____/ ___|/ _ \\/ ___|{morado + negrita}               | |  \n"
                "  | | "f"{rosa}| |\\/| |  _| |  \\| | | | | | | | |  _|    {verde}_  | | | | |  _|| |  _| | | \\___ \\ {morado + negrita}              | |  \n"
                "  | | "f"{rosa}| |  | | |___| |\\  | |_| | | |_| | |___  {verde}| |_| | |_| | |__| |_| | |_| |___) |{morado + negrita}              | |  \n"
                "  | | "f"{rosa}|_|  |_|_____|_| \\_|\\___/  |____/|_____|  {verde}\\___/ \\___/|_____\\____|\\___/|____/{morado + negrita}               | |  \n"
                "  | |  "f"{verde_lima}_        _       _ _       _                    _           __{morado + negrita}                            | |  \n"
                "  | | "f"{verde_lima}/ |      / \\   __| (_)_   _(_)_ __   __ _    ___| |  _ __  _/_/_ _ __ ___   ___ _ __ ___{morado + negrita}   | |  \n"
                "  | | "f"{verde_lima}| |     / _ \\ / _` | \\ \\ / / | '_ \\ / _` |  / _ \\ | | '_ \\| | | | '_ ` _ \\ / _ \\ '__/ _ \\ {morado + negrita} | |  \n"
                "  | | "f"{verde_lima}| |_   / ___ \\ (_| | |\\ V /| | | | | (_| | |  __/ | | | | | |_| | | | | | |  __/ | | (_) |{morado + negrita} | |  \n"
                "  | | "f"{verde_lima}|_(_) /_/   \\_\\__,_|_| \\_/ |_|_| |_|\\__,_|  \\___|_| |_| |_|\\__,_|_| |_| |_|\\___|_|  \\___/{morado + negrita}  | |  \n"
                "  | |  "f"{verde_marino}____      _____ _                              _ _           _ _            _{morado + negrita}             | |  \n"
                "  | | "f"{verde_marino}|___ \\    |_   _(_) ___ _ __ ___  _ __   ___   | (_)_ __ ___ (_) |_ __ _  __| | ___{morado + negrita}        | |  \n"
                "  | |   "f"{verde_marino}__) |     | | | |/ _ \\ '_ ` _ \\| '_ \\ / _ \\  | | | '_ ` _ \\| | __/ _` |/ _` |/ _ \\ {morado + negrita}      | |  \n"
                "  | |  "f"{verde_marino}/ __/ _    | | | |  __/ | | | | | |_) | (_) | | | | | | | | | | || (_| | (_| | (_) |{morado + negrita}      | |  \n"
                "  | | "f"{verde_marino}|_____(_)   |_| |_|\\___|_| |_| |_| .__/ \\___/  |_|_|_| |_| |_|_|\\__\\__,_|\\__,_|\\___/{morado + negrita}       | |  \n"
                "  | |  "f"{verde_pastel}_____       _       _ _       _ |_|                                   _     _{morado + negrita}             | |  \n"
                "  | | "f"{verde_pastel}|___ /      / \\   __| (_)_   _(_)_ __   __ _    ___ ___  _ __    _ __ (_)___| |_ __ _ ___{morado + negrita}  | |  \n"
                "  | |   "f"{verde_pastel}|_ \\     / _ \\ / _` | \\ \\ / / | '_ \\ / _` |  / __/ _ \\| '_ \\  | '_ \\| / __| __/ _` / __|{morado + negrita} | |  \n"
                "  | |  "f"{verde_pastel}___) |   / ___ \\ (_| | |\\ V /| | | | | (_| | | (_| (_) | | | | | |_) | \\__ \\ || (_| \\__ \\ {morado + negrita}| |  \n"
                "  | | "f"{verde_pastel}|____(_) /_/   \\_\\__,_|_| \\_/ |_|_| |_|\\__,_|  \\___\\___/|_| |_| | .__/|_|___/\\__\\__,_|___/{morado + negrita} | |  \n"
                "  | |  "f"{granate}_  _      _   _                   _         _       _          {verde_pastel}|_|{granate}_{morado + negrita}                       | |  \n"
                "  | | "f"{rojo}| || |    | | | |_ __    ___  ___ | | ___   (_)_ __ | |_ ___ _ __ | |_ ___{morado + negrita}                 | |  \n"
                "  | | "f"{granate}| || |_   | | | | '_ \\  / __|/ _ \\| |/ _ \\  | | '_ \\| __/ _ \\ '_ \\| __/ _ \\ {morado + negrita}               | |  \n"
                "  | | "f"{rojo}|__   _|  | |_| | | | | \\__ \\ (_) | | (_) | | | | | | ||  __/ | | | || (_) |{morado + negrita}               | |  \n"
                "  | |    "f"{granate}|_|(_)  \\___/|_| |_| |___/\\___/|_|\\___/  |_|_| |_|\\__\\___|_| |_|\\__\\___/{morado + negrita}                | |  \n"
                "  | | "f"{naranja} ____        _   _         __{morado + negrita}                                                              | |  \n"
                "  | | "f"{naranja}| ___|      / \\ | |_ _ __ /_/_ ___{morado + negrita}                                                         | |  \n"
                "  | | "f"{naranja}|___ \\     / _ \\| __| '__/ _` / __|{morado + negrita}                                                        | |  \n"
                "  | |  "f"{naranja}___) |   / ___ \\ |_| | | (_| \\__ \\ {morado + negrita}                                                       | |  \n"
                "  | | "f"{naranja}|____(_) /_/   \\_\\__|_|  \\__,_|___/{morado + negrita}                                                        | |  \n"
                "__| |____________________________________________________________________________________________| |__\n"
                "__   ____________________________________________________________________________________________   __\n"
                "  | |                                                                                            | |  \n"
            )
            
            respuestamenujugar = input(reset + f"{morado + negrita}\nIntroduce la opción deseada: {reset}")

            # Función para que el usuario asigne la dificultad del juego cada vez que inicia uno nuevo
            def dificultad():
                # Muestro el menú de dificultad al usuario
                print(morado + negrita + "\n\n"
                    "__| |_______________________________________________________| |__\n"
                    "__   _______________________________________________________   __\n"
                    "  | |                                                       | |  \n"
                    "  | |  "f"{rosa}____ ___ _____ ___ ____ _   _ _   _____  _    ____{morado + negrita}   | |  \n"
                    "  | | "f"{rosa}|  _ \\_ _|  ___|_ _/ ___| | | | | |_   _|/ \\  |  _ \\ {morado + negrita} | |  \n"
                    "  | | "f"{rosa}| | | | || |_   | | |   | | | | |   | | / _ \\ | | | |{morado + negrita} | |  \n"
                    "  | | "f"{rosa}| |_| | ||  _|  | | |___| |_| | |___| |/ ___ \\| |_| |{morado + negrita} | |  \n"
                    "  | | "f"{rosa}|____/___|_|   |___\\____|\\___/|_____|_/_/   \\_\\____/{morado + negrita}  | |  \n"
                    "  | |  "f"{verde}_     _____ __       _ _{morado + negrita}                             | |  \n"
                    "  | | "f"{verde}/ |   |  ___/_/_  ___(_) |{morado + negrita}                            | |  \n"
                    "  | | "f"{verde}| |   | |_ / _` |/ __| | |{morado + negrita}                            | |  \n"
                    "  | | "f"{verde}| |_  |  _| (_| | (__| | |{morado + negrita}                            | |  \n"
                    "  | | "f"{verde}|_(_) |_|  \\__,_|\\___|_|_|{morado + negrita}                            | |  \n"
                    "  | |  "f"{naranja}____      _   _                            _{morado + negrita}         | |  \n"
                    "  | | "f"{naranja}|___ \\    | \\ | | ___  _ __ _ __ ___   __ _| |{morado + negrita}        | |  \n"
                    "  | |   "f"{naranja}__) |   |  \\| |/ _ \\| '__| '_ ` _ \\ / _` | |{morado + negrita}        | |  \n"
                    "  | |  "f"{naranja}/ __/ _  | |\\  | (_) | |  | | | | | | (_| | |{morado + negrita}        | |  \n"
                    "  | | "f"{naranja}|_____(_) |_| \\_|\\___/|_|  |_| |_| |_|\\__,_|_|{morado + negrita}        | |  \n"
                    "  | |  "f"{rojo}_____    ____  _  __ __     _ _{morado + negrita}                      | |  \n"
                    "  | | "f"{rojo}|___ /   |  _ \\(_)/ _/_/ ___(_) |{morado + negrita}                     | |  \n"
                    "  | |   "f"{rojo}|_ \\   | | | | | |_| |/ __| | |{morado + negrita}                     | |  \n"
                    "  | |  "f"{rojo}___) |  | |_| | |  _| | (__| | |{morado + negrita}                     | |  \n"
                    "  | | "f"{rojo}|____(_) |____/|_|_| |_|\\___|_|_|{morado + negrita}                     | |  \n"
                    "__| |_______________________________________________________| |__\n"
                    "__   _______________________________________________________   __\n"
                    "  | |                                                       | |  \n"
                )
                dificultadañadida = False # Utiizo esta variable para controlar errores
                while not dificultadañadida:
                    dificultad_usuario = input(reset + f"{morado + negrita}\nIntroduce la dificultad deseada: {reset}")
                    if dificultad_usuario == "1" or dificultad_usuario.lower() == "fácil": # Variables para la dificultad fácil
                        intentos = 15
                        tiempo = 60
                        pistas = 3
                        dificultadañadida = True
                    elif dificultad_usuario == "2" or dificultad_usuario.lower() == "normal": # Variables para la dificultad normal
                        intentos = 10
                        tiempo = 40
                        pistas = 2
                        dificultadañadida = True
                    elif dificultad_usuario == "3" or dificultad_usuario.lower() == "difícil": # Variables para la dificultad difícil
                        intentos = 5
                        tiempo = 25
                        pistas = 1
                        dificultadañadida = True
                    else: # Control de errores
                        print (f"{morado + negrita}Solo puedes introducir las opciones {verde}1{morado + negrita}, {verde}2{morado + negrita} y {verde}3{morado + negrita}.{reset}")	
                return (int(intentos), int(tiempo), int(pistas), int(dificultad_usuario)) # Devuelvo las variables
            
            # Primer juego
            def adivinaelnumero():
                numero = random.randint(1, 100) # Se genera un número aleatorio entre 1 y 100
                intentos, tiempo, pistas, dificultad_usuario = dificultad() # El usuario entra a la función de dificultad
                print (f"{morado + negrita}-"*50)
                print (f"{verde}Adivina el número{morado}")
                print ("-"*50)
                time.sleep(1)
                print (f"- Tienes {verde}{intentos}{morado} intentos")
                print ("-"*50)
                print ("\n")
                time.sleep(1)
                i = 1
                while i <= intentos: # Mientras el usuario no supere los intentos seguirá jugando
                    print (f"{morado + negrita}-"*50) 
                    print(f"{morado + negrita}Intento número {verde}{i}{reset}") # Se le avisa al usuario cuantos intentos le quedan
                    try:
                        numero_usuario = int(input(f"{morado + negrita}Introduce tu número {verde}(1-100){morado + negrita}: {reset}")) # Se le pide al usuario que ingrese un número
                        if numero_usuario == numero: # Si el usuario acierta el número sale del bucle, le sale un panel conforme ha ganado y se actualizan los puntos
                            print (f"{dorado}-"*50) 
                            print(f"{dorado}¡ENHORABUENA, HAS GANADO!{reset}")
                            global puntos
                            if dificultad_usuario == 1:
                                print(f"{naranja}+10 puntos")
                                puntos += 10
                            elif dificultad_usuario == 2:
                                print(f"{naranja}+20 puntos")
                                puntos += 20
                            elif dificultad_usuario == 3:
                                print(f"{naranja}+30 puntos")
                                puntos += 30
                            print (f"{dorado}-"*50) 
                            time.sleep(5)
                            break
                        elif numero_usuario < 1 or numero_usuario > 100: # Control de errores
                            print(f"{rojo}Solo puedes introducir números del 0 al 100.{reset}")
                        else: # Si el usuario no acierta se le dice si el número es más grande o pequeño
                            print(f"{rojo}NO es correcto.{reset}")
                            if (numero_usuario > numero):
                                print(f"{morado + negrita}Es {rojo}menor{morado + negrita} que {rosa}{numero_usuario}{morado + negrita}.{reset}")
                            else:
                                print(f"{morado + negrita}Es {rojo}mayor{morado + negrita} que {rosa}{numero_usuario}{morado + negrita}.{reset}")
                            i += 1
                    except ValueError: # Control de errores
                        print(f"{rojo}Solo puedes introducir números.{reset}")
                if (i - 1 == intentos): # Si el usuario pierde, se le muestra que ha perdido y se le muestra que número era
                    print (f"{morado + negrita}-"*50) 
                    print(f"{rojo}GAME OVER\n¡No has conseguido el número en los intentos! {morado + negrita}El número era {reset}{rosa}{numero}{reset}")
                    print (f"{morado + negrita}-"*50) 
                    time.sleep(5)
            
            # Segundo juego
            def tiempolimitado():
                numero = random.randint(1, 100) # Se genera un número aleatorio entre 1 y 100
                intentos, tiempo, pistas, dificultad_usuario = dificultad()
                print (f"{morado + negrita}-"*50)
                print (f"{verde}Tiempo limitado{morado}") # Nombre del juego
                print ("-"*50)
                time.sleep(1)
                print (f"- Tienes {verde}{tiempo}{morado} segundos") # Te avisa de los segundos que tienes
                print ("-"*50)
                print ("\n")
                time.sleep(1)
                tiempoagotado = threading.Event() # Permite coordinar los dos hilos
                guanyar = False
                print (f"{morado + negrita}-"*50)
                def temporizador(tiempo):
                    for i in range(tiempo, -1, -1):
                        if tiempoagotado.is_set():  # Salir si el tiempo se ha agotado
                            break
                        print(f"\t\t\t\t\t{morado + negrita}Tiempo restante: {verde}{i}{reset}  ", end='\r')  # Muestra el tiempo al lado
                        time.sleep(1) # Cuenta 1 segundo y lo actualiza
                    if not tiempoagotado.is_set():
                        time.sleep(1)
                        print(f"{rojo + negrita}¡Tiempo agotado, {morado}último intento{rojo}!{reset}")  # Mensaje final, con espacio para limpiar
                        tiempoagotado.set()

                hilo_temporizador = threading.Thread(target=temporizador, args=(tiempo,)) # Creo un hilo para que funcione el temporizador mientras el usuario introduce números
                hilo_temporizador.start() # Inicio el hilo
                
                while not tiempoagotado.is_set(): # Mientas el tiempo no se agote el juego continuará
                    try:
                        print (f"{morado + negrita}Introduce tu número {verde}(1-100){morado + negrita}: {reset}")
                        numero_usuario = int(input())
                        if numero_usuario == numero: # Si el usuario gana se le muestra que ha ganado, se actualizan los puntos, sale del bucle y se detiene el temporizador
                            tiempoagotado.set()
                            print (f"{dorado}-"*50) 
                            print(f"{dorado}¡ENHORABUENA, HAS GANADO!{reset}")
                            global puntos
                            if dificultad_usuario == 1:
                                print(f"{naranja}+15 puntos")
                                puntos += 15
                            elif dificultad_usuario == 2:
                                print(f"{naranja}+25 puntos")
                                puntos += 25
                            elif dificultad_usuario == 3:
                                print(f"{naranja}+40 puntos")
                                puntos += 40
                            print (f"{dorado}-"*50) 
                            time.sleep(5)
                            guanyar = True
                            break
                        elif numero_usuario < 1 or numero_usuario > 100: # Control de errores
                            print(f"{rojo}Solo puedes introducir números del 0 al 100.{reset}")
                        else: # Si el número no es correcto se le dice si es mayor o menor
                            print(f"{rojo}NO es correcto.{reset}")
                            if (numero_usuario > numero):
                                print(f"{morado + negrita}Es {rojo}menor{morado + negrita} que {rosa}{numero_usuario}{morado + negrita}.{reset}")
                            else:
                                print(f"{morado + negrita}Es {rojo}mayor{morado + negrita} que {rosa}{numero_usuario}{morado + negrita}.{reset}")
                            print (f"{morado + negrita}-"*50) 
                    except ValueError: # Control de errores
                        print(f"{rojo}Solo puedes introducir números.{reset}")
                if not guanyar: # Si pierde le avisa que ha perdido y le muestra el número correcto
                    print (f"{morado + negrita}-"*50) 
                    print(f"{rojo}GAME OVER\n¡No has conseguido el número a tiempo! {morado + negrita}El número era {reset}{rosa}{numero}{reset}")
                    print (f"{morado + negrita}-"*50) 
                    time.sleep(5)
            
            # Tercer juego
            def adivinaconpistas():
                numero = random.randint(1, 100) # Se genera un número aleatorio entre 1 y 100
                intentos, tiempo, pistas, dificultad_usuario = dificultad() # El usuario entra a la función de dificultad
                print (f"{morado + negrita}-"*50)
                print (f"{verde}Adivina con pistas{morado}")
                print ("-"*50)
                time.sleep(1)
                if (pistas == 1): # Se le notifica de las pistas que tiene
                    print (f"- Tienes {verde}{pistas}{morado} pista")
                else:
                    print (f"- Tienes {verde}{pistas}{morado} pistas")
                print ("-"*50)
                time.sleep(1)
                guanyar = False
                if (pistas == 1): # Se le da las pistas en funcion a la dificultad
                    if (numero % 2 == 0):
                        print(f"{morado + negrita}- El número oculto {rojo}es par{morado + negrita}.{reset}")
                    else:
                        print(f"{morado + negrita}- El número oculto {rojo}es impar{morado + negrita}.{reset}")
                elif (pistas == 2):
                    if (numero % 2 == 0):
                        print(f"{morado + negrita}- El número oculto {rojo}es par{morado + negrita}.{reset}")
                    else:
                        print(f"{morado + negrita}- El número oculto {rojo}es impar{morado + negrita}.{reset}")
                    if (numero > 50):
                        print(f"{morado + negrita}- El número oculto {rojo}es mayor que 50{morado + negrita}.{reset}")
                    else:
                        print(f"{morado + negrita}- El número oculto {rojo}es menor que 50{morado + negrita}.{reset}")
                elif (pistas == 3):
                    if (numero % 2 == 0):
                        print(f"{morado + negrita}- El número oculto {rojo}es par{morado + negrita}.{reset}")
                    else:
                        print(f"{morado + negrita}- El número oculto {rojo}es impar{morado + negrita}.{reset}")
                    if (numero > 50):
                        print(f"{morado + negrita}- El número oculto {rojo}es mayor que 50{morado + negrita}.{reset}")
                    else:
                        print(f"{morado + negrita}- El número oculto {rojo}es menor que 50{morado + negrita}.{reset}")
                    if (numero % 5 == 0):
                        print(f"{morado + negrita}- El número oculto {rojo}es divisible por 5{morado + negrita}.{reset}")
                    else:
                        print(f"{morado + negrita}- El número oculto {rojo}no es divisible por 5{morado + negrita}.{reset}")
                print (f"{morado + negrita}-"*50)
                print("\n")
                time.sleep(1)
                while not guanyar:
                    print (f"{morado + negrita}-"*50)
                    try:
                        numero_usuario = int(input(f"{morado + negrita}Introduce tu número {verde}(1-100){morado + negrita}: {reset}"))
                        if numero_usuario == numero: # Si el usuario acierta el número sale del bucle, le sale un panel conforme ha ganado y se actualizan los puntos
                            print (f"{dorado}-"*50) 
                            print(f"{dorado}¡ENHORABUENA, HAS GANADO!{reset}")
                            global puntos
                            if dificultad_usuario == 1:
                                print(f"{naranja}+5 puntos")
                                puntos += 5
                            elif dificultad_usuario == 2:
                                print(f"{naranja}+10 puntos")
                                puntos += 10
                            elif dificultad_usuario == 3:
                                print(f"{naranja}+15 puntos")
                                puntos += 15
                            print (f"{dorado}-"*50) 
                            time.sleep(5)
                            guanyar = True
                            break
                        elif numero_usuario < 1 or numero_usuario > 100: # Control de errores
                            print(f"{rojo}Solo puedes introducir números del 0 al 100.{reset}")
                        else: # Si el usuario no acierta se le notifica de ello
                            print(f"{rojo}NO es correcto.{reset}")
                    except ValueError: # Control de errores
                        print(f"{rojo}Solo puedes introducir números.{reset}")
            
            # Cuarto juego
            def unsolointento():
                numero = random.randint(1, 100) # Se genera un número aleatorio entre 1 y 100
                intent = False # El intento se inicia en falso
                print (f"{morado + negrita}-"*50)
                print (f"{rojo}Un solo intento{morado}")
                print ("-"*50)
                time.sleep(1)
                print (f"- Tienes {rojo}UN SOLO INTENTO{morado}")
                print ("-"*50)
                print ("\n")
                time.sleep(1)
                print (f"{morado + negrita}-"*50)
                while not intent: # Mientras el intento no sea verdadero, se continuará jugando
                    try:
                        numero_usuario = int(input(f"{morado + negrita}Introduce tu número {verde}(1-100){morado + negrita}: {reset}"))
                        if numero_usuario == numero: # Si el usuario acierta el número le sale un panel conforme ha ganado, sale del bucle, y se actualizan los puntos
                            print (f"{dorado}-"*50) 
                            print(f"{dorado}¡ENHORABUENA, HAS GANADO!{reset}")
                            global puntos
                            print(f"{naranja}+100 puntos")
                            puntos += 100
                            print (f"{dorado}-"*50) 
                            time.sleep(5)
                            intent = True
                        elif numero_usuario < 1 or numero_usuario > 100: # Control de errores
                            print(f"{rojo}Solo puedes introducir números del 0 al 100.{reset}")
                        else: # Si el usuario pierde, se le dice el número que era y se le muestra que ha perdido
                            intent = True
                            print (f"{morado + negrita}-"*50) 
                            print(f"{rojo}GAME OVER\n¡No has conseguido el número! {morado + negrita}El número era {reset}{rosa}{numero}{reset}")
                            print (f"{morado + negrita}-"*50) 
                            time.sleep(5)
                    except ValueError: # Control de errores
                        print(f"{rojo}Solo puedes introducir números.{reset}")
            # Segun la respuesta que de el usuario entra en un juego u otro, también está la opción de retroceder de menú
            if respuestamenujugar == "1" or respuestamenujugar.lower() == "adivina el número":
                adivinaelnumero()                
            elif respuestamenujugar == "2" or respuestamenujugar.lower() == "tiempo limitado":
                tiempolimitado()
            elif respuestamenujugar == "3" or respuestamenujugar.lower() == "adivina con pistas":
                adivinaconpistas()
            elif respuestamenujugar == "4" or respuestamenujugar.lower() == "un solo intento":
                unsolointento()
            elif respuestamenujugar == "5" or respuestamenujugar.lower() == "atrás":
                atras = True
            else: # Control de errores.
                print(f"\n\n{rojo + negrita}Opción no válida. Por favor, introduce una opción válida.\n\n")
                time.sleep(3)

    # Segunda opción para ver los puntos del jugador
    elif respuestamenu == "2" or respuestamenu.lower() == "puntos":
        print(f"\n\n{morado + negrita}Actualmente, {reset + rojo}{nombre}{morado + negrita} tiene {reset + rojo}{puntos}{morado + negrita} puntos.\n\n")   
        time.sleep(3.5)

    # Tercera opción para salir del juego
    elif respuestamenu == "3" or respuestamenu.lower() == "salir":
        print(f"\n\n{morado + negrita}Saliendo del juego...\n{reset}")
        time.sleep(1.5)
        salir = True

    # Control de errores
    else:
        print(f"\n\n{rojo + negrita}Opción no válida. Por favor, introduce una opción válida.\n\n")
        time.sleep(3)