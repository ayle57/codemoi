import numpy as np
from PIL import Image
from typing import Tuple, List

# Définir la correspondance des couleurs (R : 0, N : 1, B : 2, S : 3)
COLORS: dict[int, Tuple[int, int, int]] = {
    0: (255, 0, 0),   # Rouge
    1: (0, 0, 0),     # Noir
    2: (0, 0, 255),   # Bleu
    3: (255, 255, 255)  # Blanc
}

# Règles de la phase 1 (règles pour les paires de couleurs voisines)
RULES: dict[Tuple[int, int], int] = {
    (0, 0): 1,  # RR -> N (Rouge Rouge donne Noir)
    (0, 1): 2,  # RN -> B (Rouge Noir donne Bleu)
    (0, 2): 3,  # RB -> S (Rouge Bleu donne Blanc)
    (0, 3): 1,  # RS -> N (Rouge Blanc donne Noir)
    (1, 1): 2,  # NN -> B (Noir Noir donne Bleu)
    (1, 2): 3,  # NB -> S (Noir Bleu donne Blanc)
    (1, 3): 0,  # NS -> R (Noir Blanc donne Rouge)
    (2, 2): 3,  # BB -> S (Bleu Bleu donne Blanc)
    (2, 3): 1,  # BS -> N (Bleu Blanc donne Noir)
    (3, 3): 1,  # SS -> N (Blanc Blanc donne Noir)
}

# Créer la matrice initiale 3x3, entièrement remplie de carreaux blancs (3)
def create_initial_matrix() -> np.ndarray:
    return np.full((3, 3), 3, dtype=int)

# Phase 1 : Remplir les emplacements basés sur les règles pour les voisins
def phase1(matrix: np.ndarray, new_matrix: np.ndarray) -> None:
    n = matrix.shape[0]  # Taille actuelle de la matrice
    for i in range(n):
        for j in range(n):
            # Remplir les emplacements verticaux (au-dessus et au-dessous)
            if i < n - 1:
                color1, color2 = matrix[i, j], matrix[i + 1, j]
                new_matrix[2 * i + 1, 2 * j] = RULES[tuple(sorted((color1, color2)))]
            # Remplir les emplacements horizontaux (à gauche et à droite)
            if j < n - 1:
                color1, color2 = matrix[i, j], matrix[i, j + 1]
                new_matrix[2 * i, 2 * j + 1] = RULES[tuple(sorted((color1, color2)))]

# Phase 2 : Remplir les coins restants basés sur la somme modulo 4
def phase2(matrix: np.ndarray, new_matrix: np.ndarray) -> None:
    n = matrix.shape[0]  # Taille actuelle de la matrice
    for i in range(n):
        for j in range(n):
            if i < n - 1 and j < n - 1:  # Coins intérieurs à remplir
                colors = [
                    matrix[i, j],
                    matrix[i + 1, j],
                    matrix[i, j + 1],
                    matrix[i + 1, j + 1],
                ]
                # Calcul de la couleur : somme des couleurs modulo 4
                new_matrix[2 * i + 1, 2 * j + 1] = sum(colors) % 4

# Fonction pour générer la mosaïque par itérations
def generate_mosaic(iterations: int) -> np.ndarray:
    # Démarrer avec une matrice 3x3 remplie de blanc
    matrix = create_initial_matrix()
    for _ in range(iterations):
        n = matrix.shape[0]  # Taille actuelle de la matrice
        new_size = 2 * n - 1  # Nouvelle taille après l'itération
        # Créer une nouvelle matrice vide pour la prochaine itération
        new_matrix = np.full((new_size, new_size), -1, dtype=int)
        new_matrix[::2, ::2] = matrix  # Placer les carreaux existants
        phase1(matrix, new_matrix)  # Appliquer la phase 1
        phase2(matrix, new_matrix)  # Appliquer la phase 2
        matrix = new_matrix  # Mettre à jour pour la prochaine itération
    return matrix

# Convertir la matrice en image
def matrix_to_image(matrix: np.ndarray) -> Image:
    height, width = matrix.shape  # Dimensions de la matrice
    image = Image.new("RGB", (width, height))  # Créer une image vide
    for i in range(height):
        for j in range(width):
            # Associer chaque valeur de la matrice à une couleur
            image.putpixel((j, i), COLORS[matrix[i, j]])
    return image

# Créer et sauvegarder l'image finale
def save_mosaic_image(iterations: int, path: str) -> None:
    # Générer la mosaïque finale de taille 257x257 (7 itérations)
    mosaic_matrix = generate_mosaic(iterations)
    mosaic_image = matrix_to_image(mosaic_matrix)
    mosaic_image.save(path)  # Sauvegarder l'image
    print(f"L'image a été sauvegardée à {path}")  # Afficher le chemin de l'image générée

# Appeler la fonction pour créer et sauvegarder l'image de la mosaïque
save_mosaic_image(7, "./mosaic_257x257.png")  # Sauvegarder l'image à l'emplacement spécifié
