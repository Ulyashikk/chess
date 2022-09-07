# -*- coding: utf-8 -*- ## Pour s’assurer de la compatiblite entre correcteurs
from random import *

#initialisation des grilles et autres variables de jeu
N = 'X'#joueur №1
B = 'O'#joueuer №2
joueur1 = N
joueur2 = B
tour1 = 1
tour2 = 2

grille_debut = [
  [N, N, N, N, N, N, B],
  [N, N, N, N, N, B, B],
  [N, N, N, N, B, B, B],
  [N, N, N, ' ', B, B, B],
  [N, N, N, B, B, B, B],
  [N, N, B, B, B, B, B],
  [N, B, B, B, B, B, B]
]
grille_milieu = [
  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', N, N, ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', B, ' ', ' '],
  [' ', ' ', N, ' ', B, B, ' '],
  [N, ' ', B, B, ' ', B, ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', N, ' ', ' ', ' ', ' ']
]
grille_fin = [
  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', N, ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', B, ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', B, ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

liste_grilles = [grille_debut, grille_milieu, grille_fin]

# REPRESENTATION GRAPHIQUE
def affciher_la_grille(grille):
  print('Joueur №1: O') 
  print('Joueur №2: X\n')
  print('    1   2   3   4   5   6   7 ')
  print('   ——— ——— ——— ——— ——— ——— ———')
  l = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
  for i in range(len(grille)):
    print(l[i], '|', end='')
    for elem in grille[i]:
      print('',elem, '|', end='')
    print('\n   ————————————————————————————')

#### SAISIE
###fonctions de verification
def est_dans_grille(ligne,colonne,grille):
    longueur_ligne=len(grille[0])
    longueur_colonne=len(grille)
    ligne_a_verifier,colonne_a_verifier=ord(ligne)-65,ord(colonne)-49
    return 0<=ligne_a_verifier<=longueur_ligne-1 and 0<=colonne_a_verifier<=longueur_colonne-1

def est_au_bon_format(ligne,colonne):
    return (len(ligne)==1 and len(colonne)==1) and 65<=ord(ligne)<=90 and 49<=ord(colonne)<=57

def saisir_coordonnees(ligne,colonne):
    res="Vos coordonnees: "
    while not(est_au_bon_format(ligne,colonne) and est_dans_grille(ligne,colonne,grille_debut)):
        print("coordonnees non valides")
        ligne = input("ligne: ")
        colonne = input("colonne: ")
    res+=str(ligne)+str(colonne)
    return res

def test_est_au_bon_format():
    assert est_au_bon_format("1","A")==False,"indice ligne doit etre une lettre majuscule ; indice colonne doit etre un chiffre"
    assert est_au_bon_format("A","A")==False,"indice ligne doit etre une lettre majuscule ; indice colonne doit etre un chiffre"
    assert est_au_bon_format("1","1")==False,"indice ligne doit etre une lettre majuscule ; indice colonne doit etre un chiffre"
    assert est_au_bon_format("a","1")==False,"indice ligne doit etre une lettre MAJUSCULE"
    assert est_au_bon_format("Z","9")==True,"le format de ces coordonnes devrait etre bon"

def test_est_dans_grille():
    assert est_dans_grille("A","0",grille_debut)==False,"erreur : colonne doit etre comprise entre 1 et 7 inclus"
    assert est_dans_grille("H","1",grille_debut)==False,"erreur : ligne doit etre comprise entre A et G inclus"
    assert est_dans_grille("A","3",grille_debut)==True,"ces coordonnees devraient etre dans la grille"

def case_vide(grille,ligne, colonne):
  case = ligne+colonne
  if grille[(ord(case[0])-65)][int(case[1])]==" ":
    return True
  return False

def test_case_vide():
    assert case_vide(grille_debut, "A", "5")==False, "la case est occupée"
    assert case_vide(grille_milieu,"F", "5")==False, "la case est occupée"
    assert case_vide(grille_fin,"A", "1")==True, "la case est vide"

def test_fin_de_partie():
    assert fin_de_partie(grille_debut)==False, "Partie non terminée"
    assert fin_de_partie(grille_milieu)==False, "Partie non terminée"
    assert fin_de_partie(grille_fin)==False, "Partie non terminée"

def tests():
  test_est_au_bon_format()
  test_est_dans_grille()
  #test_case_vide()
  #test_fin_de_partie()
  print("les tests ont effectué avec succes✅")
  
#verification si la case est a joueur 1
def verif_case(ligne, colonne, grille): 
  while not saisir_coordonnees(ligne,colonne):
    print("coordonnees non valides")
    ligne = input("ligne: ")
    colonne = input("colonne: ")
  lig=ligne
  col=colonne
  while saisir_coordonnees(lig,col) and if_cas_vide(ligne, colonne, grille):
    res = "Votre pion a pour coordonnees: "
    while grille[ord(lig)-65][ord(col)-49]!=joueur2:
      print("la case n'appartient pas à joueur №", tour1)
      lig = input("ligne: ")
      col = input("colonne: ") 
    res+= str(lig)+str(col)
    return res

#pour le joueur 2 on verifie si la case appartient a joueur 2 
def verif_case2(ligne, colonne, grille): 
  while not saisir_coordonnees(ligne,colonne):
    print("coordonnees non valides")
    ligne = input("ligne: ")
    colonne = input("colonne: ")
  lig=ligne
  col=colonne
  while saisir_coordonnees(lig,col) and if_cas_vide(ligne, colonne, grille):
    res = "Votre pion a pour coordonnees: "
    while grille[ord(lig)-65][ord(col)-49]!=joueur1:
      print("la case n'appartient pas à joueur №", tour1)
      lig = input("ligne: ")
      col = input("colonne: ") 
    res+= str(lig)+str(col)
    return res

#la verification si la case est vide
def if_cas_vide(ligne, colonne, grille):
  while grille[ord(ligne)-65][ord(colonne)-49]==' ':
    print("la case est vide")
    print("Veilliez taper les coordonnees")
    ligne = input("ligne: ")
    colonne = input("colonne: ")
  return ligne+colonne

#test si la case est vide
def test_if_cas_vide():
  assert if_cas_vide("D","5",grille_debut)==False,"erreur : la case appartient à joueur №1"
  assert if_cas_vide("E","1",grille_milieu)==False,"erreur : la case appartient à joueur №2"
  assert if_cas_vide("D","2",grille_milieu)==True,"la case est vide"

#la fonction pour compter les pions
def test_nb_pion():
  assert nb_pions(grille_debut)==True, 'Erreur nombre de pions'
  assert nb_pions(grille_milieu)==True, 'Erreur nombre de pions'
  assert nb_pions(grille_fin)==True, 'Erreur nombre de pions'

#la fonction pour le deplacement simple
def deplacement_simple(ligne, colonne, ligne_depl, colonne_depl, grille):
  dif_ligne= abs(ord(ligne_depl)-ord(ligne)) #la difference entre deux valeurs 
  dif_colonne= abs(ord(colonne_depl)-ord(colonne)) 
  while dif_ligne>1 or dif_ligne<0 or dif_colonne<0 or dif_colonne>1: #on verifie la distance entre les cases pour que ce deplacement soit correct 
    print('Veillez saisir les coordonnees encore une fois')
    ligne_depl = input("ligne: ")
    colonne_depl = input("colonne: ")
    dif_ligne= abs(ord(ligne_depl)-ord(ligne))
    dif_colonne= abs(ord(colonne_depl)-ord(colonne))
  return deplacement(ligne, colonne, ligne_depl, colonne_depl, grille)

#la fonction pour le deplacement capture/saut pour le joueur 1 
def deplacement_saut(ligne, colonne, ligne_depl, colonne_depl, grille):
  dif_ligne= abs(ord(ligne_depl)-ord(ligne))
  dif_colonne= abs(ord(colonne_depl)-ord(colonne))
  if dif_ligne>2 or dif_ligne<0 or dif_ligne==1 or dif_colonne>2 or dif_colonne<0 or dif_colonne==1 or grille[(ord(ligne_depl)+ord(ligne))//2-65][(ord(colonne)+ord(colonne_depl))//2-49]!=joueur1: #on verifie si le deplacement est possible et correct 
    print('Veillez saisir les coordonnees encore une fois')
    ligne_depl = input("ligne: ")
    colonne_depl = input("colonne: ")
    dif_ligne= abs(ord(ligne_depl)-ord(ligne))
    dif_colonne= abs(ord(colonne_depl)-ord(colonne))
  #print(grille[((ord(ligne_depl)+ord(ligne))//2)-65][((ord(colonne_depl)+ord(colonne))//2)-49])
  grille[((ord(ligne_depl)+ord(ligne))//2)-65][((ord(colonne_depl)+ord(colonne))//2)-49]= ' ' #on supprime la case entre les deux
  return deplacement(ligne, colonne, ligne_depl, colonne_depl, grille)

#la fonction pour le deplacement capture/saut pour le joueur 2
def deplacement_saut2(ligne, colonne, ligne_depl, colonne_depl, grille):
  dif_ligne= abs(ord(ligne_depl)-ord(ligne))
  dif_colonne= abs(ord(colonne_depl)-ord(colonne))
  if dif_ligne>2 or dif_ligne<0 or dif_ligne==1 or dif_colonne>2 or dif_colonne<0 or dif_colonne==1 or grille[(ord(ligne_depl)+ord(ligne))//2-65][(ord(colonne)+ord(colonne_depl))//2-49]!=joueur2:
    print('Veillez saisir les coordonnees encore une fois')
    ligne_depl = input("ligne: ")
    colonne_depl = input("colonne: ")
    dif_ligne= abs(ord(ligne_depl)-ord(ligne))
    dif_colonne= abs(ord(colonne_depl)-ord(colonne))
  print(grille[((ord(ligne_depl)+ord(ligne))//2)-65][((ord(colonne_depl)+ord(colonne))//2)-49])
  grille[((ord(ligne_depl)+ord(ligne))//2)-65][((ord(colonne_depl)+ord(colonne))//2)-49]= ' ' #on supprime la case entre les deux
  return deplacement(ligne, colonne, ligne_depl, colonne_depl, grille)

#la fonction pour le changement des pions
def deplacement(ligne, colonne, ligne_depl, colonne_depl, grille):
  grille[ord(ligne)-65][ord(colonne)-49], grille[ord(ligne_depl)-65][ord(colonne_depl)-49] = grille[ord(ligne_depl)-65][ord(colonne_depl)-49], grille[ord(ligne)-65][ord(colonne)-49] #le changement des cases pour deplacer le pion
  return affciher_la_grille(grille)

#il n'y a pas de but special, mais au cas ou le joueur tapes ces coordonees, alors la fonction serais utile 
def final_step(ligne, colonne,ligne_depl, colonne_depl, grille):
  while ligne_depl!='A' and colonne_depl!='3':
    print('Voulez-vous continuer le jeu?')
    str=input()
    if continuer_reponse(str)==True:
      ligne_depl=input('ligne: ')
      colonne_depl=input('colonne: ')
    else:
      print("Le jeu est fini! Vous avez perdu :(")
      break 
      return 0
  if ligne_depl=='A' and colonne_depl=='3':
    grille[(ord(ligne_depl)+ord(ligne))//2-65][(ord(colonne)+ord(colonne_depl))//2-48]= ' '
    print("\nFelicitations! Vous avez gagne!")
    return deplacement(ligne, colonne, ligne_depl, colonne_depl, grille)

#la fonction pour continuer le jeu ou pas
def continuer_reponse(str):
  if str!="oui" and str!="Oui" and str!="yes" and str!="ouais":
    return False
  return True 

def stop_jeu(mot): #stop mot pour finir le jeu
  if mot!="oui" and str!="Oui" and str!="yes" and str!="ouais":
    return False
  return True

#pour le joueur 1 continuer le jeu
def continuer_jeu(str, ligne, colonne, ligne_depl, colonne_depl, grille):
  print('Voulez-vous continuer un enchainement de sauts?')
  str=input()
  while continuer_reponse(str)==True:
    print("Les coordonnees:")
    ligne = input("ligne: ")
    colonne = input("colonne: ")
    deplacement_saut(ligne, colonne, ligne_depl, colonne_depl, grille)
    print('Voulez-vous continuer un enchainement de sauts?')
    str=input()
  if continuer_reponse(str)==False:
    print('')

#pour le joueur 2 continuer le jeu 
def continuer_jeu2(str, ligne, colonne, ligne_depl, colonne_depl, grille):
  print('Voulez-vous continuer un enchainement de sauts?')
  str=input()
  while continuer_reponse(str)==True:
    print("Les coordonnees:")
    ligne = input("ligne: ")
    colonne = input("colonne: ")
    deplacement_saut2(ligne, colonne, ligne_depl, colonne_depl, grille)
    print('Voulez-vous continuer un enchainement de sauts?')
    str=input()
  if continuer_reponse(str)==False:
    print('')
    
#une fonction pour verifier qui a gagne
def fin_de_partie(grille):
    noirs=0
    blancs=0
    for i in range(len(grille)):
        for j in range(1,len(grille[i])+1):
            if grille[i][j]=="N":
                noirs+=1
            elif grille[i][j]=="B":
                blancs+=1 
    if blancs==0:
        return "N"
    elif noirs==0:
        return "B"
    else:
        return False

def nb_pions(grille):
    pion1=0
    pion2=0
    for ligne in grille:
      for pion in ligne:
        if pion == joueur1:
          pion1 += 1
        elif pion == joueur2:
          pion2 += 1
    print("Pions du joueur 2:", pion1, "Pions du joueur 1:",pion2)
    if pion1==0 or pion2==0:
      return False
    else:
      return True
  
#le changement de joueurs et de tours
def swap_joueur(joueur1, joueur2, tour1, tour2):
  joueur1, joueur2 = joueur2, joueur1
  tour1,tour2 = tour2,tour1
  print('Tour du joueur №', tour1, "\n")

#la fonction principale pour le joueur 1
def principale(type_grille, grille):
  print('Donnez les coordonnees')
  ligne=input("ligne: ")
  colonne=input("colonne: ")
  print(verif_case(ligne, colonne, grille))
  print("Merci!")
  print("Tapez 1 pour le deplacement simple")
  print("Tapez 2 pour le saut (ou un enchainement de plusieurs sauts)")
  type_depl=input()
  while type_depl!='1' and type_depl!='2':
    print("Tapez 1 pour le deplacement simple")
    print("Tapez 2 pour le saut (ou un enchainement de plusieurs sauts)")
    type_depl=input()
  ligne_depl=input("ligne: ")
  colonne_depl=input("colonne: ")
  if type_grille=='3':
    final_step(ligne, colonne,ligne_depl, colonne_depl, grille)
  else:
    if type_depl=='2':
      deplacement_saut(ligne, colonne, ligne_depl, colonne_depl, grille) 
      continuer_jeu(str, ligne, colonne, ligne_depl, colonne_depl, grille)
    elif type_depl=='1':
      deplacement_simple(ligne, colonne, ligne_depl, colonne_depl, grille) 

#la fonction principale pour le joueur 2
def principale2(type_grille, grille):
  print('Donnez les coordonnees')
  ligne=input("ligne: ")
  colonne=input("colonne: ")
  print(verif_case2(ligne, colonne, grille))
  print("Merci!")
  print("Tapez 1 pour le deplacement simple")
  print("Tapez 2 pour le saut (ou un enchainement de plusieurs sauts)")
  type_depl=input()
  while type_depl!='1' and type_depl!='2':
    print("Tapez 1 pour le deplacement simple")
    print("Tapez 2 pour le saut (ou un enchainement de plusieurs sauts)")
    type_depl=input()
  ligne_depl=input("ligne: ")
  colonne_depl=input("colonne: ")
  if type_grille=='3':
    final_step(ligne, colonne,ligne_depl, colonne_depl, grille)
  else:
    if type_depl=='2':
      deplacement_saut2(ligne, colonne, ligne_depl, colonne_depl, grille) 
      continuer_jeu2(str, ligne, colonne, ligne_depl, colonne_depl, grille)
    elif type_depl=='1':
      deplacement_simple(ligne, colonne, ligne_depl, colonne_depl, grille) 

def choix_deplacement():
  x=randint(1,2)
  if x==1:
    return "pas simple"
  else:
    return "simple"

def pions_jouables_ordi(grille, joueur1):
    liste_pion=[]
    for i in range(len(grille)):
        for j in range(1,7):
            if grille[i][j]==joueur1:
                tuple=[i,j]
                liste_pion.append(tuple)
    return liste_pion

def deplacement_simple_possible(grille,liste_pion):
    liste_deplacements_simple=[]
    for i in range(len(liste_pion)):
        deplacement=[]
        axe_ligne=liste_pion[i][0]
        axe_colone=liste_pion[i][1]
        #la meme ligne
        if axe_colone<7:
          if grille[axe_ligne][axe_colone+1]==" ": #A droite
            ligne=axe_ligne
            colone=axe_colone+1
            deplacement.append([ligne, colone])
        if axe_colone>1:
          if grille[axe_ligne][axe_colone-1]==" ": #A gauche
            ligne=axe_ligne
            colone=axe_colone-1
            deplacement.append([ligne, colone])
            
        #la meme colonne
        if axe_ligne<6:
          if grille[axe_ligne+1][axe_colone]==" ": #En bas
            ligne=axe_ligne+1
            colone=axe_colone
            deplacement.append([ligne, colone])
        if axe_ligne>0:        
          if grille[axe_ligne-1][axe_colone]==" ": #En haut
            ligne=axe_ligne-1
            colone=axe_colone
            deplacement.append([ligne, colone])
            
        #diagonale
        if axe_ligne>0:
          if axe_colone<7:
            if grille[axe_ligne-1][axe_colone+1]==" ": #Haut droite
              ligne=axe_ligne-1
              colone=axe_colone+1
              deplacement.append([ligne, colone])
          if axe_colone>1:  
            if grille[axe_ligne-1][axe_colone-1]==" ": #Haut gauche
              ligne=axe_ligne-1
              colone=axe_colone-1
              deplacement.append([ligne, colone])     
        if axe_ligne<6:
          if axe_colone<7:
            if grille[axe_ligne+1][axe_colone+1]==" ": #Bas droite
              ligne=axe_ligne+1
              colone=axe_colone+1
              deplacement.append([ligne, colone])
          if axe_colone>1:
            if grille[axe_ligne+1][axe_colone-1]==" ": #Bas gauche
              ligne=axe_ligne+1
              colone=axe_colone-1
              deplacement.append([ligne, colone])
        liste_deplacements_simple.append(liste_pion[i])
        liste_deplacements_simple[i].append(deplacement)      
    return liste_deplacements_simple


def deplacement_valide_enchainement(grille, pion, deplacement, joueur1): #la meme fonction mais sans la verification des deplacements normaux sans prises de pion, car cela ne fais pas partie de l'enchainement
    if grille[ord(deplacement[0])-65][int(deplacement[1])]==" ":
      if (abs(int(deplacement[1])-int(pion[1]))==2 or deplacement[1]==pion[1]) and (abs(ord(deplacement[0])-ord(pion[0]))==2 or deplacement[0]==pion[0]):
        if ord(deplacement[0])==ord(pion[0]) and abs(int(deplacement[1])-int(pion[1]))==2: 
          if int(deplacement[1])>int(pion[1]): 
            if grille[(ord(deplacement[0])-65)][int(pion[1])+1] not in [joueur1," "] : #La case est elle occupée par un pion
              return (True, (ord(deplacement[0])-65), int(pion[1])+1)
          else: 
            if grille[(ord(deplacement[0])-65)][int(deplacement[1])+1] not in [joueur1," "]: #La case est elle occupée par un pion
              return (True, (ord(deplacement[0])-65), (int(deplacement[1])+1))
        elif ord(deplacement[1])==ord(pion[1]) and abs(ord(deplacement[0])-ord(pion[0]))==2:
          if (ord(deplacement[0]))>ord(pion[0]):
            if grille[(ord(pion[0])-65)+1][int(pion[1])] not in [joueur1," "]:
              return (True, (ord(pion[0])-65)+1, int(pion[1]))
          else: 
            if grille[(ord(deplacement[0])-65)+1][int(pion[1])] not in [joueur1," "]:
              return (True, (ord(deplacement[0])-65)+1, int(pion[1]))
                        
        else:
          if ord(deplacement[0])<ord(pion[0]): 
            if int(deplacement[1])>int(pion[1]):
              if grille[(ord(pion[0])-65)-1][int(pion[1])+1] not in [joueur1," "]:
                return (True, (ord(pion[0])-65)-1, int(pion[1])+1)
            else:
              if grille[(ord(deplacement[0])-65)+1][int(pion[1])-1] not in [joueur1," "]:
                return (True,((ord(deplacement[0])-65)+1),(int(pion[1])-1))
          else:
            if int(deplacement[1])>int(pion[1]):
              if grille[(ord(pion[0])-65)+1][int(pion[1])+1] not in [joueur1," "]:
                return (True, (ord(pion[0])-65)+1, int(pion[1])+1)
            else: 
              if grille[(ord(pion[0])-65)+1][int(pion[1])-1] not in [joueur1," "]:
                return (True, (ord(pion[0])-65)+1, int(pion[1])-1)
        return False


def deplacement_saisie_possible(grille,liste_pion, joueur1):
    liste_deplacements_prise=[]
    for i in range(len(liste_pion)):
      axe_ligne=liste_pion[i][0]
      axe_colone=liste_pion[i][1]
      deplacement=[]
      pion=str(chr(axe_ligne)+65)+str(axe_colone)
      print(pion)
      #la meme ligne
      if axe_colone<6:
        if deplacement_valide_enchainement(grille,pion,deplacement, joueur1):
          ligne=axe_ligne
          colone=axe_colone+1
          deplacement.append([ligne, colone])
      if axe_colone>1:
        if grille[axe_ligne][axe_colone-1]==" ": #a gauche
          ligne=axe_ligne
          colone=axe_colone-1
          deplacement.append([ligne, colone])
      #la meme colonne
      if axe_ligne<6:
        if grille[axe_ligne+1][axe_colone]==" ": #en bas
          ligne=axe_ligne+1
          colone=axe_colone
          deplacement.append([ligne, colone])
      if axe_ligne>0:
        if grille[axe_ligne-1][axe_colone]==" ": #en haut
          ligne=axe_ligne-1
          colone=axe_colone
          deplacement.append([ligne, colone])
      #diagonale
      #vers le haut
      if axe_ligne>0:
        if axe_colone<7:
          if grille[axe_ligne-1][axe_colone+1]==" ": #droite
            ligne=axe_ligne-1       
            colone=axe_colone+1
            deplacement.append([ligne, colone])
        if axe_colone>1: 
          if grille[axe_ligne-1][axe_colone-1]==" ": #gauche  
            ligne=axe_ligne-1
            colone=axe_colone-1  
            deplacement.append([ligne, colone])
      #vers le bas
      if axe_ligne<6:
        if axe_colone<7:
          if grille[axe_ligne+1][axe_colone+1]==" ": #droite
            ligne=axe_ligne+1
            colone=axe_colone+1
            deplacement.append([ligne, colone])       
        if axe_colone>1:
          if grille[axe_ligne+1][axe_colone-1]==" ": #gauche
            ligne=axe_ligne+1 
            colone=axe_colone-1  
            deplacement.append([ligne, colone])
      liste_deplacements_prise.append(liste_pion[i])
      liste_deplacements_prise[i].append(deplacement)
    return liste_deplacements_prise

def tour_ordi(grille):
    deplacement=choix_deplacement()
    liste_pion=pions_jouables_ordi(grille,joueur1)
    if deplacement=="simple":
        liste_deplacement_simple=deplacement_simple_possible(grille,liste_pion)
        i=randint(0,len(liste_deplacement_simple)-1) #choix par hasard de pion
        j=randint(0,len(liste_deplacement_simple[i][2])-1) #choix par hasard parmis ses déplacements
        pion=[liste_deplacement_simple[i][0],liste_deplacement_simple[i][1]]
        deplacement=(liste_deplacement_simple[i][2][j])
        pion=str(chr(pion[0]+65))+str(pion[1])
        deplacement=str(chr(deplacement[0]+65))+str(deplacement[1])
        print("L'ordinateur à déplacer le pion ", pion,"en ", deplacement, "\n")
    else:
      ordi_saut(grille)
    
#les fonctions de deplacements differents pour l'ordinateur
def saut_nord_est(grille,i,j):
  grille[i][j],grille[i+2][j+2]=grille[i+2][j+2],grille[i][j]
  grille[i+1][j+1]= ' '
  return affciher_la_grille(grille)

def saut_nord_ouest(grille,i,j):
  grille[i][j],grille[i-2][j-2]=grille[i-2][j-2],grille[i][j]
  grille[i-1][j-1]= ' '
  return affciher_la_grille(grille)

def saut_nord(grille,i,j):
  grille[i][j],grille[i-2][j]=grille[i-2][j],grille[i][j]
  grille[i-1][j]= ' '
  return affciher_la_grille(grille)

def saut_est(grille,i,j):
  grille[i][j],grille[i][j+2]=grille[i][j+2],grille[i][j]
  grille[i][j+1]= ' '
  return affciher_la_grille(grille)

def saut_sud_est(grille, i, j):
  grille[i][j],grille[i+2][j+2]=grille[i+2][j+2],grille[i][j]
  grille[i+1][j+1]= ' '
  return affciher_la_grille(grille)

def saut_sud_ouest(grille, i, j):
  grille[i][j],grille[i+2][j-2]=grille[i+2][j-2],grille[i][j]
  grille[i+1][j-1]= ' '
  return affciher_la_grille(grille)
  
def saut_ouest(grille,i,j):
  grille[i][j],grille[i][j-2]=grille[i][j-2],grille[i][j]
  grille[i][j-1]= ' '
  return affciher_la_grille(grille)
  
def saut_sud(grille, i, j):
  grille[i][j],grille[i+2][j]=grille[i+2][j],grille[i][j]
  grille[i+1][j]= ' '
  return affciher_la_grille(grille)

def changement_de_pions(grille, i1, j1, i2, j2):
  grille[i1][j1], grille[i2][j2]=grille[i2][j2],grille[i1][j1]
  return affciher_la_grille(grille)

#le deplacement de l'ordi
def ordi_saut(grille):
  grille_depart=grille
  for i in range(1):#pour les cases {0,0} ,{0,1}, {1,0}, {1,1}
    for j in range(1):
      if grille[i][j]==joueur1:
        if grille[i+1][j+1]==joueur2 and grille[i+2][j+2]==' ':
          return saut_sud_est(grille, i, j)
        elif grille[i+1][j]==joueur2 and grille[i+2][j]==' ':
          return saut_sud(grille, i , j)
        elif grille[i][j+1]==joueur2 and grille[i][j+2]==' ':
          return saut_est(grille, i, j)
  
  for i in range(2): #pour A et B lines 
    for j in range(2, len(grille)-2): #de 3 à 5
      #print(i,j)
      if grille[i][j]==joueur1:
        if grille[i+1][j+1]==joueur2 and grille[i+2][j+2]==' ':
          return saut_nord_est(grille,i,j)
        elif grille[i+1][j-1]==joueur2 and grille[i+2][j-2]==' ':
          return saut_sud_ouest(grille, i, j)
        elif grille[i][j+1]==joueur2 and grille[i][j+2]==' ':
          return saut_sud_est(grille, i, j)
        elif grille[i+1][j]==joueur2 and grille[i+2][j]==' ':
          return saut_sud(grille, i, j)
        elif grille[i][j-1]==joueur2 and grille[i][j-2]==' ':
          return saut_ouest(grille,i,j)

  #pour les cases A6, A7, B5, B7
  for i in range(1):
    for j in range(5,6):
      if grille[i][j]==joueur1:
        if grille[i+1][j-1]==joueur2 and grille[i+2][j-2]==' ':
          return saut_sud_ouest(grille, i, j)
        elif grille[i+1][j]==joueur2 and grille[i+2][j]==' ':
          return saut_sud(grille, i, j)
        elif grille[i][j-1]==joueur2 and grille[i][j-2]==' ':
          return saut_ouest(grille,i,j)

  
  for i in range(2,5): #pour de C a E
    for j in range(1): #pour 1 et 2
      if grille[i][j]==joueur1:
        if grille[i-1][j+1]==joueur2 and grille[i-2][j+2]==' ':
          return saut_nord_ouest(grille, i, j) 
        elif grille[i+1][j+1]==joueur2 and grille[i+2][j+2]==' ':
          return saut_sud_est(grille, i, j)
        elif grille[i+1][j]==joueur2 and grille[i+2][j]==' ':
          return saut_sud(grille, i , j)
        elif grille[i][j+1]==joueur2 and grille[i][j+2]==' ':
          return saut_est(grille,i,j)
        elif grille[i-1][j]==joueur2 and grille[i-2][j]==' ':
          return saut_nord(grille, i, j)
          
  for i in range(2, len(grille)-2): #pour le centre de la grille
    for j in range(2, len(grille[i])-2):
      if grille[i][j]==joueur1:
        if grille[i+1][j+1]==joueur2 and grille[i+2][j+2]==' ':
          return saut_sud_est(grille, i, j)
        elif grille[i-1][j+1]==joueur2 and grille[i-2][j+2]==' ':
          return saut_nord_ouest(grille, i, j) 
        elif grille[i+1][j-1]==joueur2 and grille[i+2][j-2]==' ':
          return saut_sud_ouest(grille, i, j)
        elif grille[i-1][j-1]==joueur2 and grille[i-2][j-2]==' ':
          return saut_nord_est(grille, i , j)
        elif grille[i][j+1]==joueur2 and grille[i][j+2]==' ':
          return saut_est(grille, i, j)
        elif grille[i+1][j]==joueur2 and grille[i+2][j]==' ':
          return saut_sud(grille, i , j)
        elif grille[i][j-1]==joueur2 and grille[i][j-2]==' ':
          return saut_ouest(grille,i,j)
        elif grille[i-1][j]==joueur2 and grille[i-2][j]==' ':
          return saut_nord(grille, i, j)

  for i in range(2,5): #pour de C a E
    for j in range(5,len(grille)): #pour 6 et 7
      if grille[i][j]==joueur1:
        if grille[i-1][j-1]==joueur2 and grille[i-2][j-2]==' ':
          return saut_sud_ouest(grille, i, j)
        elif grille[i+1][j-1]==joueur2 and grille[i+2][j-2]==' ':
          return saut_nord_ouest(grille, i, j) 
        elif grille[i][j-1]==joueur2 and grille[i][j-2]==' ':
          return saut_ouest(grille,i,j)
        elif grille[i+1][j]==joueur2 and grille[i+2][j]==' ':
          return saut_sud(grille, i , j)
        elif grille[i-1][j]==joueur2 and grille[i-2][j]==' ':
          return saut_nord(grille, i, j)

  for i in range(5,6): #pour F et G
    for j in range(1): #pour 1 et 2
      #print(i,j)
      if grille[i][j]==joueur1:
        if grille[i-1][j+1]==joueur2 and grille[i-2][j+2]==' ':
          return saut_nord_ouest(grille, i, j) 
        elif grille[i][j+1]==joueur2 and grille[i][j+2]==' ':
          return saut_est(grille, i, j)
        elif grille[i-1][j]==joueur2 and grille[i-2][j]==' ':
          return saut_nord(grille, i, j)

  for i in range(5,6): #pour F et G lines 
    for j in range(2, len(grille)-2): #de 3 à 5
      #print(i,j)
      if grille[i][j]==joueur1:
        if grille[i+1][j+1]==joueur2 and grille[i+2][j+2]==' ':
          return saut_nord_est(grille,i,j)
        elif grille[i-1][j]==joueur2 and grille[i-2][j]==' ':
          return saut_nord(grille, i, j)
        elif grille[i-1][j+1]==joueur2 and grille[i-2][j+2]==' ':
          return saut_nord_ouest(grille, i, j) 
        elif grille[i][j-1]==joueur2 and grille[i][j-2]==' ':
          return saut_ouest(grille,i,j)
        elif grille[i+1][j+1]==joueur2 and grille[i+2][j+2]==' ':
          return saut_sud_est(grille, i, j)

  for i in range(5,6):
    for i in range(5,6):
      if grille[i][j]==joueur1:
        if grille[i-1][j+1]==joueur2 and grille[i-2][j+2]==' ':
          return saut_nord_ouest(grille, i, j) 
        elif grille[i][j-1]==joueur2 and grille[i][j-2]==' ':
          return saut_ouest(grille,i,j)
        elif grille[i-1][j]==joueur2 and grille[i-2][j]==' ':
          return saut_nord(grille, i, j)

  #si la grille est pareille qu'au debut, c'est-a-dire il n'y a pas de possibilite pour faire la capture, donc on fait le deplacement simple
  if grille_depart==grille: #au cas ou on ne peut pas sauter
    for i in range(len(grille)):
      for j in range(len(grille[i])):
        if grille[i][j]==joueur1:
          if grille[i][j+1]==' ':
            return changement_de_pions(grille, i, j, i, j+1)
          elif grille[i+1][j+1]==' ':
            return changement_de_pions(grille, i, j, i+1, j+1)
          elif grille[i+1][j]==' ':
            return changement_de_pions(grille, i, j, i+1, j)
          elif grille[i-1][j]==' ':
            return changement_de_pions(grille, i, j, i-1, j)
          elif grille[i-1][j-1]==' ':
            return changement_de_pions(grille, i, j, i-1, j-1)
          elif grille[i][j-1]==' ':
            return changement_de_pions(grille, i, j, i, j-1)
          elif grille[i][j+1]==' ':
            return changement_de_pions(grille, i, j, i, j+1)
          elif grille[i+1][j-1]==' ':
            return changement_de_pions(grille, i, j, i+1, j-1)
          elif grille[i-1][j+1]==' ':
            return changement_de_pions(grille, i, j, i-1, j+1)        
  print("Tour de l'ordinateur est fini.")

#on verifie s'il y encore de pions
def ordi_pas_de_pions(grille):
  count_j1=0 #les pions de joueur 1
  count_j2=0 #les pions de joueur 2
  for i in range(len(grille)):
    for j in range(len(grille[i])):
      if grille[i][j]==joueur1:
        count_j1+=1
      elif grille[i][j]==joueur2:
        count_j2+=1
  if count_j1==0: #il n'existe plus de pions de joueur 1
    print("Merci pour le jeu! Vous avez gagné! Felicitations! (Le joueur №",tour1, "a gagné)")
    return False
  if count_j2==0: #il n'existe plus de pions de joueur 2
    print("Merci pour le jeu! Vous avez gagné! Felicitations! (Le joueur №",tour2, "a gagné)")
    return False
  return True

def joueur_contre_joueur(grille):
  affciher_la_grille(grille)
  print("Tour du joueur №1")
  principale(type_grille, grille)
  continuer_reponse(str)
  while continuer_reponse(str)!=True:
    if ordi_pas_de_pions(grille)!=True:
      break
    swap_joueur(joueur1, joueur2,tour1,tour2)
    affciher_la_grille(grille)
    principale2(type_grille, grille)
    print("Voulez-vous quitter le jeu?")
    mot=input()
    if stop_jeu(mot)==True:
      print("Merci pour le jeu😊")
      break
    if ordi_pas_de_pions(grille)!=True:
      break
    affciher_la_grille(grille)
    principale(type_grille, grille)


def joueur_contre_ordi_avancee(grille):
  affciher_la_grille(grille)
  print("Vous êtes un joueur №1. C'est votre tour :)")
  principale(type_grille, grille)
  while continuer_reponse(str)!=True:
    print("\nTour de l'ordinateur (joueur №2)")
    affciher_la_grille(grille)
    ordi_saut(grille)
    if ordi_pas_de_pions(grille)!=True:
      break
    print("Voulez-vous quitter le jeu?")
    mot=input()
    if stop_jeu(mot)==True:
      print("Merci pour le jeu😊 (l'ordinateur a gagné)")
      break
    affciher_la_grille(grille)
    print("Vous êtes un joueur №1. C'est votre tour :)")
    principale(type_grille, grille)


def joueur_contre_ordi_naive(grille):
  affciher_la_grille(grille)
  print("Vous êtes un joueur №1. C'est votre tour :)")
  principale(type_grille, grille)
  while continuer_reponse(str)!=True:
    print("\nTour de l'ordinateur (joueur №2)")
    affciher_la_grille(grille)
    tour_ordi(grille)
    if ordi_pas_de_pions(grille)!=True:
      break
    print("Voulez-vous quitter le jeu?")
    mot=input()
    if stop_jeu(mot)==True:
      print("Merci pour le jeu😊")
      break
    affciher_la_grille(grille)
    print("Vous êtes un joueur №1. C'est votre tour :)")
    principale(type_grille, grille)


def jeu(type_grille, type_jeu, liste_grilles):
  if type_grille==2:
    grille = liste_grilles[1]
  elif type_grille==3:
    grille = liste_grilles[2]
  elif type_grille==1:
    grille = liste_grilles[0]
  if type_grille==4:
    tests()
  else:
    if type_jeu==1:
      joueur_contre_joueur(grille)
    elif type_jeu==2:
      joueur_contre_ordi_avancee(grille)
    elif type_jeu==3:
      joueur_contre_ordi_naive(grille)


#CODE PRINCIPAL
#le menu pour choisir le type de jeu
print("Tapez 1 pour le jeu 'joueur contre joueur'")
print("Tapez 2 pour le jeu 'joueur contre ordinateur avancée'")
print("Tapez 3 pour le jeu 'joueur contre ordinateur naïve'")
type_jeu = int(input())
while type_jeu not in [1,2,3]:
  print("Tapez 1 pour le jeu 'joueur contre joueur'")
  print("Tapez 2 pour le jeu 'joueur contre ordinateur avancée'")
  print("Tapez 3 pour le jeu 'joueur contre ordinateur naïve'")
  type_jeu = int(input())

#le menu pour choisir la configuration ou lancer les tests
print("Tapez 1 pour la configuration de debut")
print("Tapez 2 pour la configuration de milieu")
print("Tapez 3 pour la configuration de fin")
print("Tapez 4 pour lancer les tests")
type_grille = int(input())
while type_grille not in [1,2,3,4]:
  print("Tapez 1 pour la configuration de debut")
  print("Tapez 2 pour la configuration de milieu")
  print("Tapez 3 pour la configuration de fin")
  print("Tapez 4 pour lancer les tests")
  type_grille = int(input())

jeu(type_grille, type_jeu, liste_grilles)