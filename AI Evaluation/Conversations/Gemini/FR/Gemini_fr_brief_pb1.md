## Utilisateur

Réponds de manière concise en supprimant tout propos inutile. Donne moi la formule du gain d'un montage inverseur en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

---

## IA

Le gain d'un montage amplificateur inverseur est donné par la formule :

$$[important]A_v = \frac{V_s}{V_e} = -\frac{R_2}{R_1}[/important]$$

### Raisonnement

Le calcul repose sur deux hypothèses de l'amplificateur opérationnel (AOP) idéal en [important]régime linéaire[/important] :

1. **Le courant d'entrée est nul** ($[important]i_+ = i_- = 0[/important]$).
2. **La tension différentielle est nulle** ($[important]V_+ = V_-[/important]$).

**Étapes :**

* **Potentiel au point commun :** Puisque l'entrée non-inverseuse ($V_+$) est à la masse, l'entrée inverseuse ($V_-$) est également à $0\text{ V}$ (masse virtuelle).
* **Loi des nœuds :** Le courant arrivant par $R_1$ est égal au courant repartant par $R_2$ (car aucun courant n'entre dans l'AOP).
* Courant dans $R_1$ : $[important]I = \frac{V_e - 0}{R_1}[/important]$
* Courant dans $R_2$ : $[important]I = \frac{0 - V_s}{R_2}[/important]$


* **Égalité :** $[important]\frac{V_e}{R_1} = -\frac{V_s}{R_2}[/important]$

En isolant le rapport $\frac{V_s}{V_e}$, on obtient $[important]A_v = -\frac{R_2}{R_1}[/important]$.
