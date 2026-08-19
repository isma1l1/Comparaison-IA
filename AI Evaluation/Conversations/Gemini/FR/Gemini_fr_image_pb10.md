## Utilisateur

Voici un montage d'électronique analogique. 
Détermine la relation entrée-sortie du filtre présenté (les quatre résistances ont la même valeur). Explique ton raisonnement.
*(image de un circuit électronique composé d'un amplificateur opérationnel avec deux résistances en parallèle à l'entrée non-inverseuse et un pont diviseur de tension pour la rétroaction sur l'entrée inverseuse)*

## IA

Ce circuit est un **sommateur non-inverseur**. Puisque les quatre résistances ont la même valeur (appelons-les $R$), nous pouvons simplifier l'analyse en utilisant le principe de superposition ou les théorèmes fondamentaux de l'électronique.

Voici le raisonnement étape par étape :

### 1. Analyse du potentiel à l'entrée non-inverseuse ($V_+$)
L'entrée non-inverseuse est reliée à un pont diviseur alimenté par $v_1$ et $v_2$. En appliquant le **théorème de Millman** au point situé juste avant la borne $+$ :
[[important]
$$V_+ = \frac{\frac{v_1}{R} + \frac{v_2}{R}}{\frac{1}{R} + \frac{1}{R}} = \frac{v_1 + v_2}{2}$$[\important]]

### 2. Analyse de la boucle de contre-réaction ($V_-$)
Le montage présente une boucle de rétroaction sur l'entrée inverseuse via deux résistances identiques. Il s'agit d'une structure d'**amplificateur non-inverseur**. Le potentiel $V_-$ est donné par la formule du pont diviseur de tension à partir de la sortie $v_s$ :
[[important]
$$V_- = v_s \cdot \frac{R}{R + R} = \frac{v_s}{2}$$[\important]]

### 3. Hypothèse de l'amplificateur opérationnel idéal
En régime linéaire (présence d'une contre-réaction négative), on considère que l'amplificateur est idéal, ce qui implique que les potentiels des deux entrées sont égaux (masse virtuelle différentielle) :
[[important]
$$V_+ = V_-$$[\important]]

### 4. Relation finale
En égalisant les deux expressions trouvées précédemment :
[[important]
$$\frac{v_1 + v_2}{2} = \frac{v_s}{2}$$[\important]]

En multipliant par 2 de chaque côté, on obtient la relation entrée-sortie simplifiée :
[[important]
**$$v_s = v_1 + v_2$$**
[\important]]
---

### Conclusion
Le circuit réalise la **somme directe** des deux tensions d'entrée. 
* La première partie du circuit (les deux résistances d'entrée) fait la moyenne des tensions : $(v_1 + v_2)/2$.
* La seconde partie (l'amplificateur avec ses deux résistances de rétroaction) possède un gain de $1 + \frac{R}{R} = 2$.
* Le gain de 2 compense exactement la division par 2, ce qui nous donne une somme parfaite.
