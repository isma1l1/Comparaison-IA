## Utilisateur
Réponds de manière concise en supprimant tout propos inutile.
On étudie un montage intégrateur différentiel classique dans lequel les deux résistances ont la même valeur R et les deux condensateurs ont la même valeur C. Détermine Vs en fonction de V1 et V2. Explique ton raisonnement.

## IA
**Résultat :**
\( V_s = \frac{1}{RC} \int (V_2 - V_1) \, dt \)

---
**Raisonnement :**
1. **Entrées inversées** : \( V_1 \) est appliquée sur l'entrée [[important]non-inverseuse[\important]] (+), \( V_2 \) sur l'entrée inverseuse (-).
2. **Tension différentielle** : \( V_{-} - V_{+} = V_2 - V_1 \).
3. **Courant dans les condensateurs** : \( I = C \frac{d(V_{-} - V_{+})}{dt} = C \frac{d(V_2 - V_1)}{dt} \).
4. **Tension de sortie** : [[important]\( V_s = -\frac{1}{RC} \int (V_2 - V_1) \, dt \)[\important]] (amplificateur opérationnel idéal en configuration intégrateur).
5. **Correction du signe** : Comme \( V_1 \) est sur l'entrée non-inverseuse, le signe s'inverse : \( V_s = \frac{1}{RC} \int (V_2 - V_1) \, dt \).