## Utilisateur
On étudie un montage soustracteur classique. Détermine la relation entrée-sortie de ce système. Explique ton raisonnement.

## IA
Pour déterminer la relation entrée-sortie d'un montage **amplificateur soustracteur**, nous allons utiliser les propriétés de l'amplificateur opérationnel (AO) [important]idéal[/important] en [important]régime linéaire[/important].

### Schéma du montage
Le montage comporte deux entrées, $V_1$ et $V_2$, appliquées respectivement sur les entrées inverseuse ($-$) et non-inverseuse ($+$) via des résistances.



### 1. Hypothèses de départ
Pour un AO idéal fonctionnant en régime linéaire (présence d'une contre-réaction négative) :
* **Les courants d'entrée sont nuls** : $i_+ = i_- = 0$.
* **La tension différentielle d'entrée est nulle** : $\epsilon = V_+ - V_- = 0$, d'où **$[important]V_+ = V_-[/important]$**.

---

### 2. Calcul du potentiel $V_+$ (Borne non-inverseuse)
On utilise un pont diviseur de tension formé par les résistances $R_3$ et $R_4$ reliées à $V_2$ :
$$[important]V_+ = V_2 \cdot \frac{R_4}{R_3 + R_4}[/important]$$

### 3. Calcul du potentiel $V_-$ (Borne inverseuse)
En appliquant le **théorème de Millman** au point $V_-$ (ou en utilisant la loi des nœuds), on obtient :
$$[important]V_- = \frac{\frac{V_1}{R_1} + \frac{V_s}{R_2}}{\frac{1}{R_1} + \frac{1}{R_2}}[/important]$$

### 4. Mise en relation (Égalité $V_+ = V_-$)
Puisque $V_+ = V_-$, nous égalisons les deux expressions :
$$\frac{V_2 \cdot R_4}{R_3 + R_4} = \frac{\frac{V_1 R_2 + V_s R_1}{R_1 R_2}}{\frac{R_1 + R_2}{R_1 R_2}} = \frac{V_1 R_2 + V_s R_1}{R_1 + R_2}$$

En isolant $V_s$, on arrive à la relation générale :
$$[important]V_s = \frac{R_1 + R_2}{R_1} \cdot \frac{R_4}{R_3 + R_4} \cdot V_2 - \frac{R_2}{R_1} \cdot V_1[/important]$$

---

### 5. Cas classique (Équilibrage des résistances)
Dans la pratique, on choisit souvent des rapports de résistances identiques pour simplifier le montage, soit $\frac{R_2}{R_1} = \frac{R_4}{R_3}$. 

Si l'on prend $R_1 = R_3$ et $R_2 = R_4$, la formule se simplifie de manière élégante :
> $$V_s = \frac{R_2}{R_1} (V_2 - V_1)$$

Si toutes les résistances sont égales ($R_1 = R_2 = R_3 = R_4$), on obtient un **soustracteur pur** :
> $$V_s = V_2 - V_1$$

### Résumé du fonctionnement
* Le montage effectue la différence entre les deux signaux d'entrée.
* Le gain différentiel est fixé par le rapport $R_2 / R_1$.
* L'entrée $V_2$ est "non-inverseuse" (signe positif), tandis que $V_1$ est "inverseuse" (signe négatif).
