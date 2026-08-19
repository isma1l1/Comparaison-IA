## Utilisateur

Réponds de manière concise en supprimant tout propos inutile. 
Identifie sans calcul la nature du filtre ci-contre, établis sa fonction de transfert sous forme canonique, et détermine les valeurs à donner à R' et C pour R = 1 kilo ohm, si on souhaite une pulsation de coupure oméga0 = 10^4 rad.s^-1 et un gain de 20 dB en haute fréquence.
*(image d'un schéma de circuit électronique comprenant un amplificateur opérationnel en montage inverseur avec une résistance R et un condensateur C en série sur l'entrée, et une résistance de contre-réaction R')*

## IA

### Analyse du Filtre

* **Nature du filtre :** C'est un filtre **passe-haut** du premier ordre (inverseur). En haute fréquence, le condensateur se comporte comme un fil, laissant passer le signal avec un gain fini ; en basse fréquence, il se comporte comme un circuit ouvert, bloquant le signal.

---

### Fonction de Transfert

En considérant l'amplificateur opérationnel comme idéal en régime linéaire :
$$H(j\omega) = \frac{\underline{s}}{\underline{e}} = -\frac{R'}{R + \frac{1}{jC\omega}} = -\frac{jR'C\omega}{1 + jRC\omega}$$

**Forme canonique :**
$$H(j\omega) = A_v \frac{j\frac{\omega}{\omega_0}}{1 + j\frac{\omega}{\omega_0}}$$
Avec :
* Gain asymptotique (HF) : $A_v = -\frac{R'}{R}$
* Pulsation de coupure : $\omega_0 = \frac{1}{RC}$

---

### Détermination des Composants

1.  **Calcul de C :**
    À partir de $\omega_0 = \frac{1}{RC}$ :
    $$C = \frac{1}{R \cdot \omega_0} = \frac{1}{10^3 \cdot 10^4} = 10^{-7} \text{ F} = \mathbf{100 \text{ nF}}$$

2.  **Calcul de R' :**
    Le gain en haute fréquence est $G_{dB} = 20 \text{ dB}$, ce qui correspond à un rapport d'amplification linéaire $|A_v| = 10^{\frac{20}{20}} = 10$.
    $$|A_v| = \frac{R'}{R} \implies R' = 10 \cdot R = 10 \cdot 10^3 = \mathbf{10 \text{ k}\Omega}$$
