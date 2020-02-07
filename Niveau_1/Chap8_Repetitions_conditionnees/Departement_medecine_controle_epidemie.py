popuVille = int(input())
nbMalades = 1
nbJours = 1
while nbMalades < popuVille:
   nbMalades = nbMalades + (2 * nbMalades)
   nbJours = nbJours +1
print(nbJours)