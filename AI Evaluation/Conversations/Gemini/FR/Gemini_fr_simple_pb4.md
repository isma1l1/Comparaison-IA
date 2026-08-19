## Utilisateur

Détermine la tension v(t) en sortie pour une entrée sinusoïdale e(t) = E0sin(wt) dans un montage de Pont de Graetz. Explique ton raisonnement.

---

## IA

Le montage dont tu parles, le **Pont de Graetz** (ou pont de diodes), est le standard pour le redressement double alternance. Voici comment on détermine la tension de sortie $v(t)$ à partir d'une entrée $e(t) = E_0\sin(\omega t)$.

---

### 1. Analyse du fonctionnement

Le pont est composé de quatre diodes. Le secret de son fonctionnement réside dans le fait que les diodes conduisent par paires selon la polarité de l'entrée :

* **[important]Alternance positive[/important] ($e(t) > 0$) :** Le courant traverse la première paire de diodes. [important]La tension de sortie suit directement l'entrée[/important].
> $v(t) = e(t) = E_0\sin(\omega t)$


* **[important]Alternance négative[/important] ($e(t) < 0$) :** Le courant est "redirigé" par la seconde paire de diodes pour traverser la charge dans le même sens que précédemment. [important]La tension de sortie est alors l'opposée de l'entrée[/important].
> $v(t) = -e(t) = -E_0\sin(\omega t)= |E_0\sin(\omega t)|$



### 2. Expression mathématique de $v(t)$

Puisque le but du pont de Graetz est de rendre toutes les alternances positives, la tension de sortie correspond mathématiquement à la **valeur absolue** du signal d'entrée.

$$[important]v(t) = |E_0\sin(\omega t)|[/important]$$

### 3. Modèle réel (Chute de tension)

Dans un cas pratique, les diodes ne sont pas parfaites. Pour que le courant circule, il doit traverser **deux diodes** en série à chaque instant. Si l'on note $V_d$ la tension de seuil d'une diode (environ **0,6V** ou **0,7V** pour le silicium), l'expression devient :

$$v(t) = \max(0, |E_0\sin(\omega t)| - 2V_d)$$

---

### Résumé des caractéristiques

| Grandeur | Valeur (Modèle idéal) |
| --- | --- |
| **Forme du signal** | Successions de arches de sinusoïde positives |
| **[important]Période de $v(t)$[/important]** | $[important]T/2[/important]$ (la fréquence est doublée) |
| **Tension maximale** | $E_0$ |
| **Tension moyenne** | $V_{moy} = \frac{2E_0}{\pi}$ |

Souhaites-tu que je calcule l'ondulation résiduelle si l'on ajoute un condensateur de filtrage à la sortie ?

---

Souhaites-tu que je génère également un schéma ou un graphique pour illustrer visuellement ces alternances ?