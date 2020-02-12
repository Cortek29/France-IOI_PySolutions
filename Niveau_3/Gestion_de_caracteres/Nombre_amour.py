prenomEnf1, prenomEnf2 = input().split(" ")
nbAmour = 0


def reduc_nb_amour():
   global nbAmour
   chiff2 = 0
   reduc_chiff = str(nbAmour)
   for chiff in reduc_chiff:
      chiff2 += int(chiff)
   nbAmour = chiff2


def calcul_nb_amour(prenom):
   global nbAmour
   nbAmour = 0
   for let in prenom:
      nbAmour += ord(let) - 65
   while nbAmour >= 10:
      reduc_nb_amour()
   return str(nbAmour)
   

nb1 = calcul_nb_amour(prenomEnf1)
nb2 = calcul_nb_amour(prenomEnf2)
print(' '.join([nb1, nb2]))