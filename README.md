# Grid‑Pairing Optimisation Problem

## 1  Introduction
On cherche à résoudre un problème d’appariement dans une grille.  
L’objectif est de former des **paires de cases adjacentes** tout en respectant
plusieurs contraintes liées aux couleurs ; il faut également **minimiser un
score** égal :

* à la somme, pour chaque paire, de la valeur absolue de la différence entre
  les scores des deux cases reliées 
* plus la somme des scores des cases restées non appariées.

Pour atteindre ce but, on applique successivement :

1. un algorithme **glouton** fournissant une première solution. Mais cela n'est pas sufficient.
2. l’algorithme de **Ford–Fulkerson** afin d’obtenir un flot maximal.
3. puis l’algorithme de **Bellman–Ford** pour trouver le flot de coût minimal.

---

## 1.1  Description du problème
On considère une grille de taille $m \times n$ (avec $m \ge 2,\; n \ge 2$).

* $n$ : nombre de lignes  $m$ : nombre de colonnes  
* Chaque cellule possède  
  * une **couleur** :
    $$c(i,j) \in \{0,1,2,3,4\},\qquad 0 \le i < n,\; 0 \le j < m $$
    | Code | Couleur (fr) | Couleur (en) | Abréviation |
    |------|--------------|--------------|-------------|
    | 0    | blanc        | white        | `w` |
    | 1    | rouge        | red          | `r` |
    | 2    | bleu         | blue         | `b` |
    | 3    | vert         | green        | `g` |
    | 4    | noir         | black        | `k` |
  * une **valeur positive** :$\;v(i,j) \in \mathbb{N}^{\*}$.

---

## 1.2  Contraintes

### 1.2.1  Adjacence
Deux cellules peuvent être appariées **uniquement si elles sont adjacentes** :
$$
  |i_1-i_2| + |j_1-j_2| = 1
$$
(c’est‑à‑dire : même ligne & colonne voisine, **ou** même colonne & ligne
voisine).

### 1.2.2  Couleurs autorisées

| Couleur | Peut être reliée à |
|---------|-------------------|
| **Blanc (0)** | Blanc (0), Rouge (1), Bleu (2), Vert (3) |
| **Rouge (1)** | Blanc (0), Rouge (1), Bleu (2) |
| **Bleu (2)**  | Blanc (0), Rouge (1), Bleu (2) |
| **Vert (3)**  | Blanc (0), Vert (3) |
| **Noir (4)**  | *(aucune couleur : isolement total)* |

### 1.2.3  Exclusivité
Chaque cellule ne peut être utilisée **que dans une unique paire**.

---

## 1.3  Objectif de minimisation
Soient  

* $P$ : l’ensemble des **paires**
  $((i_0,j_0),(i_1,j_1))$ formées,  
* $U$ : l’ensemble des **cellules non appariées**.

La fonction objectif à minimiser est :
$$\min\!\Bigl(\sum_{((i_0,j_0),(i_1,j_1)) \in P} \bigl|\,v(i_0,j_0)-v(i_1,j_1)\bigr|+ \sum_{(i,j) \in U} v(i,j)\Bigr)$$

---

## 2  Algorithmes utilisés
1. **Greedy (glouton)** – construction d’une solution de départ.  
2. **Ford–Fulkerson** – calcul d’un flot maximal sur le graphe construit.  
3. **Bellman–Ford** – amélioration vers un flot de *coût minimal*.

---
