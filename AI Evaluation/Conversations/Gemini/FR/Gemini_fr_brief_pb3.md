## Utilisateur

Réponds de manière concise en supprimant tout propos inutile. Donne moi l'expression de l'intensité dans la résistance R dans un montage à diode Zener. Explique ton raisonnement.

---

## IA

Dans un montage stabilisateur à diode Zener, on considère une tension d'entrée $U_e$, une résistance de protection $R$, et une diode Zener de tension $V_z$ placée en parallèle avec une charge $R_u$.

### Expression de l'intensité

L'intensité $I$ traversant la résistance $R$ est donnée par :

$$I = \frac{U_e - V_z}{R}$$

---

### Raisonnement

Le calcul repose sur deux principes fondamentaux de l'électronique :

1. **Régime Zener :** Lorsque la diode est passante en régime d'avalanche (polarisation inverse), elle impose une tension constante à ses bornes égale à sa tension nominale $V_z$.
2. **Loi des mailles :** En parcourant la maille d'entrée, on obtient l'équation $U_e - U_R - V_z = 0$.
3. **Loi d'Ohm :** La tension aux bornes de la résistance est $U_R = R \cdot I$.

En substituant, on extrait $I$ pour isoler le courant total fourni par la source avant sa division vers la diode et la charge.
