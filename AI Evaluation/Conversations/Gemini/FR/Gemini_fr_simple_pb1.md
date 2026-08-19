## Utilisateur

Donne moi la formule du gain d'un montage inverseur en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

---

## IA

Le montage **amplificateur inverseur** est l'un des circuits de base les plus utilisés en électronique analogique avec les amplificateurs opérationnels (AOP).

Voici la formule du gain et le raisonnement pas à pas pour y parvenir.

---

### La Formule du Gain

Le gain en tension ($A_v$) du montage inverseur est défini par le rapport entre la tension de sortie ($V_s$) et la tension d'entrée ($V_e$) :

$$[important]A_v = \frac{V_s}{V_e} = -\frac{R_2}{R_1}[/important]$$

* **$R_1$** est la résistance reliée à l'entrée.
* **$R_2$** est la résistance de contre-réaction (bouclée entre la sortie et l'entrée inverseuse).
* Le signe **négatif** indique que le signal de sortie est en opposition de phase (inversé) par rapport au signal d'entrée.

---

### Le Raisonnement (Démonstration)

Pour établir cette formule, on s'appuie sur les deux hypothèses de l'**AOP idéal en [important]régime linéaire[/important]** :

1. **Les courants d'entrée sont nuls** ($[important]i_+ = i_- = 0[/important]$) : l'AOP ne consomme aucun courant sur ses bornes d'entrée.
2. **La tension différentielle est nulle** ($\epsilon = 0$) : comme [important]la borne non-inverseuse ($+$) est reliée à la masse (0V), alors la borne inverseuse ($-$) est aussi à un **potentiel de 0V**[/important]. On appelle cela une **masse virtuelle**.

#### Étapes de la démonstration :

1. **Loi des nœuds au point $(-)$ :**
Le courant arrivant par $R_1$ (appelons-le $I_1$) doit obligatoirement repartir par $R_2$ (appelons-le $I_2$) car aucun courant n'entre dans l'AOP. Donc :

$$[important]I_1 = I_2[/important]$$


2. **Expression de $I_1$ (Loi d'Ohm) :**
Le courant traverse $R_1$ entre le potentiel $V_e$ et la masse virtuelle (0V) :

$$[important]I_1 = \frac{V_e - 0}{R_1} = \frac{V_e}{R_1}[/important]$$

3. **Expression de $I_2$ (Loi d'Ohm) :**
Le courant traverse $R_2$ entre la masse virtuelle (0V) et le potentiel de sortie $V_s$ :

$$[important]I_2 = \frac{0 - V_s}{R_2} = -\frac{V_s}{R_2}[/important]$$


4. **Égalité et conclusion :**
En égalisant les deux expressions :

$$[important]\frac{V_e}{R_1} = -\frac{V_s}{R_2}[/important]$$



En isolant le rapport $\frac{V_s}{V_e}$, on obtient bien : **$[important]A_v = -\frac{R_2}{R_1}[/important]$**.

---

### En résumé

Le gain dépend uniquement du **rapport des résistances**. Si vous voulez un gain de $-10$, il vous suffit de choisir une résistance $R_2$ dix fois plus grande que $R_1$.

Souhaitez-vous que je calcule les valeurs de résistances pour un gain spécifique ou que je vous explique un autre montage comme l'amplificateur non-inverseur ?