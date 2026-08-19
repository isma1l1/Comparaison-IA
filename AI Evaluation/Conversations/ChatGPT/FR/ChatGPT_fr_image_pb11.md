## Utilisateur

Voici un montage d'électronique analogique.
Les deux résistances R et les deux condensateurs C sont identiques. Exprime dans le domaine fréquentiel puis temporel la relation entre la tension de sortie et les deux tensions d’entrée du montage. Explique ton raisonnement.
*(image de schéma d’un amplificateur opérationnel avec deux entrées e1 et e2 via des résistances, une rétroaction capacitive, et un condensateur à la masse sur l’entrée non-inverseuse)*

## IA

On suppose l’amplificateur opérationnel idéal (courant d’entrée nul, et ([[important]v_-=v_+)[\important]]).

Notons (S(j\omega)), (E_1(j\omega)), (E_2(j\omega)) les transformées de Fourier.

1. Calcul de la tension au nœud non-inverseur

Le nœud (v_+) est relié à (e_2) par (R) et à la masse par (C). C’est un filtre passe-bas :

[
[[important]v_+(j\omega)=E_2(j\omega)[\important]],
\frac{Z_C}{R+Z_C}=E_2(j\omega),
\frac{1/(j\omega C)}{R+1/(j\omega C)}=\frac{E_2(j\omega)}{1+j\omega RC}.
]

Donc
[
v_-(j\omega)=v_+(j\omega)=\frac{E_2(j\omega)}{1+j\omega RC}.
]

2. Écriture de la loi des nœuds au nœud inverseur

Courants sortants du nœud (v_-) :

[
\frac{v_- - E_1}{R} + j\omega C (v_- - S)=0.
]

On isole (S) :

[
j\omega C (v_- - S)= -\frac{v_- - E_1}{R}
]

[
S = v_- + \frac{v_- - E_1}{j\omega RC}.
]

3. Substitution de (v_-)

[
S = \frac{E_2}{1+j\omega RC} \left(1+\frac{1}{j\omega RC}\right) - \frac{E_1}{j\omega RC}.
]

Or
[
1+\frac{1}{j\omega RC}=\frac{1+j\omega RC}{j\omega RC},
]
ce qui simplifie exactement :

[[important][
S(j\omega)=\frac{E_2(j\omega)-E_1(j\omega)}{j\omega RC}.
][\important]]

4. Domaine temporel

La division par (j\omega) correspond à une intégration. Donc :

[[important][
s(t)=\frac{1}{RC}\int (e_2(t)-e_1(t)),dt + \text{constante}.
][\important]]

Conclusion : le montage réalise un intégrateur de la différence des deux entrées.
