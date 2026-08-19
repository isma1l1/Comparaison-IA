## Utilisateur
Réponds de manière concise en supprimant tout propos inutile.
On étudie Uc(t) en fonction de E(t) dans un circuit RLC série. Détermine la nature du filtre représenté, calcule la fonction de transfert, donne l'expression de la largeur de la bande passante et trace les diagrammes de Bode en gain et en phase. Explique ton raisonnement.

---

## IA
### 1. **Nature du filtre**
Dans un circuit RLC série, la tension aux bornes du condensateur \( U_c(t) \) est étudiée en fonction de la tension d'entrée \( E(t) \). Ce circuit se comporte comme un **[important]filtre passe-bas[/important] **:
- À basse fréquence, le condensateur se charge et \( U_c(t) \) suit \( E(t) \).
- À haute fréquence, l'impédance du condensateur devient très faible, et \( U_c(t) \) tend vers 0.

---

### 2. **Fonction de transfert**
La fonction de transfert \( H(j\omega) \) est définie par :

\[
[important]H(j\omega) = \frac{U_c(j\omega)}{E(j\omega)} = \frac{1}{1 + jRC\omega - LCR\omega^2}[/important]
\]

En normalisant par la pulsation propre \( [important]\omega_0 = \frac{1}{\sqrt{LC}}[/important] \) et le facteur de qualité \( [important]Q = \frac{1}{R}\sqrt{\frac{L}{C}}[/important] \), on obtient :

\[
[important]H(j\omega) = \frac{1}{1 + j\frac{\omega}{\omega_0 Q} - \left(\frac{\omega}{\omega_0}\right)^2}[/important]
\]

---

### 3. **Largeur de la bande passante**
La largeur de la bande passante \( \Delta\omega \) est donnée par :

\[
[important]\Delta\omega = \frac{\omega_0}{Q} = \frac{R}{L}[/important]
\]

En Hertz :
\[
\Delta f = \frac{R}{2\pi L}
\]

---

### 4. **Diagrammes de Bode**
- **Gain (dB)** :
[important]
  - À \(\omega \to 0\) : \( 20\log H| = 0 \) dB.
  - À \(\omega = \omega_0\) : pic de résonance si \( Q > \frac{1}{\sqrt{2}} \).
  - À \(\omega \to \infty\) : pente de \(-40\) dB/décade.
[/important]
- **Phase (°)** :
[important]
  - \( 0^\circ \) à basse fréquence.
  - \(-90^\circ\) à \(\omega_0\).
  - \(-180^\circ\) à haute fréquence.
[/important]
---

### 5. **Explication**
- Le filtre atténue les hautes fréquences.
- La bande passante dépend de \( R \) et \( L \).
- Les diagrammes de Bode visualisent l'atténuation et le déphasage en fonction de la fréquence.

---