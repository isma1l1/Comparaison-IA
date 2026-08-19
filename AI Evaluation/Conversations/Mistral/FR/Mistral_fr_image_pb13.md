## Utilisateur
Voici un montage d'électronique analogique.
Les deux ALIs du montage fonctionnant en régime linéaire, montre que ce montage équivaut à un condensateur de capacité C, exprime C en fonction de C0 et alpha et dis quel est l'intérêt d'un tel montage.


---

## IA
Pour analyser ce montage, commençons par identifier les composants et leur rôle :

---

### **Analyse du montage**

1. **Structure du montage** :
   - Deux amplificateurs opérationnels (ALI 1 et ALI 2) fonctionnant en régime linéaire.
   - Un condensateur \( C_0 \) connecté entre la sortie du premier ALI et la masse.
   - Deux résistances : \( \alpha R \) et \( (1-\alpha)R \).
   - Une tension d'entrée \( u \) et un courant \( i \) en entrée.

2. **Hypothèses** :
   - Les ALI sont idéaux : impédance d'entrée infinie, impédance de sortie nulle, et gain infini en boucle ouverte.
   - Le régime linéaire implique que les ALI fonctionnent en mode suiveur ou amplificateur non inverseur/inverseur.

---

### **Étude des ALI**

#### **ALI 1** :
- **Configuration** : L'ALI 1 est en mode **intégrateur**.
  - La tension d'entrée \( u \) est appliquée à l'entrée non inverseuse (+).
  - Le condensateur \( C_0 \) est connecté entre la sortie et l'entrée inverseuse (-).
  - La résistance \( \alpha R \) est connectée entre l'entrée inverseuse (-) et la sortie de l'ALI 2.

- **Équation** :
  En régime linéaire, le courant traversant \( C_0 \) est donné par :
  \[
  i_{C_0} = C_0 \frac{d}{dt}(V_{out1} - V_{-1})
  \]
  Comme \( V_{-1} = V_{+1} = u \) (car l'ALI est idéal), on a :
  \[
  i_{C_0} = C_0 \frac{dV_{out1}}{dt}
  \]
  Le courant \( i \) entre dans l'ALI 1, donc :
  \[
  i = i_{C_0} = C_0 \frac{dV_{out1}}{dt}
  \]
  Cela implique :
  \[
  V_{out1} = \frac{1}{C_0} \int i \, dt
  \]

#### **ALI 2** :
- **Configuration** : L'ALI 2 est en mode **suiveur**.
  - La tension \( V_{out1} \) est appliquée à l'entrée non inverseuse (+) via la résistance \( (1-\alpha)R \).
  - La résistance \( \alpha R \) est connectée entre l'entrée inverseuse (-) et la sortie de l'ALI 1.
  - La sortie de l'ALI 2 est connectée à la masse via le condensateur \( C_0 \).

- **Équation** :
  Comme l'ALI 2 est un suiveur, \( V_{out2} = V_{+2} \).
  La tension \( V_{+2} \) est donnée par le diviseur de tension formé par \( \alpha R \) et \( (1-\alpha)R \) :
  \[
  V_{+2} = \frac{(1-\alpha)R}{R} V_{out1} + \frac{\alpha R}{R} \cdot 0 = (1-\alpha) V_{out1}
  \]
  Donc :
  \[
  V_{out2} = (1-\alpha) V_{out1}
  \]

- **Courant dans \( C_0 \)** :
  Le courant traversant \( C_0 \) est aussi donné par :
  \[
  i_{C_0} = C_0 \frac{d}{dt}(V_{out1} - V_{out2}) = C_0 \frac{d}{dt}(V_{out1} - (1-\alpha)V_{out1}) = C_0 \frac{d}{dt}(\alpha V_{out1})
  \]
  Donc :
  \[
  i_{C_0} = \alpha C_0 \frac{dV_{out1}}{dt}
  \]

- **Relation avec \( i \)** :
  On a déjà \( i = C_0 \frac{dV_{out1}}{dt} \), donc :
  \[
  i_{C_0} = \alpha i
  \]
  Cela signifie que le courant traversant \( C_0 \) est \( \alpha i \).

---

### **Équivalence avec un condensateur \( C \)**

Le montage se comporte comme un condensateur équivalent \( C \) tel que :
\[
i = C \frac{du}{dt}
\]
Or, d'après l'analyse précédente, on a :
\[
i = C_0 \frac{dV_{out1}}{dt}
\]
et
\[
V_{out1} = \frac{u}{\alpha}
\]
car \( V_{out2} = (1-\alpha)V_{out1} \) et \( V_{out2} = 0 \) (car connecté à la masse via \( C_0 \)).

Donc :
\[
\frac{dV_{out1}}{dt} = \frac{1}{\alpha} \frac{du}{dt}
\]
En substituant dans l'équation de \( i \) :
\[
i = C_0 \frac{1}{\alpha} \frac{du}{dt}
\]
On obtient :
\[
i = \frac{C_0}{\alpha} \frac{du}{dt}
\]
En comparant avec \( i = C \frac{du}{dt} \), on trouve :
\[
C = \frac{C_0}{\alpha}
\]

---
---
### **Intérêt du montage**
Ce montage permet de **simuler un condensateur de capacité équivalente \( C = \frac{C_0}{\alpha} \)**.
- **Avantage** : Si \( \alpha \) est très petit (par exemple, \( \alpha = 0.1 \)), alors \( C \) peut être **10 fois plus grand** que \( C_0 \).
- **Application** : Cela permet de réaliser des condensateurs de très grande capacité sans utiliser de composants physiques encombrants ou coûteux. C'est utile en électronique pour des applications nécessitant des constantes de temps très grandes (filtres, oscillateurs, etc.).

---
---
### **Conclusion**
Le montage équivaut à un condensateur de capacité :
\[
\boxed{C = \frac{C_0}{\alpha}}
\]
L'intérêt principal est de **simuler une capacité plus grande que \( C_0 \)** sans utiliser de condensateur physique de grande valeur.