## Utilisateur
Voici un montage d'électronique analogique.
Etablis l'expression de Vout en fonction des tensions en entrée. Explique ton raisonnement.



---

## IA
Pour établir l'expression de **Vout** en fonction des tensions d'entrée **Vin1** et **Vin2** dans ce montage, analysons le circuit étape par étape.

---

## **Analyse du circuit**

### **1. Identification du montage**
Le circuit représente un **amplificateur opérationnel (AO) en configuration de soustracteur (ou amplificateur différentiel)**.
- **Vin1** est appliqué sur l'entrée inverseuse (-) via **R1**.
- **Vin2** est appliqué sur l'entrée non-inverseuse (+) via **R2**.
- **Rf** est la résistance de rétroaction entre la sortie (Vout) et l'entrée inverseuse.
- **Rg** est la résistance de mise à la masse de l'entrée non-inverseuse.

---

### **2. Hypothèses de travail**
- L'AO est **idéal** :
  - Impédance d'entrée infinie → **Aucun courant ne rentre dans les entrées (+) et (-)**.
  - Gain en boucle ouverte infini → **La tension différentielle entre les entrées est nulle** : \( [important]V_+ = V_-[/important] \).

---

### **3. Équations de base**
#### **a. Tension à l'entrée inverseuse (-) : \( V_- \)**
Le courant traversant **R1** est :
\[
I_1 = \frac{V_{in1} - V_-}{R_1}
\]
Le courant traversant **Rf** est :
\[
I_f = \frac{V_{out} - V_-}{R_f}
\]
Comme **aucun courant ne rentre dans l'entrée (-)**, on a :
\[
[important]I_1 = I_f \implies \frac{V_{in1} - V_-}{R_1} = \frac{V_{out} - V_-}{R_f}[/important]
\]
En réarrangeant :
\[
V_- \left( \frac{1}{R_1} + \frac{1}{R_f} \right) = \frac{V_{in1}}{R_1} + \frac{V_{out}}{R_f}
\]
\[
[important]V_- = \frac{R_f V_{in1} + R_1 V_{out}}{R_1 + R_f}[/important]
\]

#### **b. Tension à l'entrée non-inverseuse (+) : \( V_+ \)**
Le courant traversant **R2** est :
\[
I_2 = \frac{V_{in2} - V_+}{R_2}
\]
Le courant traversant **Rg** est :
\[
I_g = \frac{V_+ - 0}{R_g} = \frac{V_+}{R_g}
\]
Comme **aucun courant ne rentre dans l'entrée (+)**, on a :
\[
[important]I_2 = I_g \implies \frac{V_{in2} - V_+}{R_2} = \frac{V_+}{R_g}[/important]
\]
En réarrangeant :
\[
V_+ \left( \frac{1}{R_2} + \frac{1}{R_g} \right) = \frac{V_{in2}}{R_2}
\]
\[
[important]V_+ = \frac{R_g V_{in2}}{R_2 + R_g}[/important]
\]

---
### **4. Égalité \( V_+ = V_- \)**
D'après l'hypothèse de l'AO idéal :
\[
[important]\frac{R_g V_{in2}}{R_2 + R_g} = \frac{R_f V_{in1} + R_1 V_{out}}{R_1 + R_f}[/important]
\]

---
### **5. Résolution pour \( V_{out} \)**
Multiplions les deux côtés par \( (R_1 + R_f)(R_2 + R_g) \) :
\[
[important]R_g (R_1 + R_f) V_{in2} = (R_2 + R_g)(R_f V_{in1} + R_1 V_{out})[/important]
\]
Développons :
\[
[important]R_g R_1 V_{in2} + R_g R_f V_{in2} = R_2 R_f V_{in1} + R_2 R_1 V_{out} + R_g R_f V_{in1} + R_g R_1 V_{out}[/important]
\]
Regroupons les termes en \( V_{out} \) :
\[
[important]R_g R_1 V_{in2} + R_g R_f V_{in2} - R_2 R_f V_{in1} - R_g R_f V_{in1} = V_{out} (R_2 R_1 + R_g R_1)[/important]
\]
Factorisons :
\[
[important]V_{out} = \frac{R_f (R_g V_{in2} - R_2 V_{in1}) + R_g R_1 V_{in2} - R_g R_f V_{in1}}{R_1 (R_2 + R_g)}[/important]
\]

---
### **6. Simplification (cas classique où \( R_1 = R_2 \) et \( R_f = R_g \))**
Si on suppose que **\( R_1 = R_2 \)** et **\( R_f = R_g \)**, l'expression se simplifie en :
\[
[important]V_{out} = \frac{R_f}{R_1} (V_{in2} - V_{in1})[/important]
\]

---
## **Expression finale de \( V_{out} \)**
### **Cas général :**
\[
\boxed{
V_{out} = \frac{R_f (R_g V_{in2} - R_2 V_{in1}) + R_1 R_g V_{in2} - R_1 R_f V_{in1}}{R_1 (R_2 + R_g)}
}
\]

### **Cas simplifié (si \( R_1 = R_2 \) et \( R_f = R_g \)) :**
\[
\boxed{
V_{out} = \frac{R_f}{R_1} (V_{in2} - V_{in1})
}
\]

---
## **Interprétation**
- Ce montage **soustrait** les deux tensions d'entrée, amplifiées par le rapport \( \frac{R_f}{R_1} \).
- Si \( R_f = R_1 \), alors \( V_{out} = V_{in2} - V_{in1} \).

---
As-tu besoin d'une vérification numérique ou d'une explication supplémentaire ?