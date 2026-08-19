## Utilisateur
Réponds de manière concise en supprimant tout propos inutile.
On considère un montage différentiel en électronique. Etablis l'expression de Vout en fonction des tensions en entrée et des résistances. Explique ton raisonnement.

---
## IA
**Montage différentiel (amplificateur différentiel) :**

---
### **Expression de \( V_{out} \)**
\[
[important]V_{out} = \left(1 + \frac{R_2}{R_1}\right) \cdot \frac{R_4}{R_3 + R_4} \cdot V_2 - \frac{R_2}{R_1} \cdot V_1[/important]
\]

**Si \( R_1 = R_3 \) et \( R_2 = R_4 \) (cas idéal) :**
\[
[important]V_{out} = \frac{R_2}{R_1} (V_2 - V_1)[/important]
\]

---
### **Raisonnement**
1. **[important]Théorème de superposition[/important]** : On calcule \( V_{out} \) comme la somme des effets de \( V_1 \) et \( V_2 \) séparément.
2. **Effet de \( V_1 \)** :
   - \( V_1 \) est appliqué sur l'entrée inverseuse (\( - \)) via \( R_1 \).
   - \([important] V_{out}[/important] \) est amplifié par \( [important]-\frac{R_2}{R_1} \cdot V_1[/important] \).
3. **Effet de \( V_2 \)** :
   - \( V_2 \) est appliqué sur l'entrée non-inverseuse (\( + \)) via un diviseur de tension \( [/important]\frac{R_4}{R_3 + R_4}[/important] \).
   - \( V_{out} \) est amplifié par \( [important]\left(1 + \frac{R_2}{R_1}\right) \cdot \frac{R_4}{R_3 + R_4} \cdot V_2[/important] \).