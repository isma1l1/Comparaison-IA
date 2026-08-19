## Utilisateur
Réponds de manière concise en supprimant tout propos inutile. Donne moi la formule du gain d'un montage inverseur en fonction des valeurs des ré## Utilisateur
Réponds de manière concise en supprimant tout propos inutile. Donne moi la formule du gain d'un montage inverseur en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA
Pour un amplificateur opérationnel en **montage inverseur**, on suppose l’AO idéal :

- Entrée non-inverseuse à la masse ⇒ \( [important]V_+ = 0[/important] \)
- Par **masse virtuelle**, \( V_- \approx 0 \)
- Courant d’entrée nul ⇒ le [important]courant dans \( R_1 \) = courant dans \( R_2 \)[/important]

Courants :
\[
I = \frac{V_{in} - 0}{R_1} = \frac{0 - V_{out}}{R_2}
\]
Donc :

\[
[important]\frac{V_{in}}{R_1} = \frac{-V_{out}}{R_2}[/important]
\]

On isole le gain \( G = \frac{V_{out}}{V_{in}} \) :

\[
[important]G = \frac{V_{out}}{V_{in}} = -\frac{R_2}{R_1}[/important]
\]

**Conclusion :**
- Gain proportionnel au rapport \( R_2 / R_1 \)
- Signe négatif ⇒ inversion de phase (180°)sistances R1 et R2. Explique ton raisonnement.