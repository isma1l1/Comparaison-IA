## Utilisateur

Voici un montage d'électronique analogique.
Détermine la relation entrée-sortie du filtre présenté. Explique ton raisonnement.
*(image de schéma d’un amplificateur opérationnel avec un condensateur en entrée sur la borne inverseuse, une résistance en rétroaction entre la sortie et l’entrée inverseuse, et l’entrée non-inverseuse à la masse)*

## IA

On reconnaît ici un **amplificateur opérationnel en configuration inverseuse**, avec :

* entrée appliquée via un **condensateur** (C)
* rétroaction via une **résistance** (R)
* entrée non-inverseuse à la masse

👉 C’est la configuration typique d’un **dérivateur**.

---

## 1. Hypothèses sur l’AO idéal

* (V^+ = 0) (masse)
* (V^- \approx 0) (masse virtuelle)
* courant d’entrée nul dans l’AO

---

## 2. Courants au nœud inverseur

Le courant dans le condensateur vaut :
[
i_C = C \frac{d(e - V^-)}{dt}
]
Or (V^- \approx 0), donc :
[
i_C = C \frac{de}{dt}
]

Ce courant traverse entièrement la résistance de rétroaction (pas de courant dans l’AO) :
[
i_R = \frac{V^- - s}{R} = \frac{0 - s}{R} = -\frac{s}{R}
]

---

## 3. Égalité des courants

[
i_C = i_R
\Rightarrow C \frac{de}{dt} = -\frac{s}{R}
]

---

## 4. Relation entrée-sortie

[
s(t) = -RC \frac{de(t)}{dt}
]

---

## 5. Fonction de transfert (Laplace)

[
\frac{S(p)}{E(p)} = -RC , p
]

---

## ✅ Conclusion

* Le montage est un **filtre dérivateur (passe-haut)**
* Il amplifie les variations rapides du signal
* Gain proportionnel à la fréquence (( \propto p ))

👉 En résumé :
[
\boxed{s(t) = -RC \frac{de(t)}{dt}}
]

---

Si tu veux, je peux te montrer comment ce circuit se comporte avec un sinus ou un signal carré (très parlant 👍).
