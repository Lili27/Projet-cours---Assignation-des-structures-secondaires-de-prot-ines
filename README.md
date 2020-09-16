# Projet-cours---Assignation-des-structures-secondaires-de-proteines
Réalisation d'un projet court dans le cadre d'une formation universitaire.

	I.	But du script: 
Ce projet consite à implémenter le programme de Désignation de structures secondaires des protéine(DSSP)
Pour le bon focntionnement des scripts, il faudrait etre dans un environnement conda avec python3.

	II.	Description du programme:
le programme se base sur le langage python3 sous forme de différentes fonctions et scripts qui seront détaillées par la suite.
Il se compose de 4 scripts python exécutables sur des fichiers pdb dans cette ordre: .

Le script 1: verification_liaison_hydrogene.py exécyutable via la commande: 
    python verification_liaison_hydrogene.py fichier.pdb
Ce script a pour but de vérifier la continuité des liaison peptidique au sein de la protéine. En cas de 
rupture de ces liaison un message d'erreur s'affichera et dans le cas contraire un message indiquant que 
l'utilisateur pourrait poursuivre son travail s'affichera aussi.
fonctionnement : se base sur le calcul de distance entre le  C et l'atome N des résidus. si la distance trouvée est comprise 
entre 2.2 Angstrom et 3 Angstrom, alors nous pourrons continuer.


Le script 2 : pdbHydrogene.py   exécutable via la commande: 
  python pdbHydrogene.py  fichier.pdb

Le script est composé de deux fonction, une qui récupere et vérifie l'existance du fichier en question. La seconde
fonction vérifie l'installation du programme Réduce sur conda, il est donc impératif que celui-ci soit installer. 
Dans le cas contraire, la commande d'installation est donnée par le programme. Par la suite, la fonction lance une commande Shell 
pour permettre à Reduce d'ajouter les Hydrogene dans le fichier pdb, un fichier de sortie sera fournit: fichier_H.pdb

le script 3: parser_fichier.py    exécutable par la commande:
  python parser_fichier.py  fichier_H.pdb

Prend en entré le fichier hydrogéné precedemment et récupere les atomes d'interet pour une liaison hydrogene, c-à-d: 
N, C, O et H. les données récupérées seront donc inscrites dans un fichier output fichier_H_perser.py qui va servire à la suite du programme.


le script 4: calc_energie.py  exécutable par la commande: 
  python calc_python.py fichier_H_perser.pdb
le script s'appui sur le fichier parsé pour calculer les distances qui interviennent dans les liaison hydrogene (ici que pour les Helice alpha, les aures fonctionnalité n'en pas encore été implémenter). Ces distances sont ensuite utilisées pour le calcul d'énergie de liaison. le résultat est ensuite afficher 
sur le terminal et inscrit dans un fichier output. la lettre H en fin de ligne correspondent aux atomes intervenant dans les helices Alpha.
