## Utilisateur

[Image d'un montage d'électronique analogique : un amplificateur opérationnel en configuration non-inverseuse avec les résistances R1 et R2]

Voici un montage d'électronique analogique. 
Donne-moi la formule du gain de ce circuit en fonction de la valeur des résistances R1 et R2. Explique ton raisonnement.

## IA

L'image montre une configuration classique d'**amplificateur opérationnel (AOP) non-inverseur**. Voici le détail de la formule de son gain et de la démonstration associée.

### 1. La formule du gain
Pour un amplificateur opérationnel idéal dans cette configuration, le gain en tension en boucle fermée ($A_v$) est défini par la formule suivante :

$$[important]A_v = \frac{V_{out}}{V_{in}} = 1 + \frac{R_1}{R_2}[/important]$$

---

### 2. Explication et raisonnement
Pour dériver cette formule, nous supposons que l'AOP est **idéal**, ce qui nous donne deux règles d'or :
1.  **Court-circuit virtuel :** La tension à l'entrée inverseuse ($V_-$) est égale à la tension à l'entrée non-inverseuse ($V_+$).
2.  **Impédance d'entrée infinie :** Aucun courant ne circule dans les bornes d'entrée de l'AOP.

#### Démonstration étape par étape :
* **Identifier la tension d'entrée :** Le signal d'entrée $V_{in}$ est appliqué directement à la borne non-inverseuse ($+$). Par conséquent, $[important]V_+ = V_{in}[/important]$.
* **Appliquer le court-circuit virtuel :** Grâce à la contre-réaction négative via $R_1$, l'AOP ajuste $V_{out}$ pour s'assurer que $[important]V_- = V_+[/important]$. Ainsi, la tension au nœud entre $R_1$ et $R_2$ est également $V_{in}$.
* **Principe du [important]diviseur de tension[/important] :** Les résistances $R_1$ et $R_2$ forment un diviseur de tension entre $V_{out}$ et la masse. La tension $V_-$ est la tension "prélevée" au milieu de ce diviseur :
    $$[important]V_- = V_{out} \cdot \left( \frac{R_2}{R_1 + R_2} \right)[/important]$$
* **Résoudre pour le gain :** Puisque nous savons que $V_- = V_{in}$, nous pouvons établir l'équation :
    $$V_{in} = V_{out} \cdot \left( \frac{R_2}{R_1 + R_2} \right)$$
    En réorganisant pour trouver le rapport $\frac{V_{out}}{V_{in}}$ :
    $$[important]\frac{V_{out}}{V_{in}} = \frac{R_1 + R_2}{R_2}[/important] = \frac{R_1}{R_2} + \frac{R_2}{R_2} = [important]1 + \frac{R_1}{R_2}[/important]$$

---

### Caractéristiques clés
* **Non-inverseur :** La sortie est en phase avec l'entrée (le gain est positif).
* **Gain minimum :** Le gain ne peut jamais être inférieur à **1**. Si vous retirez $R_2$ (circuit ouvert) ou si vous remplacez $R_1$ par un simple fil (court-circuit), le circuit devient un **suiveur de tension** (buffer).
* **Haute impédance d'entrée :** Comme $V_{in}$ est connecté directement à l'entrée de l'AOP, il ne consomme pratiquement aucun courant de la source.