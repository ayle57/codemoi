# Exercice  2 : Trouver les nombres de Kaprekar à 8 chiffres

**Énoncé :** Trouver tous les nombres de Kaprekar en base 10 ayant exactement 8 chiffres. Un nombre de Kaprekar est un nombre dont le carré peut être découpé en deux parties, et la somme de ces parties donne le nombre d'origine.

---

## Ma démarche pour résoudre l'exercice :
1. **Comprendre le problème :** L'objectif est de trouver tous les nombres n ayant exactement 8 chiffres et vérifiant la condition suivante :
    - Lorsque l'on élève n au carré (n^2), le résultat peut être découpé en deux parties dont la somme est égale à n.
    - Par exemple, 703 est un nombre de Kaprekar car 703² = 494209 et on peut découper 494209 en 494 et 209, et leur somme donne 703.
2. **Analyser les conditions données :**
    - Nous cherchons des nombres ayant **exactement 8 chiffres**. Cela signifie que n doit être compris entre 10 000 000 et 99 999 999.
    - Le carré de n, soit n^2, doit pouvoir être découpé en deux parties dont la somme donne n.
3. **Calculer le carré de n :** Pour chaque nombre n dans l'intervalle [10 000 000, 99 999 999], nous allons calculer n^2.
4. **Découper le carré de n :** Une fois que nous avons n^2, nous devons le découper en deux parties :
    - La **partie droite** correspond aux derniers chiffres de n^2.
    - La **partie gauche** correspond aux chiffres restants.
    - La somme des deux parties doit être égale à n.
5. **Vérifier la condition de Kaprekar :** Après avoir effectué le découpage de n^2, nous vérifions si la somme des deux parties est égale à n.
6. **Rechercher tous les nombres de Kaprekar :** Cette étape consiste à parcourir tous les nombres de l'intervalle [10 000 000, 99 999 999] et à appliquer les étapes précédentes pour vérifier s'ils sont des nombres de Kaprekar.
