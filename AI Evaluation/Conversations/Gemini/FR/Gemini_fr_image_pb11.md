## Utilisateur
Voici un montage d’électronique analogique. 
Les deux résistances R et les deux condensateurs C sont identiques. Exprime dans le domaine fréquentiel puis temporel la relation entre la tension de sortie et les deux tensions d’entrée du montage. Explique ton raisonnement.
*(image de schéma d'un montage soustracteur-intégrateur à amplificateur opérationnel avec deux résistances R et deux condensateurs C)*

## IA
Ce montage est un **soustracteur-intégrateur** (ou intégrateur différentiel). Il combine la fonction de soustraction de deux signaux d'entrée avec une fonction d'intégration temporelle.

Voici l'analyse détaillée étape par étape pour établir la relation entre la sortie $s$ et les entrées $e_1$ et $e_2$.

---

### 1. Analyse dans le domaine fréquentiel (Formalisme de Laplace)

On utilise l'approximation de l'**amplificateur opérationnel idéal** en régime linéaire (rétroaction négative sur l'entrée inverseuse). Les courants d'entrée sont nuls ($i_+ = i_- = 0$) et les potentiels sont égaux ([[important]$V_+ = V_-$[\important]]).

Soient $Z_R = R$ et $Z_C = \frac{1}{Cp}$ les impédances respectives (en utilisant la variable de Laplace $p$ ou $s$, notons-la ici $p$ pour éviter la confusion avec la sortie $s$).

#### Calcul de $V_+$ (Pont diviseur de tension) :
L'entrée non-inverseuse est reliée à un diviseur de tension formé par $R$ et $C$ à partir de $e_2$ :
[[important]$$V_+ = e_2 \cdot \frac{Z_C}{Z_R + Z_C} = e_2 \cdot \frac{\frac{1}{Cp}}{R + \frac{1}{Cp}} = \frac{e_2}{1 + RCp}$$[\important]]

#### Calcul de $V_-$ (Théorème de Millman ou loi des nœuds) :
Au nœud de l'entrée inverseuse :
[[important]$$\frac{e_1 - V_-}{R} + \frac{s - V_-}{\frac{1}{Cp}} = 0 [\important]] \implies \frac{e_1}{R} + spCp = V_- \left( \frac{1}{R} + Cp \right)$$
En multipliant par $R$ :
$$e_1 + RCps = V_- (1 + RCp) \implies V_- = \frac{e_1 + RCps}{1 + RCp}$$

#### Égalité $V_+ = V_-$ :
$$\frac{e_2}{1 + RCp} = \frac{e_1 + RCps}{1 + RCp}$$
En simplifiant par le dénominateur commun $(1 + RCp)$, on obtient :
$$e_2 = e_1 + RCp \cdot s$$

#### Relation finale en fréquence :
[[important]$$s(p) = \frac{1}{RCp} (e_2(p) - e_1(p))$$[\important]]

---

### 2. Relation dans le domaine temporel

Pour passer au domaine temporel, on rappelle que l'opération $\frac{1}{p}$ dans le domaine de Laplace correspond à l'**intégration** dans le temps.

En multipliant par $RCp$, on a : $RC \cdot p \cdot s = e_2 - e_1$.
En appliquant la transformée inverse, la multiplication par $p$ devient une dérivée :
$$RC \frac{ds(t)}{dt} = e_2(t) - e_1(t)$$

En intégrant par rapport au temps :
[[important]$$s(t) = \frac{1}{RC} \int_{0}^{t} (e_2(\tau) - e_1(\tau)) d\tau + s(0)$$[\important]]

---

### 3. Explication du raisonnement

* **Soustraction :** Le montage traite la différence $(e_2 - e_1)$. L'entrée $e_2$ arrive sur la borne non-inverseuse (signe positif) et $e_1$ sur la borne inverseuse (signe négatif).
* **Intégration :** La présence du condensateur en rétroaction sur l'entrée inverseuse impose une relation courant/tension de type intégral. Le courant traversant la résistance d'entrée est "stocké" dans le condensateur.
* **Symétrie :** Le fait que les composants soient identiques ($R$ et $C$ identiques sur les deux branches) permet de simplifier les pôles du circuit, annulant l'effet de "filtre passe-bas" individuel pour ne conserver que la fonction d'intégration pure de la différence des entrées.

**En résumé :** Ce circuit produit une tension de sortie proportionnelle à l'intégrale de la différence des tensions d'entrée. C'est un outil classique pour réaliser des calculateurs analogiques ou des correcteurs dans les boucles d'asservissement.
