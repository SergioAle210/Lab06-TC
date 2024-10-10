# pushdown_automaton.py
from stack import Stack  # Importar la clase Stack

class PushdownAutomaton:
    def __init__(self):
        self.stack = Stack()
        self.state = "q0"
        self.transitions = {
            ("q0", '0', 'Z0'): ("q0", ['X', 'X', 'Z0']),
            ("q0", '0', 'X'): ("q0", ['X', 'X']),
            ("q0", '1', 'X'): ("q1", []),
            ("q1", '1', 'X'): ("q1", []),
            ("q1", '', 'Z0'): ("q2", ['Z0']),
        }

    def reset(self):
        self.stack = Stack()
        self.state = "q0"
        self.stack.push('Z0')

    def step(self, symbol):
        top_stack = self.stack.top()
        key = (self.state, symbol, top_stack)
        if key in self.transitions:
            self.state, new_stack_symbols = self.transitions[key]
            self.stack.pop()  # Pop the top of the stack
            for symbol in reversed(new_stack_symbols):
                self.stack.push(symbol)  # Push new symbols to the stack

    def run(self, input_string):
        self.reset()
        for symbol in input_string:
            self.step(symbol)
        # After reading the input, check if we can reach q2 (final state)
        self.step('')  # Empty input to check final transition
        return self.state == "q2"
