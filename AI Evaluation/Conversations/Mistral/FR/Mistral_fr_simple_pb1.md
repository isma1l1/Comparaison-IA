## Utilisateur
Donne moi la formule du gain d'un montage inverseur en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA
### Formule du gain d’un montage inverseur

**Le gain \( A_v \) d’un montage inverseur** (avec un amplificateur opérationnel idéal) est donné par la formule :
[important]
\[
A_v = -\frac{R_2}{R_1}
\]
[/important]
---

### Explication du raisonnement

#### 1. **Schéma du montage inverseur**
Un montage inverseur utilise un amplificateur opérationnel (AOP) avec une résistance \( R_1 \) entre l’entrée \( V_{in} \) et l’entrée inverseuse (\(-\)), et une résistance \( R_2 \) entre l’entrée inverseuse et la sortie \( V_{out} \). [important]L’entrée non-inverseuse (\(+\)) est reliée à la masse.[/important]

#### 2. **Propriétés de l’AOP idéal**
- **Tension différentielle nulle** : [important]\( V_+ = V_- \)[/important]
- **Courant d’entrée nul** : [important]\( I_+ = I_- = 0 \)[/important]

#### 3. **Application des [important]lois des nœuds[/important]**
- Le courant \( I \) qui traverse \( R_1 \) est égal à celui qui traverse \( R_2 \) (car \( I_- = 0 \)).
- On a donc :
[important]
  \[
  I = \frac{V_{in} - V_-}{R_1} = \frac{V_- - V_{out}}{R_2}
  \]
  [/important]
- Comme \( V_- = 0 \) (car \( V_+ = 0 \) et \( V_+ = V_- \)), cela se simplifie en :
  \[
  \frac{V_{in}}{R_1} = \frac{-V_{out}}{R_2}
  \]

#### 4. **Expression du gain**
- En réarrangeant, on obtient :
[important]
  \[
  V_{out} = -\frac{R_2}{R_1} V_{in}
  \]
  [/important]
- Le gain [important]\( A_v = \frac{V_{out}}{V_{in}} \)[/important] est donc :
[important]
  \[
  A_v = -\frac{R_2}{R_1}
  \]
[/important]
---

### Conclusion
Le gain est **négatif**, ce qui signifie que le signal de sortie est inversé par rapport à l’entrée. Sa valeur absolue dépend uniquement du rapport des résistances \( R_2 \) et \( R_1 \).

Tu veux un exemple numérique ou une application concrète ?