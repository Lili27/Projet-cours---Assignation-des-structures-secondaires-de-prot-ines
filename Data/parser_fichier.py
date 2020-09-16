def trouve_CONH (fil_in, fil_out):
    with open(fil_in,"r") as f1, open(fil_out,"w") as f2:
        for line in f1:
            if line.startswith("ATOM"):
                if line[12:16].strip() == "C" or line[12:16].strip() == "O" or line[12:16].strip() == "N" or line[12:16].strip() == "H" :
                    residu = line[22:26].strip()
                    atom = line[6:11].strip()
                    name = line[12:16].strip()
                    x = line[30:38].strip()
                    y = line[38:46].strip()
                    z = line[46:54].strip()
                    f2.write("{} {} {} {} {} {} \n".format(residu, atom, name, x, y, z))

    return fil_out

def coordonnees(file):
    fil_txt = trouve_CONH(file, filout) #apelle la fonction trouve_CONH
    dico_coord = {}
    with open(fil_txt, "r") as f:
        for line in f:
            line = line.strip()
            line = line.split(" ")
            residu = line[0]
            atom = line[1]
            name = line[2]
            x = line[3].strip()
            y = line[4].strip()
            z = line[5].strip()
            if residu in dico_coord:
                dico_coord[residu].append([atom, name, x,y,z])
            else:
                dico_coord[residu] = [[atom, name, x,y,z]]
    return dico_coord



# PROGRAMME PRINCIPAL
if __name__ == '__main__':

    import sys
    import math
    import os 
    if len(sys.argv) != 2:
        sys.exit("ERREUR : le programme prend exactement un fichier pdb !")
    else: 
        filin = sys.argv[1]
        print("Assignassion de structures secondaires pour la protéine {}".format(filin.split(".")[0]))
    filout = str(filin.split(".")[0]) + str("parser.txt")
    coord = coordonnees(filin)
