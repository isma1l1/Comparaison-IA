## Utilisateur
Réponds de manière concise en supprimant tout propos inutile.
On étudie un montage dérivateur classique. Détermine la relation entrée-sortie de ce système. Explique ton raisonnement.

## IA
**Relation entrée-sortie d'un montage dérivateur classique (RC) :**

---
### **Hypothèse**
Circuit RC série avec :
- **Entrée** : \( v_e(t) \)
- **Sortie** : \( v_s(t) \) (tension aux bornes de R)

---
### **Loi des mailles**
\( v_e(t) = v_R(t) + v_C(t) \)

---
### **Relations fondamentales**
- \( v_R(t) = R \cdot i(t) \)
- \( i(t) = C \frac{dv_C(t)}{dt} \)

---
### **Substitution**
\( v_e(t) = R \cdot C \frac{dv_C(t)}{dt} + v_C(t) \)

Or \( v_s(t) = v_R(t) = R \cdot i(t) = R \cdot C \frac{dv_C(t)}{dt} \).

---
### **Équation différentielle**
En remplaçant \( v_C(t) = v_e(t) - v_s(t) \) :
\( v_e(t) = R \cdot C \frac{d(v_e(t) - v_s(t))}{dt} + (v_e(t) - v_s(t)) \)

---
### **Simplification**
Si \( v_e(t) \) est sinusoïdale (régime permanent) :
**Fonction de transfert** :
\( \frac{V_s}{V_e} = j \cdot R \cdot C \cdot \omega \)
ou en temporel :
**\( v_s(t) = R \cdot C \frac{dv_e(t)}{dt} \)**

---
**Conclusion** : La sortie est proportionnelle à la **dérivée** de l'entrée.