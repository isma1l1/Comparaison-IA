## Utilisateur
Donne moi la formule du gain d'un montage non-inverseur en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA
Dans un montage **amplificateur non-inverseur** (avec un ampli op idéal), le signal d’entrée est appliqué sur l’entrée **+**, et l’entrée **−** est reliée à un pont de résistances \(R_1\) (vers la masse) et \(R_2\) (vers la sortie).

### Raisonnement

1. **Hypothèse d’ampli op idéal :**
   - Le [important]courant d’entrée est nul.[/important]
   - Les tensions aux bornes des entrées sont égales :  
     \[
     [important]V_+ = V_-[/important]
     \] 

2. Comme \(V_+ = V_{in}\), alors :
   \[
   V_- = V_{in}
   \]

3. L’entrée \(V_-\) est reliée à un **[important]pont diviseur de tension[/important]** entre la sortie \(V_{out}\) et la masse :
   \[
   [important]V_- = V_{out} \cdot \frac{R_1}{R_1 + R_2}[/important]
   \] 

4. En remplaçant \(V_- = V_{in}\) :
   \[
   V_{in} = V_{out} \cdot \frac{R_1}{R_1 + R_2}
   \]

5. On isole le gain \( [important]\dfrac{V_{out}}{V_{in}}[/important]\):

\[
[important]\frac{V_{out}}{V_{in}} = 1 + \frac{R_2}{R_1}[/important]
\] 

### Conclusion

Le **gain du montage non-inverseur** est donc :
\[
G = 1 + \frac{R_2}{R_1}
\]

### Interprétation
- Le gain est toujours **≥ 1** (donc amplification).
- Plus \(R_2\) est grande par rapport à \(R_1\), plus le gain est élevé.
- Si \(R_2 = 0\), alors \(G = 1\) → montage suiveur (buffer).

Si tu veux, je peux aussi te faire un schéma ou comparer avec le montage inverseur 