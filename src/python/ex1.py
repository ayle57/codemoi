# Somme que les triplets doivent satisfaire
sum_required: int = 141
# Produit que les triplets doivent satisfaire
product_required: int = 98136

"""
Cette fonction vérifie si les entiers x1, x2, x3 respectent la somme et le produit requis
Elle retourne un booléen indiquant si le triplet est valide ou non
"""
def check_triplet(x1: int, x2: int, x3: int) -> bool:
    return x1 + x2 + x3 == sum_required and x1 * x2 * x3 == product_required

# Cette fonction retourne une liste contenant les tuples qui représentent les triplets valides
def find_triplets() -> list[tuple[int, int, int]]:
    triplets: list[tuple[int, int, int]] = []

    # Itérer à travers toutes les valeurs possibles pour x1 et x2
    for x1 in range(1, sum_required):
        for x2 in range(1, sum_required - x1):
            x3: int = sum_required - x1 - x2  # Calculer x3 en fonction de la contrainte de la somme

            # Vérifier si x3 est positif et que le triplet respecte la somme et le produit requis
            if x3 > 0 and check_triplet(x1, x2, x3):
                triplets.append((x1, x2, x3))  # Ajouter le triplet valide à la liste

    return triplets

# Appeler la fonction pour trouver les triplets valides
valid_triplets: list[tuple[int, int, int]] = find_triplets()

# Afficher le nombre de triplets valides et chaque triplet valide
print(f"Il y a {len(valid_triplets)} triplets valides.")
for triplet in valid_triplets:
    print(triplet)
