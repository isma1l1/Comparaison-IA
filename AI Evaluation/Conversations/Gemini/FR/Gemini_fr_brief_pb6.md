## Utilisateur
Réponds de manière concise en supprimant tout propos inutile. 
On considère un montage différentiel en électronique. Etablis l'expression de Vout en fonction des tensions en entrée et des résistances. Explique ton raisonnement.

## IA
Pour un amplificateur différentiel idéal (AO parfait en régime linéaire), on utilise le principe de superposition ou les théorèmes de Millman aux entrées de l'amplificateur.

### Montage et notations
* **[important]Entrée inverseuse ($V_-$) :** Reliée à $V_1$ via $R_1$ et à la sortie $V_{out}$ via $R_2$.
* **Entrée non-inverseuse ($V_+$) :** Reliée à $V_2$ via $R_3$ et à la masse via $R_4$.[/important]

### Raisonnement

1.  **Potentiel $V_+$ :** Par [important]division de tension (pont diviseur)[/important] :
    $$[important]V_+ = V_2 \cdot \frac{R_4}{R_3 + R_4}[/important]$$

2.  **Potentiel $V_-$ :** Par le [/important]théorème de Millman[/important] :
    $$[important]V_- = \frac{\frac{V_1}{R_1} + \frac{V_{out}}{R_2}}{\frac{1}{R_1} + \frac{1}{R_2}}[/important]$$

3.  **Condition d'équilibre :** En [important]régime linéaire[/important], $[important]V_+ = V_-[/important]$.
    $$[important]\frac{V_1 \cdot R_2 + V_{out} \cdot R_1}{R_1 + R_2} = V_2 \cdot \frac{R_4}{R_3 + R_4}[/important]$$

4.  **Isolement de $V_{out}$ :**
    $$[important]V_{out} = \frac{R_1 + R_2}{R_1} \cdot \frac{R_4}{R_3 + R_4} \cdot V_2 - \frac{R_2}{R_1} \cdot V_1[/important]$$

---

### Expression finale

L'expression générale est :
$$[important]V_{out} = \frac{R_2}{R_1} \left( \frac{1 + \frac{R_1}{R_2}}{1 + \frac{R_3}{R_4}} V_2 - V_1 \right[/important])$$

**Cas particulier usuel (montage équilibré) :**
Si $\frac{R_2}{R_1} = \frac{R_4}{R_3}$, alors la relation se simplifie en un pur amplificateur de différence :
$$[important]V_{out} = \frac{R_2}{R_1} (V_2 - V_1)[/important]$$
