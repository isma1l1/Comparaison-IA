## Utilisateur
Voici un montage d'électronique analogique.  
Donne moi la formule du gain de ce circuit en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA
Ce montage est un **amplificateur inverseur** avec un amplificateur opérationnel idéal.

### Raisonnement

- L’entrée non-inverseuse (+) est reliée à la masse ⇒ \( V_+ = 0 \)  
- En [important]régime linéaire[/important] avec un A.O. idéal, on a :
  - \( [important]V_- \approx V_+ = 0[/important] \) (masse virtuelle)  
  - Aucun courant n’entre dans l’A.O.  

👉 Donc, le courant qui traverse \( R2 \) est le même que celui qui traverse \( R1 \).

#### Courant dans \( R2 \) :
\[
[important]i = \frac{V_{in} - 0}{R2} = \frac{V_{in}}{R2}[/important]
\]

#### Courant dans \( R1 \) :
\[
[important]i = \frac{0 - V_{out}}{R1} = -\frac{V_{out}}{R1}[/important]
\]

#### Égalité des courants :
\[
[important]\frac{V_{in}}{R2} = -\frac{V_{out}}{R1}[/important]
\]

### Gain du circuit

\[
[important]\frac{V_{out}}{V_{in}} = -\frac{R1}{R2}[/important]
\]

### Conclusion

- Le gain est **négatif** ⇒ le signal est inversé  
- Sa valeur dépend uniquement du rapport des résistances :
  - plus \( R1 \) est grand → gain élevé  
  - plus \( R2 \) est grand → gain faible  

Si tu veux, je peux aussi te montrer comment ça se comporte avec des valeurs concrètes ou un signal réel.