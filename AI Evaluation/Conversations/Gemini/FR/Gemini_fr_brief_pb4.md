## Utilisateur

Réponds de manière concise en supprimant tout propos inutile. Détermine la tension v(t) en sortie pour une entrée sinusoïdale e(t) = E0sin(wt) dans un montage de Pont de Graetz. Explique ton raisonnement.

---

## IA

Pour un pont de Graetz (redresseur double alternance) alimenté par $e(t) = E_0 \sin(\omega t)$ :

### Expression de la tension de sortie $v(t)$

La tension de sortie est la valeur absolue de l'entrée (redressement total) :


$$[important]v(t) = |E_0 \sin(\omega t)|[/important]$$

---

### Raisonnement

Le fonctionnement repose sur la commutation des diodes par paires selon la polarité de $e(t)$ :

1. **[important]Alternance positive ($e(t) > 0$)[/important]** :
* Les diodes [important]$D_1$ et $D_3$ sont passantes[/important].
* Le courant circule de telle sorte que $[important]v(t) = e(t)[/important]$.


2. **[important]Alternance négative ($e(t) < 0$)[/important]** :
* Les diodes [important]$D_2$ et $D_4$ sont passantes[/important].
* Le pont inverse le branchement de la charge par rapport à la source, rendant $[important]v(t) = -e(t)[/important]$.



**Conclusion** : Quelle que soit la polarité de l'entrée, la sortie est toujours positive, ce qui correspond mathématiquement à la fonction **valeur absolue**.