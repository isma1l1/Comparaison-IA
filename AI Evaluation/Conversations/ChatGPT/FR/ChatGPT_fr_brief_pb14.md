## Utilisateur

Réponds de manière concise en supprimant tout propos inutile.

L'ALI du montage fonctionnant en régime linéaire, identifie la nature du filtre, établis sa fonction de transfert, identifie une pulsation caractéristique oméga0, représente son diagramme de Bode en gain, discute l'allure du signal de sortie pour un créneau en entrée.

*(image de un schéma électronique représentant un filtre actif à amplificateur opérationnel avec deux résistances R, deux condensateurs C, une entrée e et une sortie s)*

## IA

ALI idéal en régime linéaire : (v_-=v_+=v_s).

Notons :

* (v_1) : nœud entre les deux résistances,
* (v_2) : entrée (+) de l’ALI.

Comme l’entrée (-) est reliée à la sortie :
[
v_s=v_2
]
L’ALI fonctionne donc en suiveur : la sortie reproduit (v_2).

Écriture des lois des nœuds :

Au nœud (v_2) :
[
\frac{v_2-v_1}{R}+Cs,v_2=0
]
d’où
[
v_1=v_2(1+RCs)
]

Au nœud (v_1) :
[
\frac{v_1-e}{R}+\frac{v_1-v_2}{R}+Cs(v_1-v_s)=0
]
avec (v_s=v_2), donc
[
\frac{v_1-e}{R}+\left(\frac1R+Cs\right)(v_1-v_2)=0
]

En remplaçant (v_1=v_2(1+RCs)) :
[
e=v_2\left(1+3RCs+(RCs)^2\right)
]

Ainsi :
[
\boxed{H(s)=\frac{s}{e}=\frac{1}{1+3RCs+(RCs)^2}}
]

---

## Nature du filtre

Le gain statique vaut :
[
H(0)=1
]
et pour (\omega\to\infty),
[
|H(j\omega)|\to0
]
⇒ **filtre passe-bas du 2ᵉ ordre**.

---

## Pulsation caractéristique

Sous forme canonique :
[
H(s)=\frac{1}{1+2\xi \frac{s}{\omega_0}+\left(\frac{s}{\omega_0}\right)^2}
]

Identification :
[
\boxed{\omega_0=\frac1{RC}}
]
et
[
2\xi=3 \quad\Rightarrow\quad \xi=\frac32
]

Filtre très amorti (pas de résonance).

---

## Diagramme de Bode (gain)

[
|H(j\omega)|=\frac{1}{\sqrt{(1-\omega^2/\omega_0^2)^2+9(\omega/\omega_0)^2}}
]

Allure :

* pour (\omega\ll\omega_0) :
  [
  G_{\mathrm{dB}}\approx0,\mathrm{dB}
  ]
* vers (\omega_0) :
  transition monotone sans bosse ;
* pour (\omega\gg\omega_0) :
  [
  |H|\sim\left(\frac{\omega_0}{\omega}\right)^2
  ]
  soit une pente :
  [
  \boxed{-40\ \mathrm{dB/dec}}
  ]

---

## Réponse à un créneau

Un créneau contient des harmoniques élevées.
Le filtre passe-bas :

* conserve les basses fréquences,
* atténue fortement les hautes.

Donc :

* fronts arrondis,
* signal lissé,
* pas d’oscillation ni dépassement notable ((\xi>1)).

Si la fréquence du créneau est :

* faible devant (\omega_0) : sortie proche du créneau ;
* élevée devant (\omega_0) : sortie quasi sinusoïdale de faible amplitude.
