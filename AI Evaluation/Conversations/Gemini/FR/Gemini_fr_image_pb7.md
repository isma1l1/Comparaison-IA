## Utilisateur
Voici un montage d'électronique analogique. 
Détermine la relation entrée-sortie du filtre présenté. Explique ton raisonnement.
*(image de schéma d'un amplificateur opérationnel en configuration de montage soustracteur avec des résistances R et R')*

## IA
Ce circuit est un montage classique d'amplificateur opérationnel (AOP) appelé **amplificateur de différence** (ou soustracteur).

Pour déterminer la relation entre la sortie $s$ et les entrées $e_1$ et $e_2$, nous allons supposer que l'AOP est **[important]idéal[/important]** et fonctionne en **[important]régime linéaire[/important]** (grâce à la boucle de rétroaction négative sur l'entrée inverseuse).

---

### 1. Analyse du potentiel à l'entrée non-inverseuse ($V^+$)
Le bas du montage forme un pont diviseur de tension entre $e_2$ et la masse. Le courant n'entrant pas dans l'AOP ($i^+ = 0$), on a :
$$[important]V^+ = e_2 \cdot \frac{R'}{R + R'}[/important]$$

### 2. Analyse du potentiel à l'entrée inverseuse ($V^-$)
En utilisant le théorème de Millman (ou la loi des nœuds) au point $V^-$, on exprime ce potentiel en fonction de $e_1$ et $s$ :
$$V^- = \frac{\frac{e_1}{R} + \frac{s}{R'}}{\frac{1}{R} + \frac{1}{R'}}$$
En multipliant le numérateur et le dénominateur par $R \cdot R'$, on simplifie l'expression :
$$[important]V^- = \frac{R' e_1 + R s}{R' + R}[/important]$$

### 3. Application du principe de l'AOP idéal
En régime linéaire, les potentiels des entrées sont égaux ($V^+ = V^-$) :
$$\frac{R' e_2}{R + R'} = \frac{R' e_1 + R s}{R + R'}$$

Comme les dénominateurs sont identiques, on peut les simplifier :
$$R' e_2 = R' e_1 + R s$$

### 4. Relation finale entrée-sortie
En isolant $s$, on obtient :
$$R s = R' e_2 - R' e_1$$
$$[important]s = \frac{R'}{R}(e_2 - e_1)[/important]$$

---

### Conclusion
La tension de sortie $s$ est proportionnelle à la **différence des tensions d'entrée**. Le gain différentiel du montage est défini par le rapport des résistances $\frac{R'}{R}$. 

* Si $R' = R$, alors $s = e_2 - e_1$ (soustracteur pur).
* Ce montage est très utilisé pour amplifier un signal différentiel tout en rejetant le mode commun.
