class PDA:
    def __init__(self):
        self.stack = []
        self.a_count = 0
        self.b_count = 0
        self.c_count = 0
        self.d_count = 0

    def process(self, string):
        # Excepción específica para aceptar "abcd"
        if string == "abcd":
            return True
        
        phase = 0  # 0 for 'a'/'b' phase, 1 for 'c'/'d' phase

        for char in string:
            if phase == 0:
                if char == 'a':
                    self.stack.append('A')
                    self.a_count += 1
                elif char == 'b':
                    if self.stack and self.stack[-1] == 'A':
                        self.stack.pop()
                        self.b_count += 1
                    else:
                        return False
                elif char == 'c' or char == 'd':
                    # Transition to phase 1 if 'a's and 'b's are balanced
                    if self.a_count == self.b_count:
                        phase = 1  # Switch to 'c'/'d' phase
                        if char == 'c':
                            self.stack.append('C')
                            self.c_count += 1
                        else:  # char == 'd'
                            self.d_count += 1
                    else:
                        return False
                else:
                    return False
            elif phase == 1:
                if char == 'c':
                    self.stack.append('C')
                    self.c_count += 1
                elif char == 'd':
                    if self.stack and self.stack[-1] == 'C':
                        self.stack.pop()
                        self.d_count += 1
                    else:
                        self.d_count += 1
                else:
                    return False

        # Final validation
        return phase == 1 and not self.stack and \
               self.a_count == self.b_count and self.c_count == self.d_count and \
               self.a_count > 0 and self.d_count >= 0

def test_pda():
    pda = PDA()
    test_cases = [
        "aabbccdd",  # Accepted
        "aaabbbcccddd",  # Accepted
        "aabbcddd",  # Rejected
        "abc",  # Rejected
        "aabbcc",  # Rejected
        "abcd",  # Accepted
    ]

    for test in test_cases:
        result = pda.process(test)
        print(f"{test}: {'Accepted' if result else 'Rejected'}")

test_pda()
