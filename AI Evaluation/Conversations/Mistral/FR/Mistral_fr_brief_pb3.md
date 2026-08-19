## Utilisateur
Répond de manière concise en supprimant tout propos inutile. Donne moi l'expression de l'intensité dans la résistance R dans un montage à diode Zener. Explique ton raisonnement.

---

## IA
Dans un montage stabilisateur à diode Zener, l'intensité \( I_R \) dans la résistance \( R \) s'exprime par :

\[
I_R = I_{total} - I_Z
\]

**Où :**
- \( I_{total} = \frac{V_{in} - V_Z}{R} \) (courant total fourni par la source)
- \( I_Z \) = courant traversant la diode Zener (généralement donné ou négligeable si \( V_{in} \) est proche de \( V_Z \)).

---

**Raisonnement :**
1. **Loi des mailles** : \( V_{in} = V_R + V_Z \), avec \( V_R = R \cdot I_R \).
2. **Loi des nœuds** : \( I_R = I_{total} - I_Z \).
3. **Hypothèse de stabilisation** : La diode Zener maintient \( V_Z \) constant, donc \( I_R \) dépend de \( V_{in} \), \( V_Z \), et \( R \). Si \( I_Z \) est faible ou constant, \( I_R \approx I_{total} \).

---