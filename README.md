# Concours CodeMoi 2024-2025

Ce repository contient mes réponses aux problématiques posées par le [concours codemoi](https://iremsinfo.callicode.fr/) de l'irem&S Info.

## Table des Matières
- [Introduction]
- [Architecture](#architecture)
- [Choix Techniques](#choix-techniques)
- [Installation](#installation)
- [License](#licence)
- [Problèmes](#problèmes)
- [Auteurs](#auteurs)

---

## Introduction

Le concours se compose de quatre exercices portant sur différents sujets. Pour chaque exercice, il est demandé de fournir le fichier contenant le code source ainsi qu'un document explicatif détaillant notre démarche de résolution.

Le choix du langage de programmation est libre, bien que l'utilisation de Python soit obligatoire pour au moins une partie des exercices.
Dans ce projet, j'ai choisi d'utiliser **Python** et **Rust** en proposant 2 résolutions par exercice.

À noter que j'ai appris Python de manière autodidacte, et bien qu'il soit pratique, ce n'est pas un langage que j'apprécie particulièrement.

---

## Architecture

Le projet est structuré en deux dossiers principaux :

1. ``src``
Ce dossier contiendra les codes sources des solutions. Il sera organisé en deux sous-dossiers :
    - ``rust`` : Contenant l'environnement complet pour les solutions écrites en Rust.
    - ``python`` : Contenant l'environnement complet pour les solutions écrites en Python. Chaque exercice sera implémenté dans un fichier distinct.

J'espère que cette organisation vous conviendra et sera la plus claire et lisible.

---

## Choix Techniques

Comme dis au dessus, j'ai choisi de résoudre ces exercices en Python et Rust. On peut se demander pourquoi Rust, et la réponse est très simple, car c'est un language que j'apprend actuellement et que j'apprécie continuellement. Cela va contraster avec Python qui est un language haut-niveau.

---

## Installation

Pour exécuter correctement le projet en local, il est nécessaire de disposer des environnements Python et Rust (avec Cargo). Cette section est divisée en deux volets pour couvrir les spécificités de chaque langage.

Dans tous les cas, commencez par cloner ce dépôt ou télécharger l'archive associée depuis GitHub.

```bash
git clone https://github.com/ayle57/codemoi.git [directory]
cd directory
```

### Python
Pour exécuter les solutions écrites en Python, il suffit de lancer chaque script avec la commande appropriée :

```bash
python script.py
```

Cette opération est triviale, et je pars du principe que vous savez déjà comment utiliser Python.

### Rust
Les solutions en Rust nécessitent un environnement configuré avec Cargo. Si vous n'êtes pas familier avec cet outil, voici deux options :

- Utiliser l'exécutable pré-compilé
Toutes les solutions sont regroupées dans le fichier ``main.rs``. Pour simplifier l'exécution, j'ai compilé ce fichier et fourni un exécutable dans ce dépôt. Vous pouvez utiliser cet exécutable directement sans avoir besoin de configurer Cargo.

- Compiler et exécuter avec Cargo
Si vous souhaitez exécuter le projet à l'aide de Cargo, assurez-vous que l'environnement Rust est installé sur votre machine. Les dépendances nécessaires sont spécifiées dans le fichier Cargo.toml, qui fonctionne de manière similaire à un fichier ``package.json``. Pour compiler et exécuter le projet:

```bash
cargo run
```

Cela exécutera les solutions contenues dans le fichier ``main.rs``.

---

## Licence
Ce dépôt est publié sous la licence MIT. Pour plus d'informations, consultez le fichier ``LICENSE.md``.

---

## Problèmes

Je n'ai pas réussi à répondre à l'exercice 3. Je n'ai donc pas pu l'adapter en Rust. Étant donné que j'apprends Rust depuis 4 mois, je n'ai pas encore la maitrise des bibliothèques et n'ai donc pas eu un résultat satisfaisant.

---

## Auteurs
Allistair J. -  2nd9

