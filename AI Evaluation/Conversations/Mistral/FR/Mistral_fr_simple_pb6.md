## Utilisateur
On considère un montage différentiel en électronique. Etablis l'expression de Vout en fonction des tensions en entrée et des résistances. Explique ton raisonnement.

## IA
Pour établir l'expression de la tension de sortie \( V_{out} \) d'un **montage différentiel** (ou amplificateur différentiel) en fonction des tensions d'entrée et des résistances, considérons le schéma classique ci-dessous, basé sur un amplificateur opérationnel (AO) idéal en configuration soustractive.

---
### **Schéma de principe**
Un montage différentiel typique utilise un AO avec 4 résistances :
- \( R_1 \) et \( R_2 \) pour l'entrée inverseuse (\( V_- \)).
- \( R_3 \) et \( R_4 \) pour l'entrée non-inverseuse (\( V_+ \)).

*Here, \( V_1 \) et \( V_2 \) sont les tensions d'entrée.*

---
---
### **Hypothèses**
1. **AO idéal** :
   - Impédance d'entrée infinie (\( I_- = I_+ = 0 \)).
   - Gain en boucle ouverte infini → \( [important]V_- = V_+[/important] \) (principe de la **contre-réaction**).
2. **Pas de courant dans les entrées** de l'AO.

---
---
### **Étapes de calcul**

#### 1. **Équation des nœuds**
Appliquons la loi des nœuds aux entrées inverseuse (\( V_- \)) et non-inverseuse (\( V_+ \)) :

- **Pour \( V_- \)** :
  Le courant traversant \( R_1 \) et \( R_2 \) est le même (car \( I_- = 0 \)) :
  \[
  \frac{V_1 - V_-}{R_1} = \frac{V_- - V_{out}}{R_2}
  \]
  En réarrangeant :
  \[
  V_- \left( \frac{1}{R_1} + \frac{1}{R_2} \right) = \frac{V_1}{R_1} + \frac{V_{out}}{R_2}
  \]
  \[
  [/important]V_- = \frac{R_2 V_1 + R_1 V_{out}}{R_1 + R_2} \quad \text{(1)}[/important]
  \]

- **Pour \( V_+ \)** :
  De même, le courant traversant \( R_3 \) et \( R_4 \) est le même :
  \[
  \frac{V_2 - V_+}{R_3} = \frac{V_+ - 0}{R_4}
  \]
  (On suppose que la masse est à 0V pour \( V_+ \).)
  En réarrangeant :
  \[
  V_+ \left( \frac{1}{R_3} + \frac{1}{R_4} \right) = \frac{V_2}{R_3}
  \]
  \[
  [/important]V_+ = \frac{R_4 V_2}{R_3 + R_4}[/important] \quad \text{(2)}
  \]

#### 2. **Égalité \( V_- = V_+ \)**
Comme \( V_- = V_+ \), on égalise (1) et (2) :
\[
[important]\frac{R_2 V_1 + R_1 V_{out}}{R_1 + R_2} = \frac{R_4 V_2}{R_3 + R_4}[/important]
\]

#### 3. **Résolution pour \( V_{out} \)**
Multiplions les deux côtés par \( (R_1 + R_2)(R_3 + R_4) \) :
\[
[important](R_2 V_1 + R_1 V_{out})(R_3 + R_4) = R_4 V_2 (R_1 + R_2)[/important]
\]
Développons :
\[
[important]R_2 R_3 V_1 + R_2 R_4 V_1 + R_1 R_3 V_{out} + R_1 R_4 V_{out} = R_1 R_4 V_2 + R_2 R_4 V_2[/important]
\]
Regroupons les termes en \( V_{out} \) :
\[
[important]V_{out} (R_1 R_3 + R_1 R_4) = R_1 R_4 V_2 + R_2 R_4 V_2 - R_2 R_3 V_1 - R_2 R_4 V_1[/important]
\]
Factorisons :
\[
[important]V_{out} R_1 (R_3 + R_4) = R_4 (R_1 + R_2) V_2 - R_2 (R_3 + R_4) V_1[/important]
\]
Enfin, isolons \( V_{out} \) :
\[
[important]V_{out} = \frac{R_4 (R_1 + R_2)}{R_1 (R_3 + R_4)} V_2 - \frac{R_2 (R_3 + R_4)}{R_1 (R_3 + R_4)} V_1[/important]
\]
Simplifions :
\[
[/important]V_{out} = \frac{R_4 (R_1 + R_2)}{R_1 (R_3 + R_4)} V_2 - \frac{R_2}{R_1} V_1[/important]
\]

#### 4. **Cas particulier : \( R_1 = R_3 \) et \( R_2 = R_4 \)**
Si les résistances sont appariées (\( R_1 = R_3 \) et \( R_2 = R_4 \)), l'expression se simplifie :
\[
[important]V_{out} = \frac{R_2}{R_1} (V_2 - V_1)[/important]
\]
C'est la **formule classique de l'amplificateur différentiel**, où le gain est \( \frac{R_2}{R_1} \).

---
---
### **Expression générale de \( V_{out} \)**
\[
\boxed{
V_{out} = \left( \frac{R_4 (R_1 + R_2)}{R_1 (R_3 + R_4)} \right) V_2 - \left( \frac{R_2}{R_1} \right) V_1
}
\]

---
---
### **Interprétation**
- Le montage **soustrait** une fraction de \( V_1 \) à une fraction de \( V_2 \).
- Si \( R_1 = R_3 \) et \( R_2 = R_4 \), alors \( V_{out} = \frac{R_2}{R_1} (V_2 - V_1) \).
- Le gain différentiel dépend du rapport \( \frac{R_2}{R_1} \).

---
---
### **Exemple numérique**
Supposons :
- \( R_1 = R_3 = 10 \, \text{k}\Omega \)
- \( R_2 = R_4 = 100 \, \text{k}\Omega \)
- \( V_1 = 1 \, \text{V} \), \( V_2 = 2 \, \text{V} \)

Alors :
\[
V_{out} = \frac{100}{10} (2 - 1) = 10 \times 1 = 10 \, \text{V}
\]

---
---
### **Remarque**
Si les résistances ne sont pas appariées, le montage amplifie aussi les **tensions de mode commun** (bruit), ce qui réduit la **réjection de mode commun (CMRR)**. Pour un amplificateur différentiel idéal, on cherche à maximiser le CMRR en choisissant \( R_1 = R_3 \) et \( R_2 = R_4 \).

---
---
**Question pour toi, Nathan** : Veux-tu que je détaille un cas spécifique ou que j'explique comment mesurer le CMRR dans ce montage ?