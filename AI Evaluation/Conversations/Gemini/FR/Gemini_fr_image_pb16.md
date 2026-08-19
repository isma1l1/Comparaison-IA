## Utilisateur

Résous les questions A.1.1, A.1.2 et A.1.3 présentes sur ces images en détaillant ton raisonnement.
*(image du sujet de l'examen présentant un système de réservoir d'eau avec un potentiomètre linéaire et un schéma de pont de Wheatstone)*

---

## IA

Voici la résolution détaillée de l'exercice **A.1** portant sur le pont de Wheatstone utilisé pour mesurer le niveau d'eau.

### **A.1.1) Expression littérale de $V_2$**

Le circuit présenté en Figure 2 est un pont de Wheatstone. La tension $V_2$ est la différence de potentiel entre les deux branches du pont, toutes deux alimentées par la source $V_1$.

1.  **Potentiel au point central de la branche gauche ($V_g$) :**
    En utilisant la règle du diviseur de tension :
    $$V_g = V_1 \cdot \frac{R_1}{R_1 + R_2}$$
2.  **Potentiel au point central de la branche droite ($V_d$) :**
    De la même manière :
    $$V_d = V_1 \cdot \frac{R_4}{R_3 + R_4}$$
3.  **Expression de $V_2$ :**
    D'après le schéma, $V_2$ est la tension "fléchée" entre ces deux points (du point droit vers le point gauche) :
    $$V_2 = V_g - V_d$$
    $$V_2 = V_1 \cdot \left( \frac{R_1}{R_1 + R_2} - \frac{R_4}{R_3 + R_4} \right)$$

---

### **A.1.2) Relation entre $V_2$ et le niveau d'eau $x$**

On nous donne les relations liées au potentiomètre : $R_1 = kR$ et $R_2 = (1-k)R$, avec $k = \frac{x}{h}$.

1.  **Simplification du terme de gauche :**
    On remarque que $R_1 + R_2 = kR + (1-k)R = R$.
    Le premier terme devient donc : $\frac{kR}{R} = k$.
2.  **Substitution de $k$ par $x/h$ :**
    En injectant cela dans l'expression précédente :
    $$V_2 = V_1 \cdot \left( \frac{x}{h} - \frac{R_4}{R_3 + R_4} \right)$$

C'est une relation affine (de type $y = ax + b$) entre la tension de mesure $V_2$ et la hauteur d'eau $x$.

---

### **A.1.3) Condition d'équilibre et valeurs extrêmes**

#### **Condition pour $V_2 = 0$ à mi-remplissage ($x = h/2$)**
Si le réservoir est à moitié plein, alors $x = \frac{h}{2}$, ce qui implique $k = \frac{1}{2}$.
Pour que $V_2 = 0$, il faut que les deux rapports du diviseur de tension soient égaux :
$$\frac{1}{2} = \frac{R_4}{R_3 + R_4}$$
En multipliant par $(R_3 + R_4)$, on obtient : $R_3 + R_4 = 2R_4$, soit :
**$R_3 = R_4$**
*(Le pont doit être équilibré avec des résistances identiques sur la branche de référence).*

#### **Calcul des valeurs extrêmes de $V_2$**
En utilisant la condition $R_3 = R_4$, l'expression de $V_2$ se simplifie en :
$$V_2 = V_1 \cdot \left( k - \frac{1}{2} \right)$$

* **Valeur minimale $V_{2min}$ (quand $x = 0$, soit $k = 0$) :**
    $$V_{2min} = V_1 \cdot (0 - 1/2) = -\frac{V_1}{2}$$
* **Valeur maximale $V_{2max}$ (quand $x = h$, soit $k = 1$) :**
    $$V_{2max} = V_1 \cdot (1 - 1/2) = \frac{V_1}{2}$$

**Résumé :** La tension $V_2$ évolue linéairement entre $-\frac{V_1}{2}$ et $+\frac{V_1}{2}$ au fur et à mesure que le réservoir se remplit.
