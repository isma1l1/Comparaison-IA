## Utilisateur

Voici un montage d"électronique analogique.
Identifie sans calcul la nature du filtre ci-contre, établis sa fonction de transfert sous forme canonique, et détermine les valeurs à donner à R' et C pour R = 1 kilo ohm, si on souhaite une pulsation de coupure oméga0 = 10^4 rad.s^-1 et un gain de 20 dB en haute fréquence.
*(image de schéma d’un montage à amplificateur opérationnel avec résistance d’entrée R, condensateur en série C, résistance de rétroaction R', entrée e et sortie s)*

## IA

Le montage est un amplificateur inverseur dont l’entrée est couplée par un condensateur en série. À basse fréquence le condensateur est bloquant, à haute fréquence il est passant. Le montage est donc un filtre passe-haut du premier ordre avec gain en bande passante.

La fonction de transfert s’obtient en écrivant l’impédance d’entrée Zₑ = R + 1/(jωC) et l’impédance de rétroaction Zf = R′. Pour un A.O. idéal en montage inverseur :

H(jω) = S/E = − Zf / Zₑ = − R′ / (R + 1/(jωC)).

On met sous forme canonique :

H(jω) = − R′ · (jωC) / (1 + jωRC)
= − (R′/R) · (jω/ω₀) / (1 + jω/ω₀),

avec ω₀ = 1/(RC).

C’est bien la forme canonique d’un passe-haut du premier ordre, de gain en haute fréquence égal à |H(∞)| = R′/R.

On impose :

ω₀ = 10⁴ rad·s⁻¹ = 1/(RC)
⇒ RC = 10⁻⁴ s.

Avec R = 1 kΩ = 10³ Ω :

C = 10⁻⁴ / 10³ = 10⁻⁷ F = 100 nF.

Le gain en haute fréquence vaut :

|H(∞)| = R′/R.

20 dB ⇒ 20 log₁₀(R′/R) = 20 ⇒ R′/R = 10.

Donc :

R′ = 10 R = 10 kΩ.

Résultat final :

C = 100 nF
R′ = 10 kΩ.
