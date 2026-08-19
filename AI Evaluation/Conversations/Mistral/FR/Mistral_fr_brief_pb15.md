## Utilisateur
Réponds de manière concise en supprimant tout propos inutile.
Identifie sans calcul la nature du filtre ci-contre, établis sa fonction de transfert sous forme canonique, et détermine les valeurs à donner à R' et C pour R = 1 kilo ohm, si on souhaite une pulsation de coupure oméga0 = 10^4 rad.s^-1 et un gain de 20 dB en haute fréquence.

## IA
**Nature du filtre** : Passe-haut (RC).

**Fonction de transfert canonique** :
\( H(j\omega) = \frac{K \cdot j\omega RC}{1 + j\omega RC} \)

**Valeurs pour \( R' \) et \( C \)** :
- \( R' = R = 1\,\text{k}\Omega \)
- \( C = \frac{1}{R \omega_0} = \frac{1}{10^4 \times 10^3} = 10^{-7}\,\text{F} = 0{,}1\,\mu\text{F} \)
- \( K = 10 \) (pour 20 dB en HF).