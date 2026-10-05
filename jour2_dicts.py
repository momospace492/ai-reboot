# ---- DICTIONNAIRES ----

personne = {
    "nom": "Momo",
    "age": 25,
    "ville": "New York"
}

print(personne)

# Accéder à une valeur
print(personne["nom"])
print(personne["age"])

# Modifier une valeur
personne["age"] = 26
print(personne["age"])

# Ajouter une clé
personne["etudiant"] = True
print(personne)