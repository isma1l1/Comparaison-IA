## Utilisateur

Réponds de manière concise en supprimant tout propos inutile. 
Les deux ALIs du montage fonctionnant en régime linéaire, montre que ce montage équivaut à un condensateur de capacité C, exprime C en fonction de C0 et alpha et dis quel est l'intérêt d'un tel montage.
*(image de schéma électrique composé de deux amplificateurs linéaires intégrés, deux résistances notées alphaR et (1-alpha)R, et un condensateur C0 reliés en boucle de rétroaction)*

## IA

## Analyse du montage

En régime linéaire, les tensions d'entrée des ALI sont égales ($V_+ = V_-$).

1.  **ALI 1 (Suiveur) :** Sa sortie est reliée à son entrée inverseuse, donc $V_{S1} = V_+ = u$.
2.  **ALI 2 (Inverseur) :** Le potentiel à l'entrée inverseuse est nul ($V_- = V_+ = 0$).
    * Le courant traversant la résistance $\alpha R$ est $i_R = \frac{V_{S1} - 0}{\alpha R} = \frac{u}{\alpha R}$.
    * Ce même courant traverse $(1-\alpha)R$, donc la tension de sortie de l'ALI 2 est :
        $V_{S2} = 0 - (1-\alpha)R \cdot i_R = -(1-\alpha)R \cdot \frac{u}{\alpha R} = -\frac{1-\alpha}{\alpha}u$.
3.  **Courant d'entrée $i$ :** Il traverse le condensateur $C_0$ vers la sortie de l'ALI 2.
    $i = C_0 \frac{d(u - V_{S2})}{dt}$
    $i = C_0 \frac{d}{dt} \left( u + \frac{1-\alpha}{\alpha}u \right) = C_0 \frac{d}{dt} \left( \frac{\alpha + 1 - \alpha}{\alpha}u \right) = \frac{C_0}{\alpha} \frac{du}{dt}$

---

## Capacité équivalente $C$

Par identification avec la relation $i = C \frac{du}{dt}$, on obtient :
$$C = \frac{C_0}{\alpha}$$

---

## Intérêt du montage

Ce montage est un **multiplicateur de capacité** (ou "capacitance multiplier"). 
* **Intérêt :** Il permet d'obtenir une capacité équivalente très élevée (en choisissant $\alpha$ petit) à partir d'un condensateur $C_0$ de faible valeur, souvent plus compact, précis et de meilleure qualité qu'un condensateur chimique de forte valeur.
