## Utilisateur
Voici un montage d’électronique analogique. 
Identifie le régime de fonctionnement de l’ALI, exprime le potentiel v+ en fonction de s, déduis-en les tensions de basculement, représente le cycle d’hystérésis du montage dans le cas où R2 = 2*R1, et représente le signal de sortie pour une entrée sinusoïdale d’amplitude 10V. Explique ton raisonnement.
*(image d'un montage comprenant un amplificateur linéaire intégré avec une rétroaction positive via une résistance R2 reliée à l'entrée non-inverseuse, une résistance R1 reliée à la masse, une tension d'entrée e sur l'entrée inverseuse et une tension de sortie s)*

---

## IA
Ce montage est un **comparateur à deux seuils**, également appelé **trigger de Schmitt non-inverseur**. Voici l'analyse détaillée étape par étape :

### 1. Régime de fonctionnement
L'Amplificateur Linéaire Intégré (ALI) possède une boucle de **[important]rétroaction positive[/important]** (la sortie $s$ est reliée à l'entrée non-inverseuse $+$ via $R_2$). 
* **Conclusion :** L'ALI fonctionne en **régime saturé** (non-linéaire). La sortie $s$ ne peut prendre que deux valeurs : $+V_{sat}$ ou $-V_{sat}$.

### 2. Expression du potentiel $v_+$
L'entrée non-inverseuse est au potentiel $v_+$. En utilisant le **[important]théorème de Millman[/important]** (ou un [important]pont diviseur de tension[/important] pondéré) au nœud $v_+$, on obtient :
$$[important]v_+ = \frac{\frac{0}{R_1} + \frac{s}{R_2}}{\frac{1}{R_1} + \frac{1}{R_2}} = \frac{R_1}{R_1 + R_2} s[/important]$$

### 3. Tensions de basculement
Le basculement se produit lorsque la tension différentielle d'entrée $\epsilon = v_+ - v_-$ change de signe. Ici, $v_- = e$. Le basculement a lieu quand $v_+ = e$.

* Si $s = +V_{sat}$, le seuil de basculement haut ($e_H$) est :  
    $$[important]e_H = \frac{R_1}{R_1 + R_2} (+V_{sat})[/important]$$
* Si $s = -V_{sat}$, le seuil de basculement bas ($e_B$) est :  
    $$[important]e_B = \frac{R_1}{R_1 + R_2} (-V_{sat})[/important]$$

### 4. Cycle d'hystérésis (pour $R_2 = 2R_1$)
Si $[important]R_2 = 2R_1[/important]$, alors le coefficient devient $\frac{R_1}{R_1 + 2R_1} = \frac{1}{3}$. Les seuils sont donc $[important]\pm \frac{V_{sat}}{3}[/important]$.

Le cycle d'hystérésis représente $s$ en fonction de $e$ :
* Tant que $e$ est très négatif, $s = -V_{sat}$.
* [important]$s$ reste à $-V_{sat}$ jusqu'à ce que $e$ atteigne $+\frac{V_{sat}}{3}$ (montée)[/important].
* [important]$s$ reste à $+V_{sat}$ jusqu'à ce que $e$ redescende à $-\frac{V_{sat}}{3}$ (descente)[/important].

*(image de la courbe de transfert présentant un cycle d'hystérésis pour un trigger de Schmitt non-inverseur)*

---

### 5. Signal de sortie pour une entrée sinusoïdale ($10\text{V}$)
Supposons des tensions d'alimentation standard où $V_{sat} \approx 14\text{V}$. Les seuils seraient à $\pm 4.66\text{V}$. 
* L'entrée $e(t) = 10 \sin(\omega t)$ croise ces seuils.
* **Description du signal $s(t)$ :** [important]C'est un signal **carré** (ou rectangulaire) d'amplitude $\pm V_{sat}$[/important].
* **Phasage :** Comme c'est un montage **non-inverseur**, la sortie passe à $+V_{sat}$ quand l'entrée dépasse le seuil haut et passe à $-V_{sat}$ quand elle repasse sous le seuil bas. [important]Le signal de sortie est globalement "en phase" avec l'entrée[/important] (le front montant de $s$ arrive pendant la demi-alternance positive de $e$).

*(image des chronogrammes montrant l'entrée sinusoïdale et la sortie carrée correspondante)*

### Résumé du raisonnement
1.  **Rétroaction sur le $+$** $\rightarrow$ Saturation et hystérésis.
2.  **Millman sur $v_+$** $\rightarrow$ Lien direct entre la sortie et le seuil.
3.  **Comparaison avec $e$** $\rightarrow$ Détermination des points de bascule.
4.  **$R_2 = 2R_1$** $\rightarrow$ Fixe la largeur de la fenêtre d'hystérésis à $2/3$ de $V_{sat}$.
