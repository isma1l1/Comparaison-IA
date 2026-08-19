## Utilisateur
On étudie un montage intégrateur différentiel classique dans lequel les deux résistances ont la même valeur R et les deux condensateurs ont la même valeur C. Détermine Vs en fonction de V1 et V2. Explique ton raisonnement.

## IA
Pour déterminer la tension de sortie $V_s$ d'un intégrateur différentiel (aussi appelé intégrateur à soustracteur), nous allons utiliser les lois fondamentales de l'électronique analogique, en supposant que l'amplificateur opérationnel (AO) est **idéal** et fonctionne en **régime linéaire**.

### Le Montage

Le montage se compose généralement de :
* Une branche sur l'entrée inverseuse ($e^-$) avec une résistance $R$ reliée à $V_1$ et un condensateur $C$ en contre-réaction entre la sortie et $e^-$.
* Une branche sur l'entrée non-inverseuse ($e^+$) avec une résistance $R$ reliée à $V_2$ et un condensateur $C$ relié à la masse.

---

### Raisonnement étape par étape

#### 1. Hypothèses de base
* **AO Idéal :** Les courants d'entrée sont nuls ($i^+ = i^- = 0$).
*[[important] **Régime linéaire :** Grâce à la contre-réaction négative[\important]], nous avons l'égalité des potentiels d'entrée : [[important]$V_+ = V_-$[\important]].

#### 2. Calcul du potentiel $V_+$
L'entrée non-inverseuse est un simple circuit $RC$ série (pont diviseur de tension en notation complexe). En utilisant l'impédance du condensateur $Z_C = \frac{1}{jC\omega}$ :

$$V_+ = V_2 \cdot \frac{Z_C}{R + Z_C} = V_2 \cdot \frac{\frac{1}{jC\omega}}{R + \frac{1}{jC\omega}} $$
[[important]$$ V_+ = V_2 \cdot \frac{1}{1 + jRC\omega}$$[\important]]

#### 3. Calcul du potentiel $V_-$
On applique le théorème de Millman au nœud $e^-$ (ou la loi des nœuds en termes de courants) :

[[important]$$\frac{V_1 - V_-}{R} + \frac{V_s - V_-}{Z_C} = 0$$[\important]]

En isolant $V_-$ :
$$V_- \left( \frac{1}{R} + \frac{1}{Z_C} \right) = \frac{V_1}{R} + \frac{V_s}{Z_C}$$
$$V_- = \frac{\frac{V_1}{R} + \frac{V_s}{Z_C}}{\frac{1}{R} + \frac{1}{Z_C}} = \frac{V_1 \cdot Z_C + V_s \cdot R}{R + Z_C}$$

#### 4. Égalité $V_+ = V_-$
Puisque $V_+ = V_-$, les dénominateurs $(R + Z_C)$ s'annulent :

$$V_2 \cdot Z_C = V_1 \cdot Z_C + V_s \cdot R$$

On isole $V_s$ :
$$V_s \cdot R = Z_C (V_2 - V_1)$$
[[important]$$V_s = \frac{1}{jRC\omega} (V_2 - V_1)$$[\important]]

---

### Expression Finale

En repassant dans le domaine temporel, l'opération $\frac{1}{j\omega}$ correspond à une intégration par rapport au temps :

$$V_s(t) = \frac{1}{RC} \int (V_2(t) - V_1(t)) \, dt$$

### Conclusion
La tension de sortie est proportionnelle à **l'intégrale de la différence** des tensions d'entrée. 
* Si $V_2 > V_1$, la sortie augmente.
* Le terme $\frac{1}{RC}$ représente la constante de temps (ou le gain de l'intégration). 

C'est un montage très utile pour supprimer les tensions de mode commun tout en intégrant un signal différentiel.
