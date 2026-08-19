## Utilisateur

Réponds de manière concise en supprimant tout propos inutile. 
L'ALI du montage fonctionnant en régime linéaire, identifie la nature du filtre, établis sa fonction de transfert, identifie une pulsation caractéristique oméga0, représente son diagramme de Bode en gain, discute l'allure du signal de sortie pour un créneau en entrée.
*(image d'un schéma de circuit électronique de type filtre actif avec deux résistances R, deux condensateurs C et un amplificateur linéaire intégré)*

## IA

## Analyse du Filtre Sallen-Key (Passe-bas)

Ce montage est un filtre actif de **Sallen-Key**.

### 1. Nature du filtre
C'est un **filtre passe-bas du second ordre**. À haute fréquence, les condensateurs se comportent comme des courts-circuits, reliant l'entrée non-inverseuse à la masse, ce qui annule la sortie.

### 2. Fonction de transfert
En régime linéaire avec un ALI idéal en suiveur ($V_+ = V_- = s$), l'application du théorème de Millman aux nœuds intermédiaire ($V_A$) et non-inverseur ($V_+$) donne, en posant $p = j\omega$ :

$$H(j\omega) = \frac{s}{e} = \frac{1}{1 + 3RCp + (RCp)^2}$$

Soit sous forme canonique :
$$H(j\omega) = \frac{1}{1 + 2\xi \frac{j\omega}{\omega_0} + \left(\frac{j\omega}{\omega_0}\right)^2}$$

### 3. Pulsation caractéristique $\omega_0$
Par identification :
* **Pulsation propre :** $\omega_0 = \frac{1}{RC}$
* **Coefficient d'amortissement :** $\xi = \frac{3}{2} = 1,5$ (Le filtre est apériodique, il n'y a pas de résonance car $\xi > \frac{1}{\sqrt{2}}$).

---

### 4. Diagramme de Bode en gain
* **Basses fréquences ($\omega \ll \omega_0$) :** Gain constant $G_{dB} \approx 0 \text{ dB}$ (asymptote horizontale).
* **Hautes fréquences ($\omega \gg \omega_0$) :** Pente de **$-40 \text{ dB/decade}$**.
* **Coupure :** La courbe est située sous les asymptotes sans surtension du fait de l'amortissement élevé ($\xi = 1,5$).

---

### 5. Réponse à un signal créneau
Le filtre étant un passe-bas du second ordre très amorti ($\xi > 1$) :
* Le signal de sortie est **fortement lissé**.
* Les fronts raides du créneau sont remplacés par des transitions exponentielles douces.
* Il n'y a **aucun dépassement** ni oscillations (régime apériodique).
* Si la période du créneau est courte devant $\tau = 1/\omega_0$, la sortie tend vers une forme quasi-triangulaire ou une valeur moyenne constante.
