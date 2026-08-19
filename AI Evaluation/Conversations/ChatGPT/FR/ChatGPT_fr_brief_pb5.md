## Utilisateur
Réponds de manière concise en supprimant tout propos inutile.  
On étudie Uc(t) en fonction de E(t) dans un circuit RLC série. Détermine la nature du filtre représenté, calcule la fonction de transfert, donne l'expression de la largeur de la bande passante et trace les diagrammes de Bode en gain et en phase. Explique ton raisonnement.

## IA
Dans un **RLC série** avec sortie aux bornes du condensateur \(U_c(t)\) :

### 1) Nature du filtre
À basse fréquence (\(\omega \to 0\)), le condensateur se comporte comme un circuit ouvert ⇒ \(U_c \approx E\).  
À haute fréquence (\(\omega \to \infty\)), il se comporte comme un court-circuit ⇒ \(U_c \to 0\).  

C’est donc un **[important]filtre passe-bas du 2ᵉ ordre[/important]**.

---

### 2) Fonction de transfert

Impédances :
\[
Z_R = R,\quad Z_L = j\omega L,\quad Z_C = \frac{1}{j\omega C}
\]
[important]
Diviseur de tension[/important] :
\[
[important]H(j\omega) = \frac{U_c}{E} = \frac{Z_C}{Z_R + Z_L + Z_C}[/important]
\]

On obtient :

\[
[important]H(j\omega) = \frac{1}{1 - \omega^2 LC + j\omega RC}[/important]
\]

Forme canonique :

\[
H(j\omega) = [important]\frac{1}{1 - \left(\frac{\omega}{\omega_0}\right)^2 + j \frac{\omega}{Q\omega_0}}[/important]
\]

avec :

\[
[important]\omega_0 = \frac{1}{\sqrt{LC}}, \quad Q = \frac{1}{R}\sqrt{\frac{L}{C}}[/important]
\]

---

### 3) Bande passante

Pour un filtre du 2ᵉ ordre :

\[
[important]\Delta \omega = \frac{\omega_0}{Q}[/important]
\]


Donc :

\[
\Delta \omega = [important]\frac{R}{L}[/important]
\]

---

### 4) Diagramme de Bode (gain)

Module :
\[
|H(j\omega)| = \frac{1}{\sqrt{(1 - \omega^2 LC)^2 + (\omega RC)^2}}
\]
[important]
- \(\omega \ll \omega_0\) : gain ≈ 0 dB  
- \(\omega = \omega_0\) : pic possible si \(Q > \frac{1}{\sqrt{2}}\)  
- \(\omega \gg \omega_0\) : pente = **−40 dB/décade**
[/important]
---

### 5) Diagramme de Bode (phase)

Phase :
\[
\varphi(\omega) = -\arctan\left(\frac{\omega RC}{1 - \omega^2 LC}\right)
\]
[important]
- \(\omega \to 0\) : \(0^\circ\)  
- \(\omega = \omega_0\) : \(-90^\circ\)  
- \(\omega \to \infty\) : \(-180^\circ\)
[/important]
---

### 6) Interprétation rapide
- Le condensateur impose un comportement passe-bas  
- L’inductance introduit une résonance  
- La résistance fixe l’amortissement (donc la largeur de bande)

Si tu veux, je peux te tracer les courbes de Bode avec des valeurs numériques concrètes.