## Utilisateur
Réponds de manière concise en supprimant tout propos inutile. 
On étudie un montage sommateur non-inverseur classique dans lequel les quatre résistances ont la même valeur R. Détermine Vs en fonction de V1 et V2. Explique ton raisonnement.

## IA
Dans un montage sommateur non-inverseur où toutes les résistances sont égales à $R$, la tension de sortie $V_s$ est égale à la somme des tensions d'entrée :
[[important]
$$V_s = V_1 + V_2$$[\important]]

---

### Raisonnement

Le calcul s'effectue en deux étapes grâce au principe de superposition et aux propriétés de l'amplificateur opérationnel (AO) idéal en [[important]régime linéaire ($V_+ = V_-$).[\important]]

**1. Calcul de la tension sur l'entrée non-inverseuse ($V_+$)**
Le réseau d'entrée ($V_1, V_2$ et les deux résistances $R$ associées) forme un pont diviseur de tension. D'après le théorème de Millman :
[[important]$$V_+ = \frac{\frac{V_1}{R} + \frac{V_2}{R}}{\frac{1}{R} + \frac{1}{R}} = \frac{V_1 + V_2}{2}$$[\important]]

**2. Relation avec la sortie ($V_s$)**
La structure de l'AO forme un montage **amplificateur non-inverseur** par rapport à $V_+$. Le gain est défini par les deux résistances de rétroaction (également égales à $R$) :
[[important]$$V_s = V_+ \cdot \left(1 + \frac{R}{R}\right) = V_+ \cdot 2$$[\important]]

**3. Conclusion**
En remplaçant $V_+$ par son expression :
$$V_s = \frac{V_1 + V_2}{2} \cdot 2 = V_1 + V_2$$
