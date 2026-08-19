## Utilisateur

On étudie un montage sommateur non-inverseur classique dans lequel les quatre résistances ont la même valeur R. Détermine Vs en fonction de V1 et V2. Explique ton raisonnement.

## IA

Pour déterminer l'expression de la tension de sortie $V_s$ d'un montage **sommateur non-inverseur** avec deux entrées $V_1$ et $V_2$, nous allons procéder par étapes en utilisant les propriétés de l'amplificateur opérationnel (AOP) idéal.

### Schéma du montage
Le montage se compose de deux parties :
1.  Un réseau de résistances à l'entrée non-inverseuse ($V^+$).
2.  Un montage amplificateur non-inverseur classique pour la contre-réaction ($V^-$).

### 1. Hypothèses de l'AOP idéal
On considère que l'AOP fonctionne en [[important]**régime linéaire**[\important]] (grâce à la contre-réaction sur l'entrée inverseuse) :
* Les courants d'entrée sont nuls : $i^+ = i^- = 0$.
* Les potentiels des entrées sont égaux :[[important] $V^+ = V^-$.[\important]]

### 2. Calcul du potentiel $V^+$
On applique le **théorème de Millman** (ou le principe de superposition) au point $V^+$. Puisque les deux résistances d'entrée sont égales à $R$, nous avons :
[[important]
$$V^+ = \frac{\frac{V_1}{R} + \frac{V_2}{R}}{\frac{1}{R} + \frac{1}{R}} = \frac{V_1 + V_2}{2}$$[\important]]

### 3. Calcul du potentiel $V^-$
Le pont diviseur de tension formé par les deux résistances $R$ situées dans la boucle de contre-réaction nous donne :
[[important]
$$V^- = V_s \cdot \frac{R}{R + R} = \frac{V_s}{2}$$[\important]]

### 4. Relation finale
En utilisant l'égalité $V^+ = V^-$ propre au régime linéaire :

$$\frac{V_1 + V_2}{2} = \frac{V_s}{2}$$

En simplifiant par $2$, on obtient le résultat final :

> [[important]**$V_s = V_1 + V_2$**[\important]]

---

### Conclusion
Dans cette configuration spécifique où toutes les résistances sont identiques, le montage réalise une **somme directe** des tensions d'entrée. 

Le raisonnement est simple : le réseau d'entrée divise la somme par 2 (moyenne arithmétique), tandis que l'étage amplificateur non-inverseur multiplie le signal par 2 (gain de $1 + \frac{R}{R}$), ce qui annule la division initiale.
