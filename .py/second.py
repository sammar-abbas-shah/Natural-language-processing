"""class DFSA:
    def __init__(self):
        self.start = "q0"
        self.accept = {"q2"}
        self.transitions = {
            ("q0","0"):"q1",("q0","1"):"q0",
            ("q1", "0"): "q1", ("q1", "1"): "q2",
            ("q2", "0"): "q1", ("q2", "1"): "q0",
        }
    def accepts(self,s):
        state = self.start
        for ch in s:
            state = self.transitions.get((state,ch))
        return state in self.accept
#Test
machine = DFSA()
for s in ["01","101","1101","00","111","1000","10101"]:
    print(s,"->","ACCEPT "if machine.accepts(s)else "REJECT")
"""

    #define another rule which accepts 11 it and other should be rejected

class DFSA:
    def __init__(self):
        self.start = "q0"
        self.accept = {"q2"}
        self.transitions = {
            ("q0", "0"): "q0", ("q0", "1"): "q1",
            ("q1", "0"): "q0", ("q1", "1"): "q2",
            ("q2", "0"): "q2", ("q2", "1"): "q2"
        }


    def accepts(self,s):
        state = self.start
        for ch in s:
            state = self.transitions.get((state, ch))
        return state in self.accept

machine = DFSA()
for s in ["01","101","1101","00","111","1000","10101","11","0110","0011","1100","1","0"]:
    print(s, "->", "ACCEPT " if machine.accepts(s) else "REJECT")

