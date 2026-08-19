## Utilisateur
Voici un montage d'électronique analogique.

Donne-moi la formule du gain de ce circuit en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA
Ce circuit représente un **amplificateur opérationnel (AO) monté en configuration non-inverseuse**. Voici comment déterminer la formule du gain de ce montage :

---

### **Raisonnement :**

1. **Configuration non-inverseuse** :
   Dans ce montage, la tension d'entrée \( V_{in} \) est appliquée directement sur l'entrée non-inverseuse (+) de l'AO.

2. **Rétroaction négative** :
   La résistance \( R1 \) est connectée entre la sortie de l'AO et son entrée inverseuse (-), et \( R2 \) est connectée entre l'entrée inverseuse et la masse.

3. **Hypothèse de l'AO idéal** :
   - Le courant entrant dans les entrées de l'AO est nul.
   - La tension différentielle entre les entrées (+) et (-) est nulle (\( [important]V_+ = V_-[/important] \)).

4. **Calcul des tensions** :
   - La tension aux bornes de \( R2 \) est \( V_{in} \) (car \( V_- = V_{in} \)).
   - Le courant traversant \( R2 \) est donc \( I = \frac{V_{in}}{R2} \).
   - Ce même courant traverse \( R1 \), donc la tension aux bornes de \( R1 \) est \( V_{R1} = I \times R1 = \frac{V_{in}}{R2} \times R1 \).

5. **Tension de sortie \( V_{out} \)** :
   - La tension de sortie est la somme de la tension aux bornes de \( R1 \) et de \( V_{in} \) :
     \[
     [important]V_{out}[/important] = V_{in} + V_{R1} = [important]V_{in} + \frac{V_{in}}{R2} \times R1[/important]
     \]
   - En factorisant :
     \[
     [important]V_{out} = V_{in} \left(1 + \frac{R1}{R2}\right)[/important]
     \]

6. **Gain du montage** :
   Le gain \( A \) est défini comme le rapport entre la tension de sortie et la tension d'entrée :
   \[
   [important]A = \frac{V_{out}}{V_{in}} = 1 + \frac{R1}{R2}[/important]
   \]

---

### **Formule du gain :**
\[
\boxed{A = 1 + \frac{R1}{R2}}
\]

---
Si tu veux approfondir ou vérifier avec des valeurs numériques, n'hésite pas à demander !