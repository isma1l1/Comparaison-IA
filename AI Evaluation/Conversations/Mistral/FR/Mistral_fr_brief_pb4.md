## Utilisateur
Réponds de manière concise en supprimant tout propos inutile. Détermine la tension v(t) en sortie pour une entrée sinusoïdale e(t) = E0sin(wt) dans un montage de Pont de Graetz. Explique ton raisonnement.

## IA
Pour un **montage de Pont de Graetz** (redresseur double alternance à diodes), la tension de sortie \( v(t) \) en réponse à une entrée sinusoïdale \( e(t) = E_0 \sin(\omega t) \) est donnée par :

\[
[important]v(t) =  E_0 \sin(\omega t)|[/important] - 2V_d
\]

### Explication :
1. **Redressement double alternance** : Le pont de Graetz [important]inverse les alternances négatives de \( e(t) \)[/important], ce qui donne la valeur absolue \( [important]|E_0 \sin(\omega t)|[/important] \).
2. **Chute de tension aux bornes des diodes** : Chaque diode introduit une chute de tension \( V_d \) (environ 0.7 V pour le silicium). Comme deux diodes conduisent simultanément, la tension de sortie est réduite de \( 2V_d \).

### Résultat final :
\[
v(t) = |E_0 \sin(\omega t)| - 2V_d
\]