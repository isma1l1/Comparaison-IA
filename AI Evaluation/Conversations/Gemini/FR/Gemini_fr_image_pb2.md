Voici le contenu de notre échange au format Markdown, tel que demandé :

## Utilisateur
{
type: uploaded file
fileName: schema_non_inverseur.png
[Image d'un montage d'amplificateur opérationnel en configuration non-inverseuse]
}
Voici un montage d'électronique analogique. 
Donne moi la formule du gain de ce circuit en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA
Le circuit que vous avez présenté est un **amplificateur non-inverseur**.

### Formule du gain
Le gain en tension ($A_v$) de ce montage est donné par la formule suivante :

$$[important]A_v = \frac{V_{out}}{V_{in}} = 1 + \frac{R_1}{R_2}[/important]$$

---

### Raisonnement
Pour établir cette formule, on utilise les deux hypothèses fondamentales d'un amplificateur opérationnel (AO) idéal fonctionnant en [important]régime linéaire[/important] :

1.  **Le courant d'entrée est nul :** Aucun courant ne pénètre dans les entrées inverseuse ($-$) et non-inverseuse ($+$).
2.  **Le régime linéaire :** Grâce à la contre-réaction, l'AO fait tout pour annuler la différence de potentiel entre ses deux entrées. Ainsi, le potentiel à l'entrée inverseuse ($V_-$) est égal au potentiel à l'entrée non-inverseuse ($V_+$).

**Étapes de démonstration :**

* **Étape 1 :** On observe que l'entrée non-inverseuse est directement reliée à $V_{in}$, donc $V_+ = V_{in}$. En vertu de l'hypothèse de régime linéaire, $[important]V_- = V_+ = V_{in}[/important]$.
* **Étape 2 :** Les résistances $R_1$ et $R_2$ forment un [important]pont diviseur de tension[/important] entre $V_{out}$ et la masse (GND), dont le point milieu est connecté à $V_-$.
    Le potentiel $V_-$ s'exprime donc en fonction de $V_{out}$ :
    $$[important]V_- = V_{out} \times \frac{R_2}{R_1 + R_2}[/important]$$
* **Étape 3 :** Comme $V_- = V_{in}$, on peut écrire :
    $$V_{in} = V_{out} \times \frac{R_2}{R_1 + R_2}$$
* **Étape 4 :** En isolant le rapport $\frac{V_{out}}{V_{in}}$ (le gain), on obtient :
    $$[important]\frac{V_{out}}{V_{in}} = \frac{R_1 + R_2}{R_2}[/important] = \frac{R_1}{R_2} + \frac{R_2}{R_2} = [important]1 + \frac{R_1}{R_2}[/important]$$

Ce gain est toujours supérieur ou égal à 1, d'où le nom de "non-inverseur", car le signal de sortie est en phase avec le signal d'entrée.