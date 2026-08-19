## Utilisateur
Réponds de manière concise en supprimant tout propos inutile. Donne moi la formule du gain d'un montage non-inverseur en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA
Le gain \( A_v \) d'un montage amplificateur non-inverseur est donné par la formule :

\[
[important]A_v = 1 + \frac{R_2}{R_1}[/important]
\]

**Raisonnement :**
- Le montage non-inverseur utilise une résistance de contre-réaction \( R_2 \) et une résistance \( R_1 \) reliée à la masse.
- La tension d'entrée \( [important]V_{in}[/important] \) est appliquée directement sur [important]l'entrée non-inverseuse (+)[/important] de l'amplificateur opérationnel.
- Grâce à la contre-réaction, la tension aux bornes de \( R_1 \) est [important]égale à \( V_{in}[/important] \).
- Le courant traversant \( R_1 \) et \( R_2 \) est le même ([important]courant nul dans l'entrée inverseuse[/important]).
- La tension de sortie \( [important]V_{out}[/important] \) est donc amplifiée selon le [important]rapport des résistances[/important] \( R_2 \) et \( R_1 \), avec un [important]gain minimal de 1[/important] (d'où le "+1").