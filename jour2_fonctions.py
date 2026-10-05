# ---- FONCTIONS ----

# Fonction simple
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()

print("---")

# Fonction avec paramètre
def saluer(nom):
    print(f"Bonjour {nom} !")

saluer("Momo")
saluer("Sarah")

print("---")

# Fonction qui retourne une valeur
def addition(a, b):
    return a + b

resultat = addition(5, 3)
print(resultat)

print("---")

# Fonction avec plusieurs paramètres et valeurs par défaut
def presenter(nom, age, ville="New York"):
    return f"{nom}, {age} ans, habite à {ville}"

print(presenter("Momo", 25))
print(presenter("Sarah", 30, "Paris"))

print("---")

# Fonction qui calcule la moyenne d'une liste
def moyenne(notes):
    return sum(notes) / len(notes)

mes_notes = [15, 18, 12, 16]
print(f"Moyenne : {moyenne(mes_notes)}")