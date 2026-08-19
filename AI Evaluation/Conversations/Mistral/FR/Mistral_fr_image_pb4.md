## Utilisateur
Voici un montage d'électronique analogique.
Détermine la tension v(t) en sortie pour une entrée sinusoïdale e(t) = E₀sin(ωt). Explique ton raisonnement.


---

## IA
Ce schéma représente un **redresseur double alternance** à diodes, souvent utilisé pour convertir une tension alternative en une tension continue.

### Analyse du circuit :

- **Entrée :** \( e(t) = E_0 \sin(\omega t) \)
- **Sortie :** \( v(t) \)

#### Fonctionnement :
1. **Pont de diodes :**
   Le montage est composé de 4 diodes disposées en pont. Cela permet de "redresser" les deux alternances (positive et négative) du signal d'entrée.

2. **[important]Alternance positive[/important] :**
   Quand \( e(t) > 0 \), deux diodes sont passantes (celles qui permettent le passage du courant [important]dans le sens direct[/important]), et les deux autres sont bloquées. Le courant passe à travers la charge et [important]la tension de sortie \( v(t) \) suit \( e(t)[/important] \).

3. **[important]Alternance négative[/important] :**
   Quand \( e(t) < 0 \), les deux diodes qui étaient bloquées deviennent passantes, et les deux autres se bloquent. Le courant traverse toujours la charge dans le même sens, donc \( [important]v(t) \) reste positive et suit \(  e(t)|[/important] \).

#### Résultat :
La tension de sortie \( v(t) \) est la **valeur absolue** de la tension d'entrée :
\[
[important]v(t) = |E_0 \sin(\omega t)|[/important]
\]

### Visualisation :
- Si tu traces \( e(t) \) et \( v(t) \), tu verras que \( v(t) \) est toujours positive, même quand \( e(t) \) est négative.

---
**En résumé :**
Ce montage permet de transformer une tension sinusoïdale alternative en une tension toujours positive, ce qui est utile pour alimenter des circuits nécessitant une tension continue.

Si tu veux une analyse plus détaillée ou une simulation, je peux t'aider à approfondir !