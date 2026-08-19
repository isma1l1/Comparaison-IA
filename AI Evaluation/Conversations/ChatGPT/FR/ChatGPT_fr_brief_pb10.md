## Utilisateur
Répond de manière concise en supprimant tout propos inutile. 
On étudie un montage sommateur non-inverseur classique dans lequel les quatre résistances ont la même valeur R. Détermine Vs en fonction de V1 et V2. Explique ton raisonnement.

## IA
Dans un sommateur non-inverseur idéal, l’entrée + de l’AOP ne consomme aucun courant et la tension à l’entrée − est égale à celle de l’entrée +.

Le pont résistif côté entrée + (deux résistances égales R reliées à \(V_1\) et \(V_2\)) impose :
[[important]\[
V_+ = \frac{V_1 + V_2}{2}.
\][\important]]

Comme l’AOP est en[[important] régime linéaire avec contre-réaction, \(V_- = V_+\)[\important]].

Le montage de contre-réaction (deux résistances égales R entre sortie et masse via l’entrée −) est un amplificateur non-inverseur de gain :
[[important]
\[
1 + \frac{R}{R} = 2.
\][\important]]
Donc :
[[important]
\[
V_s = 2 \cdot V_+ = 2 \cdot \frac{V_1 + V_2}{2} = V_1 + V_2.
]\[\important]]