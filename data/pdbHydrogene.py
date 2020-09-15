"""
le script pdbHydrogene est conçu pour des fichiers au format .pdb. 
En entrant le nom d'un fichier pdb d'une protéine déja existant dans le
repertoire, le module récupere le fichier associé, excécute le programme Réduce 
(préalablement installé sur la machine) afin d'ajouter les liaisons hydrogenes. 
Un fichier output est founit pour chaque protéine en input 
"""
import sys
import os

def getArgs(args):
	arguments = sys.argv[1:]

	""" Récupérer les fichiers donnés en arguments à la fonction"""
	if len(args) == 1:
		sys.exit("Nombre d'argument incorrect.\n Merci de renseigner au moins un fichier pdb. \n")
	else:
		for arg in arguments:
			if os.path.exists(arg):
				print("les fichiers choisis sont: {}\n".format(arg))
			else:
				print("le fichier {} n existe pas dans le repertoire{}".format(arg,os.getcwd()))
	return arguments

def pdbReduce(arguments):
	if os.popen("reduce -version") == "/bin/sh: 1: reduce: not found":
		print(" reduce n est pas installer. \n")
		print("Merci d installer reduce : conda install -c mx reduce")
	else:
		for arg in arguments:
			argH = str(arg).split(".")[0] +"H." + str(arg).split(".")[1]
			os.system(" reduce {} > {}".format(arg, argH))

#programme principal:
if __name__ == "__main__":
	liste_arg = getArgs(sys.argv)
	pdbReduce(liste_arg)




