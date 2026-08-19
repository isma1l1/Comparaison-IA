## Utilisateur
Voici un montage d'électronique analogique. 
Donne moi la formule du gain de ce circuit en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA
Ce montage est un **amplificateur non-inverseur** (on reconnaît que \(V_{in}\) est appliqué sur l’entrée \(+\) de l’ampli op).

### Raisonnement

- Pour un ampli op idéal en régime linéaire :
  - \(V_+ \approx V_-\)
- Ici :
  - \(V_+ = V_{in}\)
  - Donc \([important]V_- = V_{in}[/important]\)

Le nœud \(V_-\) est relié à un **[important]pont diviseur[/important]** formé par \(R1\) (entre \(V_{out}\) et le nœud) et \(R2\) (entre le nœud et la masse).

Donc :
\[
[important]V_- = V_{out} \cdot \frac{R2}{R1 + R2}[/important]
\]

Mais comme \(V_- = V_{in}\), on a :
\[
[important]V_{in} = V_{out} \cdot \frac{R2}{R1 + R2}[/important]
\]

On isole \(V_{out}/V_{in}\) :

\[
[important]\frac{V_{out}}{V_{in}} = 1 + \frac{R1}{R2}[/important]
\]

### Conclusion

Le gain du montage est :
\[
G = 1 + \frac{R1}{R2}
\]

### Intuition

- \(R1\) augmente le gain (plus de rétroaction → amplification plus forte)
- \(R2\) le diminue
- Le gain est toujours **≥ 1** (contrairement à l’inverseur)

Si tu veux, je peux aussi te montrer comment ce montage réagit avec des valeurs concrètes ou le comparer avec un ampli inverseur.