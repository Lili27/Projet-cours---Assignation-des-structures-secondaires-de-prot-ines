
# Ici nous allons calculer les distances et les energies entre les résidus i et i+4 afin de déterminer un pattern de
# structure secondaire: les hélices aplha
# Il est possible de réaliser la même étape mais pour les hélices pi (i+5) et 3.10 (i+3)

# Cette fonction permet de parcourir le fichier donné en argument et d'itérer celui-ci ligne par ligne
# afin de récupérer les données nécessaires a nos calculs.
def lecture_fichier1(nom1):
    with open(nom1,"r") as filin4:
        liste2_CONH = []
        i = 0
        ligne4 = filin4.readlines()
        while i < len(ligne4):
            lecture_dico = {}
            lecture_dico["ATOM"] = int(ligne4[i][6:11])
            lecture_dico["name"] = str(ligne4[i][12:16].strip())
            lecture_dico["AA"] = str(ligne4[i][17:20])
            lecture_dico["residu"] = int(ligne4[i][22:26])
            lecture_dico["x"] = float(ligne4[i][30:38])
            lecture_dico["y"] = float(ligne4[i][38:46])
            lecture_dico["z"] = float(ligne4[i][46:54])
            liste2_CONH.append(lecture_dico)
            i += 1
    return liste2_CONH


# Cette fonction permet de calculer la distance euclidienne entre 2 points A et B distincts.
def calcul_distance(xA,yA,zA,xB,yB,zB):
    dist = math.sqrt( (xB-xA)**2 + (yB-yA)**2 + (zB-zA)**2 )
    return dist


# Cette fonction permet de calculer l'energie de liaisons d'hydrogènes par la formule de Coulomb, utilisé en DSSP, entre 2 résidus différrents.
def calcul_energie(r_NO,r_HC,r_HO,r_CN):
    F = 332
    delta = 0.084
    E = delta * ( (1/r_NO) + (1/r_HC) - (1/r_HO) - (1/r_CN)) * F
    return E


#PROGRAMME PRINCIPAL
if __name__ == '__main__':

    import sys
    import math
    if len(sys.argv) != 2:
        sys.exit("ERREUR : il faut donner un fichier pdb hydrogèné parsé a la commande !")
    print("Fichier {}".format(sys.argv[1]))
    fichier = sys.argv[1]
    # récupération des données dans une liste de dictionnaire
    lecture1 = lecture_fichier1(fichier)
    print(lecture1[0]["ATOM"])


    # On va calculer les distances entre les atomes CO du résidu i et NH du résidu i+4 afin de 
    # regarder si il y a potentiellement des H-bond pattern: n-turn(i)=: Hbond(i,i + n), n = 3,4,5
    # Dans notre fichier parsé.txt, les atomes sont (pour chaque résidu) dans l'ordre suivant: N,C,O,H

    # Donc avec i = 0, les atomes C et O du résidu i sont respectivement à i+1 et i+2
    # Les atomes N et H du résidu i +4 sont respectivement à i+4 et i+4+3 => i+4 et i+7


    # ON COMPTE PAR LIGNE 
    # 1 résidu = 4 atomes
    # Pour i+3 => i+3*4 => i+12 et i=0 donc C: i+1 /// O: i+2 /// N: i+12 /// H: i+12+3 => i+15
    # Pour i+4 => i+3*4 => i+16 et i=0 donc C: i+1 /// O: i+2 /// N: i+16 /// H: i+16+3 => i+19
    # Pour i+5 => i+5*4 => i+20 et i=0 donc C: i+1 /// O: i+2 /// N: i+20 /// H: i+20+3 => i+23


    # On écrirera les données de distances et les résidus impliqués dans un fichier.txt

    with open(sys.argv[1] + str("_helices_alpha.txt"),"w") as filout2:
        print("n° residus"+"\t"+"Distance_NO"+"\t"+"Distance_HC"+"\t"+"Distance_HO"+"\t"+"Distance_CN"+"\t"+"Energie"+"\t"+"E>-0.5kcal/mol")
        liste_distance = []
        i = 4

        while i < len(lecture1) - 12: # ou -12, -16, -20
            distance = {}
            # coordonnées des atomes C et O
            xC, yC, zC = float(lecture1[i+1]["x"]), float(lecture1[i+1]["y"]), float(lecture1[i+1]["z"])
            xO, yO, zO = float(lecture1[i+2]["x"]), float(lecture1[i+2]["y"]), float(lecture1[i+2]["z"])
            # coordonnées des atomes N et H
            xN, yN, zN = float(lecture1[i+12]["x"]), float(lecture1[i+12]["y"]), float(lecture1[i+12]["z"]) # ou +12, +16, +20
            xH, yH, zH = float(lecture1[i+15]["x"]), float(lecture1[i+15]["y"]), float(lecture1[i+15]["z"]) # ou +15, +19, +23
            # calcul des distances
            dist_NO = calcul_distance(xO,yO,zO,xN,yN,zN)
            dist_HC = calcul_distance(xC,yC,zC,xH,yH,zH)
            dist_HO = calcul_distance(xO,yO,zO,xH,yH,zH)
            dist_CN = calcul_distance(xC,yC,zC,xN,yN,zN)
            # calcul des energies de liaisons d'hydrogènes
            energie = calcul_energie(dist_NO, dist_HC, dist_HO, dist_CN)
            residus = lecture1[i]["residu"], lecture1[i+12]["residu"] # ou +12, +16, +20
            if energie > -0.5:
            # H pour alpha Helix
                print("{} {:18.3f} {:14.3f} {:14.3f} {:14.3f} {:14.3f} ".format(residus, dist_NO, dist_HC, dist_HO, dist_CN, energie))
                filout2.write("{} {} {} {} {} {} \n".format(residus, dist_NO, dist_HC, dist_HO, dist_CN, energie))
            else:
                print("{} {:18.3f} {:14.3f} {:14.3f} {:14.3f} {:14.3f} H\n".format(residus, dist_NO, dist_HC, dist_HO, dist_CN, energie))
                filout2.write("{} {} {} {} {} {} H\n".format(residus, dist_NO, dist_HC, dist_HO, dist_CN, energie))

            i += 12 # ou +12, +16, +20
            
