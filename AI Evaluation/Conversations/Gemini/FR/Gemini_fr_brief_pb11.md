## Utilisateur
Réponds de manière concise en supprimant tout propos inutile. 
On étudie un montage intégrateur différentiel classique dans lequel les deux résistances ont la même valeur R et les deux condensateurs ont la même valeur C. Détermine Vs en fonction de V1 et V2. Explique ton raisonnement.

---

## IA
Pour un **intégrateur différentiel** (ou intégrateur soustracteur) avec des composants identiques ($R$ et $C$), la tension de sortie $V_s$ est donnée par :

$$V_s = \frac{1}{RC} \int (V_1 - V_2) \, dt$$

---

### Raisonnement

Le montage utilise un amplificateur opérationnel (AO) en régime linéaire ([[important]$V_+ = V_-$[\important]]). On applique le principe de superposition ou le théorème de Millman :

1.  **Potentiel sur l'entrée non-inverseuse ($V_+$) :**
    C'est un circuit $RC$ série (filtre passe-bas). En notation complexe :
    $$V_+ = V_1 \frac{\frac{1}{jC\omega}}{R + \frac{1}{jC\omega}} = \frac{V_1}{1 + jRC\omega}$$

2.  **Potentiel sur l'entrée inverseuse ($V_-$) :**
    D'après le théorème de Millman :
    $$V_- = \frac{\frac{V_2}{R} + \frac{V_s}{1/jC\omega}}{\frac{1}{R} + jC\omega} = \frac{V_2 + jRC\omega V_s}{1 + jRC\omega}$$

3.  **Égalité $V_+ = V_-$ :**
    Les dénominateurs étant identiques, on obtient :
    [[important]$$V_1 = V_2 + jRC\omega V_s \implies jRC\omega V_s = V_1 - V_2$$[\important]]
4.  **Retour au domaine temporel :**
    L'opérateur $j\omega$ correspond à la dérivation, donc $\frac{1}{j\omega}$ correspond à l'intégration :
    $$V_s(t) = \frac{1}{RC} \int (V_1(t) - V_2(t)) \, dt$$
