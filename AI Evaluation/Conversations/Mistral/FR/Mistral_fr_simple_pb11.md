## Utilisateur
On étudie un montage intégrateur différentiel classique dans lequel les deux résistances ont la même valeur R et les deux condensateurs ont la même valeur C. Détermine Vs en fonction de V1 et V2. Explique ton raisonnement.

---
## IA
Pour déterminer la tension de sortie \( V_s \) d'un **montage intégrateur différentiel** (ou amplificateur différentiel intégrateur) avec deux résistances \( R \) et deux condensateurs \( C \) identiques, analysons le circuit étape par étape.

---

## **1. Schéma du montage**
Le montage classique est le suivant :
- **Entrées** : \( V_1 \) ([[important]non-inverseuse[\important]]) et \( V_2 \) (inverseuse).
- **Composants** :
  - Deux résistances \( R \) (une pour chaque entrée).
  - Deux condensateurs \( C \) (un en rétroaction entre la sortie et l'entrée inverseuse, et un entre l'entrée non-inverseuse et la masse).
- **Amplificateur opérationnel (AO)** : Supposé idéal (impédance d'entrée infinie, gain infini, bande passante infinie).

---

## **2. Hypothèses**
- L'AO est idéal : \( V_+ = V_- \) (tension différentielle nulle).
- Les courants dans les entrées de l'AO sont nuls (impédance d'entrée infinie).
- Les condensateurs sont initialement déchargés.

---

## **3. Analyse des courants**
### **Côté entrée non-inverseuse (\( V_1 \))**
- Le condensateur \( C \) est connecté entre \( V_1 \) et \( V_+ \).
- Le courant \( I_1 \) traversant \( R \) vers \( V_+ \) est :
  \[
  I_1 = \frac{V_1 - V_+}{R}
  \]
- Comme \( [[important]V_+ = V_-[\important]] \), notons \( V_+ = V_- = V \).

### **Côté entrée inverseuse (\( V_2 \))**
- Le courant \( I_2 \) traversant \( R \) vers \( V_- \) est :
  \[
  I_2 = \frac{V_2 - V_-}{R} = \frac{V_2 - V}{R}
  \]
- Le courant traversant le condensateur de rétroaction \( C \) est :
  \[
  I_C = C \frac{d(V_- - V_s)}{dt} = C \frac{d(V - V_s)}{dt}
  \]
- Par conservation des courants au nœud \( V_- \) (pas de courant dans l'AO) :
  \[
  I_2 = I_C \implies \frac{V_2 - V}{R} = C \frac{d(V - V_s)}{dt}
  \]

### **Côté non-inverseuse**
- Le courant traversant le condensateur connecté à \( V_1 \) est :
  \[
  I_{C1} = C \frac{d(V_1 - V_+)}{dt} = C \frac{d(V_1 - V)}{dt}
  \]
- Comme il n'y a pas de courant dans l'entrée de l'AO :
  \[
  I_1 = I_{C1} \implies \frac{V_1 - V}{R} = C \frac{d(V_1 - V)}{dt}
  \]

---

## **4. Résolution des équations**
### **Équation pour \( V \)**
De l'équation côté non-inverseuse :
\[
\frac{V_1 - V}{R} = C \frac{d(V_1 - V)}{dt}
\]
En développant :
\[
\frac{V_1 - V}{R} = C \left( \frac{dV_1}{dt} - \frac{dV}{dt} \right)
\]
Si on suppose que \( V_1 \) est constant (ou que sa dérivée est négligeable devant celle de \( V \)), alors \( \frac{dV_1}{dt} = 0 \), et :
\[
\frac{V_1 - V}{R} = -C \frac{dV}{dt}
\]
C'est une équation différentielle du premier ordre. Sa solution en régime permanent (pour un signal d'entrée constant) donne :
\[
V = V_1
\]
*(Cela signifie que \( V_+ = V_1 \) et \( V_- = V_1 \) en régime établi.)*

### **Équation pour \( V_s \)**
De l'équation côté inverseuse :
\[
\frac{V_2 - V}{R} = C \frac{d(V - V_s)}{dt}
\]
Avec \( V = V_1 \) :
\[
\frac{V_2 - V_1}{R} = C \frac{d(V_1 - V_s)}{dt}
\]
En intégrant par rapport au temps :
\[
V_1 - V_s = \frac{1}{RC} \int (V_2 - V_1) \, dt + K
\]
où \( K \) est une constante d'intégration. Si on suppose que les condensateurs sont initialement déchargés (\( V_s = 0 \) à \( t = 0 \)), alors \( K = 0 \).

Ainsi :
\[
V_s = V_1 - \frac{1}{RC} \int (V_2 - V_1) \, dt
\]

---
## **5. Expression finale de \( V_s \)**
En dérivant l'expression ci-dessus, on obtient la relation différentielle :
\[
\frac{dV_s}{dt} = \frac{V_1 - V_2}{RC}
\]
En intégrant :
[[important]\[
V_s = \frac{1}{RC} \int (V_1 - V_2) \, dt + K
\][\important]]
Si on suppose que \( V_s(0) = 0 \), alors \( K = 0 \), et :
\[
\boxed{V_s = \frac{1}{RC} \int (V_1 - V_2) \, dt}
\]

---
## **6. Interprétation**
- Le montage **intègre la différence** entre \( V_1 \) et \( V_2 \).
- Le facteur \( \frac{1}{RC} \) est la **constante de temps** de l'intégrateur.
- Si \( V_1 \) et \( V_2 \) sont des signaux constants, \( V_s \) sera une **rampe linéaire** (intégrale d'une constante).

---
## **7. Cas particulier : Entrées sinusoïdales**
Si \( V_1 \) et \( V_2 \) sont des signaux sinusoïdaux de même fréquence, par exemple :
\[
V_1 = A \sin(\omega t), \quad V_2 = B \sin(\omega t)
\]
Alors :
\[
V_s = \frac{1}{RC} \int (A - B) \sin(\omega t) \, dt = \frac{A - B}{RC \omega} (-\cos(\omega t)) + K
\]
Le montage se comporte comme un **filtre passe-bas** (atténuation des hautes fréquences).

---
## **Résumé**
   **Type de signal** | **Expression de \( V_s \)**                     |
 |--------------------|-----------------------------------------------|
 | Constant           | \( V_s = \frac{V_1 - V_2}{RC} \cdot t \)      |
 | Sinusoïdal         | \( V_s = \frac{A - B}{RC \omega} (-\cos(\omega t)) \) |

---
### **Remarque importante**
Ce montage est sensible aux **dérives** (offset) et au **bruit**, car il intègre tous les signaux, y compris les perturbations. En pratique, on ajoute souvent une résistance en parallèle avec le condensateur de rétroaction pour limiter le gain en continu (montage "intégrateur réel").

---
As-tu d'autres questions sur ce montage ou son application ?