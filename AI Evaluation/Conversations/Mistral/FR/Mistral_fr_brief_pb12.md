## Utilisateur
Réponds de manière concise en supprimant tout propos inutile.
Simplifie ce circuit entre les points A et B pour le réduire à un circuit avec un générateur de tension et une résistance. Donne leurs valeurs en fonction des données.

*(image de circuit électrique avec des résistances et des sources de tension)*

---
## IA
Pour simplifier le circuit entre les points **A** et **B** :

1. **Résistance équivalente** :
   - Les résistances de **10 Ω** (en haut) et **20 Ω** (en bas) sont en série avec la **30 Ω** : **10 + 20 + 30 = 60 Ω**.
   - Cette combinaison est en parallèle avec la résistance de **10 Ω** (au centre) :
     \( R_{eq} = \frac{60 \times 10}{60 + 10} = \frac{600}{70} = \frac{60}{7} \, \Omega \).
   - Enfin, cette résistance équivalente est en série avec la résistance de **10 Ω** (à gauche) :
     \( R_{totale} = 10 + \frac{60}{7} = \frac{130}{7} \, \Omega \).

2. **Tension équivalente** :
   - Les sources de tension \( V_{src1} \), \( V_{src2} \), et \( V_{src3} \) sont en série et en opposition.
   - \( V_{eq} = V_{src1} - V_{src2} + V_{src3} \).

---
**Circuit simplifié** :
- **Générateur de tension** : \( V_{eq} = V_{src1} - V_{src2} + V_{src3} \)
- **Résistance équivalente** : \( R_{totale} = \frac{130}{7} \, \Omega \)
