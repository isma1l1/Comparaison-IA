## Utilisateur
On étudie un montage comparateur à hystérésis inverseur dans lequel la résistance entre la masse et l'entrée non-inverseuse est notée R1 et la résistance entre l'entrée non-inverseuse et la sortie de l'ALI est notée R2. Identifie le régime de fonctionnement de l'ALI, exprime le potentiel v+ en fonction de s, déduis-en les tensions de basculement, représente le cycle d'hystérésis du montage dans le cas où R2 = 2*R1, et représente le signal de sortie pour une entrée sinusoïdale d'amplitude 10V. Explique ton raisonnement.

## IA
Le montage que vous décrivez est un **comparateur à hystérésis (ou trigger de Schmitt) inverseur**. C'est un classique de l'électronique non-linéaire, utilisé pour transformer un signal bruité en un signal carré propre.

Voici l'analyse détaillée de votre montage :

---

### 1. Régime de fonctionnement
Dans ce montage, la sortie est reliée à l'entrée non-inverseuse ($V^+$) par la résistance $R_2$. Il s'agit d'une **[important]réaction positive[/important]**.
* **Conséquence :** L'ALI (Amplificateur Linéaire d'Intégration) fonctionne en **régime saturé**. 
* La tension de sortie $s$ ne peut prendre [important]que deux valeurs : $+V_{sat}$ ou $-V_{sat}[/important]$ (généralement proches des tensions d'alimentation).

---

### 2. Expression du potentiel $V^+$
L'entrée non-inverseuse est au centre d'un pont diviseur de tension entre la sortie $s$ et la masse (puisque $R_1$ est reliée à la masse). En utilisant le [important]théorème de Millman ou la formule du pont diviseur[/important], on obtient :

$$[important]V^+ = s \cdot \frac{R_1}{R_1 + R_2}[/important]$$

---

### 3. Tensions de basculement
Le basculement se produit lorsque la [important]tension d'entrée[/important] $e$ (appliquée sur la borne inverseuse $V^-$) [important]franchit le seuil $V^+$[/important]. 

* **Seuil haut ($V_H$) :** Si la sortie est à $+V_{sat}$, le basculement vers le bas aura lieu quand $e$ dépasse :
    $$[important]V_H = +V_{sat} \cdot \frac{R_1}{R_1 + R_2}[/important]$$
* **Seuil bas ($V_B$) :** Si la sortie est à $-V_{sat}$, le basculement vers le haut aura lieu quand $e$ descend en dessous de :
    $$[important]V_B = -V_{sat} \cdot \frac{R_1}{R_1 + R_2}[/important]$$

---

### 4. Cycle d'hystérésis (Cas $[important]R_2 = 2R_1[/important]$)
Si $R_2 = 2R_1$, alors le ratio devient :
$$\frac{R_1}{R_1 + 2R_1} = \frac{1}{3}$$
Les seuils sont donc $[important]V_H = \frac{V_{sat}}{3}[/important]$ et $[important]V_B = -\frac{V_{sat}}{3}[/important]$.

**Représentation du cycle ($s$ en fonction de $e$) :**
* Le cycle se parcourt dans le sens **[important]anti-horaire[/important]** (car il est inverseur).
* Si $e$ est très négatif, $s = +V_{sat}$.
* [important]Quand $e$ augmente et atteint $+V_{sat}/3$, $s$ bascule brutalement à $-V_{sat}$.[/important]
* [important]Il faut ensuite que $e$ redescende jusqu'à $-V_{sat}/3$ pour que $s$ repasse à $+V_{sat}$.[/important]

---

### 5. Signal de sortie pour une entrée sinusoïdale (10V)
Supposons une alimentation symétrique où $V_{sat} \approx 15V$. Nos seuils sont donc à $+5V$ et $-5V$.

**Raisonnement :**
1.  **Au démarrage ($t=0$, $e=0$) :** Supposons $s = +V_{sat}$.
2.  **Montée du sinus :** Le signal $e$ grimpe. Tant qu'il reste sous $5V$, $s$ reste à $+15V$. Dès que $e > 5V$, la sortie **chute** à $-15V$.
3.  **Sommet du sinus (10V) :** La sortie reste à $-15V$.
4.  **Descente du sinus :** $e$ repasse sous $5V$, mais **rien ne se passe** (c'est l'effet mémoire de l'hystérésis). Il faut attendre que $e$ descende sous le seuil bas ($-5V$) pour que la sortie **remonte** à $+15V$.
5.  **Résultat :** On obtient un [important]signal carré dont les fronts sont décalés par rapport aux passages à zéro de la sinusoïde[/important].

---

### Résumé des caractéristiques
| Paramètre | Valeur / Formule |
| :--- | :--- |
| **Type de réaction** | Positive (instable) |
| **Régime** | De saturation |
| **Largeur de l'hystérésis** | $\Delta V = \frac{2 \cdot R_1 \cdot V_{sat}}{R_1 + R_2}$ |
| **Seuils (si $R_2=2R_1$)** | $\pm \frac{V_{sat}}{3}$ |
