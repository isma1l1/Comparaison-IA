## Utilisateur

Voici un montage d"électronique analogique.
Les deux ALIs du montage fonctionnant en régime linéaire, montre que ce montage équivaut à un condensateur de capacité C, exprime C en fonction de C0 et alpha et dis quel est l'intérêt d'un tel montage.
*(image de schéma d'un circuit électronique comprenant deux amplificateurs linéaires intégrés, un condensateur C0 et deux résistances dépendant d'un paramètre alpha)*

---

## IA

Ce montage est un circuit classique de multiplication de capacité, souvent appelé **multiplicateur de capacité** ou **capacité active**.

Voici l'analyse étape par étape pour déterminer la capacité équivalente $C$ vue de l'entrée.

### 1. Analyse du premier ALI (Suiveur)
L'ALI n°1 est monté en **suiveur de tension** (sa sortie est rebouclée sur son entrée inverseuse). Comme il fonctionne en régime linéaire :
* $V_+ = u$
* $V_- = V_{s1}$ (tension de sortie de l'ALI 1)
* D'où : **$V_{s1} = u$**

### 2. Analyse du second ALI (Amplificateur inverseur)
L'ALI n°2 a son entrée non-inverseuse à la masse ($V_+ = 0$). En régime linéaire, par le principe du mode commun (masse virtuelle), on a $V_- = 0$.

Appliquons la loi des nœuds (ou le théorème de Millman) à l'entrée inverseuse de l'ALI 2. Le courant arrivant de la résistance $\alpha R$ repart dans la résistance $(1-\alpha)R$ :
$$\frac{V_{s1} - 0}{\alpha R} + \frac{V_{s2} - 0}{(1-\alpha) R} = 0$$

En remplaçant $V_{s1}$ par $u$, on obtient la tension de sortie du second ALI :
$$\frac{u}{\alpha R} = -\frac{V_{s2}}{(1-\alpha)R} \implies V_{s2} = -\frac{1-\alpha}{\alpha} u$$

### 3. Calcul du courant d'entrée et de la capacité équivalente
Le courant d'entrée $i$ ne peut pas entrer dans l'ALI 1 (impédance d'entrée infinie). Il traverse donc entièrement le condensateur $C_0$ pour rejoindre la sortie du second ALI ($V_{s2}$).

D'après la loi d'Ohm généralisée aux bornes de $C_0$ (en notation complexe) :
$$i = j C_0 \omega (u - V_{s2})$$

En remplaçant $V_{s2}$ par l'expression trouvée précédemment :
$$i = j C_0 \omega \left( u - \left( -\frac{1-\alpha}{\alpha} u \right) \right)$$
$$i = j C_0 \omega u \left( 1 + \frac{1-\alpha}{\alpha} \right)$$
$$i = j C_0 \omega u \left( \frac{\alpha + 1 - \alpha}{\alpha} \right) = j \left( \frac{C_0}{\alpha} \right) \omega u$$

L'impédance équivalente du montage est $Z = \frac{u}{i} = \frac{1}{j \left( \frac{C_0}{\alpha} \right) \omega}$. Par identification avec $Z = \frac{1}{j C \omega}$, on en déduit la capacité équivalente :

$$C = \frac{C_0}{\alpha}$$

---

### Synthèse et Intérêt du montage

* **Expression :** La capacité équivalente est **$C = \frac{C_0}{\alpha}$**.
* **Intérêt :** 1.  **Multiplication de capacité :** Puisque $0 < \alpha < 1$, le facteur $1/\alpha$ est supérieur à 1. Ce montage permet de simuler une capacité de très forte valeur à partir d'un condensateur $C_0$ de petite taille (physiquement moins encombrant et souvent de meilleure qualité).
    2.  **Capacité variable :** Si on remplace les deux résistances par un potentiomètre unique de résistance totale $R$ dont le curseur définit $\alpha$, on obtient une **capacité variable électroniquement**. Il suffit de tourner le curseur pour modifier la valeur de $C$ sans changer de composant.
    3.  **Intégration :** C'est très utile en micro-électronique où il est difficile de fabriquer des condensateurs de forte valeur sur une puce de silicium.
