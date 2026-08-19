## Utilisateur
Réponds de manière concise en supprimant tout propos inutile. Donne moi la formule du gain d'un montage inverseur en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA
Le gain \( A_v \) d'un montage inverseur (amplificateur inverseur) est donné par la formule :

\[
[important]A_v = -\frac{R_2}{R_1}[/important]
\]

**Raisonnement :**
- Le courant entrant dans l'amplificateur opérationnel (AO) idéal est nul (impédance d'entrée infinie).
- La [important]tension aux bornes de l'entrée inverseuse (\( V^- \)) est égale à la tension de l'entrée non inverseuse (\( V^+ \))[/important], qui est généralement [important]reliée à la masse (0 V)[/important].
- En appliquant la [important]loi des nœuds[/important] à l'entrée inverseuse, on obtient :

  \[
  [important]\frac{V_{in} - V^-}{R_1} = \frac{V^- - V_{out}}{R_2}[/important]
  \]

- Comme \( V^- = 0 \) V, on simplifie :
  \[
  \frac{V_{in}}{R_1} = -\frac{V_{out}}{R_2}
  \]
- Le gain \( [important]A_v = \frac{V_{out}}{V_{in}}[/important] \) est donc :

  \[
  [important]A_v = -\frac{R_2}{R_1}[/important]
  \]
