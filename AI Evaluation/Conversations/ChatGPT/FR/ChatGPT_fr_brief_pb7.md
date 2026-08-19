## Utilisateur
Réponds de manière concise en supprimant tout propos inutile. 
On étudie un montage soustracteur classique. Détermine la relation entrée-sortie de ce système. Explique ton raisonnement.

## IA
On suppose un amplificateur opérationnel [important]idéal[/important] en régime linéaire (gain infini, courant d’entrée nul, \([important]V^+=V^-[/important]\)).

Montage soustracteur classique :
- \(V_1\) appliquée via \(R_1\) à l’entrée inverseuse
- rétroaction \(R_2\) entre sortie et entrée inverseuse
- \(V_2\) appliquée via un pont \(R_3, R_4\) à l’entrée non-inverseuse

1) Tension à l’entrée non-inverseuse :
\[
[important]V^+ = V_2 \cdot \frac{R_4}{R_3 + R_4}[/important]
\]

2) Par égalité des entrées :
\[
V^- = V^+ = V_2 \cdot \frac{R_4}{R_3 + R_4}
\]

3) Loi des courants au nœud inverseur :
\[
[important]\frac{V_1 - V^-}{R_1} + \frac{V_{out} - V^-}{R_2} = 0[/important]
\]

4) Résolution :
\[
[important]V_{out} = V^- \left(1 + \frac{R_2}{R_1}\right) - \frac{R_2}{R_1} V_1[/important]
\]

5) En remplaçant \(V^-\) :
\[
[important]V_{out} = \left(1 + \frac{R_2}{R_1}\right)\frac{R_4}{R_3 + R_4} V_2 - \frac{R_2}{R_1} V_1[/important]
\]

Cas particulier usuel (soustracteur pur) :
si \(\frac{R_2}{R_1} = \frac{R_4}{R_3}\), alors
\[
[important]V_{out} = \frac{R_2}{R_1}(V_2 - V_1)[/important]
\]

Conclusion : le montage réalise une soustraction pondérée des entrées.
