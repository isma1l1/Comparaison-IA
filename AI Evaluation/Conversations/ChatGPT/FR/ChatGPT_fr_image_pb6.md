## Utilisateur

Voici un montage d'électronique analogique.
Etablis l'expression de Vout en fonction des tensions en entrée. Explique ton raisonnement.
*(image de schéma d’un amplificateur opérationnel avec deux entrées Vin1 et Vin2, résistances R1, R2, Rf et Rg, et une sortie Vout)*

## IA

On suppose l’ampli op idéal (gain infini, courant d’entrée nul, et (V^- = V^+)).

---

### 1) Tension à l’entrée non-inverseuse (V^+)

Le nœud (+) est un [important]pont diviseur[/important] entre (V_{in2}) (via (R_2)) et la masse (via (R_g)) :

[
[important]V^+ = V_{in2},\frac{R_g}{R_2 + R_g}[/important]
]

---

### 2) Égalité des entrées de l’AO

Ampli op idéal en [important]régime linéaire[/important] ⇒
[
[important]V^- = V^+[/important] = V_{in2},\frac{R_g}{R_2 + R_g}
]

---

### 3) Écriture de la [important]loi des nœuds[/important] au point (V^-)

Au nœud inverseur, aucun courant n’entre dans l’AO, donc :

[
[important]\frac{V_{in1} - V^-}{R_1} + \frac{V_{out} - V^-}{R_f} = 0[/important]
]

---

### 4) Résolution

On isole (V_{out}) :

[
\frac{V_{out} - V^-}{R_f} = - \frac{V_{in1} - V^-}{R_1}
]

[
V_{out} - V^- = -\frac{R_f}{R_1}(V_{in1} - V^-)
]

[
[important]V_{out} = V^- \left(1 + \frac{R_f}{R_1}\right) - \frac{R_f}{R_1} V_{in1}[/important]
]

---

### 5) Substitution de (V^-)

[
[important]V_{out} = \left(1 + \frac{R_f}{R_1}\right)\left( \frac{R_g}{R_2 + R_g} V_{in2} \right) - \frac{R_f}{R_1} V_{in1}[/important]
]

---

### Résultat final

[
\boxed{
V_{out} = \left(1 + \frac{R_f}{R_1}\right)\frac{R_g}{R_2 + R_g},V_{in2}
;-;
\frac{R_f}{R_1},V_{in1}
}
]

---

### Interprétation

* (V_{in1}) est **amplifié en inverseur**
* (V_{in2}) est **atténué puis amplifié en non-inverseur**
* Le montage agit comme un **soustracteur pondéré**

Si tu veux, je peux te montrer le cas particulier où ça devient un vrai amplificateur différentiel (avec symétrie des résistances).
