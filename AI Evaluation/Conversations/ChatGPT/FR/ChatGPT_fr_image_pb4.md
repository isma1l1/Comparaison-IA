## Utilisateur
Voici un montage d'électronique analogique. 
Détermine la tension v(t) en sortie pour une entrée sinusoïdale e(t) = E0sin(wt). Explique ton raisonnement.

## IA
Le montage représenté est un **pont de diodes (pont de Graetz)**. Il sert à redresser une tension alternative.

### Fonctionnement
- À chaque [important]demi-période[/important] du signal d’entrée \( e(t) = E_0 \sin(\omega t) \), [important]**deux diodes conduisent** tandis que les deux autres sont bloquées[/important].
- Le pont “retourne” les alternances négatives pour que le [important]courant traverse toujours la charge dans le **même sens[/important]**.
- Résultat : la tension de sortie est toujours **positive** (redressement [/important]double alternance[/important]).

### Expression de la sortie

#### Cas idéal (diodes parfaites, sans chute de tension) :
\[
[important]v(t) = |E_0 \sin(\omega t)|[/important] 
\]

#### Cas réel (avec chute de tension \( V_D \) par diode) :
À chaque conduction, il y a **2 diodes en série**, donc :
\[
v(t) = |E_0 \sin(\omega t)| - 2V_D
\]
(valable seulement lorsque \( |E_0 \sin(\omega t)| > 2V_D \), sinon \( v(t) = 0 \)).

### Conclusion
Le montage transforme une sinusoïde en une **sinusoïde redressée double alternance**.  
Graphiquement, c’est la valeur absolue du signal d’entrée (éventuellement abaissée par les chutes de tension des diodes).

Si tu veux, je peux te tracer la forme du signal pour visualiser