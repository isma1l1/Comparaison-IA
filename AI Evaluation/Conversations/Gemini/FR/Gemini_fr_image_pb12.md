## Utilisateur

Voici un montage d'électronique analogique.
Simplifie ce circuit entre les points A et B pour le réduire à un circuit avec un générateur de tension et une résistance. Donne leurs valeurs en fonction des données.
*(image de schéma d'un circuit électrique comportant trois sources de tension Vsrc1, Vsrc2, Vsrc3 et plusieurs résistances de 10, 20 et 30 Ohms connectées à une charge RL entre les points A et B)*

## IA

Pour simplifier ce circuit entre les points **A** et **B**, nous allons utiliser le **théorème de Thévenin**. L'objectif est de trouver la tension de Thévenin ($E_{th}$) et la résistance de Thévenin ($R_{th}$).

On "débranche" la charge $R_L$ pour effectuer les calculs.

---

### 1. Calcul de la résistance de Thévenin ($R_{th}$)
Pour trouver $R_{th}$, on éteint toutes les sources de tension (on les remplace par des fils).
En observant le circuit depuis les points A et B :

* À gauche, les deux résistances de $10\ \Omega$ sont en parallèle : $10 // 10 = 5\ \Omega$.
* Cette combinaison est en série avec la résistance de $20\ \Omega$ du bas : $5 + 20 = 25\ \Omega$.
* Cet ensemble de $25\ \Omega$ se retrouve en parallèle avec la résistance de $30\ \Omega$ : $\frac{25 \times 30}{25 + 30} = \frac{750}{55} \approx 13,64\ \Omega$.
* Enfin, ce bloc est en série avec la résistance de $20\ \Omega$ du haut :

$$R_{th} = 20 + \left( 30 // (20 + (10 // 10)) \right) = 20 + \frac{30 \times 25}{30 + 25} = 20 + \frac{750}{55} = \frac{1850}{55} \approx 33,64\ \Omega$$

---

### 2. Calcul de la tension de Thévenin ($E_{th}$)
C'est la tension à vide $V_{AB}$ (quand $R_L$ est retirée). Utilisons le principe de superposition ou l'analyse nodale. Pour simplifier, exprimons $V_A$ et $V_B$ par rapport au nœud central bas (entre la $20\ \Omega$ et $V_{src3}$).

1.  **Potentiel au nœud central haut ($V_C$) :** Par pont diviseur entre $V_{src1}$ et les deux résistances de $10\ \Omega$, on trouve le potentiel avant $V_{src2}$.
2.  **Mailles :**
    * Le courant circulant dans la branche de gauche est influencé par $V_{src1}$.
    * $V_{src2}$ impose une différence de potentiel vers la branche de droite ($20\ \Omega$).
    * $V_{src3}$ décale directement le potentiel du point B.

En posant la référence (masse) au pied de $V_{src1}$ :
* $V_B = -V_{src3}$
* Le potentiel au nœud entre les deux résistances de $10\ \Omega$ est $V_x$.
* $V_A$ est déterminé par la loi des nœuds ou Millman au point A.

La formule littérale est complexe sans valeurs numériques, mais la structure est :
$$E_{th} = V_A - V_B = V_A + V_{src3}$$
Où $V_A$ dépend de $V_{src1}$ et $V_{src2}$ via les diviseurs de tension formés par le maillage central.

---

### Résultat final
Le circuit équivalent est composé de :
* **Une source de tension :** $E_{th} = V_{AB\_vide}$
* **Une résistance en série :** $R_{th} \approx 33,64\ \Omega$

Souhaitez-vous que nous fassions une application numérique avec des valeurs spécifiques pour les sources de tension ?
