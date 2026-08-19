## Utilisateur

On étudie Uc(t) en fonction de E(t) dans un circuit RLC série. Détermine la nature du filtre représenté, calcule la fonction de transfert, donne l'expression de la largeur de la bande passante et trace les diagrammes de Bode en gain et en phase. Explique ton raisonnement.

## IA

Pour étudier ce système, nous allons passer en représentation complexe. On note $\underline{e}(t) = E_0 e^{j\omega t}$ la tension d'entrée et $\underline{u}_c(t) = U_{c0} e^{j\omega t}$ la tension aux bornes du condensateur.

---

### 1. Calcul de la fonction de transfert

En utilisant un pont[important]diviseur de tension[/important] dans le circuit RLC série, la fonction de transfert $\underline{H}(j\omega)$ est définie par :

$$[important]\underline{H}(j\omega) = \frac{\underline{u}_c}{\underline{e}} = \frac{\frac{1}{jC\omega}}{R + jL\omega + \frac{1}{jC\omega}}[/important]$$

En multipliant le numérateur et le dénominateur par $jC\omega$, on obtient la forme canonique d'un système du second ordre :

$$[important]\underline{H}(j\omega) = \frac{1}{1 - LC\omega^2 + jRC\omega}[/important]$$

En introduisant la pulsation propre [important]$\omega_0 = \frac{1}{\sqrt{LC}}$ [/important]et le facteur de qualité [important]$Q = \frac{1}{R}\sqrt{\frac{L}{C}}$[/important] (ou $RC\omega_0 = \frac{1}{Q}$), on écrit :
[important]
$$\underline{H}(jx) = \frac{1}{1 - x^2 + j\frac{x}{Q}} \quad[/important] \text{avec} \quad x = \frac{\omega}{\omega_0}$$

---

### 2. Nature du filtre

Pour déterminer la nature du filtre, on regarde le comportement aux limites :

* **Basses fréquences ($\omega \to 0$) :** $\underline{H} \to 1$. Le signal passe sans atténuation.
* **Hautes fréquences ($\omega \to \infty$) :** $\underline{H} \to \frac{1}{-LC\omega^2} \to 0$. Le signal est fortement atténué (pente de -40 dB/décade).

C’est donc un filtre **[important]passe-bas du second ordre[/important]**.

---

### 3. Largeur de la bande passante

La bande passante à -3 dB est définie par les fréquences telles que $G(\omega) \geq \frac{G_{max}}{\sqrt{2}}$. Pour un filtre du second ordre avec un $Q$ élevé, elle est centrée autour de la résonance.
L'expression de la largeur de la bande passante $\Delta \omega$ (pour le courant ou si $Q \gg 1$) est :

$$[important]\Delta \omega = \frac{\omega_0}{Q} = \frac{R}{L}[/important]$$

---

### 4. Diagrammes de Bode

#### A. Diagramme de gain ($G_{dB} = 20 \log |\underline{H}|$)
* [important]**Asymptote BF ($x \ll 1$) :** $G_{dB} \approx 0$ dB[/important]. Droite horizontale.
* [important]**Asymptote HF ($x \gg 1$) :** $G_{dB} \approx -40 \log(x)$. Pente de **-40 dB/décade**.[/important]
* [important]**À la cassure ($x = 1$) [/important]:** Si $Q > \frac{1}{\sqrt{2}}$, il y a une [important]résonance avec un pic de gain $G_{max} = 20 \log \left( \frac{Q}{\sqrt{1 - 1/4Q^2}} \right)$[/important].

#### B. Diagramme de phase ($\phi = \arg(\underline{H})$)
* [important]**BF :** $\phi \to 0$ rad[/important] (le signal est en phase).
* **À la [important]pulsation propre ($x = 1$) :** $\phi = -\frac{\pi}{2}$ rad.
* **HF :** $\phi \to -\pi$ rad[/important] (le signal est en opposition de phase).

---

### Explication du raisonnement
1.  **Loi des mailles/Diviseur :** On traduit le montage physique en équation mathématique complexe.
2.  **Normalisation :** On réduit l'expression pour faire apparaître $\omega_0$ et $Q$, ce qui permet de comparer le filtre à des modèles standards.
3.  **Analyse asymptotique :** En faisant tendre $\omega$ vers 0 et l'infini, on "voit" si le filtre bloque les graves ou les aigus.
4.  **Logarithmes :** On passe en décibels pour transformer les puissances de la fonction de transfert en pentes linéaires faciles à tracer.

Souhaites-tu que je détaille le calcul de la pulsation de résonance ou le tracé précis pour une valeur de $Q$ spécifique ?