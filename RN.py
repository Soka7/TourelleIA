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
        biaisA = BiaisAleatoires()
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
                        Neur[ran] = [poidsA, biaisA]
        
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
                        Neur[ran] = [poidsA, biaisA]

Reseau1 = Reseau()

def PoidsAleatoire():
    return(random.randint(-50, 50))

def BiaisAleatoires():
    return(random.uniform(-0.1, 0.1))

#Creer tableau
Reseau1.AddOrigin()
for _ in range(6):
    Reseau1.AjouterNeurone()

Reseau1.A = "Neurone1"
Reseau1.B = "Neurone2"
Reseau1.Lier()

Reseau1.A = "Neurone1"
Reseau1.B = "Neurone3"
Reseau1.Lier()

Reseau1.A = "Neurone2"
Reseau1.B = "Neurone4"
Reseau1.Lier()

Reseau1.A = "Neurone2"
Reseau1.B = "Neurone5"
Reseau1.Lier()

Reseau1.A = "Neurone3"
Reseau1.B = "Neurone4"
Reseau1.Lier()

Reseau1.A = "Neurone3"
Reseau1.B = "Neurone5"
Reseau1.Lier()

Reseau1.A = "Neurone5"
Reseau1.B = "Neurone6"
Reseau1.Lier()

Reseau1.A = "Neurone4"
Reseau1.B = "Neurone6"
Reseau1.Lier()

for n in Reseau1.reseau:
    print(n)

def CalculEntreeStart():
    global Entree
    ExempleArray1D = [0.0, 0.5019608, 1.0, 0.2509804]
    Entree = 0
    for Flo in ExempleArray1D:
        Entree += Flo
    return Entree

def CalculSommePonderee():
    SommePonderee = 0
    Entree = CalculEntreeStart()
    SommePonderee += Entree
    
    
    
    
    
    
    
    
    

import matplotlib.pyplot as plt

def AfficherReseauGUI(reseau):
    """
    Affiche le réseau neuronal avec poids et biais sur chaque connexion.
    Chaque cellule du reseau.reseau contient soit "0" (pas de connexion)
    soit [poids, biais].
    """
    plt.ion()
    fig, ax = plt.subplots(figsize=(12, 6))

    # Extraire les noms des neurones (sauf "Or")
    noms_neurones = [ligne[0] for ligne in reseau.reseau if ligne[0] != "Or"]
    nb_neurones = len(noms_neurones)

    # Répartir les neurones en 3 couches pour l'exemple
    couche_entree = noms_neurones[:2]
    couche_cachee = noms_neurones[2:4]
    couche_sortie = noms_neurones[4:]
    couches = [couche_entree, couche_cachee, couche_sortie]

    positions = {}

    # Positionner les neurones par couche (x = couche, y = réparti verticalement)
    for i, couche in enumerate(couches):
        y_start = 1
        y_step = 2
        for j, neurone in enumerate(couche):
            x = i * 4
            y = y_start + j * y_step
            positions[neurone] = (x, y)
            ax.plot(x, y, 'o', markersize=20, color='skyblue')
            ax.text(x, y, neurone, fontsize=10, ha='center', va='center')

    # Dessiner les connexions avec poids et biais
    for ligne in reseau.reseau:
        origine = ligne[0]
        if origine not in positions:
            continue
        for j, val in enumerate(ligne[1:], start=1):
            if val != "0":
                destination = reseau.reseau[0][j]
                if destination not in positions:
                    continue
                x0, y0 = positions[origine]
                x1, y1 = positions[destination]

                # Dessiner la flèche
                ax.annotate("",
                            xy=(x1, y1), xycoords='data',
                            xytext=(x0, y0), textcoords='data',
                            arrowprops=dict(arrowstyle="->", color="black", lw=1.5))
                
                # Afficher poids et biais au milieu de la flèche
                poids, biais = val
                xm, ym = (x0 + x1)/2, (y0 + y1)/2
                ax.text(xm, ym, f"w={poids}, b={biais:.2f}", color='red', fontsize=8, ha='center', va='center')

    ax.axis('off')
    ax.set_title("Réseau neuronal (poids et biais par connexion)", fontsize=16)
    plt.tight_layout()
    plt.show()
    plt.pause(50)

AfficherReseauGUI(Reseau1)