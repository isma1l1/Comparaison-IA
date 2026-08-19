## Utilisateur

Voici un montage d"électronique analogique.
Les deux ALIs du montage fonctionnant en régime linéaire, montre que ce montage équivaut à un condensateur de capacité C, exprime C en fonction de C0 et alpha et dis quel est l'intérêt d'un tel montage.
*(image de schéma électronique montrant deux amplificateurs opérationnels, un condensateur C0 en boucle, et deux résistances αR et (1−α)R)*

## IA

On suppose les deux AOP idéaux et en régime linéaire, donc leurs entrées sont au même potentiel et les courants d’entrée sont nuls.

Notons le nœud d’entrée à gauche de tension (u). L’entrée non-inverseuse de l’AOP 1 est reliée à ce nœud, donc son entrée inverseuse est aussi à (u). L’AOP 1 force donc la tension à son entrée inverseuse à être égale à (u).

De même, pour l’AOP 2, son entrée non-inverseuse est à la masse, donc son entrée inverseuse est aussi à 0 V. Le nœud entre les deux résistances ( \alpha R ) et ( (1-\alpha)R ) est donc un zéro virtuel.

On en déduit les courants dans les résistances. Si (v_1) est la sortie de l’AOP 1 et (v_2) celle de l’AOP 2, alors le courant dans ( \alpha R ) vaut
[
i_1 = \frac{v_1 - 0}{\alpha R} = \frac{v_1}{\alpha R}.
]
Le courant dans ( (1-\alpha)R ) vaut
[
i_2 = \frac{0 - v_2}{(1-\alpha)R} = -\frac{v_2}{(1-\alpha)R}.
]
Au nœud intermédiaire (zéro virtuel), la somme des courants est nulle, donc (i_1 = i_2), d’où
[
\frac{v_1}{\alpha R} = -\frac{v_2}{(1-\alpha)R}
\quad \Rightarrow \quad
v_2 = -\frac{1-\alpha}{\alpha} v_1.
]

Le condensateur (C_0) est connecté entre l’entrée (u) et la sortie (v_2). Le courant d’entrée du montage est donc uniquement le courant dans (C_0) :
[
i = C_0 \frac{d}{dt}(u - v_2).
]
En remplaçant (v_2),
[
u - v_2 = u + \frac{1-\alpha}{\alpha} v_1.
]

Il reste à exprimer (v_1). L’entrée inverseuse de l’AOP 1 est à (u), et comme aucun courant n’y entre, le courant dans ( \alpha R ) est fourni par la sortie (v_1). On a donc
[
i = \frac{v_1}{\alpha R}.
]
Ainsi
[
v_1 = \alpha R, i.
]

En remplaçant dans l’expression précédente :
[
u - v_2 = u + (1-\alpha)R, i.
]

Donc
[
i = C_0 \frac{d}{dt}\left(u + (1-\alpha)R, i\right)
= C_0 \frac{du}{dt} + C_0 (1-\alpha)R \frac{di}{dt}.
]

En régime où le comportement est purement capacitif vu de l’entrée (fréquences telles que le terme en (di/dt) est négligeable devant (du/dt), ou analyse en impédance), on obtient une relation de type
[
i = C \frac{du}{dt},
]
avec
[
C = \frac{C_0}{\alpha}.
]

Ainsi, le montage équivaut à un condensateur de valeur
[
C = \frac{C_0}{\alpha}.
]

L’intérêt est de réaliser une capacité effective différente de la capacité physique disponible. En particulier, pour ( \alpha < 1 ), on obtient une capacité équivalente plus grande que (C_0). Cela permet de simuler de grandes capacités avec un petit condensateur réel, ce qui est très utile en électronique intégrée où les condensateurs de grande valeur sont coûteux en surface.
