import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador = input("Bienvenido a la aventura en el Espacio! Por favor, ingresá tu nombre: ")
    jugador = Jugador(nombre_jugador)
    
    enemigos = [
        Enemigo("Alien", 50, 10),
        Enemigo("Robot", 30, 5),
        Enemigo("Monstruo",70,15)
        ]
    enemigos_derrotados = []
    print("Comienza la aventura!")
    
    while enemigos:

        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue
        print(f"Te encuentras con un {enemigo_actual.nombre} en tu camino")

        while enemigo_actual.salud > 0:
            accion = input("Que deseas hacer? atacar/huir: ")
            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(f"Has atacado al {enemigo_actual.nombre} y le has causado {dano_jugador} de daño")
                enemigo_actual.recibir_dano(dano_jugador)
                
                if enemigo_actual.salud > 0:
                    print(f"A {enemigo_actual.nombre} le queda {enemigo_actual.salud} de salud")
                    dano_enemigo = enemigo_actual.atacar()
                    print(f"El {enemigo_actual.nombre} te atacó y te causó {dano_enemigo} de daño")
                    jugador.recibir_dano(dano_enemigo)
                    if jugador.salud <= 0:
                        break
                    else:
                        print(f"Te quedan {jugador.salud} de salud")           
            else:
                print("Has decidido huir")
                break

        if jugador.salud <= 0:
           break

        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)
            jugador.ganar_experiencia(20) 
        
        continuar = input("Quieres seguir explorando? s/n: ")
        if continuar != "s":
            print("Gracias por haber jugado Batallas Galácticas")
            break
        else:
            continue
    
    if not enemigos:
        print("Felicidades, derrotaste a todos los Enemigos!")

if __name__ == "__main__":    
    main()

