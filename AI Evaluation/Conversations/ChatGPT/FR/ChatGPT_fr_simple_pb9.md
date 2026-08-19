## Utilisateur

On étudie un montage dérivateur classique. Détermine la relation entrée-sortie de ce système. Explique ton raisonnement.

## IA

On considère le montage dérivateur classique réalisé avec un amplificateur opérationnel idéal : l’entrée non-inverseuse est à la masse, l’entrée inverseuse reçoit le signal d’entrée via un condensateur C, et une résistance R est placée en contre-réaction entre la sortie et l’entrée inverseuse.

On suppose l’amplificateur opérationnel idéal, donc le courant d’entrée est nul et, en régime de [important]rétroaction négative[/important], la tension différentielle entre les deux entrées est nulle. Comme l’entrée non-inverseuse est à 0 V, l’entrée inverseuse est au potentiel de masse virtuelle, donc v⁻ ≈ 0.

On note v_e(t) la tension d’entrée et v_s(t) la tension de sortie. Le condensateur est branché entre l’entrée v_e et le nœud inverseur (au potentiel nul). La tension à ses bornes vaut donc simplement v_e(t).

Le courant dans un condensateur s’écrit i_C = C d(v_C)/dt. Ici v_C = v_e(t) - v⁻(t) ≈ v_e(t), donc le courant vaut [important]i_C = C dv_e/dt[/important].

Ce courant entre dans le nœud inverseur. Comme aucun courant n’entre dans l’amplificateur opérationnel, il traverse entièrement la résistance de contre-réaction R. On a donc [important]i_R = i_C[/important].

Or la tension aux bornes de la résistance est v⁻ - v_s ≈ 0 - v_s = -v_s, donc [important]i_R = (0 - v_s)/R = -v_s/R[/important].

En identifiant les courants : [important]-v_s/R = C dv_e/dt[/important].

On en déduit la relation entrée-sortie :

[important]v_s(t) = - R C dv_e(t)/dt[/important].
Le montage réalise donc une dérivation temporelle du signal d’entrée, avec un gain proportionnel à RC et une inversion de signe due à la configuration inverseuse.
