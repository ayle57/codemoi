"""
Cette fonction vérifie si un nombre n est un nombre de Kaprekar en base 10.
Pour cela, on calcule n^2 et on découpe le résultat en deux parties.
On vérifie si la somme des deux parties est égale à n.
"""
def is_kaprekar(n: int) -> bool:
    n_squared = n * n  # Calculer le carré de n
    str_n_squared = str(n_squared)  # Convertir le carré de n en chaîne de caractères

    # Découper le carré en deux parties
    length = len(str_n_squared)
    right_part = int(str_n_squared[length // 2:])  # Partie droite
    left_part = int(str_n_squared[:length // 2]) if str_n_squared[:length // 2] else 0  # Partie gauche

    # Vérifier si la somme des deux parties donne n
    return left_part + right_part == n

# Cette fonction trouve tous les nombres de Kaprekar ayant exactement 8 chiffres.
def find_kaprekar_numbers() -> list[int]:
    kaprekar_numbers = []  # Liste pour stocker les nombres de Kaprekar

    # Parcourir tous les nombres de 10^7 à 10^8-1 (8 chiffres)
    for n in range(10**7, 10**8):
        if is_kaprekar(n):  # Vérifier si n est un nombre de Kaprekar
            kaprekar_numbers.append(n)  # Ajouter n à la liste si c'est un nombre de Kaprekar

    return kaprekar_numbers

# Appeler la fonction pour trouver tous les nombres de Kaprekar à 8 chiffres
kaprekar_numbers = find_kaprekar_numbers()

# Afficher le nombre total de nombres de Kaprekar trouvés et les afficher
print(f"Il y a {len(kaprekar_numbers)} nombres de Kaprekar à 8 chiffres.")
print("Les nombres de Kaprekar à 8 chiffres sont :")
for num in kaprekar_numbers:
    print(num)
