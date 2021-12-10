#Motus
from operator import countOf
import random
def choixMot(mot):
    nombre = random.randint(0,9)
    mot = mot[nombre]
    return mot

def chercheLettre(mot,motc,tour):
    couleur = []
    for i in range(len(motc)):
        if mot[tour] == motc[tour]:
            couleur = 1
            return couleur
        else:
            couleur = 3
            return couleur
    
           
def CouleurL(chiffre):
    if chiffre == 1:
        return "\033[1;31;40m"
    else :
        return "\033[1;36;40m"
#Cette Fonction ne fonctionne pas
def couleurJaune(motc,motu,indice):
    for i in range(len(motc)):
        if motc[i] == motu[indice]:
            return "\033[1;36;40m"

#Couleurs
#1-Rouge = "\033[1;31;40m"
#2-Jaune = "\033[1;33;40m"
#3-Bleu = "\033[1;36;40m"

#Programme
#Variables
motCache = ['Bonbon','Arrive','Rideau','Tonton','Grande','Fourmi','Pousse','Cinema','Nounou','Doudou']
motATrouver = choixMot(motCache)
motATrouver = str(motATrouver)
motATrouver = list(motATrouver.strip())
lettreP = motATrouver[0]
chance = 8
#Début Jeu
print("\n === Jeu Motus ===")
print("Voila la première Lettre :",lettreP)

#Jeu
for i in range(8):
    print("\nIls vous reste plus que ", chance,"Tours")
    motUti = input(str("\nDis moi un mot :"))
    motUti = list(motUti.strip())
    if motUti != motATrouver:
        for tour in range(len(motATrouver)):
            test = chercheLettre(motUti,motATrouver,tour)
            lettre = motUti[tour]
            if test != 3:
                couleurLettre = CouleurL(test)
                print(couleurLettre,lettre,'\033[0m')
            else:
                couleurLettre = couleurJaune(motATrouver,motUti,test)
                print(couleurLettre,lettre,'\033[0m')
        chance = chance-1
#Fin Jeu
    else:
        motATrouver = ''.join(motATrouver)
        print("Bravo vous avez trouvé le mot, qui était\033[1;37;40m", motATrouver,"\033[0m")
        break
motATrouver = ''.join(motATrouver)
print("Perdu vous n'avez pas trouvé le mot, qui était\033[1;37;40m", motATrouver,"\033[0m")