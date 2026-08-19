## Utilisateur
Réponds de manière concise en supprimant tout propos inutile. 
On étudie un montage dérivateur classique. Détermine la relation entrée-sortie de ce système. Explique ton raisonnement.

## IA
Montage dérivateur classique à amplificateur opérationnel idéal (entrée inverseuse avec condensateur en série, résistance en rétroaction).

Hypothèses : A.O. idéal ⇒ courant d’entrée nul et \(V_- \approx V_+ = 0\) (masse virtuelle).

Courant dans le condensateur :
\[
i_C = C \,\frac{dV_{in}}{dt}
\]

Ce courant traverse la résistance de rétroaction \(R\) (pas d’autre chemin) :
\[
i_R = \frac{0 - V_{out}}{R} = -\frac{V_{out}}{R}
\]

Égalité des courants \(i_C = i_R\) :
\[
C \,\frac{dV_{in}}{dt} = -\frac{V_{out}}{R}
\]

Donc :
\[
V_{out} = -RC \,\frac{dV_{in}}{dt}
\]

Conclusion : le montage réalise la dérivation du signal d’entrée, avec un gain \(-RC\).
