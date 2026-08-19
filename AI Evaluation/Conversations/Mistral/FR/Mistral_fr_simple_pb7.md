## Utilisateur
On étudie un montage soustracteur classique. Détermine la relation entrée-sortie de ce système. Explique ton raisonnement.

## IA
### **Montage Soustracteur Classique : Relation Entrée-Sortie**

Un **montage soustracteur** est généralement réalisé à l'aide d'un **amplificateur opérationnel (AO)** en configuration linéaire. Le schéma classique utilise **deux entrées** (notées \( V_1 \) et \( V_2 \)) et produit une tension de sortie \( V_{out} \) proportionnelle à la **différence** entre ces deux entrées.

---

---
#### **1. Schéma du montage**
Le montage soustracteur standard ressemble à ceci :

- \( V_1 \) est appliquée sur l'entrée **non-inverseuse** (+) via une résistance \( R_1 \).
- \( V_2 \) est appliquée sur l'entrée **inverseuse** (-) via une résistance \( R_2 \).
- Une résistance de **rétroaction** \( R_f \) [important]relie la sortie à l'entrée inverseuse[/important].
- Une résistance \( R_3 \) relie l'entrée inverseuse à la masse (ou à une référence).

---
#### **2. Hypothèses de travail**
Pour simplifier l'analyse, on suppose que :
- L'AO est **[important]idéal[/important]** :
  - Gain en boucle ouverte infini (\( A \to \infty \)).
  - Impédance d'entrée infinie (\( Z_{in} \to \infty \)).
  - Impédance de sortie nulle (\( Z_{out} = 0 \)).
- Les résistances sont **appariées** : \( R_1 = R_2 = R \) et \( R_f = R_3 = R' \).
  *(C'est une condition courante pour un soustracteur équilibré.)*

---
#### **3. Analyse du montage**
On utilise les **deux règles d'or de l'AO idéal** :
1. **Tension différentielle nulle** : \( [important]V_+ = V_-[/important] \).
2. **Courant nul aux entrées** : \( I_+ = I_- = 0 \).

##### **Étape 1 : Tension à l'entrée non-inverseuse (\( V_+ \))**
L'entrée non-inverseuse est reliée à \( V_1 \) via \( R_1 \). Comme \( I_+ = 0 \), il n'y a pas de chute de tension aux bornes de \( R_1 \).
Donc :
\[
V_+ = V_1
\]

##### **Étape 2 : Tension à l'entrée inverseuse (\( V_- \))**
L'entrée inverseuse est reliée à \( V_2 \) via \( R_2 \) et à la sortie via \( R_f \). On applique le **théorème de Millman** (ou la loi des nœuds) :
\[
[important]V_- = \frac{V_2 \cdot \frac{1}{R_2} + V_{out} \cdot \frac{1}{R_f}}{\frac{1}{R_2} + \frac{1}{R_f}}[/important]
\]
Si \( R_2 = R \) et \( R_f = R' \), alors :
\[
[important]V_- = \frac{V_2 \cdot \frac{1}{R} + V_{out} \cdot \frac{1}{R'}}{\frac{1}{R} + \frac{1}{R'}} = \frac{V_2 R' + V_{out} R}{R + R'}[/important]
\]

##### **Étape 3 : Égalité \( V_+ = V_- \)**
D'après la règle 1 :
\[
V_1 = \frac{V_2 R' + V_{out} R}{R + R'}
\]
On isole \( V_{out} \) :
\[
V_1 (R + R') = V_2 R' + V_{out} R
\]
\[
V_{out} R = V_1 (R + R') - V_2 R'
\]
\[
[important]V_{out} = \frac{R + R'}{R} V_1 - \frac{R'}{R} V_2[/important]
\]

##### **Étape 4 : Cas des résistances appariées**
Si \( R_1 = R_2 = R \) et \( R_f = R_3 = R' \), et si on choisit \( R' = R \) (cas le plus simple), alors :
\[
V_{out} = \frac{R + R}{R} V_1 - \frac{R}{R} V_2 = 2V_1 - V_2
\]
**Mais ce n'est pas la configuration standard d'un soustracteur !**

Pour un **soustracteur pur**, on utilise généralement :
\[
R_1 = R_2 = R \quad \text{et} \quad R_f = R_3 = R'
\]
avec \( \frac{R'}{R} = 1 \) (c'est-à-dire \( R' = R \)).
Dans ce cas, la relation devient :
\[
V_{out} = V_1 - V_2
\]

**Explication :**
- Si \( R_1 = R_2 = R \) et \( R_f = R_3 = R \), alors :
  \[
  V_{out} = \frac{R + R}{R} V_1 - \frac{R}{R} V_2 = 2V_1 - V_2
  \]
  **Ce n'est pas un soustracteur pur !**

Pour obtenir \( V_{out} = V_1 - V_2 \), il faut que :
\[
\frac{R_f}{R_1} = \frac{R_3}{R_2}
\]
et \( R_1 = R_2 \), \( R_f = R_3 \).
Ainsi, avec \( R_1 = R_2 = R \) et \( R_f = R_3 = R' \), on a :
\[
V_{out} = \frac{R'}{R} (V_1 - V_2)
\]
Si \( R' = R \), alors :
\[
\boxed{V_{out} = V_1 - V_2}
\]

---
#### **4. Relation finale**
Pour un **montage soustracteur équilibré** (avec \( R_1 = R_2 = R \) et \( R_f = R_3 = R' \)) :
\[
\boxed{V_{out} = \frac{R_f}{R_1} (V_1 - V_2)}
\]
Si \( R_f = R_1 \), alors :
\[
\boxed{V_{out} = V_1 - V_2}
\]

---
#### **5. Explication physique**
- L'AO amplifie la **différence** entre \( V_+ \) et \( V_- \).
- En équilibrant les résistances, on s'assure que le gain pour \( V_1 \) et \( V_2 \) est le même, mais avec un signe opposé pour \( V_2 \) (car elle est appliquée sur l'entrée inverseuse).
- Le résultat est une **soustraction pure** des deux tensions d'entrée.

---
---
### **Résumé**
| Condition sur les résistances | Relation entrée-sortie |
|--------------------------------|-------------------------|
| \( R_1 = R_2 = R \), \( R_f = R_3 = R' \) | \( V_{out} = \frac{R'}{R} (V_1 - V_2) \) |
| \( R_1 = R_2 = R_f = R_3 = R \) | \( V_{out} = V_1 - V_2 \) |

---
**As-tu besoin d'une simulation ou d'un exemple numérique pour illustrer ce résultat ?**
