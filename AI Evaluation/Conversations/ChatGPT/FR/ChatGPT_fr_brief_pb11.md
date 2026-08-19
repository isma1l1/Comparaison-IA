## Utilisateur

Réponds de manière concise en supprimant tout propos inutile.
On étudie un montage intégrateur différentiel classique dans lequel les deux résistances ont la même valeur R et les deux condensateurs ont la même valeur C. Détermine Vs en fonction de V1 et V2. Explique ton raisonnement.

## IA

Op-amp idéal ⇒ [[important](V^- = V^+ = V_x)[\important]].

Dans chaque branche (symétrie R, C identiques), on écrit la loi des nœuds. Le montage est tel que chaque entrée forme un intégrateur vers la sortie, et la différence des équations élimine (V_x).

On obtient directement une équation différentielle sur la sortie :
[
\frac{dV_s}{dt} = \frac{V_2 - V_1}{RC}.
]

En intégrant :
[[important][
V_s(t) = \frac{1}{RC}\int (V_2(t) - V_1(t)),dt + V_s(0).
][\important]]

La sortie est donc proportionnelle à l’intégrale de la différence des deux entrées, avec constante (1/RC).
