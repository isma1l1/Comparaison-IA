## Utilisateur

Voici un montage d'électronique analogique.
Détermine la relation entrée-sortie du filtre présenté (les quatre résistances ont la même valeur). Explique ton raisonnement.
*(image de schéma d’un montage avec un amplificateur opérationnel, deux entrées v1 et v2 via résistances, et une boucle de rétroaction avec deux résistances vers la masse et la sortie)*

## IA

On suppose un amplificateur opérationnel idéal (entrée infiniment impédante, gain infini, etc.) et que les **quatre résistances sont égales à R**.

---

### 1) Tension à l’entrée non-inverseuse (+)

Les deux sources (v_1) et (v_2) sont reliées à l’entrée (+) via deux résistances égales.

Comme l’entrée de l’AOP ne consomme **aucun courant**, ce nœud est simplement un **pont diviseur symétrique** entre (v_1) et (v_2).

Donc :
[[important]
[
V_+ = \frac{v_1 + v_2}{2}
][\important]]

---

### 2) Fonctionnement de la boucle de rétroaction

Le montage côté entrée inverseuse (−) est un **amplificateur non-inverseur classique** :

* Résistance (R) entre sortie et entrée − (rétroaction)
* Résistance (R) entre entrée − et masse

Le gain d’un ampli non-inverseur vaut :
[
A_v = 1 + \frac{R_f}{R_g}
]

Ici :
[[important]
[
A_v = 1 + \frac{R}{R} = 2
][\important]]

---

### 3) Relation entrée-sortie

L’AOP impose ([[important]V_- \approx V_+[\important]]), donc :

[
v_s = A_v \cdot V_+ = 2 \cdot \frac{v_1 + v_2}{2}
]

---

### ✅ Résultat final :

[
\boxed{[[important]v_s = A_v \cdot V_+ = v_1 + v_2[\important]]}
]

---

### 💡 Interprétation

Ce montage réalise simplement un **additionneur analogique** (somme de deux signaux), mais de façon élégante :

* Moyenne des entrées à l’entrée +
* Puis amplification ×2

---

Si tu veux, je peux aussi te montrer comment modifier ce montage pour faire une **moyenne**, une **soustraction**, ou un **filtre avec fréquence de coupure** 👍
