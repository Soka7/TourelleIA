import random

al = ["Neurone1", "Neurone2", "Neurone3", "Neurone4", "Neurone5", "Neurone6"]

class Reseau:
    def __init__(self):
        self.reseau = []
        self.A = ""
        self.B = ""
        self.poids = 0
    
    def AjouterNeurone(self):
        self.reseau.append([al[0]])
        self.reseau[0].append(al[0])
        al.remove(al[0])
        for element in range(1, len(self.reseau)):
            while len(self.reseau[element]) != len(self.reseau):
                self.reseau[element].append("0")
            
    def AddOrigin(self):
        self.reseau.append(["Or"])
        
    def Lier(self):
        poidsA = PoidsAleatoire()
        #Lier A en fonction de B.(Plan x, y avec origine en haut a gauche)
        compteur = 0
        for Neu in self.reseau[0]:
            if Neu == self.A:
                Lie = Neu
            else:
                compteur += 1
        for Neur in self.reseau:
            if Neur[0] == self.B:
                for ran in range(len(Neur)):
                    if self.reseau[0][ran] == Lie:
                        Neur[ran] = poidsA
        
        #Lier B en fonction de A.(Plan x, y avec origine en haut a gauche)          
        compteur = 0
        for Neu in self.reseau[0]:
            if Neu == self.B:
                Lie = Neu
            else:
                compteur += 1
        for Neur in self.reseau:
            if Neur[0] == self.A:
                for ran in range(len(Neur)):
                    if self.reseau[0][ran] == Lie:
                        Neur[ran] = poidsA

Reseau1 = Reseau()

def PoidsAleatoire():
    return(random.randint(-50, 50))

#Creer tableau
Reseau1.AddOrigin()
for _ in range(6):
    Reseau1.AjouterNeurone()

Reseau1.A = "Neurone6"
Reseau1.B = "Neurone3"
Reseau1.Lier()

for n in Reseau1.reseau:
    print(n)