## Utilisateur

On étudie un montage intégrateur différentiel classique dans lequel les deux résistances ont la même valeur R et les deux condensateurs ont la même valeur C. Détermine Vs en fonction de V1 et V2. Explique ton raisonnement.

## IA

On suppose un montage intégrateur différentiel idéal à amplificateur opérationnel, avec deux entrées (V_1) et (V_2), chacune reliée à l’entrée inverseuse et non-inverseuse via des résistances (R), et une rétroaction capacitive (C).

Hypothèses classiques : ampli op idéal ⇒

* courant d’entrée nul,
* [[important](V_- = V_+)[\important]].

1. Tension au nœud d’entrée

L’entrée non-inverseuse reçoit (V_2) via une résistance (R), mais comme aucun courant n’entre dans l’ampli op, il n’y a pas de chute de tension dans cette résistance. Donc :
[
V_+ = V_2
]
Par égalité des potentiels :
[
V_- = V_2
]

2. Équation de courant au nœud inverseur

Au nœud (V_-), on applique la loi des nœuds. Deux branches :

* courant venant de (V_1) à travers (R),
* courant dans le condensateur de rétroaction vers la sortie (V_s).

Courant dans la résistance :
[
i_R = \frac{V_1 - V_-}{R} = \frac{V_1 - V_2}{R}
]

Courant dans le condensateur :
[
i_C = C \frac{d(V_- - V_s)}{dt} = C \frac{d(V_2 - V_s)}{dt}
]

Comme aucun courant ne rentre dans l’ampli op :
[
i_R = i_C
]

Donc :
[
\frac{V_1 - V_2}{R} = C \frac{d(V_2 - V_s)}{dt}
]

3. Mise sous forme exploitable

On développe :
[
\frac{V_1 - V_2}{R} = C \left( \frac{dV_2}{dt} - \frac{dV_s}{dt} \right)
]

Donc :
[
\frac{dV_s}{dt} = \frac{dV_2}{dt} - \frac{1}{RC}(V_1 - V_2)
]

4. Intégration

On intègre :
[
V_s(t) = V_2(t) - \frac{1}{RC} \int (V_1(t) - V_2(t)), dt + K
]

où (K) dépend des conditions initiales.

5. Interprétation

La sortie est donc :

* une copie de (V_2),
* moins l’intégrale de la différence (V_1 - V_2).

Autrement dit, le montage réalise un intégrateur de la tension différentielle (V_1 - V_2), avec une contribution directe de (V_2).
