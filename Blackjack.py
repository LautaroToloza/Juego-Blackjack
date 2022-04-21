__author__ = "Lautaro Toloza"

import random, time

"""
Juego del blackjack: con condicionales, contadores y tuplas.
2 jugadores: crupier y jugador.
"""
numeros = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'AS', 'J', 'Q', 'K')
palos = ('Picas', 'Tréboles', 'Rombos', 'Corazones')
# Inicialización de banderas (figuras y utilización de carta 3).
figura_ok = jugadorf_carta3 = crupierf_carta3 = False
cont_jugador = cont_crupier = 0

# Carta 1 del jugador
carta1_jugador = random.choice(numeros)
palo_jugador = random.choice(palos)
# carta 1 del crupier
carta1_crupier = random.choice(numeros)
palo_crupier = random.choice(palos)
# Carta 2 del jugador
carta2_jugador = random.choice(numeros)
palo2_jugador = random.choice(palos)
# carta 2 del crupier
carta2_crupier = random.choice(numeros)
palo2_crupier = random.choice(palos)

# Inicializacion de carta 3 de jugador y crupier
carta3_jugador = palo3_jugador = None
carta3_crupier = palo3_crupier = None
print("\t\033[1;33m" + 'Bienvenidos al programa del Blackjack!!' + '\033[0;m')
print("**" * 25)
# Análisis carta 1 jugador.
if carta1_jugador == 'J' or carta1_jugador == 'Q' or carta1_jugador == 'K':
    cont_jugador += 10
    figura_ok = True
elif carta1_jugador == 'AS':
    op = input(
        "\nJugador le tocó un AS.\nOpciones.. \nIngresando un '1' sumara 1 punto. \nIngresando un '2' sumara 11 puntos. \nIngrese su opción: ")
    if op == "1":
        cont_jugador += 1
    elif op == "2":
        cont_jugador += 11
    else:
        print('\nError de carga. Ingrese correctamente la opción')
        op = input(
            "Jugador le tocó un AS.\nOpciones.. \nIngresando un '1' sumara 1 punto. \nIngresando un '2' sumara 11 puntos. \nIngrese su opción: ")
        if op == "1":
            cont_jugador += 1
        elif op == "2":
            cont_jugador += 11
else:
    cont_jugador += carta1_jugador

# Análisis carta 1 crupier.
if carta1_crupier == 'J' or carta1_crupier == 'Q' or carta1_crupier == 'K':
    cont_crupier += 10
    figura_ok = True
elif carta1_crupier == 'AS':
    op = input(
        "\nCrupier le tocó un AS.\nOpciones.. \nIngresando un '1' sumara 1 punto. \nIngresando un '2' sumara 11 puntos. \nIngrese su opción: ")
    if op == "1":
        cont_crupier += 1
    elif op == "2":
        cont_crupier += 11
    else:
        print('\nError de carga. Ingrese correctamente la opción')
        op = input(
            "Crupier le tocó un AS.\nOpciones.. \nIngresando un '1' sumara 1 punto. \nIngresando un '2' sumara 11 puntos. \nIngrese su opción: ")
        if op == "1":
            cont_crupier += 1
        elif op == "2":
            cont_crupier += 11
else:
    cont_crupier += carta1_crupier

# Muestreo de la primera jugada.
time.sleep(1)
print("\n\033[1;34m" + 'Datos de la primera jugada... ' + '\033[0;m')
print("--" * 20)
print('Carta uno del jugador: ', carta1_jugador, "de", palo_jugador)
print('Carta uno del crupier: ', carta1_crupier, "de", palo_crupier)
print("Puntaje parcial del jugador: ", cont_jugador)
print("Puntaje parcial del crupier: ", cont_crupier)
if palo_jugador == palo_crupier and carta1_jugador == carta1_crupier:
    print('La carta uno del jugador y del croupier fueron iguales!!')
print("--" * 20)

# Análisis carta 2 jugador.
if carta2_jugador == 'J' or carta2_jugador == 'Q' or carta2_jugador == 'K':
    cont_jugador += 10
    figura_ok = True
elif carta2_jugador == 'AS':
    op = input(
        "\nJugador le tocó un AS.\nOpciones.. \nIngresando un '1' sumara 1 punto. \nIngresando un '2' sumara 11 puntos. \nIngrese su opción: ")
    if op == "1":
        cont_jugador += 1
    elif op == "2":
        cont_jugador += 11
    else:
        print('\nError de carga. Ingrese correctamente la opción')
        op = input(
            "Jugador le tocó un AS.\nOpciones.. \nIngresando un '1' sumara 1 punto. \nIngresando un '2' sumara 11 puntos. \nIngrese su opción: ")
        if op == "1":
            cont_jugador += 1
        elif op == "2":
            cont_jugador += 11
else:
    cont_jugador += carta2_jugador

# Análisis carta 2 crupier.
if carta2_crupier == 'J' or carta2_crupier == 'Q' or carta2_crupier == 'K':
    cont_crupier += 10
    figura_ok = True
elif carta2_crupier == 'AS':
    op = input(
        "\nCrupier le tocó un AS.\nOpciones.. \nIngresando un '1' sumara 1 punto. \nIngresando un '2' sumara 11 puntos. \nIngrese su opción: ")
    if op == "1":
        cont_crupier += 1
    elif op == "2":
        cont_crupier += 11
    else:
        print('\nError de carga. Ingrese correctamente la opción')
        op = input(
            "Crupier le tocó un AS.\nOpciones.. \nIngresando un '1' sumara 1 punto. \nIngresando un '2' sumara 11 puntos. \nIngrese su opción: ")
        if op == "1":
            cont_crupier += 1
        elif op == "1":
            cont_crupier += 11
else:
    cont_crupier += carta2_crupier

# Muestreo de la segunda jugada.
time.sleep(1)
print("\n\033[1;34m" + 'Datos de la segunda jugada... ' + '\033[0;m')
print("--" * 20)
print('Carta dos del jugador: ', carta2_jugador, "de", palo2_jugador)
print('Carta dos del crupier: ', carta2_crupier, "de", palo2_crupier)
print("Puntaje parcial del jugador: ", cont_jugador)
print("Puntaje parcial del crupier: ", cont_crupier)
print("--" * 20)

# Análisis carta 3 jugador.
if cont_jugador <= 16:
    carta3_jugador = random.choice(numeros)
    palo3_jugador = random.choice(palos)
    jugadorf_carta3 = True
    if carta3_jugador == 'J' or carta3_jugador == 'Q' or carta3_jugador == 'K':
        cont_jugador += 10
        figura_ok = True
    elif carta3_jugador == 'AS':
        op = input(
            "\nJugador le tocó un AS.\nOpciones.. \nIngresando un '1' sumara 1 punto. \nIngresando un '2' sumara 11 puntos. \nIngrese su opción: ")
        if op == "1":
            cont_jugador += 1
        elif op == "2":
            cont_jugador += 11
        else:
            print('\nError de carga. Ingrese correctamente la opción')
            op = input(
                "Jugador le tocó un AS.\nOpciones.. \nIngresando un '1' sumara 1 punto. \nIngresando un '2' sumara 11 puntos. \nIngrese su opción: ")
            if op == "1":
                cont_jugador += 1
            elif op == "2":
                cont_jugador += 11
    else:
        cont_jugador += carta3_jugador

# Análisis carta 3 crupier.
if cont_crupier <= 16:
    carta3_crupier = random.choice(numeros)
    palo3_crupier = random.choice(palos)
    crupierf_carta3 = True
    if carta3_crupier == 'J' or carta3_crupier == 'Q' or carta3_crupier == 'K':
        cont_crupier += 10
        figura_ok = True
    elif carta3_crupier == 'AS':
        op = input(
            "\nCrupier le tocó un AS.\nOpciones.. \nIngresando un '1' sumara 1 punto. \nIngresando un '2' sumara 11 puntos. \nIngrese su opción: ")
        if op == "1":
            cont_crupier += 1
        elif op == "2":
            cont_crupier += 11
        else:
            print('\nError de carga. Ingrese correctamente la opción')
            op = input(
                "Crupier le tocó un AS.\nOpciones.. \nIngresando un '1' sumara 1 punto. \nIngresando un '2' sumara 11 puntos. \nIngrese su opción: ")
            if op == "1":
                cont_crupier += 1
            elif op == "1":
                cont_crupier += 11
    else:
        cont_crupier += carta3_crupier

time.sleep(1)
if jugadorf_carta3 == True or crupierf_carta3:
    print("\n\033[1;34m" + 'Datos de la tercera jugada... ' + '\033[0;m')
    print("--" * 20)
if jugadorf_carta3:
    print('Carta tres del jugador: ', carta3_jugador, "de", palo3_jugador)
if crupierf_carta3:
    print('Carta tres del crupier: ', carta3_crupier, "de", palo3_crupier)

# Muestra de los resultados finales
time.sleep(1)
print("\n\033[1;31m" + 'Muestra del resultado final... ' + '\033[0;m')
print("**" * 25)
if figura_ok:
    print("Hubo al menos 1 figura!! ")
print("Puntaje final del jugador: ", cont_jugador)
print("Puntaje final del crupier: ", cont_crupier)
if cont_jugador > cont_crupier and cont_jugador <= 21:
    print("\n\033[1;33m" + 'EL GANADOR DEL JUEGO FUE EL JUGADOR!! ' + '\033[0;m')
elif cont_crupier > cont_jugador and cont_crupier <= 21:
    print("\n\033[1;33m" + 'EL GANADOR DEL JUEGO FUE EL CRUPIER!! ' + '\033[0;m')
elif cont_crupier > 21 and cont_jugador <= 21:
    print("\n\033[1;33m" + 'EL GANADOR DEL JUEGO FUE EL JUGADOR!! ' + '\033[0;m')
elif cont_jugador > 21 and cont_crupier <= 21:
    print("\n\033[1;33m" + 'EL GANADOR DEL JUEGO FUE EL CRUPIER!! ' + '\033[0;m')
elif cont_jugador > 21 and cont_crupier > 21:
    print("\n\033[1;33m" + 'PERDIERON LOS DOS, SUPERARON LOS 21 PUNTOS!! ' + '\033[0;m')
else:
    print("\n\033[1;33m" + 'SE PRODUJO UN EMPATE, JUEGUEN NUEVAMENTE!! ' + '\033[0;m')
print("**" * 25)
print("Fin del programa, este programa fue realizado por: " + __author__)
