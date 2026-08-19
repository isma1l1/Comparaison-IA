## Utilisateur
Donne moi l'expression de l'intensité dans la résistance R dans un montage à diode Zener. Explique ton raisonnement.

## IA
Pour déterminer l'expression de l'intensité \( I_R \) dans la résistance \( R \) d'un montage à diode Zener, considérons le schéma classique suivant :

---

### **Montage classique avec diode Zener**
- Une source de tension \( V_{in} \) (tension d'entrée).
- Une résistance \( R \) en série.
- Une diode Zener en parallèle avec la charge (ou la sortie), polarisée dans le sens inverse.

---

### **Hypothèses**
- La diode Zener est idéale : elle maintient une tension constante \( V_Z \) (tension Zener) à ses bornes lorsqu'elle est en conduction inverse.
- La tension d'entrée \( V_{in} \) est supérieure à \( V_Z \).

---

### **Analyse du circuit**
1. **Tension aux bornes de la résistance \( R \) :**
   La tension aux bornes de \( R \) est \( V_R = V_{in} - V_Z \).

2. **Intensité dans la résistance \( R \) :**
   D'après la loi d'Ohm, l'intensité \( I_R \) traversant la résistance \( R \) est donnée par :
   \[
   I_R = \frac{V_R}{R} = \frac{V_{in} - V_Z}{R}
   \]

---

### **Explication du raisonnement**
- La diode Zener est conçue pour maintenir une tension constante \( V_Z \) à ses bornes lorsqu'elle est polarisée en inverse. Cela signifie que la tension aux bornes de la charge (ou de la sortie) est stabilisée à \( V_Z \).
- La tension \( V_R \) aux bornes de la résistance \( R \) est donc la différence entre la tension d'entrée \( V_{in} \) et la tension Zener \( V_Z \).
- L'intensité \( I_R \) est simplement le rapport entre cette tension \( V_R \) et la valeur de la résistance \( R \).

---

### **Cas particuliers**
- Si \( V_{in} < V_Z \), la diode Zener ne conduit pas et \( I_R = 0 \) (la tension de sortie n'est pas régulée).
- Si \( V_{in} > V_Z \), la diode Zener conduit et régule la tension de sortie à \( V_Z \).

---

### **Résumé**
L'expression de l'intensité dans la résistance \( R \) est donc :
\[
\boxed{I_R = \frac{V_{in} - V_Z}{R}}
\]

---
Si tu veux approfondir un point particulier ou voir un exemple numérique, n'hésite pas à demander !