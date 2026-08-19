## Utilisateur

Voici un montage d'électronique analogique. 
Donne moi la formule du gain de ce circuit en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA

C'est un grand classique ! Ce montage est un [important]**amplificateur inverseur**[/important] (Inverting Amplifier) basé sur un amplificateur opérationnel (AO).

Voici la formule du gain et le raisonnement détaillé pour y parvenir.

---

### 1. La Formule du Gain
Le gain en tension, noté $A_v$ (ou $G$), est le rapport entre la tension de sortie ($V_{out}$) et la tension d'entrée ($V_{in}$). Pour ce montage, la formule est :

$$[important]A_v = \frac{V_{out}}{V_{in}} = -\frac{R1}{R2}[/important]$$

---

### 2. Le Raisonnement (Hypothèses de l'AO idéal)
Pour établir cette formule, on considère que l'amplificateur opérationnel est **idéal** et fonctionne en [important]**régime linéaire** (grâce à la boucle de rétroaction sur l'entrée négative)[/important].

#### A. Le concept de la "Masse Virtuelle"
1. Comme l'entrée non-inverseuse ($+$) est reliée directement à la masse, son potentiel est $V_+ = 0$.
2. Dans un AO idéal en régime linéaire, la différence de potentiel entre les deux entrées est nulle ($[important]\epsilon = V_+ - V_- = 0[/important]$).
3. Par conséquent, le potentiel à l'entrée inverseuse ($-$) est aussi de **0V**. On appelle ce point une **[important]masse virtuelle[/important]**.

#### B. Loi des nœuds (Théorème de Millman ou Loi d'Ohm)
Appliquons la loi des nœuds au point de jonction entre $R1$, $R2$ et l'entrée ($-$) de l'AO. On note $i_1$ le courant traversant $R2$ et $i_2$ le courant traversant $R1$.

* Comme l'impédance d'entrée de l'AO est infinie, **aucun courant ne rentre dans l'AO**. Donc : $i_1 = i_2$.
* Selon la loi d'Ohm pour $R2$ : $[important]i_1 = \frac{V_{in} - 0}{R2} = \frac{V_{in}}{R2}[/important]$
* Selon la loi d'Ohm pour $R1$ : $[important]i_2 = \frac{0 - V_{out}}{R1} = -\frac{V_{out}}{R1}[/important]$

#### C. Égalité des courants
En égalisant les deux expressions :
$$[important]\frac{V_{in}}{R2} = -\frac{V_{out}}{R1}[/important]$$

En isolant $V_{out} / V_{in}$, on obtient la relation finale :
$$[important]\frac{V_{out}}{V_{in}} = -\frac{R1}{R2}[/important]$$

---

### Ce qu'il faut retenir :
* Le signe **négatif** indique que le signal de sortie est en opposition de phase (inversé) par rapport au signal d'entrée.
* Le gain dépend uniquement du **rapport des résistances**. Si $R1 > R2$, le montage amplifie ; si $R1 < R2$, il atténue.