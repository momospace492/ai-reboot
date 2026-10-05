# ---- BOUCLES ----

# Boucle for sur une liste
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)

print("---")

# Boucle for avec range (0 à 4)
for i in range(5):
    print(i)

print("---")

# Boucle for avec range (1 à 5)
for i in range(1, 6):
    print(i)

print("---")

# Boucle sur un dictionnaire
personne = {"nom": "Momo", "age": 25, "ville": "New York"}
for cle, valeur in personne.items():
    print(f"{cle} : {valeur}")