## Utilisateur
Réponds de manière concise en supprimant tout propos inutile.
On étudie un montage comparateur à hystérésis inverseur dans lequel la résistance entre la masse et l'entrée non-inverseuse est notée R1 et la résistance entre l'entrée non-inverseuse et la sortie de l'ALI est notée R2. Identifie le régime de fonctionnement de l'ALI, exprime le potentiel v+ en fonction de s, déduis-en les tensions de basculement, représente le cycle d'hystérésis du montage dans le cas où R2 = 2*R1, et représente le signal de sortie pour une entrée sinusoïdale d'amplitude 10V. Explique ton raisonnement.

---
## IA
**Régime de fonctionnement** : L'ALI fonctionne en **[important]régime non-linéaire (saturé)[/important]**.

---
**Potentiel \( v_+ \)** :
\( [important]v_+ = \frac{R1 \cdot s + R2 \cdot 0}{R1 + R2} = \frac{R1}{R1 + R2} \cdot s[/important] \)

---
**Tensions de basculement** :
- **Seuil haut** : \( V_{H} = \frac{R1}{R1 + R2} \cdot V_{sat+} \)
- **Seuil bas** : \( V_{B} = \frac{R1}{R1 + R2} \cdot V_{sat-} \)

Avec \( [important]R2 = 2R1[/important] \) :
- \( [important]V_{H} = \frac{1}{3} V_{sat+}[/important] \)
- \( [important]V_{B} = \frac{1}{3} V_{sat-}[/important] \)

---
**Cycle d'hystérésis** :
- **Largeur** : \( \Delta V = V_H - V_B = \frac{1}{3}(V_{sat+} - V_{sat-}) \).
- **Représentation** : [important]Droite avec hystérésis entre \( V_B \) et \( V_H \)[/important].

---
**Signal de sortie pour \( v_e = 10 \sin(\omega t) \)** :
- **Sortie** : [important]Signal carré entre \( V_{sat+} \) et \( V_{sat-} \), basculant aux seuils \( V_H \) et \( V_B \)[/important].

---
**Explication** :
L'ALI sature car \( v_+ \) dépend de \( s \) (rétroaction positive). Les seuils dépendent de \( R1 \) et \( R2 \). Le signal sinusoïdal fait basculer la sortie aux seuils, créant un signal carré.