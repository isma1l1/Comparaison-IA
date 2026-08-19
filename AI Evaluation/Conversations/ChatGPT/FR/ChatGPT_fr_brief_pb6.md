## Utilisateur
Réponds de manière concise en supprimant tout propos inutile.  
On considère un montage différentiel en électronique. Etablis l'expression de Vout en fonction des tensions en entrée et des résistances. Explique ton raisonnement.

## IA
Pour un amplificateur différentiel classique à 4 résistances :
[important]
- \(R_1\) entre \(V_1\) et l’entrée inverseuse  
- \(R_2\) en contre-réaction (sortie → entrée inverseuse)  
- \(R_3\) entre \(V_2\) et l’entrée non-inverseuse  
- \(R_4\) entre l’entrée non-inverseuse et la masse  
[/important]
**1. Tension sur l’entrée non-inverseuse**

Pont diviseur :
\[
[important]V_+ = \frac{R_4}{R_3 + R_4} V_2[/important]
\]

**2. Idéalité de l’AO**

\[
[important]V_- = V_+ = \frac{R_4}{R_3 + R_4} V_2[/important]
\]

**3. [important]Loi des nœuds[/important] en entrée inverseuse**

\[
[important]\frac{V_1 - V_-}{R_1} + \frac{V_{out} - V_-}{R_2} = 0[/important]
\]

On isole \(V_{out}\) :
\[
[important]V_{out} = V_- \left(1 + \frac{R_2}{R_1}\right) - \frac{R_2}{R_1} V_1[/important]
\]

**4. Substitution de \(V_-\)**

\[
[important]V_{out} = \left(1 + \frac{R_2}{R_1}\right)\frac{R_4}{R_3 + R_4} V_2 - \frac{R_2}{R_1} V_1[/important]
\]

**5. Cas symétrique (condition différentielle)**

Si :
\[
\frac{R_2}{R_1} = \frac{R_4}{R_3}
\]

alors :
\[
[important]V_{out} = \frac{R_2}{R_1}(V_2 - V_1)[/important]
\]

C’est le fonctionnement différentiel pur (rejet du mode commun).
