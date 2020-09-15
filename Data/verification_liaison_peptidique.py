# Avant de commencer notre analyse sur les protéines, il faut vérifier pour chacune d'elle la distance
# peptidique entre ces résidus. Si pour sa totalité, la distance trouvée est comprise 
# entre 2.2Angstrom et 3Angstrom, alors nous pourrons continuer. Sinon ce la voudra 
# signifier une rupture de la liaison peptidique et donc du squelette carbonné.


# Cette 1ère fonction récupère les coordonnés de l'atome C pour chaque résidu
def trouve_C(nom):
	with open(nom, "r") as filin1:
		liste_C = []
		for ligne1 in filin1:
			dict_C = {}
			if ligne1.startswith("ATOM") and ligne1[12:16].strip() == "C" :
				dict_C["resid"] = int(ligne1[6:11])
				dict_C["x"] = float(ligne1[30:38])
				dict_C["y"] = float(ligne1[38:46])
				dict_C["z"] = float(ligne1[46:54])
				liste_C.append(dict_C)
		return liste_C


# Cette 2ème fonction récupère les coordonnés de l'atome N pour chaque résidu
def trouve_N(nom):
	with open(nom, "r") as filin2:
		liste_N = []
		for ligne2 in filin2:
			dict_N = {}
			if ligne2.startswith("ATOM") and ligne2[12:16].strip() == "N" :
				dict_N["resid"] = int(ligne2[6:11])
				dict_N["x"] = float(ligne2[30:38])
				dict_N["y"] = float(ligne2[38:46])
				dict_N["z"] = float(ligne2[46:54])
				liste_N.append(dict_N)
		return liste_N


# Cette fonction permet de calculer la distance entre les atomes C et N de la liaison peptidique.
def distance(liste1,liste2):
	longueur = []
	count = 0
	for i in range(len(liste1)-1):
		xA, yA, zA = float(liste1[i]["x"]), float(liste1[i]["y"]), float(liste1[i]["z"])
		xB, yB, zB = float(liste2[i+1]["x"]), float(liste2[i+1]["y"]), float(liste2[i+1]["z"])
		dist = math.sqrt( (xB-xA)**2 + (yB-yA)**2 + (zB-zA)**2 )
		longueur.append(dist)
	return longueur


# PROGRAMME PRINCIPAL
import sys
import math
if len(sys.argv) != 2:
	sys.exit("ERREUR : il faut donner un argument a la commande !")
print("Fichier {}".format(sys.argv[1]))
fichier = sys.argv[1]
liste1 = trouve_C(fichier)
liste2 = trouve_N(fichier)
print("CA",liste1[0])
print("N",liste2[0])
distance_liaison_C_N = distance(liste1,liste2)
count = 0
for i in range(len(distance_liaison_C_N)):
	if distance_liaison_C_N[i] < 3 :
		count += 1
if len(distance_liaison_C_N) == count:
	print("Les {} liaisons peptidiques ne sont pas rompus. On peut continuer".format(count))