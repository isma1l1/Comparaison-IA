## Utilisateur

Réponds de manière concise en supprimant tout propos inutile. Donne moi la formule du gain d'un montage non-inverseur en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

---

## IA

### Formule du gain

Le gain en tension $A_v$ d'un montage amplificateur non-inverseur est :

$$[important]A_v = \frac{V_{out}}{V_{in}} = 1 + \frac{R_2}{R_1}[/important]$$

---

### Raisonnement

Le calcul repose sur deux propriétés de l'amplificateur opérationnel (AOP) idéal en [important]régime linéaire[/important] :

1. **Le court-circuit virtuel :** Les tensions des entrées sont égales ($[important]V_+ = V_-[/important]$). Ici, $V_+ = V_{in}$, donc $V_- = V_{in}$.
2. **L'impédance d'entrée infinie :** Aucun courant n'entre dans les bornes de l'AOP.

**Étapes :**

* Les résistances $R_1$ et $R_2$ forment un **pont diviseur** de tension depuis la sortie $V_{out}$ vers l'entrée $V_-$.
* L'expression de la tension au point milieu est : $[important]V_- = V_{out} \cdot \frac{R_1}{R_1 + R_2}[/important]$.
* En substituant $V_-$ par $V_{in}$ (propriété 1) : $[important]V_{in} = V_{out} \cdot \frac{R_1}{R_1 + R_2}[/important]$.
* En isolant le rapport $\frac{V_{out}}{V_{in}}$, on obtient : $\frac{R_1 + R_2}{R_1}$, soit **$[important]1 + \frac{R_2}{R_1}[/important]$**.
