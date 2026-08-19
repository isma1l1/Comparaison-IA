```markdown
## Utilisateur
Réponds de manière concise en supprimant tout propos inutile. Donne moi la formule du gain d'un montage non-inverseur en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA
Pour un **amplificateur opérationnel en montage non-inverseur**, on suppose un AOP idéal (gain infini, courant d’entrée nul, tension différentielle nulle).

On a donc :
- ( [important]\V^+ = V^-[/important] \)
- L’entrée non-inverseuse reçoit \( V_{in} \), donc \( V^- = V_{in} \)

Le pont de résistances donne :
- \( [important]V^- = V_{out} \cdot \dfrac{R1}{R1 + R2}[/important] \)

Donc :
\[
[important]V_{in} = V_{out} \cdot \frac{R1}{R1 + R2}[/important]
\]

On isole le gain \( G = \dfrac{V_{out}}{V_{in}} \) :

\[
[important]G = 1 + \frac{R2}{R1}[/important]
\]

**Résultat :**
\[
G = 1 + \frac{R2}{R1}
\]
```
