from PDA import PushdownAutomaton  # Importar la clase PushdownAutomaton
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Crear una instancia del autómata
automaton = PushdownAutomaton()

# Interacción con el usuario
print(Fore.LIGHTBLACK_EX + "Automata de Pila: Lenguaje L(P) = {0^n 1^{n+1} | n >= 1}")
input_string = input(Fore.YELLOW + "Ingresa una cadena de 0's y 1's: ")

# Evaluar si la cadena es aceptada
if automaton.run(input_string):
    print(Fore.GREEN + f"La cadena '{input_string}' es aceptada.")
else:
    print(Fore.RED + f"La cadena '{input_string}' NO es aceptada.")
