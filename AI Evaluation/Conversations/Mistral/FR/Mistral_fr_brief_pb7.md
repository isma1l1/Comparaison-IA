## Utilisateur
Réponds de manière concise en supprimant tout propos inutile.
On étudie un montage soustracteur classique. Détermine la relation entrée-sortie de ce système. Explique ton raisonnement.

---
## IA
**Relation entrée-sortie d'un montage soustracteur classique** :
\( V_{out} = V_2 - V_1 \)

---
**Raisonnement** :
1. **Amplificateur opérationnel [important]idéal[/important]** : \( [important]V^+ = V^-[/important] \) (tension différentielle nulle).
2. **Superposition** :
   - \( V_1 \) est appliquée sur l'entrée inverseuse (\( V^- \)) via \( R_1 \).
   - \( V_2 \) est appliquée sur l'entrée non-inverseuse (\( V^+ \)) via \( R_2 \).
3. **Équation des nœuds** :
   - \( V^- = V_1 \) (si \( R_1 = R_2 = R \) et \( R_f = R \)).
   - \( V^+ = V_2 \).
4. **Sortie** : \( V_{out} = V^+ - V^- = V_2 - V_1 \).
