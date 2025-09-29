import random

def LettreAleatoire():
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return(random.choice(Alphabet))

class Reseau:
    def __init__(self):
        self.reseau = []
    
    def AjouterNeurone(self):
        lettre = LettreAleatoire()
        self.reseau.append([lettre])
        self.reseau[0].append(lettre)
        for element in range(1, len(self.reseau)):
            while len(self.reseau[element]) != len(self.reseau):
                self.reseau[element].append("0")
            
    def AddOrigin(self):
        self.reseau.append(["Or"])

Reseau1 = Reseau()

Reseau1.AddOrigin()
Reseau1.AjouterNeurone()
for _ in range(15):
    Reseau1.AjouterNeurone()

for n in Reseau1.reseau:
    print(n)