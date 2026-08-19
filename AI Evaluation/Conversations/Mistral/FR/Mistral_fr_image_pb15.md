## Utilisateur
Voici un montage d'électronique analogique.
Identifie sans calcul la nature du filtre ci-contre, établis sa fonction de transfert sous forme canonique, et détermine les valeurs à donner à R' et C pour R = 1 kilo ohm, si on souhaite une pulsation de coupure oméga0 = 10^4 rad.s^-1 et un gain de 20 dB en haute fréquence.

---

## IA
### 1. **Nature du filtre**
Le montage représenté est un **filtre actif passe-bas du second ordre** (ou filtre passe-bas de Sallen-Key).
C'est un filtre du second ordre car il contient deux éléments réactifs (le condensateur \( C \) et la résistance \( R' \) en boucle de rétroaction).
Il est de type **passe-bas** car le signal de sortie \( s \) est prélevé après les éléments réactifs, qui atténuent les hautes fréquences.

---

### 2. **Fonction de transfert sous forme canonique**
Pour un filtre passe-bas du second ordre de Sallen-Key, la fonction de transfert \( H(j\omega) \) s'écrit sous la forme canonique :

\[
H(j\omega) = \frac{H_0 \cdot \omega_0^2}{(j\omega)^2 + 2\zeta\omega_0(j\omega) + \omega_0^2}
\]

Où :
- \( H_0 \) est le gain statique (en basse fréquence),
- \( \omega_0 \) est la pulsation de coupure,
- \( \zeta \) est le coefficient d'amortissement.

Pour ce montage, le gain en haute fréquence est donné par \( 1 + \frac{R'}{R} \).
On souhaite un gain de **20 dB en haute fréquence**, ce qui correspond à un gain en tension de \( 10 \) (car \( 20 \log_{10}(10) = 20 \) dB).
Donc :
\[
1 + \frac{R'}{R} = 10 \implies \frac{R'}{R} = 9 \implies R' = 9R
\]

Avec \( R = 1 \) kΩ, on a :
\[
R' = 9 \times 1\,\text{k}\Omega = 9\,\text{k}\Omega
\]

---

### 3. **Détermination de \( C \)**
La pulsation de coupure \( \omega_0 \) est donnée par :
\[
\omega_0 = \frac{1}{\sqrt{R R' C^2}}
\]

On souhaite \( \omega_0 = 10^4 \) rad/s.
En remplaçant \( R \) et \( R' \) par leurs valeurs :
\[
10^4 = \frac{1}{\sqrt{1000 \times 9000 \times C^2}} = \frac{1}{\sqrt{9 \times 10^6 \times C^2}} = \frac{1}{3000 C}
\]

On en déduit :
\[
C = \frac{1}{3000 \times 10^4} = \frac{1}{3 \times 10^7} \approx 33\,\text{nF}
\]

---
### 4. **Valeurs finales**
- \( R' = 9\,\text{k}\Omega \)
- \( C \approx 33\,\text{nF} \)

---
Si tu veux vérifier les calculs ou approfondir l'analyse, n'hésite pas à me le dire !