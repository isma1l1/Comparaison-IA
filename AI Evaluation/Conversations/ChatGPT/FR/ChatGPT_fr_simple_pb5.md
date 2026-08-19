## Utilisateur

On étudie Uc(t) en fonction de E(t) dans un circuit RLC série. Détermine la nature du filtre représenté, calcule la fonction de transfert, donne l'expression de la largeur de la bande passante et trace les diagrammes de Bode en gain et en phase. Explique ton raisonnement.

---

## IA

On considère un circuit **RLC série** et on observe la tension aux bornes du condensateur (U_C(t)) en réponse à l’entrée (E(t)).

---

## 1) Nature du filtre

À basse fréquence ((\omega \to 0)) :

* Le condensateur se comporte comme un circuit **ouvert** → toute la tension est à ses bornes
  ⇒ (U_C \approx E)

À haute fréquence ((\omega \to \infty)) :

* Le condensateur se comporte comme un **court-circuit** → (U_C \to 0)

Le circuit laisse passer les **basses fréquences** et atténue les hautes :

**C’est un filtre [important]passe-bas du 2ᵉ ordre[/important]**

---

## 2) Fonction de transfert (H(j\omega))

On applique un [important]diviseur de tension[/important] :

[
[important]H(j\omega) = \frac{U_C}{E} = \frac{Z_C}{Z_R + Z_L + Z_C}[/important]
]

avec :
[important]
* (Z_R = R)
* (Z_L = j\omega L)
* (Z_C = \frac{1}{j\omega C})
[/important]
Après simplification :

[
[important]H(j\omega) = \frac{1}{1 + j\omega RC - \omega^2 LC}[/important]
]

---

### Forme canonique

On pose :

* pulsation propre : (\[important]omega_0 = \frac{1}{\sqrt{LC}}[/important])
* facteur de qualité : ([important]Q = \frac{1}{R}\sqrt{\frac{L}{C}}[/important])

On obtient :

[
[important]H(j\omega) = \frac{1}{1 - \left(\frac{\omega}{\omega_0}\right)^2 + j \frac{\omega}{\omega_0 Q}}[/important]
]

---

## 3) Bande passante

Pour un filtre du 2ᵉ ordre, la largeur de bande est :

[
[important]\Delta \omega = \frac{\omega_0}{Q}[/important]
]

Or :

[
Q = \frac{1}{R}\sqrt{\frac{L}{C}} \Rightarrow \Delta \omega = \frac{R}{L}
]

**Résultat important :**

[
\boxed{[important]\Delta \omega = \frac{R}{L}[/important]
]

---

## 4) Diagrammes de Bode

### Gain

On trace le module :

[
|H(j\omega)| = \frac{1}{\sqrt{(1 - \omega^2 LC)^2 + (\omega RC)^2}}
]
Comportement :
[important]
* (\omega \ll \omega_0) : gain ≈ 1 → **0 dB**
* (\omega = \omega_0) : possible **résonance** si (Q > 1/\sqrt{2})
* (\omega \gg \omega_0) : pente = **−40 dB/décade**
[/important]
---

### Phase

[
\varphi(\omega) = -\arctan\left(\frac{\omega RC}{1 - \omega^2 LC}\right)
]

Comportement :
[important]
* basse fréquence : (0^\circ)
* à (\omega_0) : (-90^\circ)
* haute fréquence : (-180^\circ)
[/important]
---

## 5) Visualisation (fonction clé)

Pour comprendre le Bode, la fonction à analyser est :

H(j\omega)=\frac{1}{1-\omega^2LC + j\omega RC}

---

## 6) Interprétation physique

* À basse fréquence : le condensateur **stocke la tension** → sortie ≈ entrée
* À haute fréquence : il **court-circuite** le signal → sortie nulle
* La résistance contrôle l’**amortissement** :

  * faible (R) → pic de résonance (filtre sélectif)
  * grand (R) → réponse plus plate

---

## Résumé

* **Type** : filtre passe-bas 2ᵉ ordre
* **Fonction de transfert** :
  [
  H(j\omega)=\frac{1}{1 + j\omega RC - \omega^2 LC}
  ]
* **Bande passante** :
  [
  \Delta \omega = \frac{R}{L}
  ]
* **Bode** :

  * gain : 0 dB → −40 dB/décade
  * phase : (0° \to -180°)
