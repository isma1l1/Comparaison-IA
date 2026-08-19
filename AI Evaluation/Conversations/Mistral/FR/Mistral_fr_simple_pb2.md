## Utilisateur
Donne moi la formule du gain d'un montage non-inverseur en fonction des valeurs des résistances R1 et R2. Explique ton raisonnement.

## IA
### Formule du gain d'un montage non-inverseur

Pour un **amplificateur opérationnel en montage non-inverseur**, le gain en tension \( A_v \) est donné par la formule suivante :

\[
[important]A_v = 1 + \frac{R_2}{R_1}[/important]
\]

---

### Explication du raisonnement

#### 1. **Schéma du montage non-inverseur**
Dans un montage non-inverseur, la tension d'entrée \( V_{in} \) est appliquée directement sur l'entrée non-inverseuse (+) de l'amplificateur opérationnel. La résistance \( R_1 \) est connectée entre la sortie de l'amplificateur et l'entrée inverseuse (-), tandis que \( R_2 \) est connectée entre l'entrée inverseuse et la masse.

#### 2. **Hypothèses idéales**
On suppose que l'amplificateur opérationnel est idéal :
- **Impédance d'entrée infinie** : Aucun courant ne circule dans les entrées (+) et (-).
- **Gain en boucle ouverte infini** : La différence de tension entre les entrées (+) et (-) est nulle (\( [important]V_+ = V_-[/important] \)).

#### 3. **Calcul du gain**
- La tension sur l'entrée non-inverseuse est \( V_{in} \).
- La tension sur l'entrée inverseuse est \( V_- \), et comme \( V_+ = V_- \), on a \( [important]V_- = V_{in}[/important] \).

En appliquant la **[important]loi des nœuds[/important]** à l'entrée inverseuse :
\[
\frac{V_{out} - V_-}{R_2} + \frac{V_- - 0}{R_1} = 0
\]
En remplaçant \( V_- \) par \( V_{in} \) :
\[
\frac{V_{out} - V_{in}}{R_2} + \frac{V_{in}}{R_1} = 0
\]
En réarrangeant l'équation pour isoler \( V_{out} \) :

\[
[important]V_{out} = V_{in} \left(1 + \frac{R_2}{R_1}\right)[/important]
\] 
Le **gain en tension** \( A_v \) est donc :

\[
[important]A_v = \frac{V_{out}}{V_{in}} = 1 + \frac{R_2}{R_1}[/important]
\]

---

### Conclusion
Le gain d'un montage non-inverseur dépend uniquement du rapport des résistances \( R_2 \) et \( R_1 \). Ce montage est très utilisé car il permet d'obtenir un gain supérieur ou égal à 1, sans inverser la phase du signal d'entrée.

Si tu veux un exemple numérique ou une application pratique, n'hésite pas à demander !