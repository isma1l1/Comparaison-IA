## Utilisateur

Voici un montage d'électronique analogique.
Identifie le régime de fonctionnement de l'ALI, exprime le potentiel v+ en fonction de s, déduis-en les tensions de basculement, représente le cycle d'hystérésis du montage dans le cas où R2 = 2*R1, et représente le signal de sortie pour une entrée sinusoïdale d'amplitude 10V. Explique ton raisonnement.
*(image de schéma d’un amplificateur opérationnel avec R1 à la masse, R2 en contre-réaction positive vers l’entrée non-inverseuse, entrée e sur l’entrée inverseuse, et sortie s)*

## IA

Ce montage est un **comparateur à hystérésis** (ou trigger de Schmitt) basé sur un ALI.

---

## 1) Régime de fonctionnement de l’ALI

L’ALI fonctionne en **[important]régime saturé (non linéaire)[/important]** :

* Il n’y a **pas de contre-réaction négative**, mais une **contre-réaction positive via (R_2)**
* Donc la sortie bascule entre :
  [
  [important]s = +V_{sat} \quad \text{ou} \quad s = -V_{sat}[/important]
  ]

---

## 2) Expression de (v_+) en fonction de (s)

Le nœud (v_+) est relié :

* à la masse via (R_1)
* à la sortie (s) via (R_2)

→ C’est un **[important]pont diviseur[/important]** entre (s) et 0 V :

[
[important]v_+ = \frac{R_1}{R_1 + R_2} \cdot s[/important]
]

---

## 3) Condition de basculement

L’ALI compare :

* entrée non-inverseuse : (v_+)
* entrée inverseuse : (e)

Le basculement se produit quand :
[
[important]e = v_+[/important]
]

Donc les seuils sont :

[
e_{seuil} = \frac{R_1}{R_1 + R_2} \cdot s
]

Comme (s = \pm V_{sat}), on obtient :

* seuil haut :
  [
  [important]e_H = \frac{R_1}{R_1 + R_2} \cdot (+V_{sat})[/important]
  ]

* seuil bas :
  [
  [important]e_B = \frac{R_1}{R_1 + R_2} \cdot (-V_{sat})[/important]
  ]

---

## 4) Cas ([important]R_2 = 2R_1[/important]

Alors :

[
\frac{R_1}{R_1 + R_2} = \frac{R_1}{3R_1} = \frac{1}{3}
]

Donc :

[
[important]e_H = +\frac{V_{sat}}{3}, \quad e_B = -\frac{V_{sat}}{3}[/important]
]

---

## 5) Cycle d’hystérésis

C’est une [important]boucle rectangulaire[/important] :

* [important]Si (e) monte :

  * basculement à (+V_{sat}) quand (e = +V_{sat}/3)[/important]
* [important]Si (e) descend :

  * basculement à (-V_{sat}) quand (e = -V_{sat}/3)[/important]

Donc :

* sortie reste à +Vsat tant que (e > -V_{sat}/3)
* sortie reste à −Vsat tant que (e < +V_{sat}/3)

**Aspect du cycle :**

* rectangle entre (-V_{sat}) et (+V_{sat})
* seuils horizontaux à (\pm V_{sat}/3)

---

## 6) Réponse à une entrée sinusoïdale (amplitude 10 V)

Supposons :
[
e(t) = 10 \sin(\omega t)
]

Comparaison avec seuils :

* basculement vers +Vsat quand :
  [
  e(t) > +\frac{V_{sat}}{3}
  ]

* basculement vers -Vsat quand :
  [
  e(t) < -\frac{V_{sat}}{3}
  ]

### Interprétation

La sortie est un **[important]signal carré[/important]** :

* elle [important]commute **avant les passages par zéro[/important]**
* les [important]transitions ont lieu quand la sinusoïde atteint ±(V_{sat}/3)[/important]

### Si (V_{sat} \approx 15\text{ V}) :

* seuils ≈ ±5 V
* la sinusoïde (±10 V) dépasse largement ces seuils

Donc :

* sortie = créneau saturé ±15 V
* rapport cyclique ≈ 50 % (symétrique)

---

## 7) Résumé rapide

* Montage = **trigger de Schmitt**
* ALI en **régime saturé**
* (v_+ = \frac{R_1}{R_1 + R_2}s)
* seuils = ±(V_{sat}/3) (si (R_2 = 2R_1))
* sortie = **signal carré propre** à partir d’une sinusoïde

---

Si tu veux, je peux te tracer :

* le cycle d’hystérésis
* ou le signal entrée/sortie superposé 
