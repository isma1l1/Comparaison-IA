## Utilisateur

Voici un montage d"électronique analogique.
L'ALI du montage fonctionnant en régime linéaire, identifie la nature du filtre, établis sa fonction de transfert, identifie une pulsation caractéristique oméga0, représente son diagramme de Bode en gain, discute l'allure du signal de sortie pour un créneau en entrée.
*(image de schéma d'un filtre électronique avec deux résistances R, deux condensateurs C et un amplificateur linéaire intégré)*

## IA

Ce montage est une structure classique de type **Sallen-Key**. Dans cette configuration précise, il s'agit d'un **filtre passe-bas du second ordre**.

Voici l'analyse détaillée du circuit :

### 1. Analyse et Fonction de transfert

On suppose l'ALI idéal et fonctionnant en régime linéaire. Puisque la sortie est rebouclée sur l'entrée inverseuse ($-$) sans composante supplémentaire, nous sommes en présence d'un **suiveur de tension**. On a donc :
* $V_- = V_+ = s$ (car l'amplification est unité, $A=1$)

Appliquons le théorème de Millman aux deux nœuds principaux en utilisant la notation complexe (avec $p = j\omega$) :

**Au nœud entre les deux résistances (notons son potentiel $V_A$) :**
$$V_A \left( \frac{1}{R} + \frac{1}{R} + Cp \right) = \frac{e}{R} + \frac{s}{R} + sCp$$
$$V_A \left( \frac{2 + RCp}{R} \right) = \frac{e + s + RCps}{R} \implies V_A = \frac{e + s(1 + RCp)}{2 + RCp}$$

**À l'entrée non-inverseuse ($V_+$) :**
Il s'agit d'un pont diviseur entre $V_A$ et la masse :
$$s = V_+ = V_A \frac{\frac{1}{Cp}}{R + \frac{1}{Cp}} = V_A \frac{1}{1 + RCp}$$

**En combinant les deux équations :**
$$s(1 + RCp) = \frac{e + s(1 + RCp)}{2 + RCp}$$
$$s(1 + RCp)(2 + RCp) = e + s(1 + RCp)$$
$$s [ (2 + 3RCp + R^2C^2p^2) - (1 + RCp) ] = e$$
$$s [ 1 + 2RCp + R^2C^2p^2 ] = e$$

La fonction de transfert $H(j\omega) = \frac{s}{e}$ est donc :
$$H(j\omega) = \frac{1}{1 + 2RCj\omega + (RCj\omega)^2}$$

---

### 2. Identification des paramètres caractéristiques

En comparant avec la forme canonique d'un second ordre $\frac{1}{1 + \frac{2\xi}{\omega_0}j\omega + (\frac{j\omega}{\omega_0})^2}$ :

* **Pulsation propre :** $\omega_0 = \frac{1}{RC}$
* **Coefficient d'amortissement :** $2\xi = 2 \implies \xi = 1$
* **Facteur de qualité :** $Q = \frac{1}{2\xi} = 0,5$

Il s'agit d'un filtre **critiquement amorti**.

---

### 3. Diagramme de Bode en gain

Le gain en décibels est $G_{dB} = 20 \log |H(j\omega)|$.

* **Basses fréquences ($\omega \ll \omega_0$) :** $H \approx 1$, donc $G_{dB} \approx 0$ dB. L'asymptote est une droite horizontale.
* **Hautes fréquences ($\omega \gg \omega_0$) :** $H \approx \frac{1}{(j\omega/\omega_0)^2}$, donc $G_{dB} \approx -40 \log(\frac{\omega}{\omega_0})$. L'asymptote est une droite de pente **-40 dB/décade**.
* **À la coupure ($\omega = \omega_0$) :** Puisque $\xi = 1$, il n'y a **pas de résonance**. Le gain est $G_{dB}(\omega_0) = 20 \log(\frac{1}{2}) \approx -6$ dB.

---

### 4. Réponse à un signal créneau

Puisque le filtre est un passe-bas du second ordre avec un coefficient d'amortissement $\xi = 1$, il se comporte comme un système "apériodique critique" :

1.  **Filtrage :** Le filtre va supprimer les harmoniques de haute fréquence du créneau (les fronts abrupts).
2.  **Allure :** La sortie $s(t)$ ne présentera **aucun dépassement** (pas d'oscillations).
3.  **Transitions :** Les fronts montants et descendants du créneau seront "émoussés" et transformés en courbes exponentielles amorties.
4.  **Régime :** * Si la période du créneau est très grande devant $\tau = \frac{1}{\omega_0}$, la sortie aura le temps d'atteindre les paliers haut et bas.
    * Si la fréquence du créneau est élevée, le signal de sortie ressemblera à une onde pseudo-triangulaire très amortie (intégration du signal).
