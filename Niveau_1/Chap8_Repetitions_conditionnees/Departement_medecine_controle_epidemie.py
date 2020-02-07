# initialisation des variables
popuVille = int(input())
nbMalades = 1
nbJours = 1
# boucle sur condition
while nbMalades < popuVille:
   nbMalades = nbMalades + (2 * nbMalades)
   nbJours = nbJours +1
# rendu resultat
print(nbJours)