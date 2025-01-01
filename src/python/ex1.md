# Exercice 1 : Somme et produit de 3 nombres

**Énoncé :** Combien y a-t-il de triplets de nombres entiers positifs dont la somme vaut 141 et dont le produit vaut 98 136 ?

---

## Ma démarche pour résoudre l'exercice :
1. **Comprendre le problème :** L'objectif est de trouver trois entiers positifs x1, x2, et x3 qui satisfont deux conditions :
   - Leur somme doit être égale à 141 : x1 + x2 + x3 = 141.
   - Leur produit doit être égal à 98 136 : x1 × x2 × x3 = 98 136.
2. **Analyser les conditions données :**
   - La première condition est de trouver trois nombres dont la somme est 141.
   - La deuxième condition impose que le produit de ces trois nombres soit exactement 98 136.
3. **Factoriser le produit :** Pour mieux comprendre quels nombres pourraient faire partie de ces triplets, il est utile de commencer par factoriser 98 136. La décomposition en facteurs premiers de ce nombre est la suivante : 98 136 = 2^4 × 3^2 × 7 × 11. Cette factorisation nous donne des informations précieuses, car elle nous montre quels sont les facteurs de 98 136. Cela nous permet de chercher des combinaisons de ces facteurs pour former nos trois entiers.
4. **Explorer les combinaisons possibles :** Maintenant, il faut tester différentes combinaisons d'entiers, en utilisant les facteurs de 98 136, tout en veillant à ce que leur somme soit bien égale à 141. Cela implique de répartir correctement les facteurs 2^4, 3^2, 7, et 11 entre x1, x2, et x3.
5. **Rechercher tous les triplets :** Cette étape consiste à chercher systématiquement tous les triplets de nombres qui respectent les deux conditions : la somme égale à 141 et le produit égal à 98 136. C'est ici qu'un algorithme ou une méthode de recherche peut être utile pour explorer toutes les possibilités.
6. **Vérifier chaque triplet :** Une fois les triplets identifiés, il est important de les vérifier :
   - La somme des trois entiers doit bien être égale à 141.
   - Le produit des trois entiers doit bien être égal à 98 136.
