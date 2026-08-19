## Utilisateur
Voici un montage d'électronique analogique. 
Détermine la relation entrée-sortie du filtre présenté. Explique ton raisonnement.
*(image d'un schéma de montage électronique comprenant un amplificateur opérationnel avec un condensateur en entrée sur la borne inverseuse et une résistance en boucle de rétroaction)*

## IA
Ce montage est un classique de l'électronique analogique utilisant un amplificateur opérationnel (AOP). Voici l'analyse étape par étape pour déterminer la relation entre l'entrée $e$ et la sortie $s$.

### 1. Identification du montage
Le circuit est un **montage inverseur** (le signal d'entrée arrive sur la borne "$-$"). Plus spécifiquement, comme il comporte un condensateur en entrée et une résistance en contre-réaction, il s'agit d'un **dérivateur** (ou filtre passe-haut actif).

### 2. Hypothèses de calcul
Pour établir la relation, nous considérons que :
* L'AOP est **idéal** (courants d'entrée nuls : $i_+ = i_- = 0$).
* Il fonctionne en **régime linéaire** (présence d'une [important]contre-réaction sur la borne "$-$"[/important]), donc les potentiels des deux bornes sont égaux : $[important]V_+ = V_-[/important]$.

### 3. Raisonnement et mise en équation
D'après le schéma :
* La borne non-inverseuse est reliée à la masse : $[important]V_+ = 0[/important]$.
* Par conséquent, par la loi du court-circuit virtuel : **$V_- = 0$**.

Appliquons la loi des nœuds (ou le théorème de Millman) au point $V_-$ en utilisant les impédances complexes :
* Soit $[important]Z_C = \frac{1}{jC\omega}[/important]$ l'impédance du condensateur.
* Soit $R$ la résistance en rétroaction.

Le courant arrivant par le condensateur est $[important]i = \frac{e - V_-}{Z_C} = \frac{e}{Z_C}[/important]$.
Ce même courant repart intégralement à travers la résistance car $i_- = 0$ : $[important]i = \frac{V_- - s}{R} = \frac{-s}{R}[/important]$.

On égalise les deux expressions :
$$[important]\frac{e}{Z_C} = -\frac{s}{R}[/important]$$

### 4. Relation Entrée-Sortie
En remplaçant $Z_C$ par son expression $\frac{1}{jC\omega}$ :
$$e \cdot jC\omega = -\frac{s}{R}$$

On obtient la **fonction de transfert** $H(j\omega)$ :
$$[important]H(j\omega) = \frac{s}{e} = -jRC\omega[/important]$$

### 5. Interprétation temporelle
Dans le domaine temporel, la multiplication par $j\omega$ correspond à une dérivation par rapport au temps. La relation devient :
$$[important]s(t) = -RC \frac{de(t)}{dt}[/important]$$

---

### Conclusion
Ce filtre est un **dérivateur idéal**.
* **Comportement :** La tension de sortie est proportionnelle à la dérivée de la tension d'entrée. 
* **Type de filtre :** C'est un **passe-haut**. Il bloque la composante continue (si $e$ est constant, $s = 0$) et amplifie les hautes fréquences (le gain augmente avec la fréquence).

> **Note :** En pratique, on ajoute souvent une petite résistance en série avec le condensateur pour éviter l'instabilité et la saturation à très haute fréquence.
