## Utilisateur

Voici un montage d'électronique analogique.
Détermine la relation entrée-sortie du filtre présenté. Explique ton raisonnement.
*(image de schéma d’un montage à amplificateur opérationnel avec résistances R et R’, deux entrées e1 et e2, et une sortie s)*

## IA

Ce montage est un **amplificateur différentiel** (ou soustracteur) basé sur un AOP [important]idéal[/important].

### 1) Hypothèses (AOP idéal)

* Courant d’entrée nul
* ( [important]V^- = V^+[/important] ) (régime linéaire avec [important]rétroaction[/important])

---

### 2) Tension à l’entrée non-inverseuse (+)

Le nœud ( V^+ ) est un simple pont diviseur entre ( e_2 ) et la masse :

[
[important]V^+ = \frac{R'}{R + R'} , e_2[/important]
]

---

### 3) Tension à l’entrée inverseuse (−)

Même principe : le nœud ( V^- ) est un pont diviseur entre ( e_1 ) et la sortie ( s ) :

[
[important]V^- = \frac{R'}{R + R'} , e_1 + \frac{R}{R + R'} , s[/important]
]

---

### 4) Égalité des deux entrées

[
V^- = V^+
]

Donc :

[
\frac{R'}{R + R'} e_1 + \frac{R}{R + R'} s = \frac{R'}{R + R'} e_2
]

On simplifie par ( R + R' ) :

[
R' e_1 + R s = R' e_2
]

---

### 5) Relation entrée-sortie

[
R s = R'(e_2 - e_1)
]

[
\boxed{, [/important]s = \frac{R'}{R} (e_2 - e_1) [/important],}
]

---

### 6) Interprétation

* Le montage **soustrait** les deux entrées
* Le gain est ( \frac{R'}{R} )
* Si ( R' = R ), alors ( s = e_2 - e_1 )

---

Si tu veux, je peux aussi te montrer comment reconnaître ce type de montage en un coup d’œil 👀
