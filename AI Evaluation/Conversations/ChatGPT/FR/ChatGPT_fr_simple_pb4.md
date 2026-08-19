## Utilisateur
Détermine la tension v(t) en sortie pour une entrée sinusoïdale e(t) = E0sin(wt) dans un montage de Pont de Graetz. Explique ton raisonnement.

## IA
Dans un **pont de Graetz** (redresseur double alternance), le principe est simple : quelle que soit l’alternance du signal d’entrée, le courant traverse toujours la charge dans le même sens grâce aux 4 diodes.

---

### 1. Signal d’entrée
On te donne :
\[
e(t) = E_0 \sin(\omega t)
\]

---

### 2. Fonctionnement du pont de Graetz

- **Alternance positive** (\([important]\sin(\omega t) > 0[/important] \)) 
  [important]Deux diodes conduisent → la tension de sortie suit l’entrée.[/important]

- **Alternance négative** (\([important]\sin(\omega t) < 0[/important]\))
  Deux autres diodes conduisent → [important]la tension est **inversée** aux bornes de la charge.[/important]

👉 Dans les deux cas, la tension aux bornes de la charge est **[important]positive[/important]**.

---

### 3. Expression de la tension de sortie

Idéalement (diodes parfaites, sans chute de tension) :

\[
[important]v(t) = |e(t)| = E_0 |\sin(\omega t)|[/important]
\]

---

### 4. Forme finale

On obtient donc un signal **redressé double alternance** :

\[
v(t) = E_0 |\sin(\omega t)|
\]

👉 C’est une sinusoïde dont toutes les alternances négatives ont été retournées vers le haut.

---

### 5. Cas réel (avec diodes)

En pratique, chaque conduction implique **2 diodes**, donc une chute de tension (≈ 0,7 V par diode silicium) :

\[
v(t) \approx E_0 |\sin(\omega t)| - 2V_D
\]

avec \(V_D \approx 0{,}7\ \text{V}\).

---

### 6. Interprétation physique

- Le pont de Graetz réalise un **redressement complet**
- La fréquence du signal de sortie est **doublée** (car chaque alternance devient positive)
- Le signal est **toujours positif**, mais encore ondulé (non filtré)

---

Si tu veux, je peux aussi te tracer la forme du signal ou ajouter un condensateur pour voir comment on obtient une tension quasi continue.