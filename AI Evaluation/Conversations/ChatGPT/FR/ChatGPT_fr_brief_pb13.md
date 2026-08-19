## Utilisateur

Réponds de manière concise en supprimant tout propos inutile.
Les deux ALIs du montage fonctionnant en régime linéaire, montre que ce montage équivaut à un condensateur de capacité C, exprime C en fonction de C0 et alpha et dis quel est l'intérêt d'un tel montage.

*(image d'un schéma électronique montrant deux ALI, deux résistances αR et (1−α)R, et un condensateur C₀ montés pour réaliser une capacité équivalente)*

## IA

ALI idéaux en régime linéaire ⇒

* (V_-=V_+) et (i_-=i_+=0).

Notons :

* (u) la tension d’entrée,
* (v) le nœud entre les deux résistances.

L’ALI ① est monté en suiveur : sa sortie vaut donc (u).

L’ALI ② a son entrée (+) à la masse, donc son entrée (-) (le nœud (v)) est au potentiel nul :
[
v=0.
]

Le pont résistif entre (u) et la sortie de ② donne :
[
\frac{u-0}{\alpha R}=\frac{0-v_s}{(1-\alpha)R}
]
d’où
[
v_s=-\frac{1-\alpha}{\alpha}u.
]

Le condensateur (C_0) est branché entre (u) et (v_s), donc sa tension vaut :
[
u-v_s
= u+\frac{1-\alpha}{\alpha}u
=\frac{u}{\alpha}.
]

Le courant absorbé :
[
i=C_0\frac{d}{dt}(u-v_s)
= \frac{C_0}{\alpha}\frac{du}{dt}.
]

Ainsi le dipôle vérifie :
[
i=C\frac{du}{dt}
]
avec
[
\boxed{C=\frac{C_0}{\alpha}}.
]

Comme (0<\alpha<1), on obtient :
[
C>C_0.
]

Intérêt :

* réaliser une grande capacité équivalente avec un petit condensateur physique ;
* éviter l’emploi de condensateurs volumineux (technique de multiplication de capacité, type « Miller »).
