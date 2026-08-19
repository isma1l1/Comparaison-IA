## Utilisateur
On étudie un montage soustracteur classique. Détermine la relation entrée-sortie de ce système. Explique ton raisonnement.

## IA
On considère un **montage soustracteur classique** réalisé avec un amplificateur opérationnel [important]idéal[/important].

Schéma implicite standard :
- Deux entrées \( V_1 \) et \( V_2 \)
- Quatre résistances \( R_1, R_2, R_3, R_4 \)
- \( V_1 \) appliquée sur l’entrée inverseuse via \( R_1 \), avec contre-réaction \( R_2 \)
- \( V_2 \) appliquée sur l’entrée non-inverseuse via un pont \( R_3, R_4 \)

Hypothèses d’un AOP idéal :
- Courant d’entrée nul
- \( [/important]V^+ = V^-[/important] \)

1) Tension à l’entrée non-inverseuse

Le point \( V^+ \) est donné par un pont diviseur :

\[
[important]V^+ = \frac{R_4}{R_3 + R_4} \, V_2[/important]
\]

2) Égalité des entrées

\[
V^- = V^+ = \frac{R_4}{R_3 + R_4} \, V_2
\]

3) Loi des courants au nœud inverseur

Comme aucun courant ne rentre dans l’AOP :

\[
[important]\frac{V_1 - V^-}{R_1} = \frac{V^- - V_{out}}{R_2}[/important]
\]

4) Remplacement de \( V^- \)

\[
\frac{V_1 - V^-}{R_1} = \frac{V^- - V_{out}}{R_2}
\]

On isole \( V_{out} \) :

\[
V_{out} = V^- - \frac{R_2}{R_1}(V_1 - V^-)
\]

Développement :

\[
V_{out} = V^- \left(1 + \frac{R_2}{R_1}\right) - \frac{R_2}{R_1} V_1
\]

5) Substitution de \( V^- \)

\[
[important]V_{out} = \left( \frac{R_4}{R_3 + R_4} \right)\left(1 + \frac{R_2}{R_1}\right) V_2 - \frac{R_2}{R_1} V_1[/important]
\]

---

Cas particulier classique (montage soustracteur équilibré) :

Si :
\[
\frac{R_2}{R_1} = \frac{R_4}{R_3}
\]

alors la relation se simplifie en :

\[
[important]V_{out} = \frac{R_2}{R_1} (V_2 - V_1)[/important]
\]

---

Conclusion :

Le montage réalise une **soustraction amplifiée** des deux signaux d’entrée. Le gain dépend du rapport des résistances, et l’équilibrage des rapports garantit une soustraction propre sans erreur de mode commun.
