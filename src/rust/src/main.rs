// Somme et produit requis pour les triplets
const SUM_REQUIRED: i64 = 141;
const PRODUCT_REQUIRED: i64 = 98136;

// Vérifie si un triplet respecte la somme et le produit requis
fn check_triplet(x1: i64, x2: i64, x3: i64) -> bool {
    x1 + x2 + x3 == SUM_REQUIRED && x1 * x2 * x3 == PRODUCT_REQUIRED
}

// Trouve tous les triplets valides
fn find_triplets() -> Vec<(i64, i64, i64)> {
    let mut triplets: Vec<(i64, i64, i64)> = Vec::new();

    // Itérer à travers toutes les valeurs possibles pour x1 et x2
    for x1 in 1..SUM_REQUIRED {
        for x2 in 1..(SUM_REQUIRED - x1) {
            let x3 = SUM_REQUIRED - x1 - x2;  // Calculer x3 en fonction de la contrainte de la somme

            // Vérifier si x3 est positif et que le triplet respecte la somme et le produit requis
            if x3 > 0 && check_triplet(x1, x2, x3) {
                triplets.push((x1, x2, x3));  // Ajouter le triplet valide à la liste
            }
        }
    }

    triplets
}

// Vérifie si un nombre est un nombre de Kaprekar
fn is_kaprekar(n: i64) -> bool {
    let n_squared = n * n;  // Calculer le carré de n
    let n_squared_str = n_squared.to_string();  // Convertir le carré de n en chaîne de caractères

    // Découper le carré en deux parties
    let length = n_squared_str.len();
    let right_part: i64 = n_squared_str[length / 2..]
        .parse()
        .unwrap_or(0);  // Partie droite
    let left_part: i64 = n_squared_str[..length / 2]
        .parse()
        .unwrap_or(0);  // Partie gauche

    // Vérifier si la somme des deux parties donne n
    left_part + right_part == n
}

// Trouve tous les nombres de Kaprekar ayant exactement 8 chiffres
fn find_kaprekar_numbers() -> Vec<i64> {
    let mut kaprekar_numbers = Vec::new();

    // Parcourir tous les nombres de 10^7 à 10^8-1 (8 chiffres)
    for n in 10_000_000..10_000_0000 {
        if is_kaprekar(n) {  // Vérifier si n est un nombre de Kaprekar
            kaprekar_numbers.push(n);  // Ajouter n à la liste si c'est un nombre de Kaprekar
        }
    }

    kaprekar_numbers
}

fn main() {
    // Exercice 1 : Triplets valides
    let valid_triplets = find_triplets();
    println!("Il y a {} triplets valides.", valid_triplets.len());
    for triplet in valid_triplets {
        println!("{:?}", triplet);
    }

    // Exercice 2 : Nombres de Kaprekar à 8 chiffres
    let kaprekar_numbers = find_kaprekar_numbers();
    println!("Il y a {} nombres de Kaprekar à 8 chiffres.", kaprekar_numbers.len());
    for num in kaprekar_numbers {
        println!("{}", num);
    }
}
