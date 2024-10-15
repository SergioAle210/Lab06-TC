from PDA import PushdownAutomaton  # Importar la clase PushdownAutomaton
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Crear una instancia del autómata
automaton = PushdownAutomaton()

def mostrar_menu():
    print(Fore.CYAN + "\n--- Menú del Autómata de Pila ---")
    print(Fore.CYAN + "1. Probar una cadena")
    print(Fore.CYAN + "2. Información sobre el autómata")
    print(Fore.CYAN + "3. Salir")
    print(Fore.CYAN + "----------------------------------")

def procesar_cadena():
    input_string = input(Fore.YELLOW + "\nIngresa una cadena de 0's y 1's: ")
    
    # Evaluar si la cadena es aceptada
    if automaton.run(input_string):
        print(Fore.GREEN + "\n" + "="*60)
        print(Fore.GREEN + f"✨ ¡Felicidades! La cadena '{input_string}' es aceptada.")
        print(Fore.GREEN + "="*60 + "\n")
    else:
        print(Fore.RED + "\n" + "="*60)
        print(Fore.RED + f"❌ Lo siento, la cadena '{input_string}' NO es aceptada.")
        print(Fore.RED + "="*60 + "\n")

def mostrar_info():
    print(Fore.LIGHTMAGENTA_EX + "\nEste es un autómata de pila que acepta el lenguaje:")
    print(Fore.LIGHTMAGENTA_EX + "L(P) = {0^n 1^{n+1} | n >= 1}")
    print(Fore.LIGHTMAGENTA_EX + "Reconoce cadenas que comienzan con n ceros, seguidos de n+1 unos.")

def main():
    while True:
        mostrar_menu()
        opcion = input(Fore.YELLOW + "Selecciona una opción: ")

        if opcion == "1":
            procesar_cadena()
        elif opcion == "2":
            mostrar_info()
        elif opcion == "3":
            print(Fore.LIGHTBLUE_EX + "Saliendo del programa. ¡Adiós!")
            break
        else:
            print(Fore.RED + "\nOpción inválida. Por favor selecciona una opción válida.")

if __name__ == "__main__":
    print(Fore.LIGHTMAGENTA_EX + "Automata de Pila: Lenguaje L(P) = {0^n 1^{n+1} | n >= 1}")
    main()
