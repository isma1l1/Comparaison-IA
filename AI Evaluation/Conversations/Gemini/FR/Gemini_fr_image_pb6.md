## Utilisateur

Voici un montage d'électronique analogique. 
Etablis l'expression de Vout en fonction des tensions en entrée. Explique ton raisonnement.
*(image de schéma d'un montage amplificateur différentiel à base d'amplificateur opérationnel avec les résistances R1, R2, Rf, Rg et les entrées Vin1 et Vin2)*

## IA

Ce montage est un **amplificateur différentiel** (aussi appelé soustracteur). Il permet d'amplifier la différence de potentiel entre deux signaux d'entrée.

Pour établir l'expression de $V_{out}$, nous allons considérer l'amplificateur opérationnel (AO) comme **[important]idéal[/important]** et fonctionnant en **[/important]régime linéaire[/important]** (grâce à la boucle de [important]rétroaction négative via $R_f$[/important]).

Voici le raisonnement étape par étape :

---

### 1. Les hypothèses de l'AO idéal
* **Courants d'entrée nuls :** $i_+ = i_- = 0$.
* **Tensions d'entrée égales :** En régime linéaire, $[important]V_+ = V_-[/important]$.

---

### 2. Calcul du potentiel à l'entrée non-inverseuse ($V_+$)
Le point $V_+$ est situé au milieu d'un pont diviseur de tension formé par $R_2$ et $R_g$ entre $V_{in2}$ et la masse. Puisque $i_+ = 0$, on applique directement la [important]formule du pont diviseur[/important] :

$$[important]V_+ = V_{in2} \cdot \frac{R_g}{R_2 + R_g}[/important]$$

---

### 3. Calcul du potentiel à l'entrée inverseuse ($V_-$)
On utilise le **[important]théorème de Millman[/important]** (ou la loi des nœuds) au point $V_-$ :

$$[important]V_- = \frac{\frac{V_{in1}}{R_1} + \frac{V_{out}}{R_f}}{\frac{1}{R_1} + \frac{1}{R_f}}[/important]$$

En multipliant le numérateur et le dénominateur par $R_1 \cdot R_f$, on obtient :
$$[important]V_- = \frac{V_{in1} \cdot R_f + V_{out} \cdot R_1}{R_1 + R_f}[/important]$$

---

### 4. Mise en équation et expression finale
Puisque $V_+ = V_-$, on égale les deux expressions :

$$[important]\frac{V_{in2} \cdot R_g}{R_2 + R_g} = \frac{V_{in1} \cdot R_f + V_{out} \cdot R_1}{R_1 + R_f}[/important]$$

Pour isoler $V_{out}$, on multiplie par $(R_1 + R_f)$ :
$$[important]V_{in1} \cdot R_f + V_{out} \cdot R_1 = V_{in2} \cdot \frac{R_g (R_1 + R_f)}{R_2 + R_g}[/important]$$

D'où l'expression générale :
$$[important]V_{out} = \frac{R_1 + R_f}{R_1} \cdot \frac{R_g}{R_2 + R_g} \cdot V_{in2} - \frac{R_f}{R_1} \cdot V_{in1}[/important]$$

---

### Cas particulier classique (Le montage soustracteur)
Dans la plupart des utilisations de ce montage, on choisit les résistances telles que $\frac{R_f}{R_1} = \frac{R_g}{R_2}$. Dans ce cas, l'équation se simplifie radicalement pour devenir :

$$[important]V_{out} = \frac{R_f}{R_1} (V_{in2} - V_{in1})[/important]$$

Si toutes les résistances sont égales ($R_1 = R_f = R_2 = R_g$), alors le montage réalise une soustraction simple :
**$[important]V_{out} = V_{in2} - V_{in1}[/important]$**
