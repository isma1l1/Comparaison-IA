## Utilisateur
Réponds de manière concise en supprimant tout propos inutile. 
On étudie un montage soustracteur classique. Détermine la relation entrée-sortie de ce système. Explique ton raisonnement.

## IA
Voici la détermination de la relation entrée-sortie pour un montage soustracteur [important]idéal[/important].

### Schéma du montage
Le montage comporte deux entrées, $V_1$ (sur la borne inverseuse via $R_1$) et $V_2$ (sur la borne non-inverseuse via $R_3$), avec des résistances de rétroaction $R_2$ et de mise à la masse $R_4$.



---

### Raisonnement
On suppose l'amplificateur opérationnel **idéal** et en **[important]régime linéaire[/important]** ($[important]V_+ = V_-[/important]$).

1.  **Potentiel $V_+$ (Diviseur de tension) :**
    Le courant entrant dans la borne étant nul :
    $$[important]V_+ = V_2 \cdot \frac{R_4}{R_3 + R_4}[/important]$$

2.  **Potentiel $V_-$ (Théorème de Millman) :**
    $$[important]V_- = \frac{\frac{V_1}{R_1} + \frac{V_s}{R_2}}{\frac{1}{R_1} + \frac{1}{R_2}}[/important]$$

3.  **Égalité $V_+ = V_-$ :**
    En égalisant les deux expressions et en isolant $V_s$, on obtient la relation générale :
    $$[important]V_s = \frac{R_1 + R_2}{R_1} \cdot \frac{R_4}{R_3 + R_4} \cdot V_2 - \frac{R_2}{R_1} \cdot V_1[/important]$$

---

### Relation Entrée-Sortie
Dans le cas classique où les résistances sont équilibrées (**$R_1 = R_3$** et **$R_2 = R_4$**), la formule se simplifie :

$$[important]V_s = \frac{R_2}{R_1} (V_2 - V_1)[/important]$$

Si toutes les résistances sont identiques, la sortie est la différence directe des entrées : **$V_s = V_2 - V_1$**.
