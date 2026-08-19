## Utilisateur

Réponds de manière concise en supprimant tout propos inutile. 
On étudie Uc(t) en fonction de E(t) dans un circuit RLC série. Détermine la nature du filtre représenté, calcule la fonction de transfert, donne l'expression de la largeur de la bande passante et trace les diagrammes de Bode en gain et en phase. Explique ton raisonnement.

## IA

## Étude du Filtre RLC Série (Sortie aux bornes du condensateur)

### 1. Nature du filtre
Le circuit se comporte comme un **diviseur de tension**. À basse fréquence ($\omega \to 0$), le condensateur se comporte comme un circuit ouvert ($Z_C \to \infty$), donc $u_C \approx e$. À haute fréquence ($\omega \to \infty$), il se comporte comme un court-circuit ($Z_C \to 0$).
* **Nature :** Filtre **[important]passe-bas** du second ordre[/important].

---

### 2. Fonction de transfert
On utilise la [important]division de tension[/important] en notation complexe :

$$[important]\underline{H}(j\omega) [/important]= \frac{\underline{U}_c}{\underline{E}} = \frac{\frac{1}{jC\omega}}{R + jL\omega + \frac{1}{jC\omega}} = [important]\frac{1}{1 - LC\omega^2 + jRC\omega}[/important]$$

En posant la pulsation propre $[important]\omega_0 = \frac{1}{\sqrt{LC}}[/important]$ et le facteur de qualité $[important]Q = \frac{1}{R}\sqrt{\frac{L}{C}}[/important]$ :

$$[important]\underline{H}(j\omega) = \frac{1}{1 - \left(\frac{\omega}{\omega_0}\right)^2 + j\frac{1}{Q}\frac{\omega}{\omega_0}}[/important]$$

---

### 3. Largeur de la bande passante
La bande passante à $-3$ dB est l'intervalle $\Delta\omega = \omega_2 - \omega_1$ pour lequel $G_{dB} \geq G_{max} - 3$. 
Pour un filtre passe-bas du second ordre, si $Q$ est élevé ($Q > 1/\sqrt{2}$), la résonance est centrée sur $\omega_0$.
* **Expression :** $[important]\Delta\omega \approx \frac{\omega_0}{Q} = \frac{R}{L}[/important]$ (valable pour un pic de résonance marqué).

---

### 4. Diagrammes de Bode

#### Gain $G_{dB} = 20\log|\underline{H}(j\omega)|$
* **[important]Basses fréquence ($\omega \ll \omega_0$) :** $G_{dB} \to 0$. Pente de **0 dB/decade**.[/important]
* [important]**Hautes fréquences ($\omega \gg \omega_0$) :** $G_{dB} \approx -40\log(\frac{\omega}{\omega_0})$. Pente de **-40 dB/decade**.[/important]
* **À la [important]coupure ($\omega = \omega_0$) :** $G_{dB} = 20\log(Q)$. Si $Q > 1/\sqrt{2}$, il y a une surtension (pic).[/important]

#### Phase $\phi = \arg(\underline{H}(j\omega))$
[important]
* **Basses fréquences :** $\phi \to 0$ rad.
* **À la coupure :** $\phi = -\pi/2$ rad ($-90$°).
* **Hautes fréquences :** $\phi \to -\pi$ rad ($-180$°).
[/important]