
def trouve_CONH(nom):
	with open(nom, "r") as filin3, open(sys.argv[1]+str("_parsing.txt"),"w") as filout1:		
		liste1_CONH = []
		i = 1
		ligne3 = filin3.readlines()
		while i < len(ligne3):
		#for ligne3 in filin3:
			dict_CONH = {}
			if ligne3[i].startswith("ATOM") :
				if ligne3[i][12:16].strip() == "N" or ligne3[i][12:16].strip() == "C" or ligne3[i][12:16].strip() == "O" or ligne3[i][12:16].strip() == "H" :
					dict_CONH["ATOM"] = int(ligne3[i][6:11])
					dict_CONH["name"] = str(ligne3[i][12:16])
					dict_CONH["resid"] = int(ligne3[i][22:26])
					dict_CONH["x"] = float(ligne3[i][30:38])
					dict_CONH["y"] = float(ligne3[i][38:46])
					dict_CONH["z"] = float(ligne3[i][46:54])
					liste1_CONH.append(dict_CONH)
					filout1.write(ligne3[i])

				

			i += 1
		return liste1_CONH


	

# PROGRAMME PRINCIPAL
import sys
import math
if len(sys.argv) != 2:
	sys.exit("ERREUR : il faut donner un fichier pdb a la commande !")
print("Fichier {}".format(sys.argv[1]))
fichier = sys.argv[1]
liste3 = trouve_CONH(fichier)
print("avant")
print(liste3[0])
print(liste3[1])
