# Exercice 4 : Mosaïque Persane 1

**Énoncé :** Vous devez fournir une image représentant le résultat d’une mosaïque persane de taille 257 × 257, chaque pixel correspondant à un carreau de la mosaïque.
**Sortie :** ./mosaic_257x257.png

---

## Ma démarche pour résoudre l'exercice :

### 1. **Comprendre le problème :**

L’objectif est de générer une mosaïque de taille \( 257 \times 257 \), à partir d’une petite matrice initiale de \( 3 \times 3 \) carreaux blancs. Cette matrice va ensuite être transformée progressivement par un processus itératif qui dure **7 étapes**.

À chaque étape :
- Les carreaux existants sont étendus en appliquant des règles spécifiques pour déterminer la couleur des nouveaux carreaux.
- Le processus repose sur deux phases :
   - **Phase 1** : Remplir les cases intermédiaires entre les carreaux en utilisant des règles basées sur les voisins immédiats.
   - **Phase 2** : Remplir les cases restantes (les coins) en utilisant les couleurs des quatre cases voisines et en faisant un calcul modulaire.

---

### 2. **Comprendre les règles :**

#### Phase 1 : Remplissage des cases intermédiaires
- Les cases qui se trouvent entre les carreaux de la matrice initiale sont remplies selon les **règles de voisinage**.
- Par exemple, si un carreau est voisin de deux autres de couleurs différentes, on applique une règle spécifique pour déterminer la couleur du carreau à remplir. Il y a 10 règles pour ces paires de couleurs.

#### Phase 2 : Remplissage des cases de coin
- Les coins de la matrice (qui ne sont pas encore remplis) sont attribués une couleur en fonction des quatre couleurs voisines.
- Chaque couleur est associée à un nombre entre 0 et 3, et on additionne ces valeurs avant d’appliquer un calcul **modulo 4** pour obtenir la couleur finale de la case de coin.

---

### 3. **Étapes de la solution :**

#### Étape 1 : Initialisation
La mosaïque commence avec une matrice \( 3 \times 3 \) remplie uniquement de carreaux blancs.

#### Étape 2 : Génération de la mosaïque
- **Itération 1 à 7 :** À chaque itération, la taille de la mosaïque double, passant de \( 3 \times 3 \) à \( 5 \times 5 \), puis à \( 9 \times 9 \), etc., jusqu'à ce qu'on obtienne une matrice de \( 257 \times 257 \).
- À chaque étape, les carreaux sont placés selon les règles de la phase 1, puis les coins sont remplis en appliquant la phase 2.

#### Étape 3 : Conversion en image
Une fois que la mosaïque a atteint sa taille finale, elle est convertie en une image où chaque carreau est représenté par un pixel coloré.
Les couleurs sont associées aux valeurs RGB suivantes :
- Rouge (R) : (255, 0, 0)
- Noir (N) : (0, 0, 0)
- Bleu (B) : (0, 0, 255)
- Blanc (S) : (255, 255, 255)

#### Étape 4 : Sauvegarde de l'image
L’image est ensuite enregistrée sous le nom **`mosaic_257x257.png`**.

---

### 4. **Description du processus Python :**

Le script Python suit ces étapes :

1. **Initialisation de la matrice :** La fonction `create_initial_matrix()` crée la matrice initiale de \( 3 \times 3 \), remplie de carreaux blancs.

2. **Phase 1 :** La fonction `phase1()` applique les règles de voisinage pour remplir les cases intermédiaires de la matrice.

3. **Phase 2 :** La fonction `phase2()` remplit les coins en utilisant les valeurs des quatre voisins et le calcul modulo 4.

4. **Génération de la mosaïque :** La fonction `generate_mosaic()` effectue les 7 itérations nécessaires pour créer la mosaïque finale de \( 257 \times 257 \).

5. **Conversion en image :** La fonction `matrix_to_image()` convertit la matrice finale en une image où chaque couleur est traduite en un pixel RGB.

---

### 5. **Résultat attendu :**

En exécutant le script, vous obtiendrez une image de **257 × 257** pixels représentant la mosaïque persane générée. Cette image sera enregistrée sous le nom **`mosaic_257x257.png`** et reflétera le résultat du processus itératif décrit ci-dessus.
