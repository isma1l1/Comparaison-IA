## Utilisateur
On considère un montage différentiel en électronique. Etablis l'expression de Vout en fonction des tensions en entrée et des résistances. Explique ton raisonnement.

## IA
Considérons le montage différentiel classique à amplificateur opérationnel avec quatre résistances :  [important]
- \(R_1\) entre \(V_1\) et l’entrée inverseuse  
- \(R_2\) en contre-réaction entre la sortie et l’entrée inverseuse  
- \(R_3\) entre \(V_2\) et l’entrée non-inverseuse  
- \(R_4\) entre l’entrée non-inverseuse et la masse  [/important]

On suppose l’AO idéal :  
- courant d’entrée nul  
- \([important]V^- = V^+[/important]\)

1) Tension sur l’entrée non-inverseuse  

Le point \(V^+\) est un [important]pont diviseur[/important] formé par \(R_3\) et \(R_4\) :

\[
[important]V^+ = V_2 \cdot \frac{R_4}{R_3 + R_4}[/important]
\]

Donc, par égalité des entrées :

\[
[important]V^- = V^+ = V_2 \cdot \frac{R_4}{R_3 + R_4}[/important]
\]

2) Équation au nœud inverseur  

Au nœud \(V^-\), la somme des courants est nulle :

\[
[important]\frac{V_1 - V^-}{R_1} + \frac{V_{out} - V^-}{R_2} = 0[/important]
\]

On remplace \(V^-\) :

\[
\frac{V_1 - V^-}{R_1} = - \frac{V_{out} - V^-}{R_2}
\]

On isole \(V_{out}\) :

\[
V[important]_{out} = V^- - \frac{R_2}{R_1}(V_1 - V^-)[/important]
\]

Développons :

\[
[important]V_{out} = V^- \left(1 + \frac{R_2}{R_1}\right) - \frac{R_2}{R_1} V_1[/important]
\]

3) Remplacement de \(V^-\)

\[
[important]V_{out} = \left(1 + \frac{R_2}{R_1}\right) \cdot V_2 \cdot \frac{R_4}{R_3 + R_4} - \frac{R_2}{R_1} V_1[/important]
\]

C’est l’expression générale.

4) Cas particulier : amplificateur différentiel équilibré  

Si les rapports de résistances sont égaux :

\[
\frac{R_2}{R_1} = \frac{R_4}{R_3}
\]

alors l’expression se simplifie en :

\[
[important]V_{out} = \frac{R_2}{R_1}(V_2 - V_1)[/important]
\]

Conclusion  

Le montage réalise une amplification de la différence \(V_2 - V_1\), à condition que les rapports de résistances soient appariés. Sinon, il introduit un gain différent sur chaque entrée et ne rejette pas parfaitement le mode commun.
