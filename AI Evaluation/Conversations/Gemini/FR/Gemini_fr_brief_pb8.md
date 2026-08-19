## Utilisateur

Réponds de manière concise en supprimant tout propos inutile. 
On étudie un montage comparateur à hystérésis inverseur dans lequel la résistance entre la masse et l'entrée non-inverseuse est notée R1 et la résistance entre l'entrée non-inverseuse et la sortie de l'ALI est notée R2. Identifie le régime de fonctionnement de l'ALI, exprime le potentiel v+ en fonction de s, déduis-en les tensions de basculement, représente le cycle d'hystérésis du montage dans le cas où R2 = 2*R1, et représente le signal de sortie pour une entrée sinusoïdale d'amplitude 10V. Explique ton raisonnement.

## IA

### 1. Régime de fonctionnement
L'ALI fonctionne en **[important]régime saturé[/important]** (non-linéaire) car il existe une boucle de [important]rétroaction positive[/important] reliant la sortie à l'entrée non-inverseuse ($v^+$). La tension de sortie $s$ ne peut prendre que deux valeurs : $+V_{sat}$ ou $-V_{sat}$.

---

### 2. Expression de $v^+$
D'après le [important]pont diviseur de tension[/important] entre la sortie $s$ et la masse :
$$[important]v^+ = s \cdot \frac{R_1}{R_1 + R_2}[/important]$$

---

### 3. Tensions de basculement
Le basculement se produit lorsque $v^+ = v^-$. Comme l'entrée est inverseuse, $v^- = e$.
* **Seuil haut ($V_H$)** : Si $s = +V_{sat}$, le basculement a lieu pour $e > [important]V_H = +V_{sat} \cdot \frac{R_1}{R_1 + R_2}[/important]$.
* **Seuil bas ($V_B$)** : Si $s = -V_{sat}$, le basculement a lieu pour $e < [important]V_B = -V_{sat} \cdot \frac{R_1}{R_1 + R_2}[/important]$.

---

### 4. Cas particulier $[important]R_2 = 2R_1[/important]$
Le rapport devient : $\frac{R_1}{R_1 + 2R_1} = \frac{1}{3}$.
D'où : **$[important]V_H = \frac{V_{sat}}{3}[/important]$** et **$[important]V_B = -\frac{V_{sat}}{3}[/important]$**.

**Cycle d'hystérésis ($s$ en fonction de $e$) :**
* Le cycle est parcouru dans le sens **anti-horaire** (caractère inverseur).
* [important]La sortie chute à $-V_{sat}$ quand $e$ franchit $V_H$[/important].
* [important]La sortie remonte à $+V_{sat}$ quand $e$ franchit $V_B$[/important].

---

### 5. Signal de sortie Entrée $e(t) = 10 \sin(\omega t)$
En supposant $V_{sat} = 15V$ (valeur usuelle), les seuils sont à $\pm 5V$.
* **Initialement ($e=0$)** : Si $s = +V_{sat}$, la sortie reste à $+15V$ tant que $e < +5V$.
* **Basculement bas** : Dès que l'entrée dépasse $+5V$, $s$ passe instantanément à $-15V$.
* **Maintien** : $s$ reste à $-15V$ même quand $e$ redescend sous $+5V$.
* **Basculement haut** : $s$ repasse à $+15V$ uniquement quand $e$ devient inférieur à $-5V$.

Le signal de sortie est un **[important]signal carré déphasé[/important]** par rapport à l'entrée, dont les [important]transitions sont centrées sur les passages aux seuils $\pm 5V$[/important].
