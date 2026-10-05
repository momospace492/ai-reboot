# ---- CONDITIONS ----

age = 20

if age >= 18:
    print("Majeur")
else:
    print("Mineur")

print("---")

# Plusieurs conditions
note = 15

if note >= 16:
    print("Très bien")
elif note >= 14:
    print("Bien")
elif note >= 12:
    print("Assez bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")

print("---")

# Conditions combinées
age = 25
permis = True

if age >= 18 and permis:
    print("Peut conduire")
else:
    print("Ne peut pas conduire")

print("---")

# Vérifier si un élément est dans une liste
fruits = ["pomme", "banane", "orange"]

if "banane" in fruits:
    print("La banane est dans la liste")

if "mangue" not in fruits:
    print("La mangue n'est pas dans la liste")