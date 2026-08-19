## Utilisateur
On étudie un montage dérivateur classique. Détermine la relation entrée-sortie de ce système. Explique ton raisonnement.

## IA
### **Relation entrée-sortie d'un montage dérivateur classique**

Un **montage dérivateur** est un circuit RC (résistance-condensateur) où la tension de sortie est prélevée aux bornes de la résistance. Voici comment déterminer sa relation entrée-sortie.

---

#### **1. Schéma du montage**


- **V_in** : Tension d'entrée (source)
- **V_out** : Tension de sortie (aux bornes de R)
- **R** : Résistance
- **C** : Condensateur

---

#### **2. Loi des mailles et relation courant-tension**
En appliquant la **loi des mailles** :
\[
V_{in} = V_R + V_C
\]
où :
- \( V_R = R \cdot i(t) \) (loi d'Ohm)
- \( i(t) = C \frac{dV_C}{dt} \) (relation courant-tension du condensateur)

En remplaçant \( V_C \) par \( V_{in} - V_R \) :
\[
i(t) = C \frac{d(V_{in} - V_R)}{dt}
\]
Or \( V_R = V_{out} \), donc :
\[
i(t) = C \frac{d(V_{in} - V_{out})}{dt}
\]

Mais \( V_R = R \cdot i(t) \), donc :
\[
V_{out} = R \cdot C \frac{d(V_{in} - V_{out})}{dt}
\]

---

#### **3. Équation différentielle**
En développant :
\[
V_{out} = RC \left( \frac{dV_{in}}{dt} - \frac{dV_{out}}{dt} \right)
\]
\[
V_{out} + RC \frac{dV_{out}}{dt} = RC \frac{dV_{in}}{dt}
\]

C'est une **équation différentielle du 1er ordre**.

---

#### **4. Solution en régime harmonique (analyse fréquentielle)**
En régime sinusoïdal, on utilise la **transformée de Laplace** ou les **complexes** :
- \( V_{in}(j\omega) \) : Tension d'entrée en notation complexe
- \( V_{out}(j\omega) \) : Tension de sortie en notation complexe
- L'impédance du condensateur : \( Z_C = \frac{1}{jC\omega} \)

La tension de sortie est aux bornes de \( R \), donc :
\[
V_{out} = V_{in} \cdot \frac{R}{R + Z_C} = V_{in} \cdot \frac{R}{R + \frac{1}{jC\omega}}
\]
\[
V_{out} = V_{in} \cdot \frac{jRC\omega}{1 + jRC\omega}
\]

---
#### **5. Fonction de transfert**
La **fonction de transfert** \( H(j\omega) \) est :
\[
H(j\omega) = \frac{V_{out}}{V_{in}} = \frac{jRC\omega}{1 + jRC\omega}
\]

En posant \( \tau = RC \) (constante de temps) :
\[
H(j\omega) = \frac{j\tau\omega}{1 + j\tau\omega}
\]

---
#### **6. Comportement fréquentiel**
- **À basse fréquence** (\( \omega \to 0 \)) :
  \( H(j\omega) \approx j\tau\omega \)
  → **Comportement dérivateur** : \( V_{out} \propto \frac{dV_{in}}{dt} \).

- **À haute fréquence** (\( \omega \to \infty \)) :
  \( H(j\omega) \approx 1 \)
  → **Gain unitaire** (le condensateur se comporte comme un court-circuit).

---
#### **7. Relation entrée-sortie temporelle (approximation dérivateur)**
Si \( \omega \gg \frac{1}{\tau} \) (haute fréquence) :
\[
V_{out}(t) \approx RC \frac{dV_{in}}{dt}
\]
**C'est la relation classique d'un dérivateur.**

---
### **Résumé**
| Domaine          | Relation entrée-sortie                          |
|------------------|-------------------------------------------------|
| **Temporel**     | \( V_{out} + RC \frac{dV_{out}}{dt} = RC \frac{dV_{in}}{dt} \) |
| **Fréquentiel**  | \( H(j\omega) = \frac{jRC\omega}{1 + jRC\omega} \) |
| **Approximation dérivateur** | \( V_{out}(t) \approx RC \frac{dV_{in}}{dt} \) (si \( \omega \gg \frac{1}{RC} \)) |

---
### **Explication physique**
- Le condensateur **bloque les basses fréquences** (tension continue) et **laisse passer les hautes fréquences**.
- La tension aux bornes de \( R \) est proportionnelle à la **dérivée de la tension d'entrée** si la fréquence est suffisamment élevée.

---
**Question pour toi, Nathan** :
Veux-tu que je développe un exemple concret avec des valeurs numériques pour \( R \) et \( C \), ou bien as-tu besoin de précisions sur un point particulier ?