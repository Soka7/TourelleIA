import random

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&é"
print(len(Alphabet))
al = []
for le in Alphabet:
    al.append(le)

def LettreAleatoire(al):
    rdm = random.randint(0, len(al)-1)
    lett = al[rdm]
    del(al[rdm])
    return(lett)

class Reseau:
    def __init__(self):
        self.reseau = []
    
    def AjouterNeurone(self):
        lettre = LettreAleatoire(al)
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
for _ in range(6):
    Reseau1.AjouterNeurone()

for n in Reseau1.reseau:
    print(n)