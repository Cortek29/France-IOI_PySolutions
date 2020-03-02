ligneEntiers = []
entreeNbs = []
def lire_entier():
    global ligneEntiers, entreeNbs
    entreeNbs = input().split(' ')
    ligneEntiers = ligneEntiers + ([int(i) for i in entreeNbs])
    entreeNbs = []
    lire_entier()


while True:
    try:
        lire_entier()
    except:
        print(sum(ligneEntiers))
    break

# ligneEntiers = []
# entreeNbs = []
# def lire_entier():
#     global ligneEntiers, entreeNbs
#     try:
#         entreeNbs = input().split(' ')
#         ligneEntiers = ligneEntiers + ([int(i) for i in entreeNbs])
#         entreeNbs = []
#         lire_entier()
#     except:
#         print(sum(ligneEntiers))
#     pass

# lire_entier()