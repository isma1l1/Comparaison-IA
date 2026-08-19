## Utilisateur
Donne moi l'expression de l'intensité dans la résistance R dans un montage à diode Zener. Explique ton raisonnement.

## IA
Dans un montage classique avec une **diode Zener en régulation**, on a généralement :

- une tension d’entrée \( V_{in} \),
- une résistance série \( R \),
- une diode Zener en parallèle avec la charge (ou seule),
- une tension de sortie stabilisée \( V_Z \) (tension Zener).

---

### Raisonnement

Quand la diode Zener fonctionne en régime de régulation (c’est-à-dire en **zone de claquage inverse**), elle impose :

\[
V_{out} = V_Z
\]

La résistance \( R \) est donc soumise à la différence de potentiel :

\[
V_R = V_{in} - V_Z
\]

D’après la loi d’Ohm, l’intensité qui traverse la résistance est :

\[
I_R = \frac{V_{in} - V_Z}{R}
\]

---

### Interprétation

- Cette intensité \( I_R \) est le **courant total fourni par la source**.
- Elle se divise ensuite en :
  - courant dans la Zener \( I_Z \),
  - courant dans la charge \( I_L \) (s’il y en a une).

Donc :

\[
I_R = I_Z + I_L
\]

---

### Condition importante

Pour que la formule reste valable **en régime de régulation**, il faut que :

- \( V_{in} > V_Z \)
- et que le courant Zener reste dans sa plage de fonctionnement (ni trop faible, ni trop élevé).

---

Si tu veux, je peux te faire un schéma du montage ou te donner un exemple numérique