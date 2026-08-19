## Utilisateur
On considère un montage différentiel en électronique. Etablis l'expression de Vout en fonction des tensions en entrée et des résistances. Explique ton raisonnement.

## IA
Pour établir l'expression de la tension de sortie $V_{out}$ d'un amplificateur différentiel (souvent appelé soustracteur), nous allons utiliser les propriétés de l'amplificateur opérationnel (AOP) considéré comme **[important]idéal[/important]** et fonctionnant en **[important]régime linéaire[/important]** (grâce à la [important]contre-réaction sur l'entrée inverseuse[/important]).

---

### 1. Schéma et Notations
Le montage se compose de quatre résistances ($R_1, R_2, R_3, R_4$) et de deux tensions d'entrée ($V_1$ et $V_2$).
[important]
* **Entrée inverseuse ($V_-$) :** Reliée à $V_1$ via $R_1$ et à la sortie $V_{out}$ via $R_2$.
* **Entrée non-inverseuse ($V_+) :** Reliée à $V_2$ via $R_3$ et à la masse via $R_4$.[/important]

---

### 2. Hypothèses de calcul
* **[important]Régime linéaire[/important] :** Les tensions aux entrées de l'AOP sont égales, soit $[important]V_+ = V_-[/important]$.
* **Courants d'entrée nuls :** Les courants entrant dans les bornes $+$ et $-$ de l'AOP sont considérés comme nuls ($i_+ = i_- = 0$).

---

### 3. Raisonnement étape par étape

#### Étape A : Calcul de $V_+$
L'entrée non-inverseuse est simplement un **[important]pont diviseur de tension[/important]** formé par $R_3$ et $R_4$ alimenté par $V_2$. Puisque $i_+ = 0$, on a :
$$[important]V_+ = V_2 \cdot \frac{R_4}{R_3 + R_4}[/important]$$

#### Étape B : Calcul de $V_-$
On applique le **[important]théorème de Millman[/important]** (ou le principe de superposition) au nœud de l'entrée inverseuse :
$$V_- = \frac{\frac{V_1}{R_1} + \frac{V_{out}}{R_2}}{\frac{1}{R_1} + \frac{1}{R_2}}$$
En simplifiant l'expression (multiplication par $R_1 \cdot R_2$), on obtient :
$$[important]V_- = \frac{R_2 V_1 + R_1 V_{out}}{R_1 + R_2}[/important]$$

#### Étape C : Égalité $[important]V_+ = V_-[/important]$
Puisque l'AOP est idéal en régime linéaire, on pose l'égalité :
$$[important]\frac{R_4}{R_3 + R_4} V_2 = \frac{R_2 V_1 + R_1 V_{out}}{R_1 + R_2}[/important]$$

---

### 4. Expression finale de $V_{out}$
En isolant $V_{out}$, on arrive à la formule générale :
$$[important]V_{out} = \frac{R_1 + R_2}{R_1} \cdot \frac{R_4}{R_3 + R_4} V_2 - \frac{R_2}{R_1} V_1[/important]$$

Que l'on peut réécrire ainsi :
$$[important]V_{out} = \left( 1 + \frac{R_2}{R_1} \right) \left( \frac{R_4}{R_3 + R_4} \right) V_2 - \frac{R_2}{R_1} V_1[/important]$$

---

### 5. Cas particulier classique (Le Soustracteur)
Dans la majorité des applications, on choisit les résistances telles que le rapport de division soit identique sur les deux branches, soit **$\frac{R_2}{R_1} = \frac{R_4}{R_3}$**.

Dans ce cas précis, l'expression se simplifie radicalement :
$$[important]V_{out} = \frac{R_2}{R_1} (V_2 - V_1)[/important]$$

> **Note :** Si toutes les résistances sont égales ($R_1 = R_2 = R_3 = R_4$), alors $[important]V_{out} = V_2 - V_1[/important]$. Le montage effectue alors une soustraction pure des deux signaux d'entrée.
