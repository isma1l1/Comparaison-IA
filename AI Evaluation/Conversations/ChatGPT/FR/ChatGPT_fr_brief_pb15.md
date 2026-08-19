## Utilisateur

Réponds de manière concise en supprimant tout propos inutile.
Identifie sans calcul la nature du filtre ci-contre, établis sa fonction de transfert sous forme canonique, et détermine les valeurs à donner à R' et C pour R = 1 kilo ohm, si on souhaite une pulsation de coupure oméga0 = 10^4 rad.s^-1 et un gain de 20 dB en haute fréquence.

*(image de un schéma électronique représentant un filtre actif avec un amplificateur opérationnel en configuration inverseuse, une résistance R en série avec un condensateur C à l’entrée, et une résistance de rétroaction R' entre la sortie et l’entrée inverseuse. Les bornes d’entrée sont notées e et la sortie s.)*

## IA

AOP idéal, entrée non-inverseuse à la masse (\Rightarrow) montage inverseur.

* À basse fréquence, (C) bloque (\Rightarrow s=0).
* À haute fréquence, (C) est un court-circuit (\Rightarrow) gain constant.

Donc c’est un **filtre passe-haut du 1er ordre**.

Impédances :
[
Z_e=R+\frac1{j\omega C},\qquad Z_f=R'
]

Fonction de transfert :
[
H(j\omega)=\frac{s}{e}=-\frac{R'}{R+\frac1{j\omega C}}
]

En multipliant par (j\omega C) :
[
H(j\omega)=-\frac{R'j\omega C}{1+j\omega RC}
]

Forme canonique :
[
H(j\omega)= -\frac{R'}{R},\frac{j\omega/\omega_0}{1+j\omega/\omega_0}
]
avec
[
\omega_0=\frac1{RC}
]

Gain en haute fréquence :
[
G_\infty=\left|\frac{R'}{R}\right|
]

Or (20,\mathrm{dB}\Rightarrow G_\infty=10), donc
[
\frac{R'}{R}=10
]
et comme (R=1,\text{k}\Omega),
[
\boxed{R'=10,\text{k}\Omega}
]

Puis
[
\omega_0=\frac1{RC}=10^4
]
donc
[
C=\frac1{R\omega_0}
=\frac1{10^3\times10^4}
=10^{-7},\text{F}
]

[
\boxed{C=100,\text{nF}}
]
