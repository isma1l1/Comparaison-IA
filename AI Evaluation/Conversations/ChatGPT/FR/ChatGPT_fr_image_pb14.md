## Utilisateur

Voici un montage d"électronique analogique.
L'ALI du montage fonctionnant en régime linéaire, identifie la nature du filtre, établis sa fonction de transfert, identifie une pulsation caractéristique oméga0, représente son diagramme de Bode en gain, discute l'allure du signal de sortie pour un créneau en entrée.
*(image de schéma d’un montage analogique avec un AOP en suiveur, deux résistances en série entre l’entrée et l’entrée non-inverseuse, un condensateur entre la sortie et le point intermédiaire des résistances, et un condensateur entre l’entrée non-inverseuse et la masse)*

## IA

Le montage est un filtre actif de type Sallen–Key à gain unitaire (l’ALI est monté en suiveur, donc (s = v_{+})). Les deux résistances sont en série entre l’entrée et le nœud d’entrée non-inverseuse, avec un condensateur de rétroaction entre la sortie et le point intermédiaire, et un condensateur à la masse sur l’entrée non-inverseuse. C’est la topologie classique d’un filtre passe-bas du second ordre.

Pour établir la fonction de transfert, on note (V_1) le nœud entre les deux résistances, (V_2) le nœud d’entrée de l’ALI (donc la sortie, puisque suiveur). En écrivant les lois de Kirchhoff en régime de Laplace (variable (s)) et en supposant (R) et (C) identiques :

[
H(s)=\frac{S(s)}{E(s)}=\frac{1}{1+3RC,s+(RC)^2 s^2}
]

Il s’agit donc d’un passe-bas du second ordre, de forme canonique :

[
H(s)=\frac{1}{1+\frac{s}{Q\omega_0}+\left(\frac{s}{\omega_0}\right)^2}
]

On identifie directement :

[
\omega_0=\frac{1}{RC}, \quad Q=\frac{1}{3}
]

Le filtre est fortement amorti (pas de résonance).

Diagramme de Bode (gain) : à basse fréquence ((\omega \ll \omega_0)), le gain vaut 1 (0 dB). Autour de (\omega_0), la transition est progressive (pas de bosse, car (Q<1/\sqrt{2})). À haute fréquence ((\omega \gg \omega_0)), la pente tend vers (-40\ \mathrm{dB/dec}), caractéristique d’un second ordre.

Réponse à un créneau en entrée : chaque front du créneau excite la dynamique du filtre. Comme le système est du second ordre très amorti ((Q=1/3)), la réponse à un échelon est monotone, sans dépassement. Le signal de sortie est donc un créneau fortement adouci : les transitions deviennent des montées/descendes exponentielles sans oscillation, et si la fréquence du créneau est élevée devant (\omega_0), le signal de sortie tend vers une forme quasi sinusoïdale de faible amplitude (comportement intégrateur à haute fréquence).
