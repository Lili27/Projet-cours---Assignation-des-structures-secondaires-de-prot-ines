
# Par leurs numéros, on fait défiler les atomes et on cherche les coordonnés des CA et N 
# de chaque atome. Puis comparaison de distance entre le CA[i] et N[i+1] car au dessus
# de 1.8-2.2 Angstrom, rupture de la liaison peptidique.
# De là on récupère les O et H présents sur les CA et N et on a nos liaison hydrogènes.
# Pour une hélice alpha: le O de CA[i] et le H de N[i+4]
#		petit sillon: distance =
# 		grand sillon: distance = 



def trouve_CA(nom):
	with open(nom, "r") as filin1:
		liste_CA = []
		for ligne1 in filin1:
			dict_CA = {}
			if ligne1.startswith("ATOM") and ligne1[12:16].strip() == "CA" :
				dict_CA["resid"] = int(ligne1[6:11])
				dict_CA["x"] = float(ligne1[30:38])
				dict_CA["y"] = float(ligne1[38:46])
				dict_CA["z"] = float(ligne1[46:54])
				liste_CA.append(dict_CA)
		return liste_CA

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
liste1 = trouve_CA(fichier)
liste2 = trouve_N(fichier)
print("CA",liste1[0])
print("N",liste2[0])
distance_liaison_CA_N = distance(liste1,liste2)
count = 0
for i in range(len(distance_liaison_CA_N)):
	if (distance_liaison_CA_N[i] > 2.2) and (distance_liaison_CA_N[i] < 3) :
		count += 1
if len(distance_liaison_CA_N) == count:
	print("Les {} liaisons peptidiques ne sont pas rompus".format(count))